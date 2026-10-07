// Central place for contact details and site-wide text.
// Everything marked TODO must be confirmed by Manu before going live.

export const site = {
  name: 'Manu am Berg',
  person: 'Manuel Stähelin',
  // TODO: confirm exact title / qualification
  role: 'Bergführer mit eidg. Fachausweis',
  description:
    'Manuel Stähelin, Bergführer. Skitouren, Freeride, Hochtouren und Klettern in den Schweizer Alpen.',
  // TODO: confirm address
  email: 'info@manuelstaehelin.ch',
  // TODO: add phone in international format, e.g. '+41 79 123 45 67' (empty = hidden)
  phone: '',
  // TODO: add Instagram URL (empty = hidden)
  instagram: '',
  // Optional form service (e.g. https://formspree.io/f/xxxx). Empty = the form opens the visitor's mail app.
  formEndpoint: '',
  // TODO: postal address for the Impressum (required by Swiss law for commercial sites)
  address: ['Manuel Stähelin', 'Strasse Nr.', 'PLZ Ort', 'Schweiz'],
};

/** Prefix an internal path with the deploy base path (needed on github.io/<repo>/). */
export function url(path = '') {
  const base = import.meta.env.BASE_URL.replace(/\/$/, '');
  return `${base}/${path.replace(/^\//, '')}`;
}
