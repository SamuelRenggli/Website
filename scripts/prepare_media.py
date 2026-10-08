"""Turn the raw photo/video folder into web-ready assets.

Usage (from the repo root):
    py -3.11 scripts/prepare_media.py "Manu Bergführer Content"

Requires: Pillow, pillow-heif (pip install pillow pillow-heif) and ffmpeg on PATH.

- Photos are resized to max 2400 px, re-encoded as JPEG and stripped of all
  metadata (EXIF/GPS). Astro then builds AVIF/WebP variants at build time.
- Videos are cut, scaled and compressed to H.264 MP4 for the web. Snow has
  large smooth gradients, so videos use a low CRF and aq-mode=3 against banding.
- The raw folder is sorted into two subfolders: every file listed in PHOTOS or
  VIDEOS goes to "Auf Website", everything else to "Nicht verwendet".

To add a photo: add a line to PHOTOS below (source file -> web name) and rerun.
The file may sit anywhere in the raw folder; the script finds and sorts it.
Existing outputs are skipped; delete an output file to regenerate it.
"""
import os
import shutil
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
UNUSED_DIR = 'Nicht verwendet'

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
    'drone10_1.7.4.jpg': 'firngrat',
    'drone1_1.1.1.jpg': 'drohne-gipfel',
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
}

# Shared quality settings: CRF ~21-23 keeps snow and sky free of blocks and banding
Q = ['-x264-params', 'aq-mode=3']

# (source, output, ffmpeg args) - all outputs without audio unless noted
VIDEOS = [
    # Hero background loop: muted, 14 s from the 4K ridge flight, three sizes
    ('Alle_ridge.mp4', 'hero-1440.mp4', ['-ss', '15', '-t', '14', '-vf', 'scale=2560:-2', '-an', '-crf', '22', *Q]),
    ('Alle_ridge.mp4', 'hero-1080.mp4', ['-ss', '15', '-t', '14', '-vf', 'scale=1920:-2', '-an', '-crf', '22', *Q]),
    ('Alle_ridge.mp4', 'hero-720.mp4', ['-ss', '15', '-t', '14', '-vf', 'scale=1280:-2', '-an', '-crf', '24', *Q]),
    # Vertical clips (played on demand)
    ('20260205_133024.mp4', 'clip-pulver.mp4', ['-vf', 'scale=1080:-2', '-crf', '22', *Q, '-c:a', 'aac', '-b:a', '128k']),
    # Drone from above, 4K source, silent
    ('Sämi_Tälli1.mp4', 'clip-drohne-spuren.mp4', ['-vf', 'scale=1080:-2', '-an', '-crf', '22', *Q]),
]

# poster frames: (video output, time, poster name)
POSTERS = [
    ('hero-1440.mp4', '0.5', 'hero-poster.jpg'),
    ('clip-pulver.mp4', '1', 'clip-pulver.jpg'),
    ('clip-drohne-spuren.mp4', '12', 'clip-drohne-spuren.jpg'),
]


def find_files(src):
    """Map file name -> full path for everything in the raw folder and its subfolders."""
    return {f: os.path.join(d, f) for d, _, files in os.walk(src) for f in files}


def sort_folder(src):
    """Move used originals to USED_DIR and all others to UNUSED_DIR."""
    used = set(PHOTOS) | {v[0] for v in VIDEOS}
    for name, path in find_files(src).items():
        target = os.path.join(src, USED_DIR if name in used else UNUSED_DIR, name)
        if os.path.normcase(path) != os.path.normcase(target):
            os.makedirs(os.path.dirname(target), exist_ok=True)
            shutil.move(path, target)
    missing = sorted(used - set(find_files(src)))
    if missing:
        print('not in raw folder (existing outputs are kept):', ', '.join(missing))


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
    sort_folder(source)
    photos(source)
    videos(source)
