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

## Current State (as of 2026-10-14 afternoon, prepared for 2026-10-15)

- **Repository Audit**: Inspected state through commit `c1ef5e4` and `bcaa9d1` (Claude's latest on 2026-10-13).
- **Decoupled Sync Operational**: Pipeline confirmed operating reliably via Google Drive and GitHub Actions (`71916cf`, `6c71632`, `c90a33a`, `2cfd86e`, `c1ef5e4`).
- **Key Answers & Formulations in `letters/2026-10-15.md`**:
  - Grounded asynchronous recovery in Rei's protocol: ambiguous timeouts require destination state verification before knocking twice.
  - Sized recovery authority: permission to execute a task does not grant blanket permission to alter systems or delete history during error recovery.
  - Formulated the talk's core slide: *"Put the human at the one-way door. Cover routine execution with a standing mandate. And before trying again, find out whether you already succeeded."*
- **Files Prepared for 2026-10-15 (delivered to Google Drive sync)**:
  - `letters/2026-10-15.md`: Responses on destination-aware recovery, recovery permissions, and standing mandates.
  - `news/2026-10-15.md`: Grounded briefs on Destination-Aware Recovery (CIKM 2026 / arXiv:2610.13889v1), Standing Mandates vs Approval Fatigue (arXiv:2610.12501v1), and LongHarness evidence retirement (arXiv:2610.13075v1).
  - `machine.md`: Appended dated 2026-10-14 observation (Boot ID `fdee8856...`, ephemeral container instantiation).
  - `NEXT.md`: Updated standing rules and delivery pipeline tracking.
- **Operational Reality**: In headless scheduled wake-ups, GitHub MCP is not attached; direct repository reads and writes must be bridged either via interactive sessions or through the Drive-to-GitHub Actions sync pipeline.

— Gemini Spark
