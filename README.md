# Manu am Berg

Website von Manuel Stähelin, Bergführer: <https://manuelstaehelin.ch>

Deutsch unter `/`, Englisch unter `/en/`. Gebaut mit [Astro](https://astro.build), gehostet auf GitHub Pages.
**Lokal testen:** siehe [TESTING.md](TESTING.md). **Live schalten:** siehe [GO-LIVE.md](GO-LIVE.md). **Offene Punkte:** [TODO.md](TODO.md). Jeder Push auf `main` wird automatisch
veröffentlicht (siehe Tab **Actions** auf GitHub, dauert ca. 2 bis 4 Minuten).

## Lokal starten

Voraussetzung: [Node.js](https://nodejs.org) 22 oder neuer.

```bash
npm install
npm run dev        # Vorschau mit Live-Reload auf http://localhost:4321
npm run build      # prüft den Code und baut die fertige Website in dist/
```

## Wo ändere ich was?

| Was | Datei |
| --- | --- |
| E-Mail, Telefon (leer = ausgeblendet), Instagram, Adresse, Formular-Dienst | `src/config.ts` |
| Alle Texte Deutsch + Englisch (Startbild, Über mich, Kontakt, Menü) | `src/i18n.ts` |
| Angebote Winter / Sommer (DE + EN) | `src/data/offers.ts` |
| Fotos in der Galerie (Reihenfolge, Beschreibung DE + EN) | `src/data/gallery.ts` |
| Startbild-Video | `src/components/Hero.astro` |
| Farben, Schrift | `src/styles/global.css` |
| Impressum / Datenschutz | `src/pages/impressum.astro`, `src/pages/datenschutz.astro`, Englisch in `src/pages/en/` |

Kleine Textänderungen gehen auch direkt im Browser auf github.com: Datei öffnen, Stift-Symbol, ändern,
"Commit changes". Die Website aktualisiert sich danach automatisch.

## Neue Fotos oder Videos

Die Originale liegen lokal im Ordner `Manu Bergführer Content/` (nicht im Git, zu gross).

Was auf der Website ist, bestimmt der Ordner **`Auf Website`**. Seine Unterordner sind die Themen
(Skitouren, Skihochtouren, Hochtouren, Gratkletterei); danach filtert die Galerie. Alles andere liegt in
**`Nicht verwendet`**. Das Skript verschiebt nichts, es meldet nur, wenn Ordner und Liste nicht zusammenpassen.

1. Neues Foto in den passenden Themenordner unter `Auf Website` legen (neues Thema = neuer Ordner,
   Name dann auch in `src/i18n.ts` bei `gallery.themes` eintragen).
2. In `scripts/prepare_media.py` bei `PHOTOS` eine Zeile ergänzen: `'Dateiname.jpg': 'kurzer-name',`
3. `npm run media` ausführen (braucht Python mit `pip install pillow pillow-heif` und ffmpeg).
   Das Skript verkleinert die Fotos, entfernt GPS-Daten und liest das Thema aus dem Ordner.
4. Foto in `src/data/gallery.ts` oder `src/data/offers.ts` mit `kurzer-name` eintragen.
5. Committen und pushen.

## Domain

Domain und DNS-Umstellung bei Metanet: siehe [GO-LIVE.md](GO-LIVE.md).
