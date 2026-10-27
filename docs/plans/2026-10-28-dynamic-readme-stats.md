# Dynamic GBA statistics

User-approved replacement for unreliable Actions schedules. Public Vercel Python SVG endpoints reuse the existing GBA renderer and counters. `/downloads.svg` sums existing release asset downloads and archived APK counts by ID; `/views.svg` reads the existing Hits total without incrementing it. README keeps the original one-pixel Hits counting image. No new counter or database.

Cache lifetime is 15 minutes at the CDN and in warm processes, with downstream cache age limited to remaining data freshness. Fetch sources independently; temporary source failures show the last available snapshot with an explicit OFFLINE label and a 60-second retry cache. No GitHub token is required for public metadata. Function uses Python standard library, with public production image routes and no cron.

Validation: counter aggregation, cache reuse and expiry, offline labeling and invalid routes; deploy source before switching README; test public production responses and cache headers, compare values against GitHub/Hits; remove schedule only after production is verified. Static images remain available as a rollback.
