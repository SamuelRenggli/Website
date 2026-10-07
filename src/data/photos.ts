import type { ImageMetadata } from 'astro';

const files = import.meta.glob<{ default: ImageMetadata }>('../assets/photos/*.jpg', { eager: true });

/** Look up a prepared photo by its slug (file name without .jpg). */
export function photo(slug: string): ImageMetadata {
  const file = files[`../assets/photos/${slug}.jpg`];
  if (!file) throw new Error(`Photo "${slug}" not found in src/assets/photos`);
  return file.default;
}
