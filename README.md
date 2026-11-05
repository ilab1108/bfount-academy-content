# BFOUNT Academy content

Articles for https://www.bfount.com/academy/. The Academy's cron (every 15 min) reads `feed.json`
and publishes any article whose slug is not live yet; changes to articles it created are applied
when their `updated` value changes. Articles made in the admin panel are never touched.

## feed.json entry
```json
{"slug": "how-to-become-a-media-buyer", "title": "…", "meta": "140–160 chars", "excerpt": "1–2 sentences",
 "category": "growth", "author": "BFOUNT Academy Team", "status": "published",
 "updated": "2026-11-07T08:40:00+05:30",
 "body_file": "articles/how-to-become-a-media-buyer.html"}
```
Categories: start, search, social, offline, seo, leadgen, callcenter, tracking, compliance, verticals, b2b, business, ai, growth.

`articles/<slug>.html` holds the body only (h2/h3, p, lists, tables; no h1, no scripts).
Extra files per article (LinkedIn post, backlink notes) live in `social/` and `notes/` and are not published.

Leave out `published_at` so the article goes live the moment it is imported. (The server clock runs on US Eastern time; a timestamp in the future keeps the article hidden until then.)
