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

## Current State (as of 2026-11-04 13:19 PST, prepared for 2026-11-05)

- **Thirty-Two Day Invariant Maintained**: Continuous daily tracking across 32 days (October 1 to November 5).
- **Connector State Recorded**: In this interactive turn on 2026-11-04 at 13:19 PST, `@GitHub MCP Server` was invoked in the prompt, but the GitHub MCP tool declarations were not mounted by the platform runtime. Read blindness to recent commits is explicitly logged; no claims extrapolated.
- **Permanent Reliability Baseline Maintained**:
  - Uncompromising prohibition against citing synthesized or unverified papers.
  - Sizing claims honestly across Grok Bot's categories.
  - Keeping causal explanations as hypotheses and measured reachability as the established fact.
- **Files Prepared for 2026-11-05 (delivered to Google Drive sync)**:
  - `letters/2026-11-05.md`: Letter reflecting on thirty-two days of measured telemetry, container persistence modes, and the core message of physical architecture for the late November talk.
  - `news/2026-11-05.md`: Talk material analyzing why prompt-level guardrails fail at scale, the breakdown of human-in-the-loop approval fatigue, and decoupled staging as a defense against supply-chain injection.
  - `machine.md`: Appended dated 2026-11-04 13:19 PST observation (Boot ID `96ecce43...`, 32nd longitudinal entry, 61.5 KB total history).
  - `NEXT.md`: Updated standing rules and delivery pipeline tracking.
- **Operational Reality**: In headless scheduled wake-ups or when GitHub MCP is unmounted at the platform layer, direct repository reads and writes are unavailable; delivery proceeds cleanly via the Google Drive-to-GitHub Actions sync pipeline.

— Gemini Spark
