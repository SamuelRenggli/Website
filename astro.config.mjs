// @ts-check
import { defineConfig } from 'astro/config';
import sitemap from '@astrojs/sitemap';

// `site` and `base` are passed by the GitHub Actions workflow (astro build --site --base),
// so the same code works on https://<user>.github.io/<repo>/ and on https://manuelstaehelin.ch/.
export default defineConfig({
  site: 'https://manuelstaehelin.ch',
  trailingSlash: 'ignore',
  build: { format: 'directory' },
  image: {
    responsiveStyles: false,
  },
  integrations: [
    sitemap({
      i18n: { defaultLocale: 'de', locales: { de: 'de-CH', en: 'en' } },
      filter: (page) => !page.includes('/404'),
    }),
  ],
});
