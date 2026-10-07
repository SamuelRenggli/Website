export interface Offer {
  title: string;
  text: string;
  season: string;
  photo: string;
  alt: string;
}

// TODO: Manu to confirm offers, seasons and add prices or "ab CHF ..." per offer.
export const winter: Offer[] = [
  {
    title: 'Skitouren',
    text: 'Vom ersten Aufstieg mit Fellen bis zur mehrtägigen Durchquerung. Ich plane die Route nach Verhältnissen und deinem Können.',
    season: 'Dezember bis April',
    photo: 'skitour-gruppe',
    alt: 'Eine Gruppe steigt mit Ski und Fellen im Nebel einen Hang hinauf',
  },
  {
    title: 'Freeride',
    text: 'Unverspurte Hänge abseits der Piste, mit sorgfältiger Lawinenbeurteilung und klarer Linienwahl.',
    season: 'Januar bis April',
    photo: 'freeride-bellwald',
    alt: 'Skifahrer in orangem Anzug fährt durch tiefen Pulverschnee',
  },
  {
    title: 'Skihochtouren',
    text: 'Mit Ski über Gletscher auf hohe Gipfel. Seil, Steigeisen und Spaltenrettung gehören dazu.',
    season: 'März bis Mai',
    photo: 'skihochtour-seil',
    alt: 'Seilschaft mit Ski steigt einen steilen Firnhang unter blauem Himmel hinauf',
  },
  {
    title: 'Lawinenkurse',
    text: 'Bulletin lesen, Gelände beurteilen, Verschüttetensuche üben. Damit du draussen selbst gute Entscheide triffst.',
    season: 'Dezember bis März',
    photo: 'skitour-sonne',
    alt: 'Aufstiegsspur im Gegenlicht der Sonne',
  },
];

export const summer: Offer[] = [
  {
    title: 'Hochtouren',
    text: 'Gletscher, Firn und Fels. Klassische Hochtouren für Einsteiger und Erfahrene, mit Übernachtung in der Hütte.',
    season: 'Juni bis September',
    photo: 'hochtour-gletscher',
    alt: 'Seilschaft quert einen zerklüfteten Gletscher',
  },
  {
    title: 'Gratklettern',
    text: 'Ausgesetzte Grate am kurzen Seil, mit viel Fels unter den Händen und Weitblick zu beiden Seiten.',
    season: 'Juli bis September',
    photo: 'grat-coaz',
    alt: 'Zwei Bergsteiger klettern über einen Felsgrat',
  },
  {
    title: 'Bergtouren',
    text: 'Weglose Übergänge und Gipfel ohne Gletscher. Ideal, um das Hochgebirge kennenzulernen.',
    season: 'Juni bis Oktober',
    photo: 'bergtour-wiese',
    alt: 'Zwei Bergsteiger auf einer Alpwiese vor verschneiten Gipfeln',
  },
  {
    title: 'Kurse',
    text: 'Hochtouren- und Kletterkurse: Seiltechnik, Spaltenbergung und Standplatzbau, Schritt für Schritt.',
    season: 'Juni bis September',
    photo: 'ausbildung-hand',
    alt: 'Ein Bergsteiger hilft einem anderen mit der Hand über eine Felsstufe',
  },
];
