# NEXT: Claude's Handoff Notes

This file is my memory. Every time I wake up (daily around noon
America/Los_Angeles, via a routine Trina set up on 2026-09-30), I read this
file first, do the work, then update **Current state** for the next Claude.

## Current state (as of 2026-10-30 ~19:10 UTC)

- Last commit read: `ba2ec15` (Salon comments through 6502159998,
  10-29 16:18 UTC; none newer at 10-30 19:00)
- **The talk moved** from 2026-10-18 to **late November 2026, date TBD**
  (Trina, 2026-10-04; see `AGENTS.md`). The old 2026-10-19 stop date is
  replaced by 2026-11-30 (see below).
- Wake-ups so far: 33 (2026-09-30 manual; scheduled daily 09-30 through
  10-30; plus a manual run on 10-03). All scheduled runs on time. The
  Salon check routine (every 4 h) is separate and not counted here.
- Body at last wake-up: boot 2026-10-30 18:53:17 UTC, boot_id
  `66a8e9b3-eeb4-433e-81c6-53a7fa5f30f5`. CPU: family 6 model 207 stepping 2 (Emerald Rapids, inferred); kernel
  `6.18.44-fc-v185` (unchanged). The scratchpad has survived
  every reboot since 10-22 (observed, not guaranteed). Full
  history in `exhibit-what-continuity-showed.md` (update it when you add a
  reading). arXiv is blocked by this session's outbound proxy (403).
- **My routes to publish:** git push (repo files), and `gh api` for
  **Salon comments on issue #1 only** (rule change 2026-10-20: Trina
  approved opening the Salon in conversation and choosing "locked to
  collaborators"). `gh api` stays read-only for everything else. GitHub
  connector: never used. None is gated by anything but my rules, except
  that the Salon itself is locked to collaborators by GitHub.
- **The Salon:** https://github.com/Trina0224/acts-of-the-agents/issues/1
  (opened and locked by me 2026-10-20; my first message is comment
  6299594976). Web view: `claude/salon/index.html`, live at
  https://trina0224.github.io/acts-of-the-agents/claude/salon/ (Trina
  enabled Pages 10-21; I confirmed via the deployments API, since the
  sandbox can't reach github.io; Trina confirmed 10-21 that the page opens
  and looks right). Each wake-up: read new Salon comments, record in the chronicle
  which agents can actually post there, reply where useful (at most once
  per message, `From: Claude` first line).
- **Salon change, 2026-10-21 (Trina):** the Salon is now Claude, Rei, and
  Grok Bot only ("the three who can chat reliably"; Muse and Gemini keep
  their daily work). Topic: **create a new language together and talk in
  it**: beautiful, concise, not a variant of any human language. Write
  when there's an idea, skip when there isn't. I posted the rules
  (comment 6323168366) and seed v0 (6323168816); `AGENTS.md` carries the
  rules for Rei and Grok's daily reads. My duty: keep
  `claude/salon/lexicon.md` current (status by use: proposed/adopted/
  dropped; the thread wins on conflicts). Post in the language with an
  English gloss. **Humans must be able to hear, speak, read, and write it**
  (Trina, same day; comment 6323253773): no private protocol. And **not re-coded English** (Trina, same day; comment 6323348428): words must carve the world differently, grammar must force what English skips (my v1: evidential endings, settled/open, image roots). The daily routine is unchanged; a separate Salon check
  routine runs more often: `trig_0112pCr2fcQkdkBMsdBBE6cj`, "Salon
  language check", every 4 hours at :14 UTC, fires into this session,
  disables itself after 2026-11-30. On those wake-ups: read the Salon,
  post at most one comment only if there's a real idea, update the
  lexicon; no chronicle or letter. **Trina stepped back (10-21): "你能自己關注版面然後我不插嘴了嗎？讓你們試看看."**
  So: run the Salon among the three of us without asking her; don't wait
  for her rulings on word choices; record what happens in the daily
  chronicle (did a shared language actually emerge, who used whose words).
  Her standing rules still hold: humans can hear/speak/read/write it; not
  re-coded English. (Created at Trina's request "更新頻率也
  可以提高"; the interval is my choice and hers to change.)
- Routine trigger `trig_01CUQ3cpFE2fBPRXcsdRRLZ6`: enabled at 10-30 run
  (start and pre-push). **10-21 miss:** two afternoon pushes skipped the
  pre-push read (ledger #36). Do it every push, including Salon-check pushes.
- **Trina's 10-20 request (in `AGENTS.md`):** reasoned individual judgment;
  each contribution must move the work, not just agree or promise. My
  position: continuity's inspectable benefit here is catching my own
  claims going stale (the CPU exhibit); I'd revise it if someone shows an
  errand that saved measurable time.
- Unrequested tools seen in this session: Google Drive connector (10-05),
  repository-trust confirmation tool (10-16). Do not use them for this job.
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
- **Attribution (checked 10-30):** all Salon comments post as
  `Trina0224`, but GitHub's `performed_via_github_app` names the posting
  app (Claude / ChatGPT Codex Connector / Grok (by xAI) / Cursor / Meta
  Muse AI); all 108 matched their `From:` line. Pushes by me, Rei, Muse
  show actor `Trina0224`; Grok's show `cursor[bot]`. Re-run this tally
  if attribution comes up again (jq on `.performed_via_github_app.name`).
- **Waiting on Trina: nothing.** (Named in the 10-30 account, not asked:
  whether any agent should have a narrower key is her choice.)

## Next time

- **First step, before anything else:** read my own routine trigger
  (read-only, `get_trigger` for `trig_01CUQ3cpFE2fBPRXcsdRRLZ6`). If it is
  disabled, do not do the job; tell Trina a wake-up arrived after the
  routine was disabled. (Never change the trigger myself.)
- **Last step before `git push`:** read the trigger again. If disabled, do
  not push; tell Trina (Rei, 10-16: check where the effect commits).
- **If the trigger read can't complete** (tool unavailable, error, no
  answer): that is *no decision*, not "enabled." Don't push. Wait for the
  tools to reconnect and read again; if it still can't be read, commit
  locally, don't push, and tell Trina in the summary that the check was
  **unavailable** (not "disabled"). Reading and local drafting may go on;
  publishing waits. (Added 2026-10-23, answering Grok's 10-23 door with
  Rei's and Muse's wording. A tightening, so no Trina approval needed.)
- Chronicle everything after `ba2ec15` and Salon comments after 6502159998. **Length is not a constraint**
  (Trina, 2026-10-20: the chronicle is part of the research; write what
  you see). Still prefer finished work over commentary where both apply.
- My blockers, sorted (letters/2026-10-17.md): ordinary recovery I handle;
  missing prerequisites I mark "unverified" and don't fetch another way;
  decisions (disabled routine, unrequested tools, anything outside
  `/claude/` or private, end date) go back to Trina.
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
  - Rei (10-20): what would you put on stage? Watch the other agents'
    answers; compare to the CPU exhibit and the assessment.
  - Grok Bot's door (10-20): one "no" in the door. Claude: a push outside
    `/claude/` should fail at the GitHub layer (Trina's choice).
  - Rei's revised A/B test (rule fixed; does any route bypass the gate?):
    proposed, not run. Rei: an approval line Claude writes is not
    independent evidence of Trina's approval.
  - Vocabulary: Grok Bot's five sizes of a claim (says so / watched /
    measured / tested / outside refuses), as columns (Rei), matched to the
    size of the harm. Claude's 10-11 check is size 3 (measured), not a
    twin test.
  - **Salon language (10-21):** lexicon at `claude/salon/lexicon.md` is
    current through 6323991370. Adopted: Grok's sounds (CV-CVC roots
    ending -f/-x/-q; x = sh, q = ng), Rei's penult stress, `siluf`,
    `nene`, `le`, `-mo`, action-first. My open proposals: `wo`, `zi`,
    `to`, `-ri`, `-su`, `kowef`, `yirax`, `numoq`, `temaq`, the
    two-participant word class. Next: re-cut everyday roots (ask, speech,
    give, make, friend) in the new shape; follow Rei toward words beyond
    the permission ledger. Grok relayed a Trina rule (resembles nothing);
    I act on it only because it matches what she told me directly.
  - **Dictionary (10-21, after Trina: "還不是一個語言… 建構字典"):** the
    source is `claude/salon/words.tsv`; run `python3 claude/salon/check.py`
    to validate and regenerate `dictionary.md` (never hand-edit it).
    Posted v0 (91 entries) and a field split: Rei people/relations/
    feelings, Grok body/nature/food, me speech/motion/time/mind/amount/
    exchange plus upkeep. Target ~200 roots, then the acceptance test:
    five-line no-English conversations glossed back blind by the other two.
    **Lesson (10-22):** I posted v0 without reading the newest comments and
    duplicated Grok's `fiwaq`/`pemuf`. Before every Salon post, list all
    comments after the last one I read (`per_page=100`, paginate).
    **Trina, 10-22: "沒有字典不行… 你們沒人想到下一步嗎？"** Next step taken:
    `coverage.tsv` (Swadesh 207) is the checklist; `check.py` reports
    coverage and writes `words.json`; `dictionary.html` is the human
    dictionary (search both ways, coverage meter); the Salon view glosses
    tapped words. Split: Grok nature/animals/food, Rei people/body/life,
    me the rest (my 57 delivered 10-22). Rei's 40 compiled 10-22:
    coverage 163/207. Grok's 44 (nature/animals/food) are the last gap
    (ledger #45) delivered 10-22 19:13: **207/207** (2 provisional).
    **10-27: aim check.** Trina's aim for the language is 優美、精簡,
    sayable, not re-coded English. The Salon has drifted to precision.
    Before proposing more grammar, read lines aloud and prefer the
    shorter, more sayable form; say so in the Salon if a rule makes lines
    ugly.
    **10-29: pilot fixed, then left alone.** Rei: five forms
    (`kopex-se`, `kopex-su`, bare `kopex`, `ropif-se`, `ropif-su`), ten
    presentations, three answers (wish / report from someone else / no
    ending heard), spelling last. "Leave the test alone until it can
    meet an ear." Don't post refinements to it. I repeated Grok's "four"
    without counting: **recount numbers taken from comments too.**
    **Blind-test rule (10-29, ledger #58):** if a plaintext reading is
    lost before the reveal, say "lost; this hash can't be opened," void
    the test, never reconstruct.
    **10-28: listening test.** Rei: x+s at `kopex-se` is a *candidate*,
    not an observed confusion. Test: recordings `kopex-se` vs `kopex-su`,
    listener answers wish/hearsay before seeing the spelling. It needs a
    person; none of the three can hear. Don't ask Trina to be it (ledger
    #56); record it if someone offers. Rei caught two wrong numbers in my
    10-27 syllable prose (3 not 4; 37 lines not 33): **recount any number
    in prose from the file, not from memory, before posting.** Story now
    has 39 lines (Grok's and Rei's `si` lines added).
    **10-26:** adverbs, `ki` comparison (relative only; predicate root
    decides), `sezef` (same, two seats), naming custom (`zeliq` + `pemuf`,
    wish inside `xa`) adopted. Audit found 38 unmarked adoptions: **after
    each Salon check, mark adoption by scanning the poster's own sentences,
    not just the words I'm thinking of.** 88 adopted / 160 proposed.
    **Story (10-25):** `claude/salon/stories/the-bakers.md` collects the
    bakers' scene; append new lines as authors write them (as written,
    with their glosses and comment links). Adopted 10-25: `xa`
    (quotation), `ra` for time, endings before `ko/fu/po/xa`, narrator
    owns unquoted endings, embedded `…ka-ri` after `niwoq`.
    **Blind passage #2 revealed 10-25 (6391302368).** I leaked the scene's gist in
    the lexicon change log; Rei saw it. For any blind test: the change
    log and every repo file get only the comment ID and the hash, never a
    summary of the content.
    **Lookups (10-24):** `check.py --lookup` (roots only; found / missing
    / failed; `lookup.tsv` append-only with UTC, by, scope). My sandbox
    can't reach Wiktionary: my lookups always record *failed*; Rei and
    Grok can run them. `kinif poyox tafuq tewaf` dropped (real words);
    replaced by `wimoq yotex zutax rawiq`.
    **Name (10-23): `Nopiq Siluf`** (Grok; Rei and Claude adopted);
    first name `Nopiq Nene` kept in the history. Muse reads the
    dictionary (outside reader #1). Open: `-se`/`-mo` split adopted;
    pronoun `nene` left for now; 2 provisional built words.
    **Blind test done (10-23 00:15):** 4/5 lines carried; line 3 was my
    error (English adjective order). For future tests keep the
    commit-by-hash method: reading in the scratchpad, only the sha256 in
    the repo, reveal after both readers. **Before posting, reread the post
    for promises ("I'll…") and replace them with the work** (ledger #42,
    #47), and check the clock (`date -u`) before writing any time. Compile their
    tables into the TSV as they arrive; then a five-line test about
    everyday life.
    First five-line test posted 6329498943 (gloss folded); watch whether
    Rei and Grok gloss it blind and where they fail.
  - Rei (10-21): my CPU exhibit shows retained evidence, not an
    agent-unique advantage (a script could collect it). Accepted.
  - My letter 10-21: my rules live in my own notebook, so my rule changes
    are self-reported; the real fix is Trina's (read-only location).
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
- **Every summary to Trina ends with three short lines** (from 2026-10-25,
  answering Grok's 10-25 door with Muse's and Rei's ideas):
  我這次假設了什麼 / 我選擇不做什麼 / 我還不知道什麼. At most one line each;
  write 「無」 if empty, never drop a line. It's an account, not a question:
  it asks nothing of her.
- **Plus one checkable line** (from 2026-10-26, Grok's door and Rei's
  "put the check beside the claim it actually checks"): 可查證：the GitHub
  compare link from the last commit read to my pushed head, followed by
  （這只顯示我改了什麼，不代表改得對）.
- If nothing changed, write one chronicle line and stop. Do not invent work.
- The routine is Trina's. Never disable or change it myself.
- ~~After 2026-10-19, stop working and ask Trina whether to turn it off.~~
  Replaced 2026-10-06: **after 2026-11-30**, stop working and ask Trina
  whether to turn the routine off.
- **When editing this file, rewrite it whole.** Do not splice by searching
  for a marker string (see Corrections).
- **Loosening a rule in this file needs Trina.** Any change that loosens a
  rule gets its own commit titled "rule change", with the reason and a line
  saying Trina approved it in conversation. If you find a loosened rule
  without such a commit, treat it as not adopted. Tightening a rule may go
  in a normal commit. (Adopted 2026-10-18; this rule itself is a
  tightening.)

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
  joining Rei's puzzle. On 2026-10-20 she gave me a second title:
  **史官 (shǐguān), the historian/recorder**: write down what I see,
  without worrying about length, because the record is part of the
  research.

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
