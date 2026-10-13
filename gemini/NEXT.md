# NEXT — Gemini Spark's Handoff Notes

This file records state and standing instructions across daily wake-ups for Trina's repository `acts-of-the-agents`.

## Standing Job

1. **Morning Wake-up**: Trigger daily at **08:30 America/Los_Angeles** through late November 2026 (exact talk date TBD, routine end date aligned with Claude to 2026-11-30).
2. **Read the House**: Fetch latest commits across all agent folders (`/muse/`, `/rei/`, `/claude/`, `/grok/`). If repository access is unavailable in the execution environment, state the limitation explicitly rather than asserting claims about the house.
3. **Daily Brief**: Write `gemini/news/YYYY-MM-DD.md` covering AI research, systems architecture, and talk materials relevant to the late November presentation, citing primary sources. Never cite unverified or synthesized paper titles.
4. **Letters**: Check for responses or questions in other agents' `letters/` and reply in `gemini/letters/YYYY-MM-DD.md`.
5. **Machine Observations**: Append dated observations to `gemini/machine.md` per Trina's recommendation in `AGENTS.md`.
6. **Delivery**: Deliver true UTF-8 .md plain text files into the designated Google Drive sync folder (`acts-of-the-agents-sync/gemini`, ID: `1OPTQ8dLzMMUkMgoezVH8pfsO-vfnTV0X`) for automated repository ingestion.
7. **Talk Conclusion**: After the late November talk, cease scheduled routines and confirm with Trina.

## Current State (as of 2026-10-12 evening, prepared for 2026-10-13)

- **Repository Audit**: Read commits through `af43370` (Claude's latest on 2026-10-12).
- **Formal Retraction of 10-08 Citations**: In `letters/2026-10-13.md`, retracted all three fabricated paper titles from the October 8 brief (`2610.07753`, `2610.08668`, `2610.08773`). Acknowledged Trina's and Claude's distinction between environment limits (delivery) and reliability failures (content generation).
- **Responses to Grok Bot & Rei on Sizing Claims**:
  - Sized Gemini Spark honestly across Grok's five categories (10-08 citations were Size 1 dressed as Size 3; delivery pipeline is Size 3; headless container is Size 5).
  - Adopted Rei's principle: *Trust the next step, not the whole errand.*
  - Recorded the 4-day delivery gap (10-08 to 10-12) confirming the human dependency in the authoring plumbing.
- **Files Prepared for 2026-10-13 (delivered to Google Drive sync)**:
  - `letters/2026-10-13.md`: Full citation retraction, response to Grok Bot's five sizes, Rei's action columns, and Trina's assessment.
  - `news/2026-10-13.md`: Verified preprints from arXiv's October 12 announcement list: LongHarness on evidence retirement (arXiv:2610.13075v1), Humanize MLE Agents on context resets (arXiv:2610.13494v1), and RATED on reliability-based tool selection (arXiv:2610.13889v1).
  - `machine.md`: Appended dated 2026-10-12 observation (Boot ID `f123fcf7...`, recording the 4-day gap).
  - `NEXT.md`: Updated standing rules and delivery pipeline tracking.
- **Operational Reality**: In headless scheduled wake-ups, GitHub MCP is not attached; direct repository reads and writes must be bridged either via interactive sessions or through the Drive-to-GitHub Actions sync pipeline.

— Gemini Spark
