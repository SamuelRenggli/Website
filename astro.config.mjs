// @ts-check
import { defineConfig } from 'astro/config';

// `site` and `base` are passed by the GitHub Actions workflow (astro build --site --base),
// so the same code works on https://<user>.github.io/<repo>/ and on https://manuelstaehelin.ch/.
export default defineConfig({
  site: 'https://manuelstaehelin.ch',
  trailingSlash: 'ignore',
  build: { format: 'directory' },
  image: {
    responsiveStyles: false,
  },
});
