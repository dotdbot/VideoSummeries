# HTML Page Patterns by Video Type

Confirmed patterns from real pages in the VideoSummeries repo. Use these as the design spec for new pages — don't reinvent each time.

---

## Pattern A: Finance / Stocks (Hebrew — מיחה מאמריקה style)

**Badges:** `badge-he` + `badge-stocks`  
**Direction:** `<html lang="he" dir="rtl">`  
**Key sections:**
- TL;DR with meltup/market-state warning if applicable
- Stock table: `<table>` with columns Ticker / Name / Sector / Status / Notes
- Sentiment tags: `tag-wait`, `tag-watch`, `tag-caution`, `tag-hold`
- Alert box: `.alert-box` with yellow border for key macro warning
- Sector rows: `.sector-header` with `colspan="5"` emoji label

**Sector header CSS:**
```css
.sector-header td { background: var(--surface2); color: var(--muted); font-size: 11px; font-weight: 700; text-transform: uppercase; letter-spacing: 1px; padding: 6px 14px; }
```

---

## Pattern B: Numbered List / Accounts / Resources

**Example:** Twitter/X 20 Must-Follow Accounts  
**Badges:** `badge-he` or `badge-en` + relevant topic badge  
**Key sections:**
- Group by category (News / Analysis / Must-Follow)
- `.account-row` layout: number circle + handle + name + description + category tag
- Category tags: `.cat-news`, `.cat-analysis`, `.cat-must`, `.cat-he`
- Tips section at bottom with `ul.tips` (li::before `💡 `)

**Account row CSS:**
```css
.account-row { display: flex; align-items: flex-start; gap: 14px; padding: 14px 0; border-bottom: 1px solid var(--border); }
.account-num { font-size: 22px; font-weight: 900; color: var(--surface2); min-width: 32px; text-align: center; font-family: monospace; }
.account-handle { font-family: monospace; font-size: 13px; color: var(--accent); font-weight: 700; }
.cat-news { background: #1a2744; color: var(--accent); }
.cat-analysis { background: #1a3a1a; color: var(--green); }
.cat-must { background: #3d1a00; color: var(--yellow); }
.cat-he { background: #2d1a5c; color: #c0a0ff; }
```

---

## Pattern C: Income / Business Guide ("5 Ways to Make Money")

**Example:** DJI Drone income streams, $3,500/month  
**Badges:** `badge-en` + `badge-biz`  
**Key sections:**
- Income snapshot table (Rate / Volume / Monthly Est.)
- `.way-item` cards with left-border color-coded by strength
- Optional comparison section if multiple similar videos exist
- Tips/getting-started bullets at bottom

**Way-item CSS:**
```css
.way-item { background: var(--surface2); border-radius: 10px; padding: 20px; margin-bottom: 14px; border-left: 4px solid var(--green); }
.way-item.bonus { border-left-color: var(--yellow); }
.way-item.extra { border-left-color: var(--muted); }
.way-title { font-size: 17px; font-weight: 700; margin-bottom: 6px; display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 8px; }
.way-price { font-family: monospace; font-size: 15px; font-weight: 900; color: var(--green); }
```

**Income table:**
```html
<table class="income-table">
  <thead><tr><th>Stream</th><th>Rate</th><th>Volume/Month</th><th>Monthly Est.</th></tr></thead>
  <tbody>
    <tr><td>...</td><td>$X/unit</td><td>Y units</td><td><strong>$Z</strong></td></tr>
    <tr class="total-row"><td colspan="3">Total</td><td>$TOTAL/mo</td></tr>
  </tbody>
</table>
```
```css
.total-row td { font-weight: 700; color: var(--green); background: var(--surface2) !important; }
```

---

## Pattern D: Interview / Founder Story

**Example:** Brett Adcock (Figure/HARK), Pulsia founder  
**Badges:** `badge-en` + `badge-ai` + `badge-interview`  
**Key sections:**
- Company row listing (icon + name + valuation + description)
- Prediction cards (`.prediction.on-track` / `.prediction.miss`) with status badge
- Quote blocks for key quotes
- Timeline items for journey narrative
- Key people section

**Company row CSS:**
```css
.company-row { display: flex; align-items: flex-start; gap: 16px; padding: 16px 0; border-bottom: 1px solid var(--border); }
.company-icon { font-size: 28px; min-width: 40px; text-align: center; }
```

**Prediction card CSS:**
```css
.prediction { background: var(--surface2); border-radius: 10px; padding: 20px; margin-bottom: 16px; border-left: 4px solid var(--accent); }
.prediction.on-track { border-left-color: var(--green); }
.prediction.miss { border-left-color: var(--yellow); }
.status-badge.status-on { background: #0d3320; color: var(--green); }
.status-badge.status-miss { background: #2d2000; color: var(--yellow); }
```

---

## Pattern E: Agency / Business Blueprint

**Example:** 1-Person AI Agency $100K/month  
**Badges:** `badge-en` + `badge-ai` + `badge-biz`  
**Key sections:**
- Gen comparison grid (3-column, color-coded bad/mid/good)
- Offer suite items with price ranges
- Math box showing revenue/expense/profit breakdown
- 4-column marketing table with ✅/⚠️ status tags
- AI agent tasks as bullet list

**Gen comparison CSS:**
```css
.gen-row { display: flex; gap: 14px; margin-bottom: 14px; }
.gen-box { flex: 1; background: var(--surface2); border-radius: 10px; padding: 16px; }
.gen-box.bad { border-left: 4px solid var(--red); }
.gen-box.mid { border-left: 4px solid var(--yellow); }
.gen-box.good { border-left: 4px solid var(--green); }
```

**Math box CSS:**
```css
.math-box { background: #0d3320; border: 1px solid var(--green); border-radius: 10px; padding: 20px 24px; }
.math-row { display: flex; justify-content: space-between; padding: 6px 0; border-bottom: 1px solid var(--border); font-size: 14px; }
.math-row:last-child { border-bottom: none; font-weight: 700; color: var(--green); font-size: 16px; }
.math-row.expense { color: var(--red); }
```

---

## Pattern F: Solopreneur / Founder Playbook (Step-by-Step)

**Example:** Brett Williams $1.8M Solopreneur Playbook  
**Badges:** `badge-en` + `badge-biz`  
**Key sections:**
- Stat row at top (6 key metrics: revenue, employees, hours/day, clients, rate, passive %)
- Step cards (`.step-item`) with numbered label + bold title + rich description
- Price comparison grid (`.price-compare` with `.price-opt` rows, `.price-opt.win` for winner)
- Revenue breakdown bullets
- Key lessons bullets at bottom

**Step card CSS:**
```css
.step-item { background: var(--surface2); border-radius: 10px; padding: 20px; margin-bottom: 14px; border-left: 4px solid var(--accent); }
.step-num { font-size: 11px; font-weight: 700; text-transform: uppercase; letter-spacing: 1px; color: var(--muted); margin-bottom: 4px; }
.step-title { font-size: 18px; font-weight: 700; margin-bottom: 10px; }
.step-desc { font-size: 14px; color: var(--muted); line-height: 1.75; }
.step-desc strong { color: var(--text); }
```

**Price comparison CSS:**
```css
.price-compare { display: flex; flex-direction: column; gap: 10px; margin-top: 12px; }
.price-opt { display: flex; gap: 12px; align-items: flex-start; padding: 12px; border-radius: 8px; background: var(--surface); border: 1px solid var(--border); }
.price-opt.win { border-color: var(--green); background: #0d2a1a; }
.price-opt-label { font-size: 12px; font-weight: 700; min-width: 32px; }
.price-opt-desc { font-size: 14px; color: var(--muted); }
```

---

## Pattern G: Product Catalog / Machine List

**Example:** 18 Machines from China  
**Badges:** `badge-en` + `badge-biz`  
**Key sections:**
- TL;DR with core thesis
- Full catalog table (# / Product / Price / Revenue / Key Insight), highlighted finale row
- Best picks section (grouped by: lowest cost, highest revenue, best recurring, best trend)
- Key themes bullets

**Table highlight row (grand finale or best pick):**
```html
<tr style="background: #0d2a1a;">
  <td class="num" style="color:var(--yellow)">18⭐</td>
  <td><strong>💧 Mini Purified Water Bottling Plant</strong></td>
  ...
</tr>
```

**Catalog table CSS:**
```css
.num { font-family: monospace; font-weight: 700; color: var(--accent); font-size: 13px; }
.price { font-family: monospace; font-weight: 700; color: var(--yellow); white-space: nowrap; }
.revenue { font-weight: 600; color: var(--green); }
```

**Note:** For long catalogs (15+ rows), always add a "Best Picks by Category" card after the table — it makes the page scannable without reading every row.

---

## Universal Elements (all pages)

```css
/* Bullets */
ul.bullets { list-style: none; display: flex; flex-direction: column; gap: 10px; font-size: 15px; }
ul.bullets li::before { content: "→ "; color: var(--accent); font-weight: 700; }

/* Quote block */
.quote-block { background: var(--surface2); border-left: 3px solid var(--accent); padding: 14px 18px; border-radius: 0 8px 8px 0; margin: 12px 0; font-style: italic; font-size: 15px; }
.quote-block cite { display: block; margin-top: 6px; font-style: normal; font-size: 12px; color: var(--muted); }

/* Stats row */
.stat-row { display: flex; flex-wrap: wrap; gap: 16px; margin-bottom: 20px; }
.stat-box { background: var(--surface2); border-radius: 10px; padding: 16px 20px; flex: 1; min-width: 140px; text-align: center; }
.stat-box .val { font-size: 26px; font-weight: 900; color: var(--green); font-family: monospace; }
.stat-box .lbl { font-size: 12px; color: var(--muted); margin-top: 4px; text-transform: uppercase; letter-spacing: 0.5px; }

/* TL;DR */
.tl-dr { background: #1a2744; border: 1px solid var(--accent); border-radius: 10px; padding: 20px 24px; margin-bottom: 20px; font-size: 16px; line-height: 1.8; }
.tl-dr strong { color: var(--accent); }
```

## Badge Classes Quick Reference

| Class | Color | Use For |
|-------|-------|---------|
| `badge-he` | blue/accent | Hebrew content |
| `badge-en` | green | English content |
| `badge-stocks` | dark green | Finance/stocks |
| `badge-biz` | blue | Business/guide |
| `badge-ai` | purple | AI/tech |
| `badge-interview` | blue | Interview/talk |

CSS for badge-biz (add inline if not in template):
```css
.badge-biz { background: #1a2744; color: #79c0ff; }
```
