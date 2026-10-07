// Central place for contact details. Texts in both languages live in src/i18n.ts.
// Everything marked TODO must be confirmed by Manu before going live.

export const site = {
  name: 'Manu am Berg',
  person: 'Manuel Stähelin',
  // TODO: confirm address
  email: 'info@manuelstaehelin.ch',
  // Phone number in international format, e.g. '+41 79 123 45 67'. Leave empty to hide it everywhere.
  phone: '',
  instagram: 'https://www.instagram.com/manuelstaehelin/',
  // Optional form service (e.g. https://formspree.io/f/xxxx). Empty = the form opens the visitor's mail app.
  formEndpoint: '',
  // TODO: postal address for the Impressum (required by Swiss law for commercial sites)
  address: ['Manuel Stähelin', 'Strasse Nr.', 'PLZ Ort', 'Schweiz'],
  ratesUrl: 'https://sbv-asgm.ch/tarife-avb/',
};

/** Prefix an internal path with the deploy base path (needed on github.io/<repo>/). */
export function url(path = '') {
  const base = import.meta.env.BASE_URL.replace(/\/$/, '');
  return `${base}/${path.replace(/^\//, '')}`;
}
