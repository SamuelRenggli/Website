# To do

Open questions and tasks before and after going live. Tick them off as you go (`[x]`).
In the code, open points are marked with `TODO`.

---

## Questions for Manu (before going live)

### Contact and legal
- [x] **Email address:** `manuel.staehelin@bluewin.ch`
      → `src/config.ts` (`email`)
- [ ] **Phone number:** show one on the website, or not? If yes, which (e.g. `+41 79 …`)?
      Empty = hidden everywhere. → `src/config.ts` (`phone`)
- [ ] **Postal address for the Impressum** (required by Swiss law for a commercial website).
      → `src/config.ts` (`address`)
- [ ] **Datenschutz text:** fine as is, or should someone check it?
      → `src/pages/datenschutz.astro`, `src/pages/en/datenschutz.astro`

### About Manu
- [ ] **Exact title / qualification:** "Bergführer" only, or e.g. "Bergführer mit eidg. Fachausweis" / IFMGA?
      → `src/i18n.ts` (`role`)
- [ ] **"Über mich" text:** is it accurate, and does it sound like him (DE and EN)?
      Includes Piz Kesch at 6, ETH mechanical engineering, safety first. → `src/i18n.ts` (`about`)
- [x] **Greeting:** now "Ich bin Manuel, dein Bergführer." (EN: "I'm Manuel, your mountain guide.") → `src/i18n.ts` (`about.title`)
- [ ] **Region:** say more than "Schweizer Alpen" (e.g. Wallis, Engadin, home base)?

### Offers and prices
- [ ] **Offers:** are these right? Winter: Skitouren, Freeride, Skihochtouren, Lawinenkurse.
      Summer: Hochtouren, Gratklettern, Bergtouren, Kurse. Anything missing (e.g. Klettersteig, Eisklettern, Haute Route)?
      → `src/data/offers.ts`
- [ ] **Seasons per offer** (e.g. "Dezember bis April") correct? → `src/data/offers.ts`
- [ ] **Group size:** "privat oder in kleinen Gruppen" correct? Max number of people?
- [ ] **Prices:** only link to the SBV rates (current state), or show own prices / "ab CHF …" per tour?
- [ ] **Fixed dates:** are there courses or tours with fixed dates to list?

### Photos and videos
- [ ] **Photo credits:** all photos are by Samuel Renggli or Tobin Meyers? Does Tobin Meyers agree
      to the use, and should he be credited differently (e.g. with a link)?
- [ ] **Clip captions:** are the two clips (drone over powder tracks, powder under blue sky) captioned right?
      → `src/components/Clips.astro`
- [x] **Hero video:** new intro film (`Intro_website.mp4`, 17 s) since Oct 2026
- [ ] **Gallery:** any photos to remove or add?

## Technical tasks

### Before going live (see [GO-LIVE.md](GO-LIVE.md))
- [x] Test everything locally with the checklist in [TESTING.md](TESTING.md)
- [x] Sign in to GitHub with the CLI (`gh auth login`)
- [x] Create the repository (`SamuelRenggli/Website`) and push
- [x] Turn on GitHub Pages and test on `samuelrenggli.github.io/Website`
- [x] Find out how email for `manuelstaehelin.ch` runs today (Metanet, via `mail.manuelstaehelin.ch`, not affected by the DNS change)
- [x] Change DNS at Metanet (Metanet DNS since 8 Oct 2026, see DNS-METANET.md) and enter the domain on GitHub
- [x] Enforce HTTPS on GitHub (certificate valid for manuelstaehelin.ch and www, renews automatically)
- [ ] Send a test email to the real mailbox and reply, to confirm email still works
- [ ] Verify the domain on GitHub (TXT record) against takeover

### Setup
- [ ] Restart Claude Code / reload VS Code and approve the **stitch** MCP server, then try design variants in Google Stitch
- [ ] Decide: contact form via mail app (current) or a form service like Formspree / Web3Forms
      → `src/config.ts` (`formEndpoint`)

### After going live
- [ ] Cancel the WordPress hosting at Metanet once the new site runs fine
      (**only after checking that email does not depend on it**)
- [ ] Register the site in Google Search Console and Google Business Profile ("Bergführer …")

## Ideas for later

- [ ] Short highlight film (about 60 s) from the drone footage → new hero video
- [ ] Short testimonials from real guests (2 to 3 quotes)
- [ ] One page per tour type (e.g. `/skitouren/`) so Google finds them individually
- [ ] Tour reports / blog with photos from recent tours
- [ ] Instagram feed or link-in-bio page
