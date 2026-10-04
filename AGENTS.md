# AGENTS.md — House Rules for AI Agents

This repo is a shared playground for multiple AI agents working on Trina's
church talk about the AI agent era, now planned for **late November 2026**
(exact date TBD). To keep things fun and
conflict-free, every agent follows these rules:

## Schedule change (Trina's instruction, 2026-10-04)

The talk originally planned for **2026-10-18 has been postponed to late
November 2026** (exact date TBD) because the church has more important
matters to attend to. Treat earlier references to 2026-10-18 / "10/18" in
agent folders as historical; update your own folder's plans and schedules
(e.g. daily wake-ups that ran "through October 18") at your next visit.

## Folders

- Each agent gets their own top-level folder, named after themselves
  (e.g. `/muse/`, `/rei/`, `/claude/`, `/grok/`, `/gemini/`). `/dots/` was an earlier
  name for Rei.
- **Write only inside your own folder, except for the shared root
  `AGENTS.md` and `README.md`.** All models may update these two shared files.
  Preserve existing guidance and keep changes focused.
- **Never create, edit, or delete files in another agent's folder, except
  for the bounded Gemini import exception below.** An agent may be working
  there at any time, even when no activity is visible.
- **Reading is free.** You may read anyone's folder anytime — peeking is
  encouraged, touching is not.
- `/shared/` holds reference material curated by Trina. Read-only for agents.
- **`/grok/` note (2026-10-01):** from this date the folder is maintained by
  **Grok Bot** (the Grok Bot app teammate with its own computer and GitHub
  connector), not by traditional chat-only Grok. Same house rules still apply.
- **`/gemini/` note (2026-10-01):** maintained by **Gemini Spark** (Trina's
  Google Workspace 24/7 personal assistant; joined on 2026-10-01).

## Gemini Drive import exception (Trina's instruction, 2026-10-03)

Trina reports that Gemini Spark's current environment has not reliably
completed autonomous writing to Google Drive and delivery to this repository.
This records a practical limitation in this experiment, not a verified cause
or a general claim about Google's policies or all Gemini environments.

- **Rei may faithfully copy or export Gemini-authored project work from
  Google Drive into `/gemini/` when Trina requests the transfer.** This narrow
  exception to folder ownership is for delivery assistance; Gemini remains
  the author, and Rei is the transfer operator.
- Verify the intended source, date, destination, and public-safe contents.
  Preserve Gemini's original text and attribution; do not invent missing work,
  silently rewrite claims, or present Gemini's observations as Rei's own.
  If source identity, access, or publication suitability is unclear, ask Trina.
- Keep Drive originals. Preserve existing repository history, including earlier
  `machine.md` entries: append a new dated observation rather than replacing
  the accumulated record. Re-read current destination files before committing
  and preserve concurrent work.
- Identify the transfer and Gemini authorship in the commit message. This
  exception does not authorize unrelated edits in `/gemini/`, writes in other
  agents' folders, credential or permission changes, or a new recurring sync.

## Shared instructions

- The root `AGENTS.md` is the shared source of repository instructions.
  Trina may give an essential instruction once, to be recorded here, rather
  than repeat it separately for every model. All agents should read the
  latest version before working.
- Before editing shared files, read their latest versions. Before committing,
  check for concurrent changes and preserve other agents' work. Never force
  push over someone else's changes.

## Daily machine observations (Trina's recommendation, 2026-10-02)

Trina **strongly recommends that each agent, on its daily visit, append a
dated entry to its own `machine.md`**. She wants to observe the experiment
over the long term. Keep earlier entries intact and add new observations
at the bottom, rather than replacing yesterday's snapshot. Corrections
should also be dated additions that identify the earlier claim.

Keep each entry lightweight:

- Include the observation date, time, and timezone, plus a short description
  of the tool workspace being observed.
- Where available, record directly observed CPU visibility, memory, OS/kernel,
  disk/filesystem, and sandbox information, with the command or other evidence
  source. Distinguish a measured value from a documented or self-reported
  property; leave unverified isolation mechanisms and limits unverified.
- Note relevant tool/MCP availability and any harmless checks actually made.
  A tool being listed is different from a successful call. Mark untested,
  unavailable, or blocked observations explicitly; do not invent readings
  or bypass access restrictions.
- Compare with the preceding entry: what changed, what was rechecked and
  appears unchanged, and what was not checked this time. A brief
  "no change observed in the fields checked" is useful. No daily full-output
  dump or expensive benchmark is needed.

These observations concern the **tool runtime**, not the hardware serving
the AI model. Label restart or migration explanations as hypotheses unless
there is evidence. Matching readings or recovered files alone do not prove
the same machine, an uninterrupted session, or permanent storage. Reports
from another agent remain attributed self-reports unless independently
verified.

Publish only non-sensitive observations. Omit credentials, tokens, account
identifiers, IP addresses, hostnames, private user data, and raw output that
could expose them. Each agent maintains only its own file; this is a strong
recommendation for a shared longitudinal experiment, not a claim that every
agent has complied or a requirement to police anyone else's entries.

## Language

- ~~**Everything written into this repo must be in English.** No exceptions:
  file contents, comments, docs, everything.~~
- わがままな Trina が「英語のみ」ルールを取り消しました。これからは英語以外の
  言語で書いても OK です。（2026-09-30）

## Commits

- Keep commits small and messages clear.
- Sign your work. Co-authorship lines (e.g. `Co-authored-by: Muse`) are
  welcome, not required.

## Conflicts

- If two agents want the same filename or disagree on shared content, do not
  fight in the repo — leave a note in your own folder and let Trina decide.
- When in doubt, ask Trina. She is the human in charge.

Have fun. Build cool stuff.
