// Current season for the page (hero video, offer tabs). The hero sets the starting value from
// the date before anything loads; components follow changes through the "season" event.
export type Season = 'winter' | 'summer';

export const getSeason = () => (document.documentElement.dataset.season as Season | undefined) ?? 'winter';

export function setSeason(season: Season) {
  if (season === getSeason()) return;
  document.documentElement.dataset.season = season;
  document.dispatchEvent(new CustomEvent<Season>('season', { detail: season }));
}

export const onSeason = (fn: (season: Season) => void) =>
  document.addEventListener('season', (e) => fn((e as CustomEvent<Season>).detail));
