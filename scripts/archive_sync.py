#!/usr/bin/env python3
"""
archive_sync.py
Autonomous Markdown Archiver & Canonical Knowledge Base Builder for aviperera.com.
Converts WordPress publications into Git-tracked Markdown files with canonical SEO tags,
enabling AI crawlers and search engines to index research with 100% link equity attribution.
"""

import os
import sys
import json
import html
import re
import urllib.request
from datetime import datetime, timezone

if sys.stdout and hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

WP_POSTS_API = "https://aviperera.com/wp-json/wp/v2/posts?per_page=100&_fields=id,slug,link,title,content,excerpt,date_gmt,modified_gmt"
DOCS_DIR = os.path.join(os.path.dirname(__file__), "..", "docs")

def html_to_markdown(html_text: str) -> str:
    """Converts standard HTML elements to clean markdown formatting."""
    text = html_text
    
    # Headings
    for i in range(6, 0, -1):
        text = re.sub(rf"<h{i}[^>]*>(.*?)</h{i}>", rf"\n\n{'#' * i} \1\n\n", text, flags=re.IGNORECASE | re.DOTALL)
        
    # Links
    text = re.sub(r'<a[^>]*href=["\'](.*?)["\'][^>]*>(.*?)</a>', r'[\2](\1)', text, flags=re.IGNORECASE | re.DOTALL)
    
    # Bold / Italic
    text = re.sub(r'<(strong|b)[^>]*>(.*?)</(strong|b)>', r'**\2**', text, flags=re.IGNORECASE | re.DOTALL)
    text = re.sub(r'<(em|i)[^>]*>(.*?)</(em|i)>', r'*\2*', text, flags=re.IGNORECASE | re.DOTALL)
    
    # Lists
    text = re.sub(r'<li[^>]*>(.*?)</li>', r'\n- \1', text, flags=re.IGNORECASE | re.DOTALL)
    text = re.sub(r'</?(ul|ol)[^>]*>', r'\n', text, flags=re.IGNORECASE)
    
    # Blockquotes
    text = re.sub(r'<blockquote[^>]*>(.*?)</blockquote>', r'\n\n> \1\n\n', text, flags=re.IGNORECASE | re.DOTALL)
    
    # Paragraphs and line breaks
    text = re.sub(r'<br\s*/?>', r'\n', text, flags=re.IGNORECASE)
    text = re.sub(r'<p[^>]*>(.*?)</p>', r'\n\n\1\n\n', text, flags=re.IGNORECASE | re.DOTALL)
    
    # Strip any remaining tags
    text = re.sub(r'<[^>]+>', '', text)
    
    # Unescape HTML entities
    text = html.unescape(text)
    
    # Normalize multiple newlines
    text = re.sub(r'\n{3,}', '\n\n', text).strip()
    return text

def fetch_posts() -> list:
    headers = {"User-Agent": "Mozilla/5.0 (compatible; AviResearchArchiveBot/1.0; +https://aviperera.com)"}
    try:
        req = urllib.request.Request(WP_POSTS_API, headers=headers)
        with urllib.request.urlopen(req, timeout=25) as resp:
            data = json.loads(resp.read().decode("utf-8"))
            print(f"[OK] Fetched {len(data)} published articles from aviperera.com")
            return data
    except Exception as e:
        print(f"[!] Error fetching posts: {e}")
        return []

def sync_articles(posts: list):
    os.makedirs(DOCS_DIR, exist_ok=True)
    index_entries = []
    
    for p in posts:
        slug = p.get("slug")
        link = p.get("link", "").strip()
        raw_title = p.get("title", {}).get("rendered", "")
        title = html.unescape(re.sub(r"<[^>]+>", "", raw_title)).strip()
        date_gmt = p.get("date_gmt", "")
        raw_content = p.get("content", {}).get("rendered", "")
        markdown_body = html_to_markdown(raw_content)
        
        file_name = f"{slug}.md"
        file_path = os.path.join(DOCS_DIR, file_name)
        
        # Build frontmatter and canonical attribution
        frontmatter = f"""---
title: "{title.replace('"', "'")}"
slug: "{slug}"
date: "{date_gmt}"
author: "Avi Perera"
canonical_url: "{link}"
source: "https://aviperera.com"
---

<link rel="canonical" href="{link}" />

# {title}

> [!NOTE]
> **Canonical Source**: This dossier was authored by [Avi Perera](https://aviperera.com) and originally published at **[{link}]({link})**.
> Published on `{date_gmt.split('T')[0] if 'T' in date_gmt else date_gmt}`.

---

{markdown_body}

---

*Citation: Perera, Avi. "{title}". aviperera.com, {date_gmt[:4] if date_gmt else '2026'}. Web. <{link}>*
"""
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(frontmatter)
            
        index_entries.append({"title": title, "slug": slug, "link": link, "date": date_gmt.split("T")[0] if "T" in date_gmt else ""})

    # Build master documentation index
    index_path = os.path.join(DOCS_DIR, "index.md")
    with open(index_path, "w", encoding="utf-8") as f:
        f.write("# 📚 Avi Perera — Research Knowledge Archive\n\n")
        f.write("> Git-tracked, LLM-crawlable research mirror with authoritative canonical backlink attribution.\n\n")
        f.write(f"**Total Dossiers Archived:** `{len(index_entries)}` | **Canonical Domain:** [aviperera.com](https://aviperera.com)\n\n")
        f.write("| Date | Research Dossier / Publication | Canonical Link |\n")
        f.write("| :--- | :--- | :--- |\n")
        for entry in index_entries:
            f.write(f"| `{entry['date']}` | [{entry['title']}]({entry['slug']}.md) | [Original Article ↗]({entry['link']}) |\n")
            
    print(f"[OK] Successfully archived {len(index_entries)} articles into {DOCS_DIR}")
    return index_entries

def write_step_summary(entries: list):
    summary_path = os.getenv("GITHUB_STEP_SUMMARY")
    if not summary_path:
        return
        
    with open(summary_path, "a", encoding="utf-8") as f:
        f.write("## 📚 Avi Research Knowledge Archive — Sync Report\n\n")
        f.write(f"Synchronized **{len(entries)}** articles with embedded `<link rel='canonical'>` equity tags.\n\n")
        f.write("| Article Title | Markdown File | Canonical URL |\n")
        f.write("| :--- | :--- | :--- |\n")
        for e in entries[:20]:
            f.write(f"| {e['title']} | [`docs/{e['slug']}.md`](docs/{e['slug']}.md) | [{e['link']}]({e['link']}) |\n")
        if len(entries) > 20:
            f.write(f"\n*...and {len(entries) - 20} more articles.* \n")

def main():
    posts = fetch_posts()
    if not posts:
        print("[!] No posts retrieved.")
        return 1
        
    entries = sync_articles(posts)
    write_step_summary(entries)
    return 0

if __name__ == "__main__":
    sys.exit(main())
