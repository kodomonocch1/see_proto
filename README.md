# see_proto
Schema-aware JSON compression with millisecond lookups — cut transfer/storage while enabling exists*/pos* queries. (Demo + wheels; core is binary-only)   JSONのスキーマアウェア圧縮。検索可能( exists*/pos* )でI/Oを激減。デモとwheel同梱、コアはバイナリ配布。
## Overview
Schema-aware JSON compression; ms-level exists*/pos* lookups. KPI: combined≈0.195, present p50≈0.18ms.

## 10-minute challenge
1) `pip install see_proto --find-links https://github.com/kodomonocc1/see_proto/releases/download/v0.1.0/`
2) Download **SEE_Proto_Windows_x64_v0.1.0_*.zip** (Assets) and unzip
3) `python samples/quick_demo.py`  → prints ratio/skip/bloom + p50/p95/p99

## ROI (quick math)
`Savings/TB = (1 - 0.195) × Price_per_GB × 1000`  → at $0.05/GB ⇒ **$40.25/TB**
