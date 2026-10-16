---
name: video-summeries
description: "Use when adding a YouTube video to the VideoSummeries site."
version: 1.0.0
author: Dotan
license: MIT
platforms: [linux, macos]
metadata:
  hermes:
    tags: [YouTube, Video, Summaries, GitHub-Pages]
    related_skills: [youtube-content]
---

# VideoSummeries Pipeline

End-to-end workflow: YouTube URL → transcript → dark-themed HTML summary → GitHub Pages gallery → Telegram reply with TTS.

## When to Use

Use when Dotan shares a YouTube video URL and wants a summary added to the VideoSummeries gallery site. Also use when he asks to re-summarize or check an existing summary.

## Credentials & Config

See `references/credentials.md` for GitHub PAT, repo URL, git identity, and Pages password. **Never log or echo the PAT in terminal output.**

## Repo Structure

```
VideoSummeries/
├── index.html              ← Main gallery (update for every new video)
├── protect.js              ← Password gate — ALWAYS include in pages
├── copy-btn.js             ← Copy button — ALWAYS include in pages
└── summaries/
    ├── YYYY-MM-DD_slug.html
    └── transcripts/        ← Raw .txt transcripts
```

Local clone: see credentials reference for path.

## Full Pipeline

### Step 0 — Setup & Duplicate Guard (ALWAYS FIRST)

```bash
cd $REPO_PATH && git pull origin main
VIDEO_ID="REPLACE_WITH_ID"
ls $REPO_PATH/summaries/*${VIDEO_ID}* 2>/dev/null && echo "⚠️ FILE EXISTS"
grep "$VIDEO_ID" $REPO_PATH/index.html && echo "⚠️ CARD EXISTS"
```

- If either hits → STOP. Send existing GitHub Pages link + TTS only. Do not redo.
- Clean stale temp files: `rm -f /tmp/ytaudio.mp3 /tmp/chunk*.mp3 /tmp/transcript.txt`

### Step 1 — Fetch Transcript

Always verify title first:
```bash
python3.11 -m yt_dlp --get-title 'YOUTUBE_URL'
```

**Primary — youtube-transcript-api:**
```bash
python3 -c "
from youtube_transcript_api import YouTubeTranscriptApi
t = YouTubeTranscriptApi.get_transcript('VIDEO_ID', languages=['en','he'])
print(' '.join([s['text'] for s in t]))
"
```

**Fallback chain (in order):**
1. **kome.ai** — browser to `https://kome.ai/tools/youtube-transcript-generator`
2. **yt-dlp + faster-whisper** — see `references/whisper-fallback.md`

**Hebrew videos:** Skip youtube-transcript-api entirely (returns "No transcript found"). Go straight to whisper with `language='he'`.

### Step 2 — Save Transcript

```bash
mkdir -p $REPO_PATH/summaries/transcripts
cp /tmp/transcript.txt $REPO_PATH/summaries/transcripts/SLUG.txt
```

### Step 3 — Generate HTML Summary Page

- **Filename:** `YYYY-MM-DD_slug.html` (slug: lowercase, hyphens, max 40 chars, no Hebrew)
- **Save to:** `$REPO_PATH/summaries/`
- **Use template:** see `templates/summary-page.html` for the full dark-theme template
- **See `references/html-spec.md`** for required sections, badge classes, RTL rules

Every page MUST have:
1. `← Back` link to `../index.html`
2. Header: badges + title + meta (date, duration, channel) + YouTube link
3. Embedded YouTube player iframe
4. TL;DR box (blue `#1a2744` = bullish / red `#2d0a0a` = bearish)
5. Content cards: Facts / Conclusions / Recommendations
6. Transcript link: `<a href="transcripts/SLUG.txt">📄 Raw Transcript</a>`
7. Footer
8. **BOTH scripts before `</body>` — NEVER OMIT:**
   ```html
   <script src="../protect.js"></script>
   <script src="../copy-btn.js"></script>
   ```

### Step 4 — Update index.html

Prepend card at TOP of `<div class="grid">`. See `references/index-card.md` for the card HTML template.

Also update hero stats: increment video count, update "Last Updated" date.

> ⚠️ `<div class="grid">` appears multiple times — include the next `<a class="card"` line in your patch old_string to ensure uniqueness.

### Step 5 — Git Push

```bash
cd $REPO_PATH
git config user.email "$GIT_EMAIL"
git config user.name "$GIT_NAME"
git add -A
git commit -m "Add summary: VIDEO TITLE (YYYY-MM-DD)"
git remote set-url origin "$PUSH_URL"
git push origin main
```

- If push fails "Can't assign requested address": transient ISP glitch, NOT auth. Wait 10s and retry (up to 3 times).

### Step 6 — Reply to Dotan

**Order: push first, then message. Never message before pushing.**

1. **Long detailed Telegram summary** (600–1200 words minimum — hard preference)
   - Every point, sub-point, number, quote, tool, framework mentioned
   - Use headers, bold, nested bullets
2. **TTS voice summary** — Hebrew if Hebrew video, English otherwise
3. Append link: `🌐 https://dotdbot.github.io/VideoSummeries/summaries/FILENAME.html`

## Tweet Summaries (second page)

The site has two pages with a top nav toggle: `index.html` (videos) and `tweets.html` (tweets). When Dotan sends an x.com / twitter.com status link:

1. Read the tweet(s) (the helper fetches text via api.fxtwitter.com) and write a short summary (HTML `<ul>` bullets are fine; match the tweet's language).
2. From the repo root run: `python3 tools/add_tweet.py URL [URL ...] --title "..." --tags "AI,Stocks" --summary "<ul><li>..</li></ul>"`. Several URLs = one card (thread/collection). It refuses duplicates and inserts the card at the top of the grid.
   Language rule: Hebrew tweets stay Hebrew, English stay English, any other language is translated to English (title, summary and the embedded tweet text). For translated tweets pass `--translation "English text"` (one per URL, in order) and `--lang Chinese`; the original stays available in a collapsible block. `--replace` rebuilds an existing card.
3. Commit + push, then reply with the summary and link `https://dotdbot.github.io/VideoSummeries/tweets.html`.

The local clone is `/opt/data/VideoSummeries`. Non-YouTube links (articles, Facebook reels) are not part of the video pipeline.

## Lessons

- Cloud IPs: web_extract returns the YouTube transcript when yt-dlp/transcript-api are blocked; if Hebrew text comes back garbled (mojibake), retry or use the browser transcript panel instead of summarizing garbage.
- Never leave the PAT in the git remote URL after pushing; reset it to the plain https URL.

- Multiple videos in same session: use unique temp filenames (`ytaudio2.mp3`, `transcript2.txt`)
- yt-dlp 403: try `-f 140` (m4a) + ffmpeg, or `uv run --with yt-dlp yt-dlp`
- Whisper timeout mid-run: recover from partial transcript, cut audio from last timestamp, continue
- macOS OpenMP crash in Whisper: always prefix with `KMP_DUPLICATE_LIB_OK=TRUE`
- git pull fails (network down): skip pull, continue from local; push reconciles
- index.html grid patch: `<div class="grid">` is not unique — always include the next `<a class="card"` in old_string
- protect.js and copy-btn.js must ALWAYS be included before `</body>` — no exceptions
- Long audio transcription: use `terminal(background=True, notify=True)` to avoid timeouts
