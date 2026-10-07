"""Turn the raw photo/video folder into web-ready assets.

Usage (from the repo root):
    py -3.11 scripts/prepare_media.py "Manu Bergführer Content"

Requires: Pillow, pillow-heif (pip install pillow pillow-heif) and ffmpeg on PATH.

- Photos are resized to max 2400 px, re-encoded as JPEG and stripped of all
  metadata (EXIF/GPS). Astro then builds AVIF/WebP variants at build time.
- Videos are cut, scaled and compressed to H.264 MP4 for the web.

To add a photo: add a line to PHOTOS below (source file -> web name) and rerun.
Existing outputs are skipped; delete an output file to regenerate it.
"""
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

# source file name -> output slug
PHOTOS = {
    # portraits
    'tobinmeyers_Innsbruck_1245.jpg': 'manu-portrait',
    'tobinmeyers_Innsbruck_1254.jpg': 'manu-portrait-arms',
    'tobinmeyers_Innsbruck_1165.jpg': 'manu-hood',
    'CLA02078.jpg': 'manu-brot',
    # offers: winter
    'tobinmeyers_Innsbruck_1170.jpg': 'skitour-gruppe',
    'tobinmeyers_bellwald_feb_2026_web_6949.jpg': 'freeride-bellwald',
    'IMG_6760.HEIC': 'skihochtour-seil',
    '_DSC3060.jpg': 'skitour-sonne',
    # offers: summer
    '20250710_144919.jpg': 'hochtour-gletscher',
    'Hochtour Coazhütte-2111.jpg': 'grat-coaz',
    'CLA01868(1).jpg': 'bergtour-wiese',
    'CLA01983(1).jpg': 'ausbildung-hand',
    # gallery
    '20190420_042359548_iOS.jpg': 'panorama-morgen',
    '20190420_104320.jpg': 'gipfelblick',
    '20230610_152711.jpg': 'gipfelkreuz-nebel',
    '20250717_090322.jpg': 'gletscher-lachen',
    '20250719_091155.jpg': 'gipfel-jubel',
    '_DSC2815.jpg': 'powder-orange',
    '_DSC2972.jpg': 'steilhang',
    '_DSC2973.jpg': 'steilhang-spray',
    '_DSC3089.jpg': 'seracs',
    'BM3_1.1.6.jpg': 'spuren-drohne',
    'BM4_1.1.7.jpg': 'spuren-kessel',
    'CLA01399.jpg': 'gipfelkreuz-wolken',
    'CLA01397.jpg': 'granitturm',
    'CLA01845.jpg': 'trollblume',
    'CLA01940(1).jpg': 'gletscher-blumen',
    'CLA01966.jpg': 'gipfel-freude',
    'CLA02014(1).jpg': 'felsturm-abend',
    'CLA02046(1).jpg': 'firngipfel',
    'CLA02126.jpg': 'seilschaft-gipfel',
    'drone10_1.7.4.jpg': 'firngrat',
    'drone13_1.7.7_1.7.8-Bearbeitet-2.jpg': 'firngrat-weit',
    'drone1_1.1.1.jpg': 'drohne-gipfel',
    'IMG_1464.HEIC': 'eisrinne',
    'IMG_2564.HEIC': 'sonnenuntergang',
    'IMG_6743.HEIC': 'skitour-gletscher',
    'IMG_8958.HEIC': 'manu-laerchen',
    'tobinmeyers_bellwald_feb_2026_web_6925.jpg': 'freeride-steil',
    'tobinmeyers_bellwald_feb_2026_web_6944.jpg': 'freeride-sonne',
    'tobinmeyers_Innsbruck_1194.jpg': 'grat-felsband',
    'tobinmeyers_Innsbruck_1352.jpg': 'gleitschirm',
}

# (source, output, ffmpeg args) - all outputs without audio unless noted
VIDEOS = [
    # Hero background loop: muted, 14 s, two sizes
    ('Manu_TriiMannli.mp4', 'hero-1080.mp4', ['-ss', '0', '-t', '14', '-vf', 'scale=1920:-2', '-an', '-crf', '27']),
    ('Manu_TriiMannli.mp4', 'hero-720.mp4', ['-ss', '0', '-t', '14', '-vf', 'scale=1280:-2', '-an', '-crf', '28']),
    # Vertical clips (with audio, played on demand)
    ('Fafler2.mp4', 'clip-fafler-abfahrt.mp4', ['-vf', 'scale=720:-2', '-crf', '27', '-c:a', 'aac', '-b:a', '96k']),
    ('Fafler1.mp4', 'clip-fafler-wald.mp4', ['-vf', 'scale=720:-2', '-crf', '27', '-c:a', 'aac', '-b:a', '96k']),
    ('20260205_133024.mp4', 'clip-pulver.mp4', ['-vf', 'scale=720:-2', '-crf', '26', '-c:a', 'aac', '-b:a', '96k']),
]

# poster frames: (video output, time, poster name)
POSTERS = [
    ('hero-1080.mp4', '0.5', 'hero-poster.jpg'),
    ('clip-fafler-abfahrt.mp4', '6', 'clip-fafler-abfahrt.jpg'),
    ('clip-fafler-wald.mp4', '20', 'clip-fafler-wald.jpg'),
    ('clip-pulver.mp4', '1', 'clip-pulver.jpg'),
]


def photos(src):
    os.makedirs(PHOTO_OUT, exist_ok=True)
    for name, slug in PHOTOS.items():
        out = os.path.join(PHOTO_OUT, slug + '.jpg')
        if os.path.exists(out):
            continue
        im = ImageOps.exif_transpose(Image.open(os.path.join(src, name))).convert('RGB')
        im.thumbnail((MAX_EDGE, MAX_EDGE), Image.LANCZOS)
        im.save(out, 'JPEG', quality=84, progressive=True, optimize=True)  # no exif= -> metadata dropped
        print(f'photo  {slug:24s} {im.width}x{im.height}  {os.path.getsize(out) // 1024} KB')


def videos(src):
    os.makedirs(VIDEO_OUT, exist_ok=True)
    for name, out_name, args in VIDEOS:
        out = os.path.join(VIDEO_OUT, out_name)
        if os.path.exists(out):
            continue
        cmd = ['ffmpeg', '-y', '-loglevel', 'error', '-i', os.path.join(src, name), '-map_metadata', '-1',
               '-c:v', 'libx264', '-preset', 'slow', '-pix_fmt', 'yuv420p', '-movflags', '+faststart', *args, out]
        subprocess.run(cmd, check=True)
        print(f'video  {out_name:24s} {os.path.getsize(out) // 1024} KB')
    for vid, t, poster in POSTERS:
        out = os.path.join(VIDEO_OUT, poster)
        if os.path.exists(out):
            continue
        subprocess.run(['ffmpeg', '-y', '-loglevel', 'error', '-ss', t, '-i', os.path.join(VIDEO_OUT, vid),
                        '-frames:v', '1', '-q:v', '4', out], check=True)
        print(f'poster {poster:24s} {os.path.getsize(out) // 1024} KB')


if __name__ == '__main__':
    source = sys.argv[1] if len(sys.argv) > 1 else os.path.join(ROOT, 'Manu Bergführer Content')
    photos(source)
    videos(source)
