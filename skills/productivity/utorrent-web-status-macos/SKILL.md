---
name: utorrent-web-status-macos
description: Check uTorrent Web torrent download status on macOS by reading the SQLite resume.dat database directly — bypasses web UI auth issues.
triggers:
  - "check torrent status"
  - "utorrent downloads"
  - "are my torrents done"
  - "utorrent web macos"
---

# uTorrent Web Status on macOS

## Context

uTorrent Web on macOS serves its web UI on a **dynamically assigned port** (not always 8080, even if the user thinks so). Port 8080 is often occupied by nginx or another service. The actual web UI requires authentication, which is tricky to automate. The most reliable approach is to **read the SQLite `resume.dat` database directly**.

## Key Facts

- **App**: `/Applications/uTorrent Web.app`
- **Data dir**: `~/Library/Application Support/uTorrent Web/`
- **Credentials file**: `users.conf` (tab-delimited: username, password_hash, salt, type, enabled)
- **Torrent state DB**: `resume.dat` — **SQLite format** (not raw bencode file)
- **Web UI ports**: Find with `lsof -iTCP -sTCP:LISTEN | grep -i utorrent`
  - uTorrent Web process typically listens on 19575, 19576, 19577 (internal), and 6882 (BitTorrent)

## Finding the Real Port

```bash
lsof -iTCP -sTCP:LISTEN | grep -i utorrent
```

Look for the port that serves HTTP (usually 19575 for the web UI).

## Approach: Read resume.dat Directly (Recommended)

The `resume.dat` is a **SQLite database** with one table:

```sql
CREATE TABLE TORRENTS(INFOHASH STRING PRIMARY KEY NOT NULL, RESUME BLOB NOT NULL, SAVE_PATH STRING DEFAULT NULL);
```

The `RESUME` column is a **bencode-encoded blob** containing all torrent metadata: name, completion time, downloaded bytes, piece info, etc.

### Python Script to Extract Status

```python
import sqlite3, os, re, datetime

def extract_str(blob, key):
    if isinstance(key, str): key = key.encode()
    pat = f'{len(key)}:'.encode() + key
    idx = blob.find(pat)
    if idx == -1: return None
    idx += len(pat)
    colon = blob.index(b':', idx)
    length = int(blob[idx:colon])
    return blob[colon+1:colon+1+length].decode('utf-8', errors='replace')

def extract_int(blob, key):
    if isinstance(key, str): key = key.encode()
    pat = f'{len(key)}:'.encode() + key + b'i'
    idx = blob.find(pat)
    if idx == -1: return None
    start = idx + len(pat)
    end = blob.index(b'e', start)
    return int(blob[start:end])

db_path = os.path.expanduser('~/Library/Application Support/uTorrent Web/resume.dat')
conn = sqlite3.connect(db_path)
c = conn.cursor()
c.execute("SELECT INFOHASH, RESUME FROM TORRENTS")
rows = c.fetchall()

print(f"Found {len(rows)} torrents:")
for infohash, blob in rows:
    name = extract_str(blob, b'name')
    completed_time = extract_int(blob, b'completed_time')
    total_downloaded = extract_int(blob, b'total_downloaded')
    paused = extract_int(blob, b'paused')
    added_time = extract_int(blob, b'added_time')

    piece_length_match = re.search(rb'12:piece lengthi(\d+)e', blob)
    pieces_len_match = re.search(rb'6:pieces(\d+):', blob)
    total_size = None
    if piece_length_match and pieces_len_match:
        piece_length = int(piece_length_match.group(1))
        num_pieces = int(pieces_len_match.group(1)) // 20
        total_size = piece_length * num_pieces

    is_complete = completed_time and completed_time > 0
    added_dt = datetime.datetime.fromtimestamp(added_time).strftime('%Y-%m-%d %H:%M') if added_time else 'unknown'

    def fmt_size(b):
        if b is None: return 'unknown'
        if b >= 1024**3: return f'{b/1024**3:.2f} GB'
        if b >= 1024**2: return f'{b/1024**2:.1f} MB'
        return f'{b/1024:.0f} KB'

    progress = 'N/A'
    if total_downloaded and total_size:
        pct = min(100.0, total_downloaded / total_size * 100)
        progress = f'{pct:.1f}%'

    status = '✅ COMPLETE' if is_complete else ('⏸ PAUSED' if paused else '⏳ DOWNLOADING')
    print(f"  {name}")
    print(f"    Status: {status} | Progress: {progress} | Downloaded: {fmt_size(total_downloaded)} / {fmt_size(total_size)}")
    print(f"    Added: {added_dt}")

conn.close()
```

## Pitfalls

- **Port 8080 may be nginx**, not uTorrent — always verify with `lsof` first.
- **resume.dat is SQLite**, not raw bencode — open with `sqlite3`, not a bencode parser.
- **Web UI auth**: The `users.conf` format is `username\tpassword_hash\tsalt\ttype\tenabled`. The web UI returns "Not Authorized" HTML page even with correct credentials via curl; the session-based auth is complex. Stick to the DB approach.
- **Piece count**: SHA1 hashes in bencode pieces blobs are 20 bytes each — divide blob length by 20 to get num_pieces.
- **`completed_time > 0`** reliably indicates a finished torrent; `0` means not yet complete.
- **`total_downloaded`** can slightly exceed `total_size` due to overhead — cap progress at 100%.
