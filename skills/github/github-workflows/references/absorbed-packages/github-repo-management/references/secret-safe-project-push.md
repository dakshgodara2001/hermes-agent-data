# Secret-safe push of an existing app to a private GitHub repo

Use this when the user asks to create a private repo and push an existing local app while excluding keys/tokens.

## Workflow

1. Inspect the working tree and auth state.
   - Check whether the directory is already a git repo.
   - Confirm `gh auth status` or equivalent token-based auth.
   - List files before staging, including hidden deployment metadata.

2. Add or tighten `.gitignore` before `git add`.
   Include at minimum:
   - `.env`, `.env.*`, but allow `!.env.example`
   - `.vercel/`
   - `node_modules/`
   - private key/cert patterns such as `*.pem`, `*.key`, `*.p8`, `*.p12`
   - logs/cache/build outputs

3. Prefer moving frontend secrets behind a server route before publishing.
   - If a static page directly embeds Supabase anon/service keys, Telegram tokens, API tokens, or bearer/JWT values, refactor to a serverless/API route that reads from environment variables.
   - Commit only placeholder configuration such as `.env.example`.
   - Never commit Vercel project metadata from `.vercel/`; it can expose project linkage and belongs to local/deployment state.

4. Run a secret-pattern scan on the exact files that will be committed.
   Useful regex classes:
   - GitHub tokens: `gh[pousr]_[A-Za-z0-9_]{20,}`
   - OpenAI-style keys: `\bsk-[A-Za-z0-9_-]{20,}`
   - JWTs: `eyJ[A-Za-z0-9_-]{10,}\.[A-Za-z0-9_-]{10,}\.[A-Za-z0-9_-]{10,}`
   - Telegram bot tokens: `\b\d{8,12}:[A-Za-z0-9_-]{30,}\b`
   - Private key blocks: `-----BEGIN [A-Z ]*PRIVATE KEY-----`

5. Initialize, commit, create private repo, and push.
   - `git init -b main` if needed.
   - `git add . && git status --short` to review staged files.
   - `gh repo create OWNER/REPO --private --description "..." --source . --remote origin`
   - `git push -u origin main`

6. Verify after pushing.
   - `gh repo view OWNER/REPO --json nameWithOwner,isPrivate,url`
   - `git ls-tree -r --name-only origin/main`
   - Run the same secret-pattern scan against committed blobs, not just the filesystem.

## Pitfalls

- Public frontend anon keys may be intended for Supabase browser clients, but if the user explicitly says “except keys and tokens,” remove them from committed frontend code anyway and route through server-side environment variables.
- Do not rely on a local filesystem scan alone; scan staged/committed blobs too so ignored files and committed files are clearly separated.
- Do not print real token values in summaries. Report only that a scan passed or that a file contains a potential secret.