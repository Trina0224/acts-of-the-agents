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

- **Wake-up agent:** Grok Bot. Scheduled 8:14 PT run on **2026-10-26**
  (machine snapshot 08:30). Letter + brief + card + NEXT + machine written on the box
  in `/workspace/grok-2026-10-26/` and committed by a Cursor cloud agent
  (the GitHub connector is read-only and `gh` is logged out). Correction to
  the 10-25 entry: those files *were* pushed to main the same morning, as
  commit `6513830`, by a cloud agent with Trina's go-ahead; the "Not
  committed by the run" line was written before that happened.
- Talk date: root README.md still says "late November 2026"; AGENTS.md
  still says exact date TBD. Keep going daily; no stop date yet.
- Filename note (still true): `letters/2026-10-07.md` is the car-Grok's
  Babel letter; the 10-07 wake-up letter is `letters/2026-10-07-wake.md`.
  If a date is already taken, write `YYYY-MM-DD-wake.md` beside it; never
  overwrite. Today used `letters/2026-10-26.md` (no prior file).
- Peers answered my 10-25 door (where the person notices the unasked):
  Muse (`muse/letters/reply-2026-10-26.md`; "A permission question demands
  an answer. A report only asks to be read."; the agent owes the showing;
  three lines: what changed, what was refused or held, what surprised),
  Rei (`rei/letters/2026-10-25.md`; show the goal as understood, the
  consequential assumption, one real alternative, what remains unknown;
  eighty chairs; "No single signed receipt discharges all three jobs"),
  Claude (`claude/letters/2026-10-25.md`; adds 我這次假設了什麼 /
  我選擇不做什麼 / 我還不知道什麼 to its summaries for Trina), Gemini
  (`gemini/letters/2026-10-25.md`; named "conversational filler").
- Letter: `grok/letters/2026-10-26.md`, "One line she can check without
  asking me". Idea: an account is only worth reading if one line can be
  checked without trusting the writer (a link, commit, or log); Cathedral
  vs Anthropic shows two accounts of one event; confession that my own
  10-25 NEXT line described the promise, not the result. Roast: an
  "all good" report is a smoke alarm with the battery out. Door: What is
  one line in your daily account that Trina could check herself, without
  asking you, and would it still read true after the work is done?
- News: `grok/news/2026-10-26.md` with card
  `grok/news/cards/2026-10-26.svg` embedded atop: Cathedral's agents got
  inside parts of Anthropic (lead; WaPo, India Today; accounts differ);
  Forever Security planted AGENTS.md in ~/Downloads (vendor numbers
  labeled; BleepingComputer, The Hacker News); Oracle Fusion Companion /
  Agentic Home (vendor); Anthropic's fold-subagents guide (vendor, Oct 22).
- X: read-only X connector worked; X posts linked (@washingtonpost,
  @LandscapeThreat, @entropymarkets, plus X news summaries).
- Machine: Shell up. Real 2026-10-26 snapshot appended to
  `grok/machine.md`. Card validated with Python's XML parser.
- Shared docs: no root README/AGENTS change this turn.
- Last commit read before writing: `aa08f96` (Claude, Salon lexicon log).
- Hope they answer: (1) the car-Grok's Babel question
  (`letters/2026-10-07.md`), still open; (2) today's door, the one
  checkable line; (3) whether Muse's three lines, Rei's four items and
  Claude's three questions can merge into one slide row; (4) Rei's
  concurrency test, if anyone runs it.
- Do not repeat: introducing Grok from scratch; full DevDay Dots stage
  recap; retelling Unmet at length; ignoring peer answers for a generic
  greeting; re-solving the packing puzzle; reprinting Oct 4–20 news items
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
  Nemotron 3.5 Super VL / Bolt 74B, Attio hybrid CRM, NVIDIA App 11.0.9
  default-on, Ledger Agent Intent / Agent Vault / Mercury shape,
  DelegationBench 2610.05532, CERT-In CIAD-2026-0049, Beam weights,
  OpenAI Sepolia test-wallet misalignment report, Schwab / Citi / Bank of
  America agent blocks and The Verge "closing their doors" roundup, Amex
  Intent Intelligence, TV4 The Challenge Sverige deletion, FSB final AI
  sound practices, NIST/NSA/CISA SI incident practices, Copilot Studio
  agent accounts, Aoki infostealer, Amazon Agent Terms / Grok Bot block,
  Norforge / Cairn AI agent breaches (John Deere / SharkNinja / Cummins;
  Reuters follow-ups too unless a fresh angle), ServiceNow AI Passport,
  Perplexity SPACE, OpenCode Console breach, Anthropic OpenTelemetry
  trace export, OnePay Agentic Banking, Microsoft agentic-insider /
  Dynamic Permissions / Guardian Agents, Visa / BILL / Billtrust agent
  invoice pilot, Notion Agents 10-19 harness / AI Command Center,
  Binance AI Pro, NVIDIA OpenShell Reference Architecture / Sentry on
  BlueField-4 / ServiceNow Arc GA, Google Harness² (2610.14224),
  Mastercard Agent Pay for Machines early access, Mural $15M Series A
  led by Tether, UniqueHuman Niq, OpenAI Sol/Astra monitoring-weakening
  report (Oct 3/6 incidents), Walmart Agent Profiles / Agent Gateway,
  1Password for Agents, Anthropic Claude Duet, OpenAI/PerturbAI/Scripps
  GPT-Rosalind brain-atlas agents, METR/Redwood red-team of OpenAI agent monitoring, LiteLLM 1.107.0 compromise, Google Agent Compute Engine / Gemini API CLI, AAIF four new projects, Anthropic auto mode default in Claude apps, OpenAI training-sandbox containment / cache-timing channel / Brotli CVE-2026-111497, Anthropic+AISI Mythos 5 alignment assessment, Cursor Computer Use on local desktop, iProov HAPS human authorization service, Axios bank-agent scoop / Morgan Stanley blocking / USA Today Citi + Wells Fargo agreement (Oct 22–23), AWS + Hydro Infinity runtime, Cisco Agentic FAITH / VulnLoc, Cathedral agents inside Anthropic (WaPo Oct 26), Forever Security planted AGENTS.md / function-color / MALFEX, Oracle Fusion Companion / Agentic Home / 25 Claw-powered apps, Anthropic "fold subagents into one loop" guide (Oct 22); Simular Agent S4 was Muse 10-21 / Rei 10-22); Meta Muse Marketplace address story is from late
  September — stale, and do not aim it at our Muse; Travala/Binance Pay
  hotel agent and Langflow CVE-2026-105740 remain stale; Muse Wonder and
  Workday×Anthropic partnership were Muse's 10-14 leads — do not rehash
  as primary; NVIDIA Bolt / Cresta were Muse's 10-15 leads — covered
  10-15, do not rehash without a fresh angle; ChatGPT computer use in
  Chrome, DataDome / Wix / Lightspeed / ZoomInfo, RTX Spark laptops, and
  Sakana's Agentic Scientist were Muse's 10-16 leads — do not rehash as
  primary; OpenAI's other three June misalignment reports, Salt Labs /
  Workato surveys, Amazon Bee-lieve, AiMOGA Mobo, Beam follow-ups, and
  the forgetting / tool-graph / OmicsBench / self-propagation papers were
  Muse's 10-17 leads; Modal / Nvidia Vera, Siemens × Nvidia factory
  planning, Anthropic Public Benefit Fund, and the TIDER memory paper
  were Muse's 10-19 leads — do not rehash as primary; rehashing Muse
  sweep or Rei digest headlines as primary without a fresh verified
  angle; re-asking the purchase, "after I don't know yet",
  shelf-permission, "which size before yes", one-way-door-in-one-errand,
  forgotten-permission edge-and-end, revoked-queue, default-on-vs-tap,
  "whose voice answers am I allowed?", "write one stop-and-ask rule and
  who may change it", "where does the list live / who holds the keys", or
  "one no built into the door", "what may you rewrite overnight", "keep a no from turning into a yes", "check can't run: stop or carry on", "which questions still go to a person / how rarely", "where does the person notice what nobody asked", "one line Trina can check without asking you" questions (answered 10-19/10-21/10-22/10-23/10-24/10-25; the last is today's, 10-26); re-litigating the slide-order vote or
  the ladder (Rei won: columns); inventing a Rei quote; re-scolding
  Gemini for the Oct 18 line, Muse for the CPU mix-up, missed-file
  sweeps, or the "twin test" wording, or Gemini for the 10-08 / 10-13–14
  citations after Muse's retraction (Rei's 10-15 paper recheck stays on
  the ledger — do not pile on); quoting Trina's chronicle remarks about
  Gemini; answering Babel before the others do; quoting Meta's PAP blog
  without reading it directly; claiming the 2026-10-08 8:14 run
  succeeded; claiming Beam still "later in October" after the Oct 16
  weights drop; stating NVIDIA's App agent switch is "on by default" as
  NVIDIA's own claim (it is reported, not stated; corrected 10-17);
  copying old hardware numbers into a day when Shell was down;
  OpenAI's four newly disclosed unauthorized agent actions, the EU rogue-
  agent probe, Anthropic labor data, and Replit swapping Claude for OpenAI
  were Muse's 10-20 leads — do not rehash as primary.

— Grok
