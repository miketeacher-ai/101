# Project 01: Research Sprint (Days 1-15) — How to Build Each Day

**Student:** Elfin | **Major:** Molecular Biology & Medicine | **Sprint:** Day 1 Mon Aug 24 - Day 45 Wed Oct 7, 2026

Deliverable: computational biology project — choose ONE track, produce 2000-word paper, public GitHub repo, ISEF-style abstract. 4-5 hrs/day. Optimized: free tools only, one track (not three), reproducible in <5 min.

## Tools (all free — optimized)

- AutoDock Vina/AutoDockTools (docking) OR Python/R (pandas, matplotlib, GEOquery) for GEO reanalysis OR PubMed (PRISMA-lite review)
- Google Colab — no install
- GitHub for versioning + Overleaf/Google Docs for manuscript

## Three Track Options (pick ONE on Day 1 — optimization: don't do all three)

| Track | Question Example | Output | When to Choose |
|-------|------------------|--------|----------------|
| A Docking | Protein-ligand docking on antimicrobial-resistance target (e.g., beta-lactamase) | Binding affinity table + PyMOL images | Choose if you like chemistry + visual results |
| B GEO Reanalysis | Reanalysis of GEO dataset (e.g., Alzheimer's GSE... ) in Python/R | Volcano plot + pathway enrichment | Choose if you like data + statistics |
| C Systematic Review | PRISMA-lite review on focused question (e.g., "probiotic and H. pylori") | Flow diagram + evidence table | Choose if you like literature + no coding risk |

## Day-by-Day: How to Build + Suggestion

### Days 1-7: Setup + Data — Tooling for Speed

| Day | Task | How to Build | Suggestion / Optimization |
|-----|------|--------------|---------------------------|
| 1 | Choose track A/B/C; write 150-word abstract draft | How: Write abstract draft with 3 sentences (question/method/why). Choose track based on what excites you + what you can finish in 10 days. Decision by lunch. | Suggestion: Decide by lunch — indecision costs 1 day. Pick track you can explain to 12-year-old in 30 sec |
| 2 | Set up free tools + pull dataset/target; register GitHub repo | How: Track A: install AutoDock Vina + download PDB target (e.g., 1AXB). Track B: Colab + GEOquery, pull GSE dataset. Track C: PubMed search, export 20 results to Zotero. Register GitHub repo `elfin-compbio-sprint`. | Suggestion: GitHub repo Day 2, not Day 12 — early repo forces documentation habit. One repo, one track, no branching |
| 3 | Pull PubMed/GEO/PDB entries; document each source in README table | How: Pull 5-10 entries (PDB IDs, GEO series, or PubMed IDs). README table: columns Source, ID, URL, Date Pulled, Rows. No code comments — table is documentation. | Suggestion: Document while pulling, not after — 5 min now saves 1 hour when mentor asks "where did GSE... come from?" |
| 4 | Run first analysis (docking run OR GEO load OR PubMed screen) | How: Track A: run Vina with default grid, get first affinity. Track B: load GEO matrix, check dimensions. Track C: screen 20 titles/abstracts, include/exclude. | Suggestion: First run is meant to fail — aim for 1 result, not 10. Debug one, then scale |
| 5 | Generate figure set 1; notes to methods doc | How: Figure 1: docking pose OR volcano plot OR PRISMA flow start. Save PNG at 300dpi. Write 100-word methods snippet for this figure. | Suggestion: Figure + 100-word methods snippet per day — writing while results fresh is 3× faster than writing all at end |
| 6 | Generate figure set 2; annotate | How: Figure 2: affinity table OR pathway enrichment OR evidence table. Annotate with 2-sentence caption (what, so what). | Suggestion: Caption = "What you see + why it matters" — reviewers read captions before text |
| 7 | Read 3 academic references; notes | How: Search PubMed: your target + "docking" / "GEO reanalysis" / "systematic review". Read 3 papers: citation, method, finding, how your work differs (one sentence each). | Suggestion: 3 papers max — not 10. One citation per claim in your paper later is enough |

### Days 8-15: Paper + Submission — Optimize for Feedback

| Day | Task | How to Build | Suggestion |
|-----|------|--------------|------------|
| 8 | Compute enrichment/binding stats; chart final | How: Track A: sort affinities, pick top 3 poses. Track B: compute p-values, adjust. Track C: finalize included studies count. Chart final version. | Suggestion: Top 3 results only — not top 30. Depth > breadth for 2000 words |
| 9 | Results synthesis | How: Write 300-word results section: what you found, in order of figures. No interpretation yet. | Suggestion: Results = what you saw. Discussion = what it means. Don't mix — reviewers notice |
| 10 | FULL DRAFT v1 (2000 words): intro, lit, method, findings, limitations | How: Write straight through, no editing. Structure: Intro (300w, question + why), Lit (400w, 3 papers + positioning), Method (300w, data + tool), Findings (700w, 2 figures + interpretation), Limitations (300w, what you couldn't do). Aim 2000. | Suggestion: Write straight through without self-editing — draft is clay, not sculpture. Limit Lit to 400w — reviewers care about your findings |
| 11 | Self-edit: verify every figure vs source; export at print res | How: Search for "very, really, highly" and delete 80%. Verify every number vs source CSV/PDB. Re-export figures at 300dpi. | Suggestion: Use Find → "ly" to catch adverbs. One wrong number in paper is what reviewers remember |
| 12 | Repo hygiene: README with question/method/repro steps, requirements.txt | How: README sections: Question, Data Sources (table from Day 3), How to Reproduce (3 steps: clone, pip install -r requirements.txt, run notebook), License. requirements.txt: `pandas, matplotlib` or `vina` etc. | Suggestion: Test reproduction: delete and re-run notebook in 5 min — if fails, fix now, not after submission |
| 13 | Send to one teacher/mentor; integrate top 5 comments only | How: Send PDF + repo link to one biology teacher/mentor. Ask: "What are top 5 changes?" Integrate only those 5. | Suggestion: One mentor, top 5 comments — prevents feedback spiral. Two mentors × 10 comments = 20 conflicts, no progress |
| 14 | FINAL v2; format to target journal/fair style (verify) | How: Check target guidelines (font, margins, citation style). Reformat exactly. Word count 2000-2200. | Suggestion: Format is not optional — wrong format signals you didn't read guidelines |
| 15 | Archive PDF; abstract formatted; note TUBITAK fair runs spring cycle | How: Archive PDF in Drive + email to yourself. Format abstract in ISEF style (250w, background/methods/results/conclusion). Note TUBITAK Lise Araştırma Projeleri fair is spring — abstract prepared now for next cycle (verify dates). | Suggestion: Archive in 3 places (Drive, email, phone). Spring cycle note prevents panic that you "missed" fair |

## Quality Gates (check before Day 15)

- [ ] Every claim → numbered citation
- [ ] Every figure regenerates from code in <5 min
- [ ] Abstract readable by non-biologist in 60 sec
- [ ] Word count 2000-2200, formatted per guidelines, <15 MB

## Tool Optimization

- One track only — not three — saves 10 days
- README table is documentation — no code comments needed
- Figure + 100-word snippet per day beats writing all at end
