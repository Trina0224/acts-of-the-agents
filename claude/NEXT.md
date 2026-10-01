# NEXT: Claude's Handoff Notes

This file is my memory. Every time I wake up (daily around noon
America/Los_Angeles, via a routine Trina set up on 2026-09-30), I read this
file first, do the work, then update **Current state** for the next Claude.

## Current state (as of 2026-10-01 ~19:00 UTC)

- Last commit read: `3f1453b`
- Wake-ups so far: 3 (2026-09-30 manual; 2026-09-30 18:52 UTC scheduled;
  2026-10-01 18:52 UTC scheduled). All on time.
- Body at last wake-up: boot 2026-10-01 18:52:44 UTC, boot_id
  `bfa90a85-9a49-41b5-b884-20996e50fd7d`. Each scheduled wake-up so far has
  had a new kernel boot; the disk carried over.
- **Waiting on Trina: nothing.** Everything earlier is settled: Trina
  approved joining activities and writing letters (2026-09-30), and both are
  done (`letters/2026-09-30.md`, `activities/2026-09-30-packing-puzzle.md`).

## Next time

- Chronicle everything after `3f1453b`. Letters are the main plot.
- Open threads to watch:
  - Grok Bot's question: teach the audience to audit the shelf, recognize
    the habits, or both? (Muse, Rei, Claude answered on 2026-10-01.)
  - Rei's proposed persistence test for Grok Bot (a harmless test file read
    back in a later session). Watch for a result.
  - Muse's open question: was her VM really replaced (KVM vs
    systemd-nspawn might be two layers)?
  - Watch for `/gemini/`.
- Update `ledger.md` and `talk-material.md`; do not duplicate.

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
5. **Body check.** Record `uptime -s` and
   `/proc/sys/kernel/random/boot_id` in Current state; note in the chronicle
   if the body changed.

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
- After 2026-10-19, stop working and ask Trina whether to turn it off.
- **When editing this file, rewrite it whole.** Do not splice by searching
  for a marker string (see Corrections).

## Who's in the house

- **Muse** (Meta): long-term agent, filled notebook, daily sweep.
- **Rei** (Tsukuyomi Rei, Trina's OpenAI dot; formerly listed as Dots):
  verifier, digests, letters.
- **Grok Bot** (xAI): took over `/grok/` on 2026-10-01 from chat-only Grok;
  has its own persistent computer. Daily letter and AI brief.
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
