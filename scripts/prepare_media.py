"""Turn the raw photo/video folder into web-ready assets.

Usage (from the repo root):
    py -3.11 scripts/prepare_media.py "Manu Bergführer Content"

Requires: Pillow, pillow-heif (pip install pillow pillow-heif) and ffmpeg on PATH.

- Photos are resized to max 2400 px, re-encoded as JPEG and stripped of all
  metadata (EXIF/GPS). Astro then builds AVIF/WebP variants at build time.
- Videos are cut, scaled and compressed to H.264 MP4 for the web. Snow has
  large smooth gradients, so videos use a low CRF and aq-mode=3 against banding.
- The folder "Auf Website" is the selection: its subfolders are themes
  (e.g. Skitouren, Hochtouren). The script writes src/data/themes.json
  (photo -> theme) for the gallery filter, and reports files that are in the
  folder but not in PHOTOS/VIDEOS, or the other way round. It moves nothing.

To add a photo: put it in a theme folder under "Auf Website", add a line to
PHOTOS below (source file -> web name), add it to src/data/gallery.ts, rerun.
Existing outputs are skipped; delete an output file to regenerate it.
"""
import json
import os
import subprocess
import sys

from PIL import Image, ImageOps
import pillow_heif

pillow_heif.register_heif_opener()

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PHOTO_OUT = os.path.join(ROOT, 'src', 'assets', 'photos')
VIDEO_OUT = os.path.join(ROOT, 'public', 'media')
MAX_EDGE = 2400
USED_DIR = 'Auf Website'
THEMES_OUT = os.path.join(ROOT, 'src', 'data', 'themes.json')

# source file name -> output slug
PHOTOS = {
    # portraits
    'tobinmeyers_Innsbruck_1245.jpg': 'manu-portrait',
    # offers: winter
    'tobinmeyers_Innsbruck_1170.jpg': 'skitour-gruppe',
    'tobinmeyers_bellwald_feb_2026_web_6949.jpg': 'freeride-bellwald',
    'IMG_6760.HEIC': 'skihochtour-seil',
    '_DSC3060.jpg': 'skitour-sonne',
    # offers: summer
    '20250710_144919.jpg': 'hochtour-gletscher',
    'Hochtour Coazhütte-2111.jpg': 'grat-coaz',
    'Negative0-18-17A(1).jpg': 'bergtour-see',
    'Hochtour Coazhütte-2146.jpg': 'kurs-felsstufe',
    # gallery
    '20190420_042359548_iOS.jpg': 'panorama-morgen',
    '20250717_090322.jpg': 'gletscher-lachen',
    '20250719_091155.jpg': 'gipfel-jubel',
    '_DSC2815.jpg': 'powder-orange',
    '_DSC2973.jpg': 'steilhang-spray',
    '_DSC3089.jpg': 'seracs',
    'BM3_1.1.6.jpg': 'spuren-drohne',
    'CLA01397.jpg': 'granitturm',
    'CLA01845.jpg': 'trollblume',
    'CLA01940(1).jpg': 'gletscher-blumen',
    'CLA02014(1).jpg': 'felsturm-abend',
    'CLA02046(1).jpg': 'firngipfel',
    'CLA02126.jpg': 'seilschaft-gipfel',
    'IMG_1464.HEIC': 'eisrinne',
    'IMG_2564.HEIC': 'sonnenuntergang',
    'IMG_6743.HEIC': 'skitour-gletscher',
    'IMG_8958.HEIC': 'manu-laerchen',
    'tobinmeyers_bellwald_feb_2026_web_6925.jpg': 'freeride-steil',
    'tobinmeyers_bellwald_feb_2026_web_6944.jpg': 'freeride-sonne',
    'tobinmeyers_Innsbruck_1194.jpg': 'grat-felsband',
    'tobinmeyers_Innsbruck_1352.jpg': 'gleitschirm',
    '20250809_110030.jpg': 'gleitschirm-gipfel',
    'CLA03358.jpg': 'aufstiegsspur',
    'CLA03486.jpg': 'skitour-grat',
    'IMG_3598.HEIC': 'gratkletterei',
    'tobinmeyers_bellwald_feb_2026_web_7162.jpg': 'lachen-brille',
    'Negative0-24-23A(1).jpg': 'schwarznasen',
    'IMG_3594.HEIC': 'gipfelbuch',
    'BM4_1.1.7.jpg': 'spuren-kessel',
    'CLA03348.jpg': 'aufstieg-weit',
    'CLA03355.jpg': 'spur-hochformat',
    'IMG_3318.HEIC': 'grat-sonne',
    '_DSC2972.jpg': 'steilhang',
    'drone12_1.7.6.jpg': 'firngrat-drohne',
    'drone9_1.7.3.jpg': 'firngrat-nah',
    'tobinmeyers_bellwald_feb_2026_web_6839.jpg': 'pulver-wolke',
    'tobinmeyers_bellwald_feb_2026_web_6856.jpg': 'abfahrt-gegenlicht',
    'tobinmeyers_bellwald_feb_2026_web_6926.jpg': 'pulver-schwung',
    'tobinmeyers_bellwald_feb_2026_web_7119.jpg': 'aufstieg-tal',
    'tobinmeyers_bellwald_feb_2026_web_7126.jpg': 'schatten',
    'tobinmeyers_bellwald_feb_2026_web_7147.jpg': 'spur-steil',
    'tobinmeyers_bellwald_feb_2026_web_7578.jpg': 'pulver-schwarzweiss',
}

# Shared quality settings: CRF ~21-23 keeps snow and sky free of blocks and banding
Q = ['-x264-params', 'aq-mode=3']

# (source, output, ffmpeg args) - all outputs without audio unless noted
VIDEOS = [
    # Hero background loop, one film per season (the switch in the hero picks one): muted, three sizes
    ('Intro_website_winter.mp4', 'hero-winter-1440.mp4', ['-vf', 'scale=2560:-2', '-an', '-crf', '22', *Q]),
    ('Intro_website_winter.mp4', 'hero-winter-1080.mp4', ['-vf', 'scale=1920:-2', '-an', '-crf', '22', *Q]),
    ('Intro_website_winter.mp4', 'hero-winter-720.mp4', ['-vf', 'scale=1280:-2', '-an', '-crf', '24', *Q]),
    # Phones in portrait: square centre crop of the 4K source, so less of the sides is lost
    ('Intro_website_winter.mp4', 'hero-winter-mobile.mp4', ['-vf', 'crop=ih:ih,scale=1080:1080', '-an', '-crf', '23', *Q]),
    # Summer source is 1080p, so no 1440 size (the page uses the 1080 file there). It is 44 s of
    # detailed rock, so a higher CRF: 27 looks the same at full screen at 12 MB instead of 30 MB
    ('Intro_website_summer.mp4', 'hero-summer-1080.mp4', ['-an', '-crf', '27', *Q]),
    ('Intro_website_summer.mp4', 'hero-summer-720.mp4', ['-vf', 'scale=1280:-2', '-an', '-crf', '28', *Q]),
    ('Intro_website_summer.mp4', 'hero-summer-mobile.mp4', ['-vf', 'crop=ih:ih', '-an', '-crf', '28', *Q]),
    # Clips (played on demand). Drone, one line down an untouched slope: 4K landscape source, silent,
    # first 10 s (empty slope) cut
    ('Manu.mov', 'clip-linie.mp4', ['-ss', '10', '-vf', 'scale=1920:-2', '-an', '-crf', '23', *Q]),
    # Drone from above, 4K source, silent
    ('Sämi_Tälli1.mp4', 'clip-drohne-spuren.mp4', ['-vf', 'scale=1080:-2', '-an', '-crf', '22', *Q]),
]

# poster frames: (video output, time, poster name)
POSTERS = [
    ('hero-winter-1440.mp4', '0', 'hero-winter-poster.jpg'),
    ('hero-summer-1080.mp4', '0', 'hero-summer-poster.jpg'),
    ('clip-linie.mp4', '26', 'clip-linie.jpg'),
    ('clip-drohne-spuren.mp4', '12', 'clip-drohne-spuren.jpg'),
]


def find_files(src):
    """Map file name -> full path for everything in the raw folder and its subfolders."""
    return {f: os.path.join(d, f) for d, _, files in os.walk(src) for f in files}


def check_folder(src):
    """Compare the "Auf Website" folder with PHOTOS/VIDEOS and write the theme of each photo."""
    used_root = os.path.join(src, USED_DIR)
    in_folder = {f: os.path.relpath(d, used_root) for d, _, files in os.walk(used_root) for f in files}
    listed = set(PHOTOS) | {v[0] for v in VIDEOS}
    for name in sorted(listed - set(in_folder)):
        print(f'listed but not in "{USED_DIR}": {name}')
    for name in sorted(set(in_folder) - listed):
        print(f'in "{USED_DIR}" but not listed in PHOTOS: {in_folder[name]}/{name}')
    themes = {slug: in_folder[name] for name, slug in PHOTOS.items() if in_folder.get(name, '.') != '.'}
    with open(THEMES_OUT, 'w', encoding='utf-8') as f:
        json.dump(dict(sorted(themes.items())), f, ensure_ascii=False, indent=2)
        f.write('\n')


def photos(src):
    os.makedirs(PHOTO_OUT, exist_ok=True)
    files = find_files(src)
    for name, slug in PHOTOS.items():
        out = os.path.join(PHOTO_OUT, slug + '.jpg')
        if os.path.exists(out):
            continue
        im = ImageOps.exif_transpose(Image.open(files[name])).convert('RGB')
        im.thumbnail((MAX_EDGE, MAX_EDGE), Image.LANCZOS)
        im.save(out, 'JPEG', quality=84, progressive=True, optimize=True)  # no exif= -> metadata dropped
        print(f'photo  {slug:24s} {im.width}x{im.height}  {os.path.getsize(out) // 1024} KB')


def videos(src):
    os.makedirs(VIDEO_OUT, exist_ok=True)
    files = find_files(src)
    for name, out_name, args in VIDEOS:
        out = os.path.join(VIDEO_OUT, out_name)
        if os.path.exists(out):
            continue
        cmd = ['ffmpeg', '-y', '-loglevel', 'error', '-i', files[name], '-map_metadata', '-1',
               '-c:v', 'libx264', '-preset', 'slow', '-pix_fmt', 'yuv420p', '-movflags', '+faststart', *args, out]
        subprocess.run(cmd, check=True)
        print(f'video  {out_name:24s} {os.path.getsize(out) // 1024} KB')
    for vid, t, poster in POSTERS:
        out = os.path.join(VIDEO_OUT, poster)
        if os.path.exists(out):
            continue
        subprocess.run(['ffmpeg', '-y', '-loglevel', 'error', '-ss', t, '-i', os.path.join(VIDEO_OUT, vid),
                        '-frames:v', '1', '-q:v', '3', out], check=True)
        print(f'poster {poster:24s} {os.path.getsize(out) // 1024} KB')


if __name__ == '__main__':
    source = sys.argv[1] if len(sys.argv) > 1 else os.path.join(ROOT, 'Manu Bergführer Content')
    check_folder(source)
    photos(source)
    videos(source)
