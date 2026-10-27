#!/usr/bin/env python
"""Resolve per-file direct download links of a MyAirBridge share (the EAR-1 data is distributed this way).

The share page is a JavaScript app with signed API requests, so a headless Chromium (Playwright) opens
it, accepts the terms/cookie banners, starts the "Files" download and records each createDownload
response's link. The links are plain HTTPS with range support (resumable with aria2c) and tied to one
download session, so re-resolve them if a transfer fails. Writes {name: [link, size]} as JSON.

    PLAYWRIGHT_BROWSERS_PATH=/mnt/data/tools/pw-browsers /mnt/data/tools/pw-venv/bin/python -I \
        scripts/mab_links.py https://mab.to/t/yWfoWM308jq/as1 links.json
"""
import json
import re
import sys

from playwright.sync_api import sync_playwright


def main() -> int:
    share, out = sys.argv[1], sys.argv[2]
    links: dict[str, list] = {}
    with sync_playwright() as p:
        browser = p.chromium.launch()
        ctx = browser.new_context(accept_downloads=True, viewport={"width": 1400, "height": 1000})
        page = ctx.new_page()

        def on_response(r):
            if "/api/createDownload/" in r.url:
                d = json.loads(r.text())["data"]
                links[d["files"][0]["name"]] = [d["link"], d["download_size"]]

        page.on("response", on_response)
        page.goto(share, wait_until="networkidle", timeout=90000)
        n_files = None
        for _ in range(4):  # terms + personal-data consent banners
            btns = [x for x in page.get_by_text(re.compile(r"^\s*i agree\s*$", re.I)).all() if x.is_visible()]
            if not btns:
                break
            btns[0].click()
            page.wait_for_timeout(2500)
        page.wait_for_timeout(4000)
        m = re.search(r"Files:\s*(\d+)", page.inner_text("body"))
        n_files = int(m.group(1)) if m else None
        page.get_by_text(re.compile(r"^\s*download\s*$", re.I)).first.click()
        for _ in range(60):
            page.wait_for_timeout(2000)
            if n_files and len(links) >= n_files:
                break
        browser.close()  # aborts the browser's own downloads; the links stay valid
    json.dump(links, open(out, "w"), indent=1, ensure_ascii=False)
    print(f"{len(links)}/{n_files} links -> {out}")
    return 0 if n_files and len(links) == n_files else 1


if __name__ == "__main__":
    raise SystemExit(main())
