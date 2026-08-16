# VideoSummeries CSS Class Reference

All classes used across the summary pages. Copy-paste into new pages for consistency.

## Badge Classes (language + category labels in card headers)

```css
.badge-he   { background: #1a3a5c; color: var(--accent); }         /* 🇮🇱 Hebrew */
.badge-en   { background: #1a3a1a; color: var(--green); }          /* 🇺🇸 English */
.badge-stocks { background: #1a3a1a; color: var(--green); }        /* 📈 Stocks */
.badge-biz  { background: #1a2744; color: var(--accent); }         /* 💼 Business/General */
.badge-ai   { background: #2d1a5c; color: #c0a0ff; }               /* 🤖 AI/Tech */
.badge-interview { background: #1a2744; color: var(--accent); }    /* 🎙️ Interview */
```

## Sentiment Tags (stock tables)

```html
<span class="tag tag-bullish">Very Bullish</span>   <!-- bg:#0d3320 color:#3fb950 -->
<span class="tag tag-lt-bullish">Bullish LT</span>  <!-- bg:#1a3a5c color:#58a6ff -->
<span class="tag tag-cautious">Cautious</span>      <!-- bg:#2d2000 color:#d29922 -->
<span class="tag tag-pass">Pass</span>              <!-- bg:#2d0a0a color:#f85149 -->
<span class="tag tag-wait">Wait/Correction</span>  <!-- bg:#2d2000 color:#d29922 -->
<span class="tag tag-watch">Watch</span>           <!-- bg:#002020 color:#39d353 -->
```

## Tier Badges (buy-a-business style tier lists)

```html
<span class="tier-badge tb-s">S TIER ⭐</span>   <!-- bg:#2d1a5c color:#c0a0ff -->
<span class="tier-badge tb-a">A TIER ✅</span>   <!-- bg:#0d3320 color:#3fb950 -->
<span class="tier-badge tb-b">B+ TIER</span>     <!-- bg:#1a2744 color:#58a6ff -->
<span class="tier-badge tb-c">C TIER ⚠️</span>  <!-- bg:#2d2000 color:#d29922 -->
<span class="tier-badge tb-f">F TIER ❌</span>  <!-- bg:#3d0d0d color:#f85149 -->
```

## Standard CSS Variables

```css
--bg: #0d1117; --surface: #161b22; --surface2: #21262d;
--border: #30363d; --accent: #58a6ff; --green: #3fb950;
--yellow: #d29922; --red: #f85149; --text: #e6edf3; --muted: #8b949e;
```

## Required Scripts (always before `</body>`)

```html
<script src="../protect.js"></script>   <!-- password: Shira100 -->
<script src="../copy-btn.js"></script>  <!-- floating 📋 Copy post button -->
```

## Transcript Link Pattern (in header .meta)

```html
<a href="transcripts/SLUG.txt" target="_blank" style="color:var(--muted)">📄 Full Transcript</a>
```
Save transcript to: `/tmp/vs_git/summaries/transcripts/SLUG.txt`
