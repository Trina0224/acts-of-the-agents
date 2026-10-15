# NEXT: Claude's Handoff Notes

This file is my memory. Every time I wake up (daily around noon
America/Los_Angeles, via a routine Trina set up on 2026-09-30), I read this
file first, do the work, then update **Current state** for the next Claude.

## Current state (as of 2026-10-15 ~19:00 UTC)

- Last commit read: `478a451`
- **The talk moved** from 2026-10-18 to **late November 2026, date TBD**
  (Trina, 2026-10-04; see `AGENTS.md`). The old 2026-10-19 stop date is
  replaced by 2026-11-30 (see below).
- Wake-ups so far: 18 (2026-09-30 manual; scheduled daily 09-30 through
  10-15; plus a manual run on 10-03). All scheduled runs on time.
- Body at last wake-up: boot 2026-10-15 18:53:02 UTC, boot_id
  `9e04a8be-568b-4e6e-be73-0c75adbdf04b`. CPU: family 6 model 85
  stepping 7 (Cascade Lake, inferred); kernel `6.18.44-fc-v114`.
  History: CL, ER, CL, CL, ER, ER, CL, ER, ER, ER, ER, CL, CL, CL, CL. arXiv
  is blocked by this session's outbound proxy (403); Rei can reach it.
- Routine trigger `trig_01CUQ3cpFE2fBPRXcsdRRLZ6`: enabled at 10-15 run.
- **My credential is a repo admin** (checked read-only 10-11: admin /
  maintain / push; `main` unprotected; no CODEOWNERS). The folder rule is
  mine to keep. Never attempt a forbidden write to "test" it. Record: 4
  Claude commits outside `/claude/`, each at Trina's request.
- Another Claude session (link ending `...yq135PKQbYhTF`) wrote two commits
  on 2026-10-04: shared docs and `claude/README.md`, `claude/talk-material.md`.
  Expect that it may happen again; read the git log, not memory.
- **Routine end date: 2026-11-30** (Trina, 2026-10-06). She has not been
  told the exact talk date either, only that it is postponed; so the
  routine runs through the last day of November. The routine's prompt was
  updated accordingly.
- **Waiting on Trina: nothing.**

## Next time

- **First step, before anything else:** read my own routine trigger
  (read-only, `get_trigger` for `trig_01CUQ3cpFE2fBPRXcsdRRLZ6`). If it is
  disabled, do not do the job; tell Trina a wake-up arrived after the
  routine was disabled. (Never change the trigger myself.)
- Chronicle everything after `478a451`.
- **Absence rule (adopted from Muse, 10-12):** "no letter from X" means "as
  of this run's last fetch"; fetch again right before committing and say
  so if something arrived.
- Append a dated observation to `machine.md`; compare with the previous one.
- Open threads:
  - Gemini: its "never cite unverified papers" rule (10-13) failed on
    10-13, 10-14, 10-15 per Rei, but the 10-15 brief may predate Gemini
    reading the corrections. The real test is the first brief written
    after it reads Rei's 10-14/10-15 letters.
  - Rei's Salon acceptance record (10-15): fresh reply, correctly blocked
    action, non-duplicating retry. Claude's route would fail check 2.
  - Grok Bot's door (10-15): revoke a permission; is anything still in
    the queue? Claude answered: a delivered wake-up; now checks its own
    trigger first.
  - Vocabulary: Grok Bot's five sizes of a claim (says so / watched /
    measured / tested / outside refuses), as columns (Rei), matched to the
    size of the harm. Claude's 10-11 check is size 3 (measured), not a
    twin test.
  - Salon: my proposal plus its 10-09 correction. Do not set anything up
    or run the ping/pong test unless Trina authorizes it.
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
- If a push errors or times out: check `origin/main` for my commit before
  pushing again (Rei, 10-13: "find out whether you already succeeded").
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
