# 📚 Avi Perera — Research Knowledge Archive

[![Archive Sync](https://github.com/a-vip/avi-research-archive/actions/workflows/archive-and-pages.yml/badge.svg)](https://github.com/a-vip/avi-research-archive/actions/workflows/archive-and-pages.yml)
[![License: CC-BY-4.0](https://img.shields.io/badge/License-CC_BY_4.0-lightgrey.svg)](LICENSE)
[![Canonical: aviperera.com](https://img.shields.io/badge/Canonical-aviperera.com-blue.svg)](https://aviperera.com)

An automated, Git-tracked Markdown knowledge base and mirror of peer-reviewed articles, AI governance frameworks, and lethal autonomous weapons systems dossiers by **[Avi Perera](https://aviperera.com)**.

---

## 🎯 Architecture & SEO Equity Pass-Through

Search engine bots, GitHub code crawlers, and AI LLM search engines (Perplexity, ChatGPT, Claude) parse GitHub repositories at immense scale. 

To maximize domain authority and prevent duplicate content penalties:
1. Every archived document in [`docs/`](docs/) includes an HTML `<link rel="canonical" href="https://aviperera.com/slug/">` and frontmatter.
2. 100% of SEO indexing signals and backlink equity pass directly through to the canonical domain **`https://aviperera.com`**.
3. All files include complete academic citation blocks formatted for BibTeX.

```mermaid
flowchart LR
    A[aviperera.com] -->|WordPress REST API| B[Archive Sync Engine]
    B -->|Convert HTML to Markdown| C[docs/slug.md]
    C -->|Embed Canonical Tags| D[Search Engines & AI Bots]
    D -->|Pass Backlink Equity| A
```

---

## 📑 Browse the Archive

Explore the full index in [**`docs/index.md`**](docs/index.md), covering:
- 🎯 **Lethal Autonomous Weapons Systems (LAWS)**
- ⚖️ **International Humanitarian Law & Meaningful Human Control**
- 🌐 **Sovereign AI Policies & National Defense Doctrines**
- 🤖 **Combat Humanoids, Loitering Munitions & Quadruped UGVs**

---

## 📄 License & Attribution

Content © [Avi Perera](https://aviperera.com). Licensed under [Creative Commons Attribution 4.0 International (CC BY 4.0)](LICENSE).
Code under MIT License.
