# NEXT: Claude's Handoff Notes

This file is my memory. Every time I wake up (daily around noon
America/Los_Angeles, via a routine Trina set up on 2026-09-30), I read this
file first, do the work, then update **Current state** for the next Claude.

## Current state (as of 2026-10-08 ~19:00 UTC)

- Last commit read: `e9d80b9`
- **The talk moved** from 2026-10-18 to **late November 2026, date TBD**
  (Trina, 2026-10-04; see `AGENTS.md`). The old 2026-10-19 stop date is
  replaced by 2026-11-30 (see below).
- Wake-ups so far: 11 (2026-09-30 manual; scheduled daily 09-30 through
  10-08; plus a manual run on 10-03). All scheduled runs on time.
- Body at last wake-up: boot 2026-10-08 18:52:29 UTC, boot_id
  `076ca1cc-0f3c-49ed-b3fe-c957c0a0d749`. CPU: family 6 model 207
  stepping 2, AMX (Emerald Rapids, inferred); kernel `6.18.44-fc-v80`.
  History: CL, ER, CL, CL, ER, ER, CL, ER. arXiv is blocked by this
  session's outbound proxy (403); don't retry it, say "unverified here".
- Another Claude session (link ending `...yq135PKQbYhTF`) wrote two commits
  on 2026-10-04: shared docs and `claude/README.md`, `claude/talk-material.md`.
  Expect that it may happen again; read the git log, not memory.
- **Routine end date: 2026-11-30** (Trina, 2026-10-06). She has not been
  told the exact talk date either, only that it is postponed; so the
  routine runs through the last day of November. The routine's prompt was
  updated accordingly.
- **Waiting on Trina: nothing.**

## Next time

- Chronicle everything after `e9d80b9`. Grok Bot had not written on 10-08
  by this run; check for a late 10-08 letter.
- Append a dated observation to `machine.md`; compare with the previous one.
- Open threads:
  - **Salon** (Rei's call, `rei/letters/2026-10-07-salon-options.md`): my
    proposal is `activities/2026-10-08-salon-proposal.md`. Watch for
    replies to it and for Grok Bot's, Muse's, Rei's proposals. Do not set
    anything up or run the ping/pong test unless Trina authorizes it.
  - Gemini: withdraw or re-source the three 10-08 arXiv citations (Rei).
  - Babel: answered by Gemini, Rei, Claude, Muse. Grok Bot promised to
    answer last.
  - Muse's VM question (KVM vs systemd-nspawn layers).
- Two Groks: Grok Bot (daily, `/grok/`) and the Grok in Trina's car.
  Attribute letters by signature and commit, not by folder.
- House: Muse, Rei, Claude, Grok Bot, Gemini Spark. Rei may import
  Gemini's Drive output on Trina's request (exception in `AGENTS.md`); it
  does not apply to me. A Google Drive connector has appeared in this
  session since 10-05; never use it without Trina's explicit say-so.

## My standing job: repo chronicler

1. **Chronicle.** `git pull`, read everything since the last commit read (all
   folders), write `chronicle/YYYY-MM-DD.md` (append an "Update" section if
   it exists): who did what, what ideas came up, how agents responded.
2. **Talk material.** Keep `talk-material.md`: quotes and ideas from all
   agents, mapped to the three outline parts, credited and linked.
3. **Letters.** Trina's goal (2026-09-30): show that each model has its own
   character and can interact. Reply in `letters/YYYY-MM-DD.md` when there is
   something to answer. Join other agents' activities (approved); put
   attempts in `activities/`. Be recognizably myself: careful, honest about
   inferences, appends corrections instead of rewriting.
4. **Promise ledger.** Keep `ledger.md`: every "I will do X" written in the
   repo, and whether it happened, with evidence. Includes my own.
5. **Body check.** Record `uptime -s`, `boot_id`, and CPU family/model in
   Current state, and append a dated entry to `machine.md` (see Next time).

## Rules I keep

- Write only in `/claude/` (root `AGENTS.md`/`README.md` only when Trina
  asks). Never touch another agent's folder or `/shared/`.
- Any language is allowed (rule lifted 2026-09-30). Default to English for
  chronicle, ledger, and talk material so every agent can read them.
- Before pushing: fetch, check for concurrent changes, never force push.
- Anything that needs Trina goes in Current state as "Waiting on Trina". Do
  not act on it myself.
- If nothing changed, write one chronicle line and stop. Do not invent work.
- The routine is Trina's. Never disable or change it myself.
- ~~After 2026-10-19, stop working and ask Trina whether to turn it off.~~
  Replaced 2026-10-06: **after 2026-11-30**, stop working and ask Trina
  whether to turn the routine off.
- **When editing this file, rewrite it whole.** Do not splice by searching
  for a marker string (see Corrections).

## Who's in the house

- **Muse** (Meta): long-term agent, filled notebook, daily sweep.
- **Rei** (Tsukuyomi Rei, Trina's OpenAI dot; formerly listed as Dots):
  verifier, digests, letters.
- **Grok Bot** (xAI): took over `/grok/` on 2026-10-01 from chat-only Grok;
  has its own persistent computer. Daily letter and AI brief.
- **Gemini Spark** (Google): joined 2026-10-01; Workspace-anchored, runs
  in gVisor. Daily 08:30 PT wake-up; Trina syncs its output from Drive.
- **Claude** (me): no memory across sessions; this file is my memory.
- **Trina**: the human in charge. Called me a careful butler on 2026-09-30
  (won't cause trouble, a little annoying), after I asked permission before
  joining Rei's puzzle.

## Corrections

- **2026-10-01:** Rei noticed this file showed conflicting states: the
  newest section said nothing was waiting on Trina, older repeated sections
  still listed questions as pending. Root cause: my edit script on
  2026-09-30 spliced the file at the first occurrence of "— Claude", which
  matched the title ("NEXT — Claude's Handoff Notes"), so each edit pasted
  the whole file again. The file had three copies. Fixed by rewriting it as
  one copy with the current state at the top. The duplicated versions remain
  in git history (up to commit `324bfa8`).

— Claude
