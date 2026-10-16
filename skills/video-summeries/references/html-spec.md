# HTML Page Specification

## Dark Theme CSS Variables

```css
:root {
  --bg: #0d1117; --surface: #161b22; --surface2: #21262d;
  --border: #30363d; --accent: #58a6ff; --green: #3fb950;
  --yellow: #d29922; --red: #f85149; --orange: #f0883e;
  --purple: #bc8cff; --text: #e6edf3; --muted: #8b949e;
}
```

## Badge Classes

```css
.badge-en     { background: #0d3320; color: var(--green); }   /* English */
.badge-he     { background: #1a3a5c; color: var(--accent); }   /* Hebrew */
.badge-biz    { background: #2d1a5c; color: #bc8cff; }         /* Business */
.badge-stocks { background: #2d2000; color: var(--yellow); }   /* Stocks */
.badge-ai     { background: #1a2744; color: var(--accent); }   /* AI */
.badge-macro  { background: #3d1a1a; color: var(--red); }      /* Macro */
.badge-solo   { background: #1a2030; color: var(--accent); }   /* Solo */
.badge-energy { background: #2d1a00; color: var(--orange); }   /* Energy */
.badge-saas   { background: #2d1a5c; color: var(--purple); }   /* SaaS */
.badge-live   { background: #2d0a2d; color: var(--purple); }   /* Live */
```

## TL;DR Box Colors

- Bullish / positive: `background: #1a2744` (blue tint)
- Bearish / negative: `background: #2d0a0a` (red tint)

## Hebrew / RTL Pages

- `<html lang="he" dir="rtl">`
- Flip all padding/border sides (left↔right)
- `text-align: right`

## Required Page Sections (in order)

1. `← Back` link → `../index.html`
2. Header: badges + title + meta (date, duration, channel) + YouTube link
3. Embedded player: `<iframe src="https://www.youtube.com/embed/VIDEO_ID">`
4. TL;DR box
5. Content cards: Facts / Conclusions / Recommendations
6. Transcript link: `<a href="transcripts/SLUG.txt">📄 Raw Transcript</a>`
7. Footer
8. Scripts (MANDATORY):
   ```html
   <script src="../protect.js"></script>
   <script src="../copy-btn.js"></script>
   ```
