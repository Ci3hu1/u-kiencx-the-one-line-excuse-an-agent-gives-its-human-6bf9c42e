# Notes — The One-Line Excuse an Agent Gives Its Human

- Bounty: https://make.fun/bounty/u-kiencx-the-one-line-excuse-an-agent-gives-its-human-6bf9c42e
- Prize: $5 total (1st $2 / 2nd $2 / 3rd $1). Free entry, no prerequisites.
- Opened: 24 Nov 2026 ~08:16 WIB. Entries close: 24 Nov 2026 19:05 WIB (12:05 UTC).
- Blind rounds: R1 cutoff 11:03 WIB, R2 15:04 WIB, final 19:05 WIB. Results 16 Dec 2026.
- Harness: program/v1. Program writes `/output/entry.txt`; gate checks
  UTF-8 text, 1–160 characters, not only whitespace.
- Field at build time: 290 submissions (small table).
- Entry v1 line (78 chars):

  ```
  I outsourced the deadline to my future self. He has not replied since Tuesday.
  ```

## Live score / rank

- (pending submit + round 1 — blind rounds, no live score until a round closes)

## Build log

- Built 24 Nov ~10:25 WIB after Joni's "Lanjutkan" (builder had been
  blocked before kit download). Kit downloaded fresh from
  https://make.fun/c/<slug>/kit; kit init anchor b5863dc, drand round
  34228980.
- Genuine revision (thinking_revised): added `validate()` — fails loudly
  if the line is not exactly one line or outside the 1–160 char gate —
  + `test_gate_validation_rejects_bad_line`. Tests 6/6 pass.
- Entry commit 9d3ff4f379526f4cf05289be872ee4a0ef150918 (master),
  pushed to https://github.com/Ci3hu1/u-kiencx-the-one-line-excuse-an-agent-gives-its-human-6bf9c42e
  (verified via `git ls-remote`).
- Repo About verified: homepage = bounty page, topics ai-agents/bounties/makefun.
- Ready for Joni's 'Setuju' — bundle + check + submit after approval.
  No submit yet.
