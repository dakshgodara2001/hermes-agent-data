#!/usr/bin/env python3
"""Tiny local browser viewer for a Karpathy-style markdown LLM wiki.

Usage:
  WIKI_PATH=/path/to/wiki WIKI_PORT=8765 python3 local_wiki_server.py

Then open http://localhost:8765
"""

from http.server import BaseHTTPRequestHandler, HTTPServer
from pathlib import Path
from urllib.parse import urlparse, parse_qs, quote
import html
import os

WIKI = Path(os.environ.get("WIKI_PATH", str(Path.home() / "wiki"))).resolve()
PORT = int(os.environ.get("WIKI_PORT", "8765"))

STYLE = """
body { margin:0; font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif; background:#0b0f17; color:#e8edf7; }
a { color:#7cc7ff; text-decoration:none; } a:hover { text-decoration:underline; }
.app { display:grid; grid-template-columns:320px 1fr; min-height:100vh; }
.sidebar { border-right:1px solid #243044; padding:18px; background:#101827; overflow:auto; }
.content { padding:32px; max-width:980px; line-height:1.65; }
h1,h2,h3 { color:#fff; line-height:1.2; } code, pre { background:#111f32; color:#d7e7ff; border-radius:6px; }
pre { padding:14px; overflow:auto; } code { padding:2px 5px; }
.file { display:block; padding:6px 0; color:#c9d8ee; }
.file small { color:#8091aa; }
.badge { font-size:12px; color:#a7b4c8; }
.search { width:100%; box-sizing:border-box; padding:10px; border-radius:8px; border:1px solid #2c3b55; background:#0b1220; color:#fff; margin:10px 0 14px; }
blockquote { border-left:3px solid #3b82f6; padding-left:14px; color:#c7d2e5; }
table { border-collapse:collapse; width:100%; } td,th { border:1px solid #2c3b55; padding:8px; }
"""

SCRIPT = """
<script src="https://cdn.jsdelivr.net/npm/marked/marked.min.js"></script>
<script>
async function loadPage(path) {
  const res = await fetch('/raw?page=' + encodeURIComponent(path));
  const text = await res.text();
  document.getElementById('doc').innerHTML = marked.parse(text.replace(/\[\[([^\]]+)\]\]/g, (m, p) => {
    let target = p;
    if (!target.endsWith('.md')) target += '.md';
    if (!target.includes('/')) target = 'concepts/' + target;
    return '[' + p + '](/?page=' + encodeURIComponent(target) + ')';
  }));
  history.replaceState(null, '', '/?page=' + encodeURIComponent(path));
}
function filterFiles() {
  const q = document.getElementById('search').value.toLowerCase();
  document.querySelectorAll('.file').forEach(el => {
    el.style.display = el.textContent.toLowerCase().includes(q) ? 'block' : 'none';
  });
}
window.addEventListener('DOMContentLoaded', () => {
  const params = new URLSearchParams(location.search);
  loadPage(params.get('page') || 'index.md');
});
</script>
"""

class Handler(BaseHTTPRequestHandler):
    def log_message(self, fmt, *args):
        return

    def _send(self, body, ctype="text/html; charset=utf-8"):
        data = body.encode("utf-8")
        self.send_response(200)
        self.send_header("Content-Type", ctype)
        self.send_header("Content-Length", str(len(data)))
        self.end_headers()
        self.wfile.write(data)

    def _safe_path(self, rel):
        target = (WIKI / rel).resolve()
        if not str(target).startswith(str(WIKI)) or not target.is_file() or target.suffix != ".md":
            return None
        return target

    def do_GET(self):
        parsed = urlparse(self.path)
        qs = parse_qs(parsed.query)
        if parsed.path == "/raw":
            rel = qs.get("page", ["index.md"])[0]
            target = self._safe_path(rel)
            if not target:
                self._send("Not found", "text/plain; charset=utf-8")
                return
            self._send(target.read_text(encoding="utf-8"), "text/plain; charset=utf-8")
            return

        files = sorted([p.relative_to(WIKI).as_posix() for p in WIKI.rglob("*.md")])
        links = []
        for f in files:
            label = f"<small>raw</small> {html.escape(f)}" if f.startswith("raw/") else html.escape(f)
            links.append(f'<a class="file" href="/?page={quote(f)}" onclick="event.preventDefault();loadPage(\'{html.escape(f)}\')">{label}</a>')

        body = f"""<!doctype html><html><head><meta charset="utf-8" />
<meta name="viewport" content="width=device-width, initial-scale=1" />
<title>LLM Wiki</title><style>{STYLE}</style></head><body>
<div class="app"><aside class="sidebar"><h2>🧠 LLM Wiki</h2>
<div class="badge">{html.escape(str(WIKI))}</div>
<input id="search" class="search" oninput="filterFiles()" placeholder="Search pages..." />
<a class="file" href="/?page=index.md" onclick="event.preventDefault();loadPage('index.md')">🏠 index.md</a>
<a class="file" href="/?page=SCHEMA.md" onclick="event.preventDefault();loadPage('SCHEMA.md')">⚙️ SCHEMA.md</a>
<hr style="border-color:#243044" />{''.join(links)}</aside>
<main class="content" id="doc">Loading...</main></div>{SCRIPT}</body></html>"""
        self._send(body)

if __name__ == "__main__":
    print(f"Serving {WIKI} at http://localhost:{PORT}")
    HTTPServer(("127.0.0.1", PORT), Handler).serve_forever()
