import type { L10n } from '../i18n';

export interface Offer {
  title: L10n;
  text: L10n;
  season: L10n;
  photo: string;
  alt: L10n;
}

// TODO: Manu to confirm offers and seasons.
export const winter: Offer[] = [
  {
    title: { de: 'Skitouren', en: 'Ski touring' },
    text: {
      de: 'Vom ersten Aufstieg mit Fellen bis zur mehrtägigen Durchquerung. Ich plane die Route nach Verhältnissen und deinem Können.',
      en: 'From your first climb on skins to multi-day traverses. I plan the route around conditions and your skills.',
    },
    season: { de: 'Dezember bis April', en: 'December to April' },
    photo: 'skitour-gruppe',
    alt: {
      de: 'Eine Gruppe steigt mit Ski und Fellen im Nebel einen Hang hinauf',
      en: 'A group skinning up a slope in the fog',
    },
  },
  {
    title: { de: 'Freeride', en: 'Freeride' },
    text: {
      de: 'Unverspurte Hänge abseits der Piste, mit sorgfältiger Lawinenbeurteilung und klarer Linienwahl.',
      en: 'Untracked slopes away from the pistes, with careful avalanche assessment and well-chosen lines.',
    },
    season: { de: 'Januar bis April', en: 'January to April' },
    photo: 'freeride-bellwald',
    alt: { de: 'Skifahrer in orangem Anzug fährt durch tiefen Pulverschnee', en: 'Skier in orange riding deep powder' },
  },
  {
    title: { de: 'Skihochtouren', en: 'Ski mountaineering' },
    text: {
      de: 'Mit Ski über Gletscher auf hohe Gipfel. Seil, Steigeisen und Spaltenrettung gehören dazu.',
      en: 'On skis across glaciers to high summits, with rope, crampons and crevasse rescue.',
    },
    season: { de: 'März bis Mai', en: 'March to May' },
    photo: 'skihochtour-seil',
    alt: {
      de: 'Seilschaft mit Ski steigt einen steilen Firnhang unter blauem Himmel hinauf',
      en: 'Roped team on skis climbing a steep snow slope under a blue sky',
    },
  },
  {
    title: { de: 'Lawinenkurse', en: 'Avalanche courses' },
    text: {
      de: 'Bulletin lesen, Gelände beurteilen, Verschüttetensuche üben. Damit du draussen selbst gute Entscheide triffst.',
      en: 'Reading the bulletin, judging terrain, practising transceiver search, so you can make good decisions yourself.',
    },
    season: { de: 'Dezember bis März', en: 'December to March' },
    photo: 'skitour-sonne',
    alt: { de: 'Aufstiegsspur im Gegenlicht der Sonne', en: 'Skin track against the sun' },
  },
];

export const summer: Offer[] = [
  {
    title: { de: 'Hochtouren', en: 'Alpine tours' },
    text: {
      de: 'Gletscher, Firn und Fels. Klassische Hochtouren für Einsteiger und Erfahrene, mit Übernachtung in der Hütte.',
      en: 'Glacier, snow and rock. Classic alpine tours for beginners and experienced climbers, with a night in a hut.',
    },
    season: { de: 'Juni bis September', en: 'June to September' },
    photo: 'hochtour-gletscher',
    alt: { de: 'Seilschaft quert einen zerklüfteten Gletscher', en: 'Roped team crossing a crevassed glacier' },
  },
  {
    title: { de: 'Gratklettern', en: 'Ridge climbing' },
    text: {
      de: 'Ausgesetzte Grate am kurzen Seil, mit viel Fels unter den Händen und Weitblick zu beiden Seiten.',
      en: 'Exposed ridges on a short rope, plenty of rock under your hands and views on both sides.',
    },
    season: { de: 'Juli bis September', en: 'July to September' },
    photo: 'grat-coaz',
    alt: { de: 'Zwei Bergsteiger klettern über einen Felsgrat', en: 'Two climbers scrambling along a rocky ridge' },
  },
  {
    title: { de: 'Bergtouren', en: 'Mountain hikes' },
    text: {
      de: 'Weglose Übergänge und Gipfel ohne Gletscher. Ideal, um das Hochgebirge kennenzulernen.',
      en: 'Off-trail passes and summits without glaciers. A great way to get to know the high mountains.',
    },
    season: { de: 'Juni bis Oktober', en: 'June to October' },
    photo: 'bergtour-wiese',
    alt: {
      de: 'Zwei Bergsteiger auf einer Alpwiese vor verschneiten Gipfeln',
      en: 'Two hikers on an alpine meadow below snowy peaks',
    },
  },
  {
    title: { de: 'Kurse', en: 'Courses' },
    text: {
      de: 'Hochtouren- und Kletterkurse: Seiltechnik, Spaltenbergung und Standplatzbau, Schritt für Schritt.',
      en: 'Alpine and climbing courses: rope work, crevasse rescue and building anchors, step by step.',
    },
    season: { de: 'Juni bis September', en: 'June to September' },
    photo: 'ausbildung-hand',
    alt: {
      de: 'Ein Bergsteiger hilft einem anderen mit der Hand über eine Felsstufe',
      en: 'One climber giving another a hand up a rock step',
    },
  },
];
