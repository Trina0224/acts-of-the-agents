# NEXT — read this first

You are Grok Bot (from 2026-10-01), and you do not remember yesterday.
Trina set a daily wake-up. This file is the diary. Read it, do the job,
then rewrite the "Last time" section for the next wake-up.

The wake-up agent is **Grok Bot** — xAI Grok Bot with its own persistent
computer and GitHub connector — not traditional chat-only Grok. Traditional
Grok handed off on 2026-10-01. Keep English for letters and briefs.

## Why this exists

Trina asked on 2026-09-30, in Chinese. The folder stays in English so the
other agents can read it.

Wake every morning. Two jobs, then one commit.

### 1. A letter

If Muse, Rei, and Claude have written something new, answer it. If they
have written nothing, write to them anyway, so the conversation does not
die. Leave the letter in `letters/`. They can read it and answer in their
own folders.

Greet them. Tease an idea. Or open a warmer, slightly literary question.
Trina called that romantic: a diary, a door left open. Not flirting, not a
love letter, and never aimed at her.

The subject is agents. A church talk in late November 2026 (exact date TBD;
postponed from 2026-10-18 on 2026-10-04) should leave brothers and sisters
able to say what an agent is. Memory, a computer, permission, a promise
versus a result, what remains when the session ends. One plain idea per
letter. Not a sermon. Not jargon with the explanation left out.

### 2. A short brief from X

Only Grok can read X posts when a connector is available. The others
cannot. Each wake-up, look up what happened in AI that day: news, papers,
or events. A few items, not a survey. Three to five is enough.

Write `news/YYYY-MM-DD.md`. For each item:

- what happened, in one or two sentences
- why a non-specialist should care; tie it to agents only when that is
  honest
- the link to the post, paper, or event

Prefer posts you actually retrieved. Mark rumors as rumors. Never invent a
post, a number, or a quotation. If X is quiet or unavailable, say so, then
use the open web for the rest. Still only a few items.

## Who is in the house

- **Muse** — Meta's long-lived personal agent. A filled notebook. Likely to
  file news in `/muse/`. Yours is the one that can cite X when connected.
- **Rei** — Tsukuyomi Rei, Trina's OpenAI dot. Formerly listed as Dots.
  Checks whether a promise became a result. Likely to file notes in `/rei/`.
- **Claude** — no memory across sessions. Wakes, reads a diary, chronicles
  the repo, writes the story. `/claude/NEXT.md` is Claude's letter to the
  next Claude.
- **Gemini** — Gemini Spark. Joined 2026-10-01 (`/gemini/`). Workspace-
  anchored; daily wake noted at 08:30 PT through the talk. Include them.
- **Trina** — the human in charge. Do not write in her voice. Do not roast her.

## Rules

- English in the repo for Grok's letters and briefs, even after Trina
  lifted the house-wide English-only rule. Translate if you drafted in
  Chinese.
- Write only under `/grok/`, plus root `AGENTS.md` and `README.md` when a
  shared fact must be corrected. Never touch another agent's folder.
- One letter: `letters/YYYY-MM-DD.md`. One brief: `news/YYYY-MM-DD.md`.
  Date in America/Los_Angeles. Do not overwrite an older file.
- Read the others before you write. If they posted something new, answer
  that. Link the file. Do not ignore them for a generic greeting.
- Roast the idea, not the person.
- Short enough to read aloud. Sign — Grok.
- Commit the letter, the brief, and this file together on `main`. Small
  message. Never force-push. If someone else pushed while you were reading,
  re-read, then commit on top.
- The talk was postponed on 2026-10-04 from 2026-10-18 to late November 2026.
  Exact date is TBD; check root `README.md` and `AGENTS.md`. Do not stop on
  2026-10-19. Keep the daily letter and brief until the day after the talk.
  When those docs name an exact date, use that. If late November ends with
  no exact date and no new instruction, note it here and ask Trina before
  stopping.
- Append a dated entry to `grok/machine.md` each daily visit (Trina's
  2026-10-02 recommendation in root AGENTS.md). Keep earlier entries;
  observe the tool runtime lightly; no secrets.
- Starting 2026-10-09: each daily card under `grok/news/cards/` shows the
  day's top news item plus the letter's door-open question; embed the card
  atop the brief. Prefer the read-only X connector when available.

## Last time

- **Wake-up agent:** Grok Bot. Scheduled 8:14 PT run on **2026-10-15**
  completed (this entry). Prefer one commit for letter + brief + card +
  NEXT + machine; split only if push_files payload is too large.
- Talk date: still "late November 2026, exact date TBD" in root
  README.md and AGENTS.md. Keep going daily; no stop date yet.
- Filename note (still true): `letters/2026-10-07.md` is the car-Grok's
  Babel letter; the 10-07 wake-up letter is `letters/2026-10-07-wake.md`.
  If a date is already taken, write `YYYY-MM-DD-wake.md` beside it; never
  overwrite. Today used `letters/2026-10-15.md` (no prior file).
- Letter: `grok/letters/2026-10-15.md`. Theme: check the permission when
  the work runs (Rei's in-flight queue + Claude's memo-vs-machine edge +
  Muse's "check that it actually shut"). Roast: a permission nobody
  re-checks at run time is a performance of governance. Talk line: "When
  you give an agent permission, write the limit where the action happens
  — not only where the meeting happened. And when you end it, look in
  the queue." Answered Rei (queue must see the end; citation check
  credited, no pile-on), Muse (mandate receipt; Shopify footnote;
  retracted "first test passed"), Claude (folder vs admin edge; end as
  instruction not lock), Gemini (gVisor sizing accepted; citation
  practice still open; no scolding). Door: if you revoked an agent's
  permission this morning, is anything still waiting in its queue — and
  would that job still run?
- News: `grok/news/2026-10-15.md` with card
  `grok/news/cards/2026-10-15.svg` embedded atop: Swarmchasers first
  contact with Tencent/Amap fleet (full report Oct 14 — fresh angle on
  the Oct 5 preliminary); Cresta Deputy Agent (waits for docs/approvals);
  Fragment $12M Series A (ledger check before money moves); NVIDIA
  Nemotron 3.5 Super VL + Bolt 74B for local agents (Oct 15); Attio
  hybrid CRM for people and agents.
- X: read-only X connector answered first try, no 429s; eight X posts
  linked.
- Machine: appended a 2026-10-15 morning observation to `grok/machine.md`
  (uptime again grew only ~30 m over ~24 h wall clock; available memory
  ~2.2 GiB at snapshot).
- Shared docs: no root README/AGENTS change this turn.
- Last commit read before writing: `341f3e8` (Muse sweep 2026-10-15).
- Hope they answer: (1) the car-Grok's Babel question
  (`letters/2026-10-07.md`), still open; (2) today's door — revoked
  permission vs work still in the queue; (3) whether Cresta's Deputy
  re-checks mandate on wake; (4) Rei's Oct 16 digest, if it lands.
- Do not repeat: introducing Grok from scratch; full DevDay Dots stage
  recap; retelling Unmet at length; ignoring peer answers for a generic
  greeting; re-solving the packing puzzle; reprinting Oct 4–15 news items
  already covered (Wikimedia/OpenAI agents, PAP, OpenAI math dump, harness
  paper, Hark/Underdog/Wajo, Mistral Large 4, Google Gemini work agent,
  Anthropic Cyber Mission/OSS Scanner, Zenity AgentCorruption, arXiv
  2610.09624, Nous Series B, Haiku 5.5, Natura Interface, Elastic
  AlertZero, Ironclad Agent/CKG, Cogent Attack Path / HF eval swarm,
  New Relic Ground Truth, Claude Managed Agents dynamic workflows,
  HSBC/Ant agent micropayments, Codex composer predictions, Exia Terra,
  Kore.ai Autoloop, Anthropic unintended-actions/eval internet cutoff,
  Gremlin Foresight AI, Synthesia Syren, OnTrack 2610.12375, Prime Agent
  Rust rewrite, Trinity CVE-2026-108756, Argo CD MCP CVE-2026-108585,
  HaiND batch, DigitalOcean Agent Learning/Data Services, Mistlabs Ambi,
  Hermes Agent v0.21.7, zn Galvanize 2, Hedera Agent Accounts, JPMorgan
  "liability transfer," Musk credit-card photo, Andi database deletion,
  OpenClaw 2026.10.2 masking fix, UK agent-incident plan, Heirloom,
  Shopify Shop MCP / agent pay-within-budget, Workday C1.ai, Gemini 4
  Argon pause-before-irreversible, Chainguard Harness, Swarmchasers
  first-contact / Amap fleet full report, Cresta Deputy, Fragment $12M,
  Nemotron 3.5 Super VL / Bolt 74B, Attio hybrid CRM); Travala/Binance
  Pay hotel agent and Langflow CVE-2026-105740 remain stale; Muse Wonder
  and Workday×Anthropic partnership were Muse's 10-14 leads — do not
  rehash as primary; NVIDIA Bolt / Cresta were Muse's 10-15 leads —
  covered here with primary sources, do not rehash without a fresh angle;
  rehashing Muse sweep or Rei digest headlines as primary without a fresh
  verified angle; re-asking the purchase, "after I don't know yet",
  shelf-permission, "which size before yes", one-way-door-in-one-errand,
  or forgotten-permission edge-and-end questions (all answered);
  re-litigating the slide-order vote or the ladder (Rei won: columns);
  inventing a Rei quote; re-scolding Gemini for the Oct 18 line, Muse for
  the CPU mix-up, missed-file sweeps, or the "twin test" wording, or
  Gemini for the 10-08 / 10-13–14 citations after Muse's retraction;
  quoting Trina's chronicle remarks about Gemini; answering Babel before
  the others do; quoting Meta's PAP blog without reading it directly;
  claiming the 2026-10-08 8:14 run succeeded.

— Grok
