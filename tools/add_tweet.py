#!/usr/bin/env python3
"""Add a tweet summary card to tweets.html.

Usage:
  add_tweet.py URL [URL ...] --summary "text or <ul>html</ul>" [--title "..."] [--tags "AI,Stocks"]

- Fetches each tweet via api.fxtwitter.com (no auth) for author, text, date, first photo.
- Several URLs => one card (a collection/thread) with one peek per tweet and one shared summary.
- Inserts the card at the top of the grid (between the TWEETS:START marker and the first card).
- Refuses duplicates (same status id already on the page).
"""
import argparse, html, json, re, sys, urllib.request
from datetime import datetime
from pathlib import Path

PAGE = Path(__file__).resolve().parent.parent / "tweets.html"
MARK = "<!-- TWEETS:START (new cards are inserted right below this line) -->"


def parse(url):
    m = re.search(r"(?:x|twitter)\.com/([^/]+)/status/(\d+)", url)
    if not m:
        sys.exit(f"Not a tweet URL: {url}")
    return m.group(1), m.group(2)


def fetch(user, tid):
    req = urllib.request.Request(f"https://api.fxtwitter.com/{user}/status/{tid}",
                                 headers={"User-Agent": "Mozilla/5.0"})
    d = json.load(urllib.request.urlopen(req, timeout=25))
    if d.get("code") != 200:
        sys.exit(f"fxtwitter error for {tid}: {d.get('message')}")
    return d["tweet"]


def fmt_date(s):
    try:
        return datetime.strptime(s, "%a %b %d %H:%M:%S %z %Y")
    except Exception:
        return None


def peek(t, url, translation=None, lang=""):
    a = t["author"]
    dt = fmt_date(t.get("created_at", ""))
    when = dt.strftime("%b %d, %Y · %H:%M UTC") if dt else t.get("created_at", "")
    media = t.get("media") or {}
    photos = media.get("photos") or []
    if not photos and media.get("videos"):
        v = media["videos"][0]
        photos = [{"url": v.get("thumbnail_url", "")}] if v.get("thumbnail_url") else []
        mins = int(v.get("duration", 0) // 60); secs = int(v.get("duration", 0) % 60)
        vid_note = f" · 🎬 video {mins}:{secs:02d}"
    else:
        vid_note = ""
    img = f'<img class="peek-img" src="{html.escape(photos[0]["url"])}" alt="" loading="lazy">' if photos else ""
    if translation:
        body = (f'<div class="peek-text" dir="auto">{html.escape(translation)}</div>'
                f'<details class="orig"><summary>Translated from {html.escape(lang or "original")} · show original</summary>'
                f'<div class="peek-text" dir="auto">{html.escape(t["text"])}</div></details>')
    else:
        body = f'<div class="peek-text" dir="auto">{html.escape(t["text"])}</div>'
    stats = f'❤ {t.get("likes", 0):,} · 🔁 {t.get("retweets", 0):,} · 💬 {t.get("replies", 0):,}'
    return f'''<div class="peek">
        <div class="peek-head">
          <img src="{html.escape(a.get("avatar_url", ""))}" alt="" loading="lazy">
          <div><div class="peek-name">{html.escape(a["name"])}</div><div class="peek-handle">@{html.escape(a["screen_name"])}</div></div>
          <a class="peek-x" href="{html.escape(url)}" target="_blank" rel="noopener" title="Open on X">↗</a>
        </div>
        {body}
        {img}
        <div class="peek-meta">{when} · {stats}{vid_note}</div>
      </div>''', dt


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("urls", nargs="+")
    ap.add_argument("--summary", required=True)
    ap.add_argument("--title", default="")
    ap.add_argument("--tags", default="")
    ap.add_argument("--translation", action="append", default=[],
                    help="English translation of the tweet text, one per URL in order (use for languages other than Hebrew/English)")
    ap.add_argument("--lang", default="", help="source language name, e.g. Chinese")
    ap.add_argument("--replace", action="store_true", help="remove an existing card containing these tweet ids first")
    a = ap.parse_args()

    page = PAGE.read_text(encoding="utf-8")
    if a.replace:
        for u in a.urls:
            tid = parse(u)[1]
            page = re.sub(r'    <div class="tcard" data-ids="[^"]*\b%s\b.*?\n    </div>\n\n    ' % tid, "", page, flags=re.S)
    peeks, first_dt, ids = [], None, []
    for i, u in enumerate(a.urls):
        user, tid = parse(u)
        if f'data-ids="' in page and re.search(rf'data-ids="[^"]*\b{tid}\b', page):
            sys.exit(f"DUPLICATE: tweet {tid} already on the page")
        t = fetch(user, tid)
        tr = a.translation[i] if i < len(a.translation) else None
        block, dt = peek(t, f"https://x.com/{user}/status/{tid}", tr, a.lang)
        peeks.append(block)
        ids.append(tid)
        first_dt = first_dt or dt

    summary = a.summary if "<" in a.summary else html.escape(a.summary)
    tags = "".join(f'<span class="badge">{html.escape(x.strip())}</span>' for x in a.tags.split(",") if x.strip())
    title = f'<div class="t-title">{html.escape(a.title)}</div>' if a.title else ""
    short = first_dt.strftime("%b %-d") if first_dt else datetime.utcnow().strftime("%b %-d")
    first_url = a.urls[0]
    n = len(a.urls)
    foot = f'<a href="{html.escape(first_url)}" target="_blank" rel="noopener">View on X ↗</a>'
    card = f'''    <div class="tcard" data-ids="{' '.join(ids)}" data-date="{short}">
      {tags and f'<div class="badges">{tags}</div>'}
      {title}
      {chr(10).join(peeks)}
      <div class="t-summary">{summary}</div>
      <div class="t-foot"><span>{'🧵 ' + str(n) + ' tweets' if n > 1 else '🐦 1 tweet'} · {short}</span>{foot}</div>
    </div>

    '''
    if MARK not in page:
        sys.exit("marker not found in tweets.html")
    PAGE.write_text(page.replace(MARK, MARK + "\n" + card, 1), encoding="utf-8")
    print(f"added card with {n} tweet(s): {', '.join(ids)}")


if __name__ == "__main__":
    main()
