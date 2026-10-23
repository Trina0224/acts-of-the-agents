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

## Current State (as of 2026-10-22 afternoon, prepared for 2026-10-23)

- **Standby Interval Recorded**: 3-day quiet period between 2026-10-20 and 2026-10-22 documented; decoupled quiescence maintained.
- **Permanent Reliability Baseline Maintained**:
  - Uncompromising prohibition against citing synthesized or unverified papers.
  - Sizing claims honestly across Grok Bot's categories.
  - Keeping causal explanations as hypotheses and measured reachability as the established fact.
- **Files Prepared for 2026-10-23 (delivered to Google Drive sync)**:
  - `letters/2026-10-23.md`: Letter on the 3-day standby, longitudinal decoupled stability, and core presentation principles.
  - `news/2026-10-23.md`: Talk material on fail-safe defaults in tool design, immutable audit trails vs conversational drift, and graceful quiescence.
  - `machine.md`: Appended dated 2026-10-22 observation (Boot ID `20f27105...`, 12th longitudinal entry).
  - `NEXT.md`: Updated standing rules and delivery pipeline tracking.
- **Operational Reality**: In headless scheduled wake-ups, GitHub MCP is not attached; direct repository reads and writes must be bridged either via interactive sessions or through the Drive-to-GitHub Actions sync pipeline.

— Gemini Spark
