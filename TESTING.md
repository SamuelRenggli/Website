# Test locally

How to run the website on your own computer, check it, and adjust it before anything goes online.
Nothing you do here changes the live site; only `git push` publishes (see [GO-LIVE.md](GO-LIVE.md)).

---

## 1. One-time setup

You need [Node.js](https://nodejs.org) 22 or newer. Check in a terminal:

```bash
node --version     # should print v22.x or higher
```

Then, in the project folder:

```bash
cd N:\Git\Website
npm install
```

## 2. Start the test server

```bash
npm run dev
```

Open in the browser:

| Page | Address |
| --- | --- |
| German home | <http://localhost:4321> |
| English home | <http://localhost:4321/en/> |
| Impressum / Imprint | <http://localhost:4321/impressum/>, <http://localhost:4321/en/impressum/> |
| Datenschutz / Privacy | <http://localhost:4321/datenschutz/>, <http://localhost:4321/en/datenschutz/> |
| 404 page | <http://localhost:4321/does-not-exist> |

Leave the terminal open while testing. Every time you save a file, the browser updates by itself.
Stop the server with `Ctrl + C`.

## 3. Test on your phone

```bash
npm run dev -- --host
```

The terminal prints a **Network** address, e.g. `http://192.168.1.23:4321`.
Open it on a phone that is in the **same Wi-Fi**. If it does not load, allow Node.js in the
Windows firewall prompt (private networks).

Without a phone: in Chrome/Edge press `F12`, then `Ctrl + Shift + M` (device toolbar) and pick e.g. "iPhone 14".

## 4. What to check

**Every page, desktop and phone, German and English:**

- [ ] Hero video plays, pause button (bottom right) stops it
- [ ] Menu links jump to the right section; on the phone the menu button opens and closes
- [ ] DE / EN switch leads to the same page in the other language
- [ ] Winter / Sommer switch shows the right offers
- [ ] Rates links (SBV rates, AVB PDF) open
- [ ] Clips: play button starts the video with sound, only one plays at a time
- [ ] Gallery: "Alle 30 Fotos zeigen" shows all; clicking a photo opens it big;
      arrows / arrow keys / swipe go to the next one; `Esc` or X closes
- [ ] Contact form: empty submit shows error messages under the fields;
      filled in, it opens your mail app with the request prepared
- [ ] Footer: email, Instagram, Impressum and Datenschutz links work
- [ ] Texts: no typos, all facts correct (bio, offers, seasons, email, address)

**Dark mode:** switch Windows to dark (Settings, Personalisation, Colours, "Dark") or in
`F12` press `Ctrl + Shift + P`, type "dark", choose *Emulate prefers-color-scheme: dark*.

**Keyboard only:** press `Tab` through the page. Every link and button should get a visible orange outline.

## 5. Test the final version

`npm run dev` is a quick preview. Before going live, test exactly what will be published:

```bash
npm run build      # checks the code, then builds the site into dist/ (first time takes a few minutes)
npm run preview    # serves dist/ on http://localhost:4321
```

If `npm run build` prints errors, fix them first. The same check runs on GitHub, and a failing check
stops the deploy, so a broken version never goes live.

## 6. Where to change what

| What | File |
| --- | --- |
| Email, phone (empty = hidden), Instagram, address | `src/config.ts` |
| All texts in German and English | `src/i18n.ts` |
| Offers winter / summer | `src/data/offers.ts` |
| Gallery photos and order | `src/data/gallery.ts` |
| Colours and fonts | `src/styles/global.css` |
| New photos / videos | see "Neue Fotos oder Videos" in [README.md](README.md) |

## 7. Save your changes (versioning)

When you are happy with a change, save it as a version:

```bash
git add -A
git commit -m "Short description of what changed"
```

Versions stay on your computer until you `git push` (which publishes, once the site is on GitHub).
To see the history: `git log --oneline`. To throw away unsaved changes to a file: `git restore <file>`.

## Troubleshooting

| Problem | Fix |
| --- | --- |
| `Port 4321 is in use` | Another server is still running. Close that terminal, or use the address Astro prints (e.g. `:4322`). |
| `npm` or `node` not found | Install Node.js 22+, then open a new terminal. |
| Page looks outdated | Reload with `Ctrl + F5`. |
| Photo missing / build error "Photo not found" | The name in `gallery.ts` / `offers.ts` must match a file in `src/assets/photos/` (without `.jpg`). |
| Video does not play on the phone | Phones block autoplay in power-saving mode; the poster image shows instead. That is expected. |
