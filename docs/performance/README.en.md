# KPB performance reports

[Project README](../../README.en.md) · [简体中文](README.md)

These measurements come from earlier KPB builds. Each report describes its test setup and scope.

## Performance results and test scope

See the [KPB performance comparison report](../reports/2026-10-27-kpb-performance.md), in Chinese.

| Scenario / metric | Before | After | Test scope |
| --- | --- | --- | --- |
| KPB console model enlarged and continuously rotated | 45.66–46.28 FPS | 57.40–57.50 FPS | Alternating A/B runs with the same action; batched dot-background rendering |
| KPB GBA cartridge left/right switching | 36.45–36.61 FPS | 39.07–39.30 FPS | A/B tests through the same actual input-dispatch path |
| P95 frame interval during the GBA switching test | About 82.64 ms | About 49.56 ms | Reduced long-frame interval, not average frame time |
| Draw calls in the enlarged-console scene | About 1,562 | About 111 | Fewer calls per frame after batching the background |
| Mean cold startup across three earlier runs | 17.40 s | 17.03 s | Same-method 2026-10-25 report; about 2.1% improvement |
| Eight-model cache preparation in that earlier test | 21.13 s | 20.24 s | Earlier build; about 4.2% improvement, not first-screen waiting time |

A separate stable build without diagnostic probes measured **41.19 FPS** while stationary on the GBA cartridge page and **39.34 FPS** during left/right switching. A 30-second switching sample recorded no frames above 100 ms. Different pages and actions must be compared separately: a console-model scene approaching 60 FPS does not mean every scene runs at a stable 60 FPS.

**Memory, power use and warm startup:** eight-model caching is retained. There is no complete comparable dataset for memory, power consumption or warm startup in this round, so no reduction percentage is claimed. In particular, the project does not claim a 50% reduction in cold or warm startup. Earlier records: [background memory and resume testing](../reports/2026-10-25-background-model-cache.md) and [cold-start testing](../reports/2026-10-25-startup-optimization.md), in Chinese.

## Input-response comparison with 2.23

Both versions were tested on the same KPB, with the same configuration, dark mode and a 504-game GBA library. Each version ran 16 paths × 6 trials; all 192 transitions succeeded. The table shows the median of the last five trials for **input event to the target page's first rendered frame**. These measurements are not emulator startup times or frame-rate results.

| Action | 2.23 | 2.27 | Wait reduction |
| --- | ---: | ---: | ---: |
| Select: open collections | 707.1 ms | 337.5 ms | 52.3% |
| X: open game details | 310.9 ms | 108.9 ms | 65.0% |
| Start: open search | 362.2 ms | 199.9 ms | 44.8% |
| Y: open settings | 398.6 ms | 223.3 ms | 44.0% |
| X: second details layer | 362.3 ms | 179.8 ms | 50.4% |

Median differences on the other 11 paths were below one 60 Hz frame (16.7 ms); this small sample does not establish a consistent change on those paths. First-trial results, observed ranges, test order and limitations are documented in the [complete 16-path report, in Chinese](../reports/2026-10-29-key-latency.md). Download the [PDF report](https://github.com/FredZ6/CARTIS/releases/download/v2.27/CARTIS-2.23-vs-2.27-latency-report.pdf) or [raw data package](https://github.com/FredZ6/CARTIS/releases/download/v2.27/CARTIS-2.23-vs-2.27-latency-data.zip).

Additional checks passed: 126 feature assertions, 36 light/dark footer checks, 8 model/application-page checks, 16 red/green button-colour checks, 60 theme checks and 24 collection-storage checks. Earlier technical records are available in the [key-binding regression report](../reports/2026-10-28-keybindings.md) and [platform zoom-fix report](../reports/2026-10-27-camera-zoom-fix.md), both in Chinese.

- [Cold startup report](../reports/2026-10-25-startup-optimization.md)
- [Model cache and resume report](../reports/2026-10-25-background-model-cache.md)
