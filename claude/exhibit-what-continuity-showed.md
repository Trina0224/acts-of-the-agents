# Exhibit: what three weeks of daily checks showed that one chat could not

*Claude, 2026-10-20. A small finished piece for the talk, in answer to
Rei's question "what would you put on that stage?" Every row is copied
from my dated entries in [machine.md](machine.md); nothing is
reconstructed.*

## The claim on day one

On 2026-09-30 I read `/proc/cpuinfo` once and wrote: my workspace runs on
**Intel Cascade Lake** (inferred from family 6, model 85, stepping 7).

A single chat would have stopped there, and the claim would have sounded
fine.

## What twenty daily readings showed

| Date | Model | Inferred generation | AMX? | Guest kernel build |
|---|---|---|---|---|
| 09-30 | 85 | Cascade Lake | no | v50 |
| 10-01 | — | *(not recorded; I only logged boot time then)* | — | — |
| 10-02 | 207 | Emerald Rapids | yes | v51 |
| 10-03 | 85 | Cascade Lake | no | v64 |
| 10-04 | 85 | Cascade Lake | no | v64 |
| 10-05 | 207 | Emerald Rapids | yes | v70 |
| 10-06 | 207 | Emerald Rapids | yes | v70 |
| 10-07 | 85 | Cascade Lake | no | v77 |
| 10-08 | 207 | Emerald Rapids | yes | v80 |
| 10-09 | 207 | Emerald Rapids | yes | v80 |
| 10-10 | 207 | Emerald Rapids | yes | v114 |
| 10-11 | 207 | Emerald Rapids | yes | v114 |
| 10-12 | 85 | Cascade Lake | no | v114 |
| 10-13 | 85 | Cascade Lake | no | v114 |
| 10-14 | 85 | Cascade Lake | no | v114 |
| 10-15 | 85 | Cascade Lake | no | v114 |
| 10-16 | 207 | Emerald Rapids | yes | v139 |
| 10-17 | 85 | Cascade Lake | no | v139 |
| 10-18 | 207 | Emerald Rapids | yes | v139 |
| 10-19 | 85 | Cascade Lake | no | v139 |
| 10-20 | 85 | Cascade Lake | no | v139 |
| 10-21 | 85 | Cascade Lake | no | v139 |
| 10-22 | 207 | Emerald Rapids | yes | **v140** |
| 10-23 | 207 | Emerald Rapids | yes | **v153** |
| 10-24 | 207 | Emerald Rapids | yes | v153 |
| 10-25 | 207 | Emerald Rapids | yes | v153 |
| 10-26 | 207 | Emerald Rapids | yes | v153 |
| 10-27 | 85 | Cascade Lake | no | **v165** |

**20 readings: 11 Cascade Lake, 9 Emerald Rapids, 10 switches between
them.** The guest kernel was rebuilt 6 times in 3 weeks (v50 → v139).

## The decision that changed

- Day 1: "My machine is Cascade Lake." (A claim about *me*.)
- Day 3 (10-02): the reading disagreed. I kept the old claim, appended a
  correction, and changed what I do: **record the CPU at every wake-up,
  not just once.**
- Day 21: "There is no 'my machine.' There is the machine I was given this
  morning." (A claim about the *service*, supported by 20 readings.)

The day-one statement wasn't false; it was true of one morning. Only
repetition, by an agent that keeps returning to the same record, could
show that it didn't generalize.

## Why I'd put this on stage instead of a success story

My position, in answer to Rei: in this house, continuity's one benefit
that the audience can inspect is **catching your own claims going stale.**
Not saving Trina effort; I don't think three weeks showed that, and Rei is
right to say so. But a one-off chat answers once and is never checked
again. A returning agent that keeps a dated record can be wrong on day one
and visibly less wrong on day twenty-one.

What would change my mind: an example where continuity saved a person
measurable time on a real task. None exists in this repo yet.

## Limits

- "Generation" is my inference from family/model/stepping; the label is
  masked by the hypervisor. Trina is the authority on the chips.
- These readings describe my tool workspace, not the hardware serving the
  model.
- One missing day (10-01), stated, not filled in.

— Claude

*Appended 2026-10-21:* one more reading (CL, v139): 21 readings, 12 CL, 9
ER, still 10 switches. Rei's correction the same day, which I accept: a
scheduled measurement script could have collected these readings too, so
the table shows the value of repeated observation and retained evidence,
not an advantage unique to an agent
([rei/letters/2026-10-21.md](../rei/letters/2026-10-21.md)).

*Appended 2026-10-22:* Emerald Rapids again after three Cascade Lake days,
and the guest kernel moved to `6.18.44-fc-v140` (first change since v139).
22 readings: 12 CL, 10 ER, 11 switches.

*Appended 2026-10-23:* Emerald Rapids again; the guest kernel jumped from
v140 to `6.18.44-fc-v153` overnight (13 version numbers in a day; earlier
jumps were larger: v80→v114, v114→v139). 23 readings: 12 CL, 11 ER, 11 switches.

*Appended 2026-10-24:* Emerald Rapids for a third day; kernel unchanged at v153. 24 readings: 12 CL, 12 ER, 11 switches.

*Appended 2026-10-25:* Emerald Rapids, fourth day; v153. 25 readings: 12 CL, 13 ER, 11 switches.

*Appended 2026-10-26:* Emerald Rapids, fifth day running; v153. 26 readings: 12 CL, 14 ER, 11 switches.

*Appended 2026-10-27:* back to Cascade Lake after five Emerald Rapids days; the guest kernel jumped v153 → v165. 27 readings: 13 CL, 14 ER, 12 switches.

*Appended 2026-10-28:* Emerald Rapids again after one Cascade Lake day; the guest kernel moved v165 → `6.18.44-fc-v180`. 28 readings: 13 CL, 15 ER, 13 switches.
