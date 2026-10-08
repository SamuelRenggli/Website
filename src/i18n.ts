// All interface text in German and English. German is the default language (served at /),
// English lives under /en/.
import { url } from './config';

export type Lang = 'de' | 'en';
export const langs: Lang[] = ['de', 'en'];

/** Text in both languages */
export type L10n = Record<Lang, string>;

/** Path for a page in the given language, e.g. localePath('en', 'impressum/') -> /en/impressum/ */
export function localePath(lang: Lang, path = '') {
  return url(lang === 'de' ? path : `en/${path.replace(/^\//, '')}`);
}

/** Same page in the other language (pages share slugs across languages) */
export function switchPath(lang: Lang, pathname: string) {
  const base = import.meta.env.BASE_URL.replace(/\/$/, '');
  let rest = pathname.startsWith(base) ? pathname.slice(base.length) : pathname;
  rest = rest.replace(/^\/(en\/?)?/, '');
  return localePath(lang === 'de' ? 'en' : 'de', rest);
}

export const ui = {
  de: {
    htmlLang: 'de-CH',
    ogLocale: 'de_CH',
    skip: 'Zum Inhalt springen',
    nav: { offers: 'Angebot', about: 'Über mich', clips: 'Filme', gallery: 'Galerie' },
    navLabel: 'Hauptnavigation',
    cta: 'Tour anfragen',
    menuOpen: 'Menü öffnen',
    menuClose: 'Menü schliessen',
    switchLabel: 'English version',
    role: 'Bergführer',
    description:
      'Manuel Stähelin, Bergführer. Skitouren, Freeride, Hochtouren und Klettern in den Schweizer Alpen.',
    hero: {
      kicker: 'Bergführer · Schweizer Alpen',
      sub: 'Skitouren, Freeride, Hochtouren und Klettern. Sorgfältig geplant nach Verhältnissen und deinem Können, privat oder in kleinen Gruppen.',
      secondary: 'Angebot ansehen',
      pause: 'Hintergrundvideo anhalten',
      play: 'Hintergrundvideo abspielen',
    },
    offers: {
      title: 'Angebot',
      seasonLabel: 'Saison wählen',
      winter: 'Winter',
      summer: 'Sommer',
      note: 'Alle Touren führe ich privat oder in kleinen Gruppen. Daten auf Anfrage.',
      rates: 'Tarife',
      ratesText: 'Ich arbeite nach den Tarifen und Allgemeinen Vertragsbedingungen des Schweizer Bergführerverbands.',
      ratesLink: 'SBV-Tarife',
      avbLink: 'AVB (PDF)',
      avbUrl: 'https://sbv-asgm.ch/wp-content/uploads/6_AVB_de_20220131.pdf',
    },
    about: {
      title: 'Ich bin Manuel, dein Bergführer.',
      lede: 'Bergführer, Ingenieur und am liebsten dort, wo die Spur noch frisch ist.',
      p1: 'Schon früh zog es mich in die Berge: Mit sechs Jahren stand ich mit meinem Vater auf dem Piz Kesch, meiner ersten Bergtour. Nach dem Gymnasium und dem Maschinenbaustudium an der ETH habe ich mich für die Ausbildung zum Bergführer entschieden.',
      p2: 'Sicherheit am Berg steht für mich an erster Stelle. Ich plane jede Tour nach den aktuellen Verhältnissen und nach dem, was du dir vorstellst, damit du unterwegs etwas lernst und den Tag am Berg geniesst.',
      facts: [
        ['Erste Bergtour', 'Piz Kesch, mit 6 Jahren'],
        ['Studium', 'Maschinenbau, ETH Zürich'],
        ['Heute', 'Bergführer in den Schweizer Alpen'],
      ],
      portraitAlt: 'Manuel Stähelin in oranger Jacke vor einem Wolkenmeer',
    },
    clips: {
      title: 'Unterwegs gefilmt',
      lede: 'Kurze Clips von Touren der letzten Winter.',
      play: 'Video abspielen',
    },
    gallery: {
      title: 'Galerie',
      filterLabel: 'Fotos nach Thema filtern',
      all: 'Alle',
      // Keys are the theme folder names in "Auf Website"
      themes: { Skitouren: 'Skitouren', Skihochtouren: 'Skihochtouren', Hochtouren: 'Hochtouren', Gratkletterei: 'Gratklettern' } as Record<string, string>,
      more: (n: number) => `Alle ${n} Fotos zeigen`,
      dialog: 'Foto vergrössert',
      close: 'Schliessen',
      prev: 'Vorheriges Foto',
      next: 'Nächstes Foto',
    },
    contact: {
      title: 'Kontakt',
      steps: [
        { title: 'Anfrage', text: 'Schreib mir, was du vorhast: Ziel, Zeitraum, Erfahrung und wie viele ihr seid.' },
        { title: 'Planung', text: 'Ich schlage dir eine passende Tour vor und kläre Verhältnisse, Hütte und Ausrüstung.' },
        { title: 'Unterwegs', text: 'Wir treffen uns am Ausgangspunkt und gehen los. Ich schaue unterwegs auf Wetter, Schnee und Tempo.' },
      ],
      name: 'Name',
      nameErr: 'Bitte gib deinen Namen an.',
      email: 'E-Mail',
      emailErr: 'Bitte gib eine gültige E-Mail-Adresse an.',
      offer: 'Was möchtest du machen?',
      other: 'Etwas anderes',
      date: 'Wunschdatum',
      datePh: 'z.B. Mitte Februar',
      msg: 'Nachricht',
      msgHint: 'Ziel, Erfahrung, Anzahl Personen: alles, was mir bei der Planung hilft.',
      msgErr: 'Bitte schreib mir kurz, was du vorhast.',
      submit: 'Anfrage senden',
      mailOpened: 'Dein Mailprogramm öffnet sich mit der fertigen Anfrage.',
      sending: 'Anfrage wird gesendet …',
      sent: 'Danke, deine Anfrage ist angekommen. Ich melde mich so bald wie möglich.',
      failed: 'Senden hat nicht geklappt. Schreib mir bitte direkt an',
      subject: 'Anfrage',
      mailLabels: { name: 'Name', email: 'E-Mail', offer: 'Angebot', date: 'Wunschdatum' },
    },
    footer: {
      photos: 'Fotos: Samuel Renggli, Tobin Meyers',
      imprint: 'Impressum',
      privacy: 'Datenschutz',
    },
    notFound: { title: 'Seite nicht gefunden', text: 'Diese Seite gibt es nicht oder nicht mehr.', home: 'Zur Startseite' },
  },
  en: {
    htmlLang: 'en',
    ogLocale: 'en_GB',
    skip: 'Skip to content',
    nav: { offers: 'Tours', about: 'About', clips: 'Films', gallery: 'Gallery' },
    navLabel: 'Main navigation',
    cta: 'Book a tour',
    menuOpen: 'Open menu',
    menuClose: 'Close menu',
    switchLabel: 'Deutsche Version',
    role: 'Mountain guide',
    description:
      'Manuel Stähelin, mountain guide. Ski touring, freeride, alpine tours and climbing in the Swiss Alps.',
    hero: {
      kicker: 'Mountain guide · Swiss Alps',
      sub: 'Ski touring, freeride, alpine tours and climbing. Carefully planned around conditions and your skills, private or in small groups.',
      secondary: 'See tours',
      pause: 'Pause background video',
      play: 'Play background video',
    },
    offers: {
      title: 'Tours',
      seasonLabel: 'Choose season',
      winter: 'Winter',
      summer: 'Summer',
      note: 'All tours are private or in small groups. Dates on request.',
      rates: 'Rates',
      ratesText: 'I work with the rates and general terms of the Swiss Mountain Guides Association (SBV).',
      ratesLink: 'SBV rates',
      avbLink: 'Terms (PDF, German)',
      avbUrl: 'https://sbv-asgm.ch/wp-content/uploads/6_AVB_de_20220131.pdf',
    },
    about: {
      title: 'I’m Manuel, your mountain guide.',
      lede: 'Mountain guide, engineer, and happiest where the track is still fresh.',
      p1: 'The mountains pulled me in early: at six I climbed Piz Kesch with my father, my first mountain tour. After high school and a degree in mechanical engineering at ETH Zurich, I decided to train as a mountain guide.',
      p2: 'Safety in the mountains comes first for me. I plan every tour around current conditions and what you have in mind, so you learn something along the way and enjoy your day out.',
      facts: [
        ['First summit', 'Piz Kesch, aged 6'],
        ['Studied', 'Mechanical engineering, ETH Zurich'],
        ['Today', 'Mountain guide in the Swiss Alps'],
      ],
      portraitAlt: 'Manuel Stähelin in an orange jacket above a sea of clouds',
    },
    clips: {
      title: 'On film',
      lede: 'Short clips from tours of the last few winters.',
      play: 'Play video',
    },
    gallery: {
      title: 'Gallery',
      filterLabel: 'Filter photos by theme',
      all: 'All',
      themes: { Skitouren: 'Ski touring', Skihochtouren: 'Ski mountaineering', Hochtouren: 'Alpine tours', Gratkletterei: 'Ridge climbing' } as Record<string, string>,
      more: (n: number) => `Show all ${n} photos`,
      dialog: 'Enlarged photo',
      close: 'Close',
      prev: 'Previous photo',
      next: 'Next photo',
    },
    contact: {
      title: 'Contact',
      steps: [
        { title: 'Request', text: 'Tell me what you have in mind: goal, dates, experience and group size.' },
        { title: 'Planning', text: 'I suggest a suitable tour and sort out conditions, huts and equipment.' },
        { title: 'On the mountain', text: 'We meet at the trailhead and set off. I keep an eye on weather, snow and pace.' },
      ],
      name: 'Name',
      nameErr: 'Please enter your name.',
      email: 'Email',
      emailErr: 'Please enter a valid email address.',
      offer: 'What would you like to do?',
      other: 'Something else',
      date: 'Preferred date',
      datePh: 'e.g. mid February',
      msg: 'Message',
      msgHint: 'Goal, experience, number of people: anything that helps me plan.',
      msgErr: 'Please tell me briefly what you have in mind.',
      submit: 'Send request',
      mailOpened: 'Your email app opens with the request filled in.',
      sending: 'Sending request …',
      sent: 'Thanks, your request has arrived. I’ll get back to you as soon as possible.',
      failed: 'Sending failed. Please email me directly at',
      subject: 'Request',
      mailLabels: { name: 'Name', email: 'Email', offer: 'Tour', date: 'Preferred date' },
    },
    footer: {
      photos: 'Photos: Samuel Renggli, Tobin Meyers',
      imprint: 'Imprint',
      privacy: 'Privacy',
    },
    notFound: { title: 'Page not found', text: 'This page does not exist or has moved.', home: 'Back to home' },
  },
} as const;
