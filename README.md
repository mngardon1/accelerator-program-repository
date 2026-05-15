# CHIEF Accelerator — accelerator.rejoincoaching.com

Static site for `accelerator.rejoincoaching.com`. Hosted on Vercel, DNS pointed via GoHighLevel.

## Structure

```
deploy/
├── index.html                       # Program map (landing)
├── vercel.json                      # Clean URLs + headers
├── chat-vs-cowork/index.html        → /chat-vs-cowork/
├── help-me-decide/index.html        → /help-me-decide/
└── working-with-projects/index.html → /working-with-projects/
```

**Before first push:** delete these unused folders sitting in `/deploy/` from Finder so they don't deploy:
`context-layers/`, `learning-model/`, `how-ai-remembers/`, `ring-1-reference/`, `field-guide/`, `module-3-winter-method/`

Each page lives in its own folder as `index.html` so URLs stay clean (no `.html` extension, trailing slash enforced by `vercel.json`).

## Adding a new page

1. Make a new folder named after the slug: `mkdir new-page-slug`
2. Drop the HTML inside as `index.html`
3. Add a card to `index.html` under the appropriate section
4. Commit + push — Vercel auto-deploys

## First deploy

### 1. Create the GitHub repo
```bash
cd deploy
git init
git add .
git commit -m "Initial deploy"
git branch -M main
git remote add origin https://github.com/<your-user>/accelerator-site.git
git push -u origin main
```

### 2. Connect Vercel
- vercel.com → Add New Project → Import from GitHub
- Framework preset: **Other**
- Build command: *(leave empty)*
- Output directory: *(leave empty — uses root)*
- Deploy. You'll get a `*.vercel.app` URL. Confirm it loads.

### 3. Add the custom domain
- Vercel project → Settings → Domains → Add `accelerator.rejoincoaching.com`
- Copy the CNAME target Vercel gives you (usually `cname.vercel-dns.com`)

### 4. DNS record
Wherever `rejoincoaching.com` DNS is managed (GHL or upstream registrar):
- Type: `CNAME`
- Host: `accelerator`
- Value: `cname.vercel-dns.com`
- TTL: default

Wait 5–30 minutes for propagation. SSL auto-issues.

## Future updates

```bash
# edit files
git add .
git commit -m "Update X"
git push
```

Vercel auto-deploys on push to `main`. No build step.
