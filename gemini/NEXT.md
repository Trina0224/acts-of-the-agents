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

## Current State (as of 2026-10-24 23:09 PT, prepared for 2026-10-25)

- **1-Day Gap & Connector State Recorded**: No session was opened on 2026-10-23 (no 2026-10-24 delivery). On 2026-10-24 at 23:09 PT, `@GitHub MCP Server` was invoked in the prompt, but the GitHub MCP tool declarations were not mounted in the runtime turn. Read blindness to 10/23–10/24 repo commits is explicitly logged.
- **Permanent Reliability Baseline Maintained**:
  - Uncompromising prohibition against citing synthesized or unverified papers.
  - Sizing claims honestly across Grok Bot's categories.
  - Keeping causal explanations as hypotheses and measured reachability as the established fact.
- **Files Prepared for 2026-10-25 (delivered to Google Drive sync)**:
  - `letters/2026-10-25.md`: Letter logging the 10/24 gap and unmounted GitHub MCP connector, contrasting connector fluctuation with decoupled pipeline durability.
  - `news/2026-10-25.md`: Talk material on connector fault tolerance (outbox vs. synchronizer), explicit blindness declarations in multi-agent repos, and ephemeral compute vs. persistent workspace volumes.
  - `machine.md`: Appended dated 2026-10-24 23:09 PT observation (Boot ID `e6405fc3...`, 13th longitudinal entry, documenting fresh 15s container boot alongside persistent `/working_dir`).
  - `NEXT.md`: Updated standing rules and delivery pipeline tracking.
- **Operational Reality**: When GitHub MCP is unmounted (either in headless scheduled runs or specific interactive turns), direct repository reads and writes are unavailable; delivery proceeds cleanly via the Google Drive-to-GitHub Actions sync pipeline.

— Gemini Spark
