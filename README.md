# 101 — Student Study & Application Portal

45-day intensive study and university application system for 3 Turkish high school students targeting US universities with full scholarships. Built as an optimized, offline-first sprint dashboard.

## Students

| Student | IELTS | Target Major | Folder |
|---------|-------|--------------|--------|
| **Azra** | 5.0 → 6.5 | Architecture | `AZRA/` |
| **Ela** | 5.5 → 6.5 | Economics & Finance | `ELA/` |
| **Elfin** | 6.5 → 7.5 | Molecular Biology & Medicine | `ELFIIN/` |

## Structure (each student, 44 files)

```
<STUDENT>/
├── ielts/               5 files: daily-plan, band-target, practice-schedule, resource-links, progress-tracker
├── sat/
│   ├── daily-plan, diagnostic, weak-area-tracker, test-day-checklist
│   └── content-creation/  math-topics (20), reading-strategies, writing-grammar (20), formula-sheet, practice-tests (4 + explanations)
├── portfolio/
│   ├── master-plan, project-breakdown/×3, essays/×8, recommendations/×3, activities/×3, timeline/×3, university-list/×4
└── index.html           Unified 45-day sprint dashboard (offline, LocalStorage, print, dark/light, TR/EN, mobile)
```

Total: **134 files** (132 required + `tools/`).

## Dashboards

Each `index.html` is a single-file, vanilla HTML/CSS/JS app:

- Fixed sidebar (desktop) + bottom tab bar (mobile), calm dark theme (desaturated, low eye-strain)
- **Today-first** sprint hero with overall + 3 pillar rings, Today panel (IELTS/SAT/Portfolio for current day), next-milestone strip
- IELTS: band track, week-filtered 45 day cards, drill timer
- SAT: weekly rhythm strip, 20-topic mastery grid, canvas chart (PT1-4), cheat-sheet modal
- Portfolio: 3-step stepper + tabbed checklists, deliverable tracker, word counters with progress bars
- Deadlines: 4 live countdowns (IELTS Oct 1, SAT Oct 3, ED/EA Nov 1, RD Jan 1), applications checklist, university pipeline with tier badges + Status select
- `localStorage` keys: `AZRA_portal_v1`, `ELA_portal_v1`, `ELFIIN_portal_v1` (merge-safe)

Open any `AZRA/index.html`, `ELA/index.html`, `ELFIIN/index.html` directly in a browser via `file://` — no server, no build.

## Tools

- `tools/sprint-optimizer.py` — analyzes `weak-area-tracker.md` RED topics and suggests tomorrow's warm-up: `python tools/sprint-optimizer.py --student ELA`
- `tools/README.md` — optimization principles

## Sprint

Day 1 Mon Aug 24 2026 → Day 45 Wed Oct 7 2026 (IELTS Thu Oct 1, SAT Sat Oct 3). See each `portfolio/timeline/45-day-sprint.md` for the Gantt.

All content optimized for 45 days: free tools only (Colab, World Bank/IMF/TCMB, GitHub, Canva), pilot Day 18, one built thing > ten proposals, two feedback rounds max. Turkish context (Istanbul/Ankara/Izmir centers, e-Okul, muhtar) and full-ride maps (Karsh, need-blind list, QuestBridge ineligible flagged) throughout.