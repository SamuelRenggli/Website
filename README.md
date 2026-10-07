# Manu am Berg

Website von Manuel Stähelin, Bergführer: <https://manuelstaehelin.ch>

Gebaut mit [Astro](https://astro.build), gehostet auf GitHub Pages. Jeder Push auf `main` wird automatisch
veröffentlicht (siehe Tab **Actions** auf GitHub, dauert ca. 2 bis 4 Minuten).

## Lokal starten

Voraussetzung: [Node.js](https://nodejs.org) 22 oder neuer.

```bash
npm install
npm run dev        # Vorschau mit Live-Reload auf http://localhost:4321
npm run build      # fertige Website in dist/
```

## Wo ändere ich was?

| Was | Datei |
| --- | --- |
| E-Mail, Telefon, Instagram, Adresse, Formular-Dienst | `src/config.ts` |
| Angebote Winter / Sommer | `src/data/offers.ts` |
| Fotos in der Galerie (Reihenfolge, Beschreibung) | `src/data/gallery.ts` |
| Text "Über mich" | `src/components/About.astro` |
| Startbild-Text und Video | `src/components/Hero.astro` |
| Farben, Schrift | `src/styles/global.css` |
| Impressum / Datenschutz | `src/pages/impressum.astro`, `src/pages/datenschutz.astro` |

Kleine Textänderungen gehen auch direkt im Browser auf github.com: Datei öffnen, Stift-Symbol, ändern,
"Commit changes". Die Website aktualisiert sich danach automatisch.

## Neue Fotos oder Videos

Die Originale liegen lokal im Ordner `Manu Bergführer Content/` (nicht im Git, zu gross).

1. Neues Foto in diesen Ordner legen.
2. In `scripts/prepare_media.py` bei `PHOTOS` eine Zeile ergänzen: `'Dateiname.jpg': 'kurzer-name',`
3. `npm run media` ausführen (braucht Python mit `pip install pillow pillow-heif` und ffmpeg).
   Das Skript verkleinert die Fotos und entfernt GPS-Daten.
4. Foto in `src/data/gallery.ts` oder `src/data/offers.ts` mit `kurzer-name` eintragen.
5. Committen und pushen.

## Domain

Die Domain `manuelstaehelin.ch` ist bei Metanet registriert. Für GitHub Pages zeigen die DNS-Einträge auf GitHub:

| Typ | Name | Wert |
| --- | --- | --- |
| A | @ | 185.199.108.153 |
| A | @ | 185.199.109.153 |
| A | @ | 185.199.110.153 |
| A | @ | 185.199.111.153 |
| CNAME | www | `<github-user>.github.io` |

Danach auf GitHub: Settings, Pages, Custom domain `manuelstaehelin.ch`, "Enforce HTTPS" aktivieren.
