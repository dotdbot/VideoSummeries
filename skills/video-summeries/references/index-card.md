# Index Card Template

Prepend this at the TOP of `<div class="grid">` in index.html:

```html
<a class="card" href="summaries/YYYY-MM-DD_slug.html">
  <div class="card-thumb">
    <img src="https://img.youtube.com/vi/VIDEO_ID/mqdefault.jpg" alt="thumbnail" loading="lazy">
    <div class="overlay"></div>
    <div class="play-btn">▶</div>
  </div>
  <div class="card-body">
    <div class="card-badges">
      <span class="badge badge-en">🇺🇸 English</span>
      <span class="badge badge-biz">💼 Business</span>
    </div>
    <div class="card-title">VIDEO TITLE</div>
    <div class="card-meta">📅 YYYY-MM-DD · ⏱ Xm · 📺 Channel Name</div>
    <div class="card-desc">Short teaser, 1-2 sentences.</div>
  </div>
</a>
```

## Replace placeholders:
- `YYYY-MM-DD` — video date
- `slug` — lowercase-hyphens, max 40 chars, no Hebrew
- `VIDEO_ID` — YouTube video ID
- Badges — pick appropriate from html-spec.md
- `VIDEO TITLE` — full title
- `Xm` — duration in minutes
- `Channel Name` — YouTube channel
- Card desc — 1-2 sentence teaser

## Also update hero stats:
- Increment the video count number
- Update "Last Updated" to today's date

## Patching tip:
`<div class="grid">` appears multiple times. Always include the next `<a class="card"` line in your `old_string` to ensure a unique match.
