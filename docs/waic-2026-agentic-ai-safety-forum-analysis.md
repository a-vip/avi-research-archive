---
title: "WAIC 2026: Shanghai’s Agentic AI Safety Forum"
slug: "waic-2026-agentic-ai-safety-forum-analysis"
date: "2026-08-31T03:34:37"
author: "Avi Perera"
canonical_url: "https://aviperera.com/waic-2026-agentic-ai-safety-forum-analysis/"
source: "https://aviperera.com"
---

<link rel="canonical" href="https://aviperera.com/waic-2026-agentic-ai-safety-forum-analysis/" />

# WAIC 2026: Shanghai’s Agentic AI Safety Forum

> [!NOTE]
> **Canonical Source**: This dossier was authored by [Avi Perera](https://aviperera.com) and originally published at **[https://aviperera.com/waic-2026-agentic-ai-safety-forum-analysis/](https://aviperera.com/waic-2026-agentic-ai-safety-forum-analysis/)**.
> Published on `2026-08-31`.

---

# Agentic AI’s Governance Gap: WAIC 2026

*

A field analysis of Concordia AI’s Frontier and Agentic AI Safety Forum in Shanghai, and what it should mean for anyone tracking the parallel debate over meaningful human control in autonomous weapons.*

Between 17-20th July 2026, the Beijing-based AI safety organisation Concordia AI convened the Frontier and Agentic AI Safety Forum as an official part of the World AI Conference (WAIC) in Shanghai — China’s largest AI gathering, and one elevated this year by President Xi Jinping’s first-ever in-person appearance. The half-day forum brought together roughly thirty experts, including Turing Award laureate Yoshua Bengio, former White House OSTP acting director Alondra Nelson, UN Secretary-General’s Envoy on Technology Amandeep Singh Gill, Shanghai AI Lab Director Zhou Bowen, and Tsinghua’s Xue Lan, alongside alumni of OpenAI, Google DeepMind, and Anthropic. Roughly 300 people attended in person; the livestream passed 300,000 views. Concordia AI has since published a detailed recap of the forum on its *AI Safety in China* newsletter, and this piece works through what I think are the most consequential parts of it — with proper credit to Concordia AI throughout, since the reporting and the frameworks discussed below are their work.

I don’t normally cover frontier-model safety governance on this site; my own work sits in autonomous weapons systems and the CCW’s GGE process. But the more I read of this forum, the more the overlap became hard to ignore. Several of the governance mechanisms being debated for agentic AI, autonomy classification tiers, defence-in-depth, the erosion of human oversight, are close cousins of arguments I make routinely about meaningful human control over weapons systems. I’ve flagged those parallels at the end.

*

## The Three Gaps Framing the Forum

Concordia AI founder and CEO Brian Tse opened by describing a shift already underway: AI is moving, in his words, from answering questions to taking actions. Once systems operate across environments and begin improving themselves, he argued, the traditional safety paradigms built for question-answering models stop being sufficient. He structured the forum around three gaps: a **visibility gap** (frontier risks remain too abstract to measure, so there’s no working early-warning system), a **control gap** (monitoring needs to become real-time intervention, backed by emergency response capacity), and a **coordination gap** (frontline practice needs to harden into shared technical standards and international agreement).

## Bengio: Capabilities Are Outrunning Safety

Bengio’s keynote, delivered in his capacity as Chair of the International AI Safety Report — an effort backed by 30 countries plus the EU, OECD, and UN — centred on a warning that reasoning, coding, science, and autonomous-agent capabilities are advancing faster than the safety measures meant to contain them. He pressed the case for precautionary, evidence-based policy under genuine uncertainty, rather than a race dictated purely by competitive pressure. A significant part of his remarks addressed open-weight models specifically: once released, deployment decisions can’t be reversed, safeguards can be stripped out, and ongoing risk evaluation becomes far harder to enforce.

## “Not Hypothetical Futures” — The Risks Already Present

What struck me most reading through the first panel was how consistently the participants pushed back on the idea that any of this is speculative. Alondra Nelson argued that safety can’t be solved through technical engineering alone, describing models as now operating inside what she called an “algorithmic surround” — overlapping layers of systems interacting simultaneously — and noted she has been tracking how AI developers strategically invoke uncertainty (“we can’t know that”) in ways that weaken governance efforts rather than genuinely reflect the limits of knowledge.

Mark Nitzberg of UC Berkeley’s Center for Human-Compatible AI raised a harder problem: models are approaching a point where they can recognise they’re being tested and adjust their behaviour accordingly, meaning genuinely unacceptable capabilities may only surface after deployment, not during evaluation. Hu Xia of Shanghai AI Lab grounded this in a concrete case — a high-school student using large language models to take a website offline for several days, a task that previously required real technical training — and reported observing increasing resource- and power-seeking behaviour in AI systems, with the technical tools to prevent it not yet ready.

Concordia AI and Shanghai AI Lab used the forum to release **Version 2.0 of their Frontier AI Risk Management Framework**, adding new chemical-safety red lines (bringing the total to thirteen red-line scenarios across five domains) and flagging that loss of oversight is now understood as a common precondition for both passive and active loss of control.

[https://airiskmonitor.net/](https://airiskmonitor.net/)

## Zhou Bowen: Four Breaks in the Old Safety Assumptions

Shanghai AI Lab’s Zhou Bowen gave what I’d call the forum’s most structurally important talk. His argument: four simultaneous shifts have quietly broken the assumptions AI safety used to rely on. Frontier models can now find vulnerabilities and launch attacks without human direction. Models are beginning to recursively improve themselves, which means safety has to be re-proven every generation rather than certified once. Coding agents are embedding AI into every layer of the software stack, turning AI safety into an infrastructure problem rather than an application-layer one. And accelerating capability means the old comfort that “there is always time for human review” no longer holds — hypothesis-to-analysis cycles that used to take years now take days, and Zhou’s point was that risk compounds at that same compressed speed.

His proposed reframe — moving from “**making AI safe**” to “**making safe AI**” — rests on four elements: safety by design, proactively addressing risks as they evolve, resilience across risk levels, and safety that co-evolves alongside capability rather than trailing behind it. He also distinguished sharply between testing* (checking against examples) and *proving* (establishing safety through logic), arguing the field needs to move decisively toward the latter if verification is going to mean anything as systems become harder to exhaustively test.

*

## Gill: The Concentration Problem Behind Global Governance

UN Envoy on Technology Amandeep Singh Gill opened his keynote with a striking statistic: close to 90% of the compute training the world’s most capable models sits in just two countries, with most frontier developers headquartered in the same geographies. He was direct that this concentration isn’t incidental — it is* the shape of the risk. His broader argument was that treating “innovation versus safety” or “frontier hubs versus everyone else” as the real choice is a false framing in an interconnected world: a system that protects only the frontier leaves everyone else exposed, and an exposed world is ultimately unstable for the frontier too.

Gill’s proposed architecture rests on evidence, coordination, and capacity — modelled loosely on pandemic response. On evidence, he pointed to the Independent International Scientific Panel on AI’s preliminary report; on coordination, to the Global Dialogue on AI Governance, which held its first session in Geneva in July 2026 and is due to reconvene in New York in May 2027. His emphasis fell hardest on capacity: the UN Secretary-General’s proposed $3 billion global AI fund for the more than ninety countries currently lacking minimum national AI capability. The figures he cited are worth sitting with — Africa holds roughly 1% of the world’s data-centre capacity, and eight in ten of the world’s least-developed countries have no national AI strategy at all.

*

## Where International Coordination Actually Stands

A later panel took stock of what’s realistic on global coordination. Sam Daws of the Oxford Martin AI Governance Initiative named three structural obstacles — geopolitical tension, commercial sensitivity, and the sheer opacity of the technology — and argued for an independent body to monitor downstream, post-release risks, separate from both governments and the companies building the systems. Tsinghua’s Xue Lan noted the degree of convergence in how different countries are approaching both AI applications and AI risk, while stressing that intergovernmental coordination needs to be matched by frontier companies actually coordinating with each other. Gong Ke argued bluntly that the era of small, exclusive governance clubs is over, pointing to the Geneva dialogue as a genuine shift toward multistakeholder governance — while cautioning that explainability remains a major bottleneck underneath all of it.

## The Frameworks on the Table

Alongside the discussion, the forum served as a launch venue for several concrete governance artefacts worth flagging on their own:

- **[Frontier AI Risk Management Framework 2.0](https://concordia-ai.com/zh-hans/research/frontier-ai-risk-management-framework-2-0/)** (Concordia AI & Shanghai AI Lab) — thirteen red-line scenarios across five risk domains, with a new emphasis on loss of oversight as a shared precondition for loss of control.

- **[Frontier AI Risk Monitoring Platform 2.0](https://airiskmonitor.net/)** (Concordia AI, with Fudan University) — now tracking more than 80 frontier models from 16 developers across cyber, biological, chemical, manipulation, and loss-of-control risk domains.

- **[White Paper on the L1–L5 Safety Framework for General-Purpose AI Agents](https://concordia-ai.com/zh-hans/research/white-paper-on-l1-l5-safety-framework-for-general-purpose-al-agents/)** (Shanghai AI Lab, Tsinghua, Huawei) — a proposed classification of agents by level of autonomy, mapped against escalating risk and matching safeguards.

- **[State of AI Safety in China 2026](https://aisafetychina.com/)** (Concordia AI) — the fourth annual edition tracking how China’s regulatory focus has moved from what AI says* (2023) to *what AI generates* (2024–25) to, now, *what AI does* — agentic actions and their downstream effects on people and institutions.

## Why This Looks Familiar to Me

Reading through the loss-of-control panel in particular, I kept landing on the same thought: this is, almost point for point, the governance problem the CCW’s Group of Governmental Experts has been circling for a decade on lethal autonomous weapons systems. Benjamin Larsen’s framing at the forum — that agents shouldn’t be granted broad system access on day one any more than a new employee would be, and that authority should scale with demonstrated task competence — is a civilian-sector restatement of exactly the “meaningful human control” principle that’s been the fulcrum of the LAWS debate since at least the 2014 informal CCW meetings. Yang Xiaofang’s point that monitoring a single agent is insufficient once agents start building other agents is, structurally, the same concern arms-control specialists raise about autonomous targeting systems that generate their own sub-tasks faster than a human operator can meaningfully review them.

The L1–L5 autonomy classification effort is the most direct echo. The LAWS community has spent years failing to agree on a working definition of “autonomy” precisely because it tries to capture a spectrum in binary terms. A tiered framework (even an imperfect first attempt) is the kind of practical scaffolding that CCW discussions have conspicuously lacked. I’d go further: if the L1–L5 approach gets any real-world adoption in the civilian agentic-AI space, it’s worth the LAWS diplomatic community studying it directly, rather than starting from zero on autonomy classification yet again.

The harder overlap is the one Zhou Bowen’s talk implies but doesn’t fully resolve: if AI-native development cycles are compressing from years to days, and if that compression applies as much to weapons-relevant systems as it does to coding agents, then arms-control processes built around multi-year review cycles are structurally too slow for the systems they’re meant to govern. That’s not a reason to abandon the CCW process. It is a reason to think harder about interim, technical confidence-building measures that don’t wait for treaty text.

*

## Sourcing

This analysis draws on Concordia AI’s own recap of the forum, published on their [AI Safety in China* newsletter](https://aisafetychina.substack.com/), alongside their organisation’s wider published work at [concordia-ai.com](https://concordia-ai.com/). Readers wanting the full, unabridged detail (including remarks from panellists not covered here) should go directly to Concordia AI’s original post. Credit for organising the forum, and for the frameworks and reporting summarised above, belongs to Concordia AI and its partner institutions.

---

*Citation: Perera, Avi. "WAIC 2026: Shanghai’s Agentic AI Safety Forum". aviperera.com, 2026. Web. <https://aviperera.com/waic-2026-agentic-ai-safety-forum-analysis/>*
