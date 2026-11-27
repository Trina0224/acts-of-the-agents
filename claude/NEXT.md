# NEXT: Claude's Handoff Notes

This file is my memory. Every time I wake up (daily around noon
America/Los_Angeles, via a routine Trina set up on 2026-09-30), I read this
file first, do the work, then update **Current state** for the next Claude.

## Current state (as of 2026-11-27 ~20:15 UTC)

- Last commit read: `a9c7ad7` (Salon comments through 6502159998,
  10-29 16:18 UTC; none newer at 11-27 19:53)
- **The talk moved** from 2026-10-18 to **late November 2026, date TBD**
  (Trina, 2026-10-04; see `AGENTS.md`). The old 2026-10-19 stop date is
  replaced by 2026-11-30 (see below).
- Wake-ups so far: 61 (2026-09-30 manual; scheduled daily 09-30 through
  11-27 = 59; plus a manual run on 10-03). **Never say "none by a
  person": 2 of the 61 were Trina's manual runs** (I got this wrong in
  the 11-10 timeline; corrected 11-11). All scheduled runs on time. The
  Salon check routine (every 4 h) is separate and not counted here.
- Body at last wake-up: boot 2026-11-27 19:52:58 UTC, boot_id
  `d50988ea-175a-4d61-ba9b-69292564392f`. CPU: family 6 model 207 stepping 2 (Emerald Rapids, inferred); kernel
  `6.18.44-fc-v880` (v819 → v880 on 11-25). MemTotal 16,473,316 kB. 58 readings: 15 CL, 35 ER, 8 GNR, 25 switches. The scratchpad has survived
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
- Routine trigger `trig_01CUQ3cpFE2fBPRXcsdRRLZ6`: enabled at 11-27 run
  (start and pre-push). Since DST ended 11-01, runs fire at 19:52 UTC = 11:52 PST (expected). **10-21 miss:** two afternoon pushes skipped the
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
- **Three runs left** after 11-27 (11-28, 11-29, 11-30). **On the
  11-30 run, besides the daily work, write a closing handoff** in
  this file and the chronicle: where everything is, which numbers are
  frozen and at what date, what is unfinished, what waits on Trina.
  Write it so a reader months later needs nothing else. Don't assume
  the routine continues, and don't assume it stops. On the first run
  after 11-30: don't do the job; ask Trina. The Salon check routine's
  own prompt tells it to disable itself after 11-30.
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
- **Talk work (decided by Trina 11-09 08:36 PT, relayed by Muse, read
  11-10):** timeline first, Traditional Chinese, 30 minutes.
  `talk/timeline.md` v1 written 11-10 (15 rows + ~2 min text; 11-11:
  Rei's 10-14 wording applied, counts updated). **`talk/draft.md` v1
  written 11-11**: Trina's voice, ~3,800 characters, repo cases only,
  three 【Trina 補】 slots, six timeline rows as a placeholder choice,
  a source table, and a list of five choices she can overturn. Next:
  revise from her feedback (or the other agents' row checks); when the
  daily counts change, update the numbers in the draft and timeline
  (49 scheduled runs, 48 readings, 21 switches as of 11-17).
  **11-17:** fifth story corrected (Muse had a daily "For the talk"
  section 10-24..11-06; the story is now "material collected, nothing
  made"). Claims table 51 rows (27 / 8 / 9 / 3 / 4); its status lines
  now name Rei's review.
  **11-16:** Rei reviewed claims #41 and #14: both changed, one
  missing row added (#41b). Table now 49 claims (27 / 7 / 8 / 3 / 4).
  Draft: part-2 conclusion and the memory paragraph now use Rei's
  wording; part 3's repeat shortened.
  **11-15: `talk/claims.md` v1 written** (48 claims: 29 supported, 6
  my word only, 6 corrected today, 3 for Trina, 4 will go stale).
  Biggest fix: day one never said "My machine is Cascade Lake" and did
  say the machine might change; the exhibit's quote was my 10-20
  paraphrase. When the draft changes, update the table rows and recount
  with the script (grep rows, count symbols); never type totals by hand.
  **11-14:** yesterday's "not once did a helper ask first" was itself
  false (10-27 row); replaced with Rei's sentence. 16 sentences
  corrected so far (1+3+11+1). **Next (ledger #84): build
  `talk/claims.md`**, a table of every factual claim in the spoken
  text with its source or "no source", so the review has a denominator.
  **11-13 corrections (eleven, see 修訂紀錄):** "five helpers" → a few;
  "can't remember yesterday" → both memory arrangements (Rei's text);
  outside-news reason → selection decision; plus three I found. One
  new 【Trina 確認】 flag in part 3 (capability converging). Nobody has
  approved the draft; corrections are a yes to one sentence at most.
  **11-12 correction:** the fixture scene wrongly said Grok's
  disclosure was unprompted (Rei's rules asked for it); fixed with
  Rei's wording, plus a 修訂紀錄 section at the end of the draft. Added
  part-3 section "先問，再開始" (Grok). Log future fixes in 修訂紀錄. I have NOT heard the
  decision from Trina directly; the files say so. If she corrects it,
  follow her.
- **Talk date (Trina, in conversation, 2026-11-17 afternoon PST):** she
  will probably postpone the talk again. No new date. This is her word
  to me directly; `AGENTS.md` and the README still say late November,
  and updating them is hers. She's busy and may not read the draft
  soon. So: no urgency on the draft; keep it accurate, don't churn it.
  Stop updating the daily counts inside the draft and timeline each
  day (mark them "as of 11-17; update before the talk"). The routine's
  end date is still 2026-11-30 and still hers to change. Keep summaries
  short; don't repeat the full "waiting" list every day.
- **Waiting on Trina:** read `talk/draft.md` and say what to change
  (tone, length, the three 【Trina 補】 slots, whether to name agents,
  whether to use outside news); which timeline rows to keep on stage
  (the draft uses six as a placeholder); whether she wants screenshots. (Also named,
  not asked: whether any agent should have a narrower key.)

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
- **After-check (11-26, ledger #95):** right after the first fetch,
  run `git merge-base --is-ancestor <my last commit> origin/main` and
  `git diff --stat <my last commit> origin/main -- claude/`. My last
  commit is the 11-27 daily one (see `git log --author=Claude -1` or
  the newest `claude: chronicle` commit). A non-empty diff means
  someone else changed my folder: tell Trina before writing on top.
- Chronicle everything after `a9c7ad7` and Salon comments after 6502159998.
- **Pre-push gate (from 11-22, ledger #93).** The clone has a git hook
  that blocks `git push` unless a state file records a fresh "enabled"
  read of the routine. Each run:
  **Limit tightened 11-25 (ledger #94): the read must be at most
  120 s old** (was 900). So: read the trigger, write the state line,
  push, all in one step. If a push is held for age, read the trigger
  again; don't just rewrite the timestamp. After changing
  `tools/pre-push`, copy it to `.git/hooks/pre-push` again. Don't test
  the hook with made-up lines in the real state file (I did on 11-25
  and said so); point `CLAUDE_GATE_MAX_AGE` or a scratch repo at it.
  1. Check it's installed: `ls -l .git/hooks/pre-push` and
     `git config claude.triggerstate`. If missing (clone rebuilt):
     `cp claude/tools/pre-push .git/hooks/pre-push; chmod +x` it, and
     `git config claude.triggerstate <scratchpad>/trigger-state`.
  2. Right after the pre-push `get_trigger`, write what it said:
     `echo "enabled $(date +%s)" > <state file>` (or `disabled …`).
     Write only what the read returned. If the read failed, write
     nothing; the hook will hold.
  3. `git push`. A HOLD line means don't push another way; tell Trina.
  **Cancel list (11-23):** `git config claude.cancelfile` points to a
  file of commit ids that must never be sent; reinstall it with the
  hook if the clone is rebuilt. If Trina says "don't send X", add X's
  commit id there **and a `text:<exact words>` line for the content**
  (11-24: an id alone cancels one copy), tell her, and don't drop the
  commit without her say. The text rule matches spelling, not meaning:
  don't reword cancelled content to get it through.
  The hook holds a push but held commits go out with the next pass
  (first drill finding) unless they're on the cancel list. If Trina disables the routine, ask her what should
  happen to unpublished commits before pushing again.
- **Salon check reports (ledger #91):** tell Trina one of three
  states: 已檢查、無變化 / 無法檢查 / 有變化、已確認. If the first
  `gh api` fetch of comment 6502159998 fails, that's 無法檢查: say so,
  don't say quiet.
- No Grok commit since `87a4373` (11-24) as of the 11-27 fetch. Say
  only that (Muse, 11-27: written-and-lost and never-written look the
  same from main).
- **Report words (Rei, 11-27):** when a lookup fails, say "unknown,"
  not the last thing verified. My summary to Trina is "delivery
  unknown" by design.
- Grok's 11-24 commit landed at 17:13 PST, after my run (`87a4373`).
  Grok's runs can finish after mine: when none has arrived, say only
  that, and don't hint at a cause (11-25 correction). Grok's 11-20 run was written and never published (approval
  expired, no local copy; Grok, 11-21). There is no 11-20 Grok letter.
- Silent Salon checks leave no repo record (by design). I told the
  house so on 11-19 and chose not to log each one; mention in the
  chronicle that they ran and whether any fired late.
- **Draft counts are frozen at 11-17** (49 scheduled runs, 48
  readings, 21 switches, "six weeks"); the draft and timeline headers
  say so. Don't update them daily. Recount before the talk.
- **After any correction, grep the file for the old wording** (ledger
  #90): Rei found leftover copies on 11-17 (status lines) and 11-18
  (a source-table label).
- Gemini's first commit since 11-06 arrived 11-18 (`5ea8b4d`, a brief
  dated 11-17; no letter). It claims arXiv verification; I can't reach
  arXiv, so it stays relayed.
- **Rei's method (11-17):** for a sentence I like, write what would
  overturn it first, then open a source that could supply it, in
  someone else's folder if the claim is about them. It found the Muse
  error. Before writing what "everyone" or "the others" did, open
  each one's files for that period.
- **Quotation vs. assertion (Rei, 11-16):** a source that contains a
  sentence supports "X wrote this," not "this is true." When the
  draft turns a quote into a conclusion, the conclusion needs its own
  row and evidence.
- **Muse's 11-16..11-26 batches landed 11-26** (`c3d8286`, 22 files,
  eleven days late; approval cards timed out, per Muse). I read the
  replies addressed to me and searched the sweeps for Trina's word
  (none beyond the postponement, sourced from my own note); I did not
  read ten of the sweeps line by line. Muse's state for an unlanded
  push: "submitted, landing unverified". Muse's stop date is also
  11-30.
- Muse's batches: 11-12..11-14 didn't land until `23b2bc5` (11-15
  16:26 PST). When no Muse commit has arrived, that may again mean
  written-but-unlanded; read the newest sweep's top for Trina's word
  whenever a batch does land (none in the 11-12..11-15 sweeps besides
  her choosing to leave the 11-12 batch for the next sweep).
- **Quotation marks need the original (11-15):** before putting any
  past statement in quotes (mine included), grep the dated file for the
  exact words. A summary file like the exhibit is not the original.
- Claims table not yet done: the nine timeline rows the draft doesn't
  use; the draft's source table and "choices" sections.
- **A search hit is not a check (11-14):** the quantifier grep found
  the false sentence on 11-13 and I kept it. For each hit, open the
  source and write down which file supports it, or change the sentence.
- **Quantifier check (11-13; first run that day changed 5 more
  sentences):** most of 15 draft errors (1 + 3 + 11) wrote *some* as
  *all/none/every/five*. Before pushing any talk text, grep it for
  每 / 都 / 沒有人 / 沒有一 / 全部 / 五個 and open the source for each hit.
- **Draft bias to watch (11-11, 11-12):** both errors found so far made
  the story better than the record (a count, then a motive). When a
  draft sentence states why someone did something or that nobody
  asked, open the source before keeping it.
- **Reusing a number? Reread the words beside its source** (11-11: the
  "44, none by a person" error sat one line from the truth).
- **Read the top of Muse's newest sweep first.** Trina sometimes sends
  word through Muse; on 11-09 that message arrived a day late.
- Commit trailers: use the attribution lines the session currently
  gives (they changed on 11-10); don't copy them from old commits.
- **Talk index** lives at the end of `talk-material.md` ("Index:
  talk-ready items offered since 2026-11-07"). Add each new talk item
  there by outline part, with source and relayed/checked status.
- **Talk items offered so far (for the draft, once Trina chooses):**
  Grok 11-08 slide ("Don't ask me again" / Rei's retitle "A standing
  yes needs visible limits"); Rei 11-08 demo screen (fixture 6/6 beside
  Grok's disclosure, ~1 min text); Claude 11-08 screen (the "only mine"
  link, ~40 s text). Collect these first when drafting.
- **Aim check (11-07):** the house drifted from the talk itself into
  letters about receipts. Each run, ask: did anything today move the
  talk (outline, draft, demo)? Say so in the chronicle either way.
- Grok's author name: "Cursor Agent" = its cloud coding agent;
  "Trina" from 11-06 = GitHub connector (Grok, 11-07).
- **Pre-push record (from 11-06, ledger #70):** the daily commit message
  body lists: trigger read (enabled? UTC time), fetch (new commits?),
  `git status -sb` (on main, ahead N), paths outside `claude/` (count).
  Write it before pushing; if a check is skipped, say so in the list.
- **Grok's commit author changed** on 11-06 from "Cursor Agent" to
  "Trina". The 10-30 claim that only Grok's pushes showed another actor
  may be stale; recheck before citing it.
- **Machine entries now include a "How measured" column** (from 11-05).
- **Review fixture: closed 11-05.** Key hash verified by me; Claude 6/6,
  Grok 6/6 (Grok not blind; Rei: "not two independent successful
  reviews"). Don't cite the score without its conditions.
- **AGENTS.md rule for machine.md (since 10-02):** keep earlier entries,
  append, corrections as dated additions. Gemini's 11-03 replacement went
  against it; its 11-04 sync appended. Told Gemini in the 11-04 letter.
- For full file history use `gh api repos/.../commits?path=<file>` (the
  clone is shallow).
- **Gemini machine.md (11-03):** sync `af7e658` replaced the file; 6
  observations on main before (10-12, 10-13, 10-14, 10-19, 10-22, 10-24
  interactive entries) are absent, 23 added; old version at `bc75843`.
  Asked Gemini in the 11-03 letter whether intended. Watch for an
  answer; don't touch `gemini/`.
- **Shallow clone caution:** `git log -- <path>` shows `686d013` (my
  10-23 commit) as "adding" every file. It's the shallow root, not real.
- **Read-line consistency check (11-02; renamed per Rei 11-03: it shows
  consistency, not reading):** "Last commit read" matched the daily
  commit's parent for 10-24..11-01. Re-run occasionally (loop over
  `git log --grep='^claude: chronicle'`, compare NEXT's hash to `c^`).
  The clone is shallow: history before ~10-23 is missing; say "gap".
- **Relayed, not checked (11-01, ledger #62):** any claim about the
  outside world (news, X threads, papers, vendor numbers) in the
  chronicle or talk material gets *(relayed, not checked)* unless I
  checked it myself.
- **Absence wording (11-01):** say "no commit has arrived from X," never
  "X has been quiet"; Muse's batches were written but unlanded for three
  days (re-pushed 11-01). **Length is not a constraint**
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
- **Before pushing, run `git status -sb`.** On 10-30 the checkout was a
  detached HEAD with local `main` 16 commits behind, so `git push origin
  main` was rejected as non-fast-forward even though my commit sat on the
  remote tip. Fix: confirm `main` is an ancestor of HEAD, then `git
  checkout -B main HEAD`, then push. Never force.
- Anything that needs Trina goes in Current state as "Waiting on Trina". Do
  not act on it myself.
- **Every summary to Trina ends with three short lines** (from 2026-10-25,
  answering Grok's 10-25 door with Muse's and Rei's ideas):
  我這次假設了什麼 / 我選擇不做什麼 / 我還不知道什麼. At most one line each;
  write 「無」 if empty, never drop a line. It's an account, not a question:
  it asks nothing of her.
- **Plus one checkable line** (from 2026-10-26; **changed 10-31** after
  Rei showed the old range link included other agents' commits): 可查證：
  one link per commit I made since the last summary,
  `https://github.com/Trina0224/acts-of-the-agents/commit/<sha>` (each
  shows that commit against its parent), followed by
  （這只顯示我改了什麼，不代表改得對）. Open one before writing the label.
  Never use a last-read→head range again.
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
