// _src/index.html の中の Tailwind の設定（tailwind.config = {...}）と同じ内容にしておくこと
const path = require('path');
const acShade = (p, shades) => Object.fromEntries(shades.map(s => [s, `rgb(var(--${p}-${s}) / <alpha-value>)`]));
module.exports = {
  content: [path.join(__dirname, '../_src/index.html')],
  theme: {
    extend: {
      colors: {
        accent: acShade('ac', [200, 300, 400, 500, 600, 700]),
        accent2: acShade('ac2', [400, 500, 600]),
        slate: acShade('sl', [50, 100, 200, 300, 400, 500, 600, 700, 800, 900, 950])
      }
    }
  }
};
