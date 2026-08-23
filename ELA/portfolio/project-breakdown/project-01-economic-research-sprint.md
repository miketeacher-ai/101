# Project 01: Economic Research Sprint (Days 1-15) — How to Build Each Day

**Student:** Ela | **Major:** Economics & Finance | **Sprint:** Day 1 Mon Aug 24 - Day 45 Wed Oct 7, 2026

Deliverable: 2000-word paper on household impacts of Turkey's inflation episode, World Bank/IMF/TCMB data, Python charts, public GitHub, Concord Review submission. 4-5 hrs/day. Optimized: free tools only, reproducible in <5 min.

## Tools (optimized)

- Google Colab (pandas, matplotlib) — no install
- World Bank Open Data, IMF WEO, TCMB EVDS (free key)
- Overleaf/Google Docs; Zotero; GitHub

## Day-by-Day: How to Build + Suggestion

### Days 1-5: Question + Data — Setup for Speed

| Day | Task | How to Build | Suggestion / Optimization |
|-----|------|--------------|---------------------------|
| 1 | Define narrow question: "How did 2021-2026 inflation reshape Turkish household consumption categories?" Write 150-word abstract draft | How: Write question as one sentence with variables (inflation → consumption categories) + one sentence why it matters (households). Abstract draft: 3 sentences (question/method/why). | Suggestion: Narrow beats broad — "reshape consumption categories" is better than "impact economy." One question, one dataset family (World Bank). If abstract takes >30 min, it's too broad |
| 2 | Pull World Bank CPI, food CPI, exchange rate, minimum wage → raw CSVs to repo | How: World Bank API via Colab `wbdata` or manual CSV download from data.worldbank.org. Save raw CSVs in `data/raw/` with date prefix. Document source URL in README table. | Suggestion: Save raw data before any cleaning — never edit raw. Use `data/raw/` and `data/clean/` separation — saves hours when you need to re-download |
| 3 | Pull IMF WEO inflation/unemployment for TR + Poland, Mexico comparators | How: IMF DataMapper → WEO dataset → export TR, Poland, Mexico 2018-2026. Add to same `data/raw/` folder. Note: Poland/Mexico chosen as emerging-market comparators with different monetary responses. | Suggestion: Two comparators max — three countries × two indicators = 6 series, enough for paper. More comparators = more cleaning, not more insight |
| 4 | Register TCMB EVDS key; pull USDTRY daily | How: Register at evds2.tcmb.gov.tr (free, instant). Use EVDS Python wrapper or manual export. Pull daily USDTRY 2021-2026. Save as CSV. | Suggestion: EVDS key arrives by email instantly — check spam. Pull daily, not monthly — daily shows volatility that monthly hides, and you can always aggregate to monthly later |
| 5 | Colab notebook 1: load + clean; document each source in README table | How: Notebook 1 = load all CSVs, handle missing values, convert dates, merge on date. README table: columns Source, URL, Series Code, Date Pulled, Rows. No comments in code — table is documentation. | Suggestion: Document while loading, not after — 5 min now saves 1 hour when mentor asks "where did this series come from?" |
| 6 | Chart set A: headline vs food inflation + exchange overlay; annotate crisis dates | How: Matplotlib: dual-axis chart (left: inflation %, right: USDTRY). Annotate Dec 2021 (rate cut), Sep 2023 (tightening). Export PNG at 300dpi. | Suggestion: One chart with two axes beats two separate charts — shows correlation instantly. Annotate crisis dates with vertical lines — reviewers love temporal anchors |
| 7 | Read 3 academic references on inflation incidence; notes | How: Search Google Scholar: "Turkey inflation household consumption" + "inflation incidence emerging markets" + "World Bank Turkey inflation". Read abstracts, then 1-2 full papers. Take notes: citation, method, finding, how your paper differs. | Suggestion: 3 papers max — not 10. You're not writing literature review, you're positioning one contribution. One citation per claim later is enough |

### Days 6-10: Analysis + Draft

| Day | Task | How to Build | Suggestion |
|-----|------|--------------|------------|
| 8 | Compute real wage index (minimum wage / CPI); chart B | How: Real wage = nominal minimum wage ÷ CPI × 100. Plot real vs nominal wage over time. Note divergence during high inflation. | Suggestion: Real wage chart is paper's star — make it large, clear, with 2 colors only. This chart alone can carry your argument |
| 9 | Category shift: food/housing share over time | How: If World Bank has consumption categories, plot food share % vs housing share %. If not, use TurkStat Household Budget Survey summary tables (available as PDF — transcribe one table). | Suggestion: If category data is hard to get in 1 day, pivot to "food vs non-food inflation gap" using CPI components you already have — don't chase perfect data, use available data well |
| 10 | FULL DRAFT v1 (2000 words): intro, lit, method, findings, limitations | How: Write straight through, no editing. Structure: Intro (300w, question + why), Lit (400w, 3 papers + positioning), Method (300w, data sources + cleaning), Findings (700w, 2 charts + interpretation), Limitations (300w, what you couldn't do). Aim 2000, not 1500. | Suggestion: Write straight through without self-editing — editing while drafting halves speed. Draft is clay, not sculpture. Limit Lit to 400w — reviewers care about your findings, not your summary |
| 11 | Self-edit: kill adjectives, verify every figure vs source; export charts at print res | How: Search for "very, really, highly" and delete 80%. Verify every number in draft vs CSV — one wrong number undermines credibility. Re-export charts at 300dpi. | Suggestion: Use Find → "ly" to catch adverbs. One wrong figure in a 2000-word paper is what reviewers remember |
| 12 | Repo hygiene: README with question/method/repro steps, requirements.txt | How: README sections: Question, Data Sources (table from Day 5), How to Reproduce (3 steps: clone, pip install -r requirements.txt, run notebook), License. requirements.txt: `pandas, matplotlib, wbdata` | Suggestion: README is what GitHub visitors read — make it 1 page, not 5. Test reproduction: delete and re-run notebook in 5 min — if fails, fix now |
| 13 | Send to one teacher/mentor; integrate top 5 comments only | How: Send PDF + repo link to one teacher/mentor. Ask: "What are top 5 changes you'd make?" Integrate only those 5. | Suggestion: One mentor, top 5 comments — prevents feedback spiral. Two mentors × 10 comments each = 20 conflicting suggestions, no progress |
| 14 | FINAL v2; format to Concord Review style (verify) | How: Check Concord Review guidelines (font, margins, citation style, word count). Reformat exactly. Word count 2000-2200. | Suggestion: Format is not optional — wrong format signals you didn't read guidelines. Check current guidelines, not 2023 memory |
| 15 | SUBMIT to Concord Review + secondary journal; archive PDF | How: Submit via Concord Review portal, save confirmation email. Submit to secondary (e.g., Journal of Student Research). Archive PDF in Drive + email to yourself. | Suggestion: Submit to secondary same day — not "later." Later = never. Archive in 3 places (Drive, email, phone) |

## Quality Gates (check before Day 15)

- [ ] Every claim → numbered citation
- [ ] Every chart regenerates from notebook in <5 min
- [ ] Abstract readable by non-economist in 60 sec
- [ ] Word count 2000-2200, formatted per guidelines, <15 MB

## Tool Optimization

- Raw vs clean data separation saves re-download time
- One chart with dual axes beats two separate charts
- README table is documentation — no code comments needed
