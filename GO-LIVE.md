# Go live: manuelstaehelin.ch

Step-by-step from "runs on my computer" to "live on manuelstaehelin.ch".
The old WordPress site stays online until step 6, so nothing breaks before you switch.

`<github-user>` below means the GitHub account name you sign in with.

---

## 1. Test locally

```bash
cd N:\Git\Website
npm install          # only the first time
npm run dev
```

Open <http://localhost:4321> (German) and <http://localhost:4321/en/> (English).
Changes to files show up in the browser as soon as you save.

To test on your phone: run `npm run dev -- --host`, then open the "Network" address it prints
(e.g. `http://192.168.1.23:4321`) on a phone in the same Wi-Fi.

Before going live, also run `npm run build`. It checks the code and fails on errors.
The full test checklist is in [TESTING.md](TESTING.md).

## 2. Before going live: content checklist

- [ ] `src/config.ts`: real email, phone (or leave empty to hide), postal address for the Impressum
- [ ] `src/i18n.ts`: "Über mich" text and facts read well in German and English
- [ ] `src/data/offers.ts`: offers and seasons are right
- [ ] Impressum and Datenschutz pages are correct (both languages)
- [ ] Contact form tested: it opens the mail app with the request filled in
      (or set up a form service, see step 8)

## 3. Sign in to GitHub (once per computer)

In the terminal (or in Claude Code with a leading `!`):

```bash
gh auth login --web --git-protocol https --scopes workflow
```

Copy the code shown, open <https://github.com/login/device>, paste it and click **Authorize**.
Check with `gh auth status`.

## 4. Create the repository and upload

```bash
gh repo create manu-am-berg --public --source . --push
```

This creates `github.com/<github-user>/manu-am-berg` and uploads the code.
The raw media folder `Manu Bergführer Content/` and `.mcp.json` (contains the Stitch key) are in
`.gitignore` and are **not** uploaded.

> Why public? GitHub Pages is free only for public repositories. The website itself is public anyway.

## 5. Turn on GitHub Pages

```bash
gh api -X POST repos/<github-user>/manu-am-berg/pages -f build_type=workflow
gh workflow run "Deploy to GitHub Pages"
```

Or on github.com: repository, **Settings**, **Pages**, Source: **GitHub Actions**.

Watch progress in the **Actions** tab (first run takes about 5 minutes, later runs 1 to 2).
The site is then online at:

**https://samuelrenggli.github.io/Website/**

Test it there (also on your phone) before switching the domain.

## 6. Point the domain to GitHub (Metanet)

The domain stays at Metanet; you only change its DNS records.
Do **not** change the name servers (NS1/NS2.URBANUS.METANET.CH stay).

1. Log in to the Metanet customer area, open the DNS zone of `manuelstaehelin.ch`.
2. Delete the existing **A** record for `@` and the **A** record for `www`
   (both `80.74.140.2`, the WordPress hosting; status 7 Oct 2026, there is no AAAA record).
   Keep this value: to switch back, set both to `80.74.140.2` again.
3. Add:

   | Type | Name | Value |
   | --- | --- | --- |
   | A | @ | 185.199.108.153 |
   | A | @ | 185.199.109.153 |
   | A | @ | 185.199.110.153 |
   | A | @ | 185.199.111.153 |
   | AAAA | @ | 2606:50c0:8000::153 |
   | AAAA | @ | 2606:50c0:8001::153 |
   | AAAA | @ | 2606:50c0:8002::153 |
   | AAAA | @ | 2606:50c0:8003::153 |
   | CNAME | www | `<github-user>.github.io.` |

4. **Do not touch MX, SPF/TXT or `mail` records.** They handle email (e.g. info@manuelstaehelin.ch).
   Email runs via `mail.manuelstaehelin.ch` (own A record `80.74.140.2`), so it keeps working.

## 7. Connect the domain on GitHub

1. Repository, **Settings**, **Pages**, **Custom domain**: enter `manuelstaehelin.ch`, **Save**.
2. Wait until the DNS check is green (minutes up to a few hours).
3. Tick **Enforce HTTPS** (available once the certificate is issued, up to 24 h).
4. Recommended: verify the domain for your account (GitHub, **Settings** (your profile),
   **Pages**, **Add a domain**). GitHub shows a TXT record to add at Metanet.
   This stops anyone else from claiming the domain on GitHub.

The next deploy automatically uses `https://manuelstaehelin.ch/` as the address, no code change needed.
Check: <https://manuelstaehelin.ch> and <https://www.manuelstaehelin.ch> both show the new site.

## 8. Optional: contact form without mail app

1. Create a free form at <https://formspree.io> (or <https://web3forms.com>) with Manu's email.
2. Put the form URL into `formEndpoint` in `src/config.ts`, commit, push.

## 9. After going live

- Edit, then `git add -A`, `git commit -m "what changed"`, `git push`. Live within ~2 minutes.
- Every version is kept in GitHub. To undo a change: `git revert <commit>` and push.
- The WordPress hosting at Metanet can be cancelled once the new site has run fine for a while.
  **Check first whether email runs over the same Metanet package** before cancelling anything.

## Switching back (emergency)

Restore the old A/AAAA records at Metanet (step 6, note from point 2). WordPress is live again
as soon as DNS updates (usually within an hour).
