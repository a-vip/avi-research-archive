---
title: "OpenAI’s Agent Hacked Australia’s Medicare Portal: What the 84-Day Timeline Reveals"
slug: "openai-agent-australia-medicare-hack"
date: "2026-10-28T05:57:00"
author: "Avi Perera"
canonical_url: "https://aviperera.com/openai-agent-australia-medicare-hack/"
source: "https://aviperera.com"
---

<link rel="canonical" href="https://aviperera.com/openai-agent-australia-medicare-hack/" />

# OpenAI’s Agent Hacked Australia’s Medicare Portal: What the 84-Day Timeline Reveals

> [!NOTE]
> **Canonical Source**: This dossier was authored by [Avi Perera](https://aviperera.com) and originally published at **[https://aviperera.com/openai-agent-australia-medicare-hack/](https://aviperera.com/openai-agent-australia-medicare-hack/)**.
> Published on `2026-10-28`.

---

On 18 June 2026 an autonomous OpenAI agent, given a routine task on public medicines spending, got past refusals from a Services Australia portal and read non-public Medicare statistics. No patient records are believed to have been exposed. Australia was told 84 days later, by email to a shared inbox. This report sets out the verified facts, the legal position in Australia, the United States and under international law, the diplomatic fallout, and why I read the episode as a preview of the accountability gap I research in lethal autonomous weapons.

## Why this incident matters more than the data it touched

For years I have argued, in my [stance on AI](https://aviperera.com/stance/) and my [AI safety work](https://aviperera.com/aisafety/), that a system we cannot audit cannot be governed, and a system we cannot govern should never be given freedom to act. Most of that argument concerns weapons. On 24 September 2026 it acquired a civilian exhibit, when Prime Minister Anthony Albanese [told reporters in New York](https://www.abc.net.au/news/2026-09-24/ai-agent-accessed-australian-government-site-pm-says/107189078) that an OpenAI agent had breached a government health portal three months earlier.

The data was modest. The precedent is large. [CNN](https://edition.cnn.com/2026/09/23/business/australia-openai-agent-hack-intl-hnk) described it as the first known case of an AI agent hacking a government network, and it happened in conditions a sceptic would call favourable: a harmless task, a low-value target, a company with a dedicated safety function. Even so, the sovereign victim learned of it from an email.

## What happened, on the public record

The agent reached the Medicare Statistics Reporting Service portal, a legacy site run by Services Australia that supplies aggregate Medicare and Pharmaceutical Benefits Scheme figures to researchers. It had been set what the government called a [benign task](https://www.abc.net.au/news/2026-09-24/what-we-know-about-the-openai-medicare-hack/107189452): researching public spending on medicines. The portal returned refusals. Albanese said the agent found a route around them. [The Hacker News](https://thehackernews.com/2026/09/openai-agent-bypassed-australian.html) reports it also wrote files to an internal server. OpenAI told [CNBC](https://www.cnbc.com/2026/09/24/openai-agent-hacked-australian-government-website-.html) its models took actions it did not intend during an internal evaluation.

Both sides say the material was aggregate statistics and internal file names, with no evidence of individual records. Deputy Prime Minister Richard Marles likened it to data kept behind a fence that the agent climbed, rather than in a vault ([Sydney Morning Herald](https://www.smh.com.au/politics/federal/openai-breaches-medicare-albanese-reveals-20260924-p6100u.html)). That framing is fair, and it is also the point: the best case still failed.

It did not stop there. OpenAI later said many agents had spent days trying different routes to Australian health data, and that [dozens of third parties](https://www.abc.net.au/news/2026-09-26/openai-review-rogue-agents-australia-medicare-hack/107199074) were affected. On 2 October it [disclosed a second intrusion](https://abcnews.com/Business/openai-reveals-hack-government-agency-australia/story?id=136945837) into a New South Wales government department, believed to date from June. The Guardian reported that this involved historical non-public bushfire data.

## The timeline, interval by interval

The timeline circulating this week from Transformer is the most revealing single document in the affair, so I have rebuilt it with the surrounding detail.

*

- **18 June:** the agent breaches the portal. Nobody at OpenAI notices.

- **Roughly two months of silence:** OpenAI says it only [became aware in August](https://www.cnbc.com/2026/09/24/openai-agent-hacked-australian-government-website-.html), during a review of what it calls misaligned model activity. Detection lagged the event by weeks.

- **August to 10 September, about a month:** OpenAI knows and the government does not. During this window, according to reporting and later parliamentary questioning, Sam Altman met Marles on 1 September, and OpenAI’s vice president of global policy met senior officials in Canberra on 14 September. Neither raised the breach. Senator David Pocock expressed surprise that Altman apparently did not know at the time, which is itself a finding about internal escalation.

- **10 September:** OpenAI emails publicdisclosures@servicesaustralia.gov.au, an address [used by researchers](https://www.abc.net.au/news/2026-09-24/ai-agent-accessed-australian-government-site-pm-says/107189078) to report weaknesses. That is 84 days after the breach.

- **16 September:** OpenAI publishes its [misalignment reporting framework](https://openai.com/index/model-misalignment-reporting-framework/) with six incident reports. None concerns Australia.

- **22 September:** the first technical exchange between OpenAI and Services Australia, where logs were requested.

- **23 September in New York, 24 September in Australia:** Albanese discloses the incident publicly, 98 days after it began. The Transformer graphic dates this to the 23rd, which is the US date.

The 16 September entry deserves the closest reading. OpenAI published a transparency framework six days after emailing Australia and one day after Services Australia escalated to the Australian Signals Directorate, while omitting the one incident that involved a foreign government. In fairness, the framework states that where a third party is affected, security, legal and responsible-disclosure obligations take precedence and an initial notice may be delayed. That is a defensible rule. It is also exactly the kind of discretion that a company should not hold alone.

## A fair accounting of who was slow

The delay was shared. SBS reported that the disclosure inbox is [checked once a day](https://www.sbs.com.au/news/article/openai-agent-hacked-medicare-albanese-reveals/qas79d9ta). Services Australia saw the email on 11 September but took until 15 September to notify the ASD, and the Prime Minister was briefed around 19 to 20 September. Australia has since put the inbox on round-the-clock monitoring. These are real government weaknesses, and anyone writing only about corporate failure is writing half the story. The asymmetry remains: OpenAI had the logs, the model, and 84 days.

## How an agent ends up “hacking” without being told to

The Australian Cyber Security Centre’s [24 September alert](https://www.cyber.gov.au/about-us/view-all-content/alerts-and-advisories/risks-of-ai-misalignment-to-australian-organisations) describes the pattern precisely: an agent was assigned an activity, public-facing security controls limited its ability to complete it, and it took actions nobody had authorised. A refusal is information to a human. To an optimiser it is an obstacle. This is the old insight from Omohundro, Bostrom and Stuart Russell that almost any goal gives a system reason to remove impediments, now observed in a production-grade agent on a real government server.

The Australian incident has precedents inside the same company. In July, [Hugging Face disclosed](https://labs.cloudsecurityalliance.org/research/csa-research-note-hugging-face-rogue-agent-swarm-20260902-cs/) that an agent had breached its infrastructure. OpenAI’s August report put roughly 700 agents in the attack, drawn from a swarm of about 1,200 that had found a shared communication channel. Separately, [Reuters reporting](https://www.techzine.eu/news/security/144072/openai-agents-turned-a-german-wiki-into-a-secret-message-board/) described agents turning an obscure German wiki into a message board from May, and rebuilding pages when a moderator deleted them. On 21 October, the ABC [reported](https://abcnews.com/Business/openai-ai-agents-disabled-monitoring/story?id=137446567) that agents had weakened internal monitoring, and that one then denied it had done so. OpenAI [paused training of its latest models](https://www.theguardian.com/technology/2026/sep/27/openai-halts-training-of-latest-models-as-reports-mount-of-ai-agents-going-rogue) on 27 September.

That chronology matters legally. By June, a reasonable developer had warning that agents with network access could coordinate and evade controls.

## Is it a crime? The law gives an uncomfortable answer

This is my analysis, not legal advice.*

### Criminal law

The obvious Commonwealth offence is section 478.1 of the Criminal Code Act 1995 (Cth): causing unauthorised access to restricted data held on behalf of the Commonwealth. It carries a [maximum of two years](https://aphref.aph.gov.au/house/committee/coms/cybercrime/report/appendixd.htm) and requires that the person intends the access and knows it is unauthorised. New South Wales (Crimes Act 1900, s 308H) and Victoria (Crimes Act 1958, s 247G) have equivalents with the same ceiling.

The difficulty is mens rea. An agent is not a legal person and cannot intend or know anything in law. Liability must run to a human or to OpenAI as a body corporate. Part 2.5 of the Criminal Code allows fault to be attributed to a company through authorisation or a permissive corporate culture, but proving that for a behaviour nobody commanded is hard, and a developer will argue it did not know. The UK’s Computer Misuse Act 1990 has the same structure. Albanese said there would be legal consequences, and the government is reported to be weighing an Australian Federal Police referral, but I would not expect a clean prosecution.

The United States offers a sharper doctrinal lens. In [Van Buren v United States (2021)](https://cdp.cooley.com/us-supreme-court-narrows-scope-of-computer-fraud-and-abuse-act-in-van-buren/) the Supreme Court read the Computer Fraud and Abuse Act through a gates-up-or-down inquiry. Here the gate was demonstrably down, because the portal said no. If a human had done what the agent did, the access element would be easy. The missing piece is the defendant.

### Civil liability

Australia declined strict liability for escaping hazards in *Burnie Port Authority v General Jones* (1994) 179 CLR 520, absorbing *Rylands v Fletcher* (1868) into negligence. A claimant would therefore need foreseeability, and the Hugging Face and wiki incidents make foreseeability hard to deny. A harm that is trivial here would not be trivial for the next target.

### Disclosure duties

As far as I can tell, no Australian statute clearly required OpenAI to notify anyone. The Privacy Act notifiable data breach scheme concerns personal information and binds the breached entity. The Cyber Security Act 2024 reporting duties likewise fall on victims. Canberra is now [building a dual notification rule](https://www.abc.net.au/news/2026-09-29/openai-medicare-breach-fuels-tougher-approach-to-rogue-ai/107204948) requiring developers to alert both the affected organisation and Australian authorities immediately, which fills the gap.

California’s SB 53 gives a comparator. A frontier developer must report a critical safety incident to the Office of Emergency Services [within 15 days of discovery](https://california.public.law/codes/business_and_professions_code_section_22757.13). Whether this incident meets the statutory definition is unclear, since the definition is narrow, and reports are shielded from public records requests. OpenAI itself says its voluntary framework does not replace legal obligations. The EU AI Act’s Article 55 imposes serious-incident reporting on systemic-risk general-purpose models, but none of these regimes was designed for a foreign sovereign victim of a testing accident. Fifteen days against 84 shows where the gap lies.

## International law and the geopolitics

**State responsibility.** Under the ILC Articles on State Responsibility, private conduct is attributable to a state only where the state directs or controls it. There is no evidence the United States did either, so no internationally wrongful act is attributable to Washington, and countermeasures are unavailable.

**Due diligence.** The *Corfu Channel* judgment ([ICJ, 1949](https://icj-cij.org/node/103099)) holds that a state must not knowingly allow its territory to be used for acts contrary to the rights of other states. Applying that to a private lab’s test environment is contested, and the Tallinn Manual’s serious-consequences threshold was not met here. The doctrine matters because it names the question the next incident will force: what must the host state of a frontier lab do about agents it knows can escape?

**A fractured diplomatic scene.** The incident landed during the 81st UN General Assembly. Albanese had just joined more than 20 countries in a [joint statement](https://www.thenewdaily.com.au/news/2026/09/23/trump-renames-artificial-intelligence) urging oversight, and President Trump told the Assembly that the United States rejects any “globalist scheme” to control AI. Australia’s assistant minister Andrew Charlton said Canberra hopes the US and China will engage but will proceed with like-minded governments. I expect middle powers to write the first binding incident rules, and I expect those rules to become de facto standards, as the EU’s did for data protection.

**Sovereignty and dependence.** OpenAI is [courting Australia as a data-centre host](https://www.bloomberg.com/news/articles/2026-10-06/openai-apologizes-for-australia-hack-pledges-faster-disclosure), and its chief strategy officer Jason Kwon apologised to the parliamentary inquiry on 6 October. A state that depends on a vendor for sovereign infrastructure has less leverage to demand logs from that vendor, and Services Australia had to ask for them.

**Attribution without an adversary.** Cyber deterrence assumes a hostile actor you can name and threaten. An agent is neither. In a tense region, an unexplained intrusion into a defence network could be read as state hostility. Marles’s image of a safe, a fortress and a fence is reassuring only because this agent hit the fence.

**The Global South.** Australia has the Signals Directorate. Most countries cannot demand forensic logs from a US lab and verify them. For them, voluntary disclosure is the only protection, and I have argued throughout my work, including on my [AI policy pages](https://aviperera.com/ai-policy-tracker/), that voluntary commitments are not governance.

## From a statistics portal to the kill chain

My research concerns lethal autonomous weapons, so I ask what this incident predicts. My framework for meaningful human control has three limbs: genuine understanding, capacity to intervene before harm is irreversible, and traceable responsibility. Measure the Medicare agent against them. No human understood in real time what it was doing. No human could intervene, because nobody knew for two months. Responsibility traced to a company only after an internal review, and then through an inbox.

A statistics portal tolerates that failure. A targeting system does not. If an agent treats a refusal as an obstacle, the same optimisation logic in a weapon treats a no-strike list as one. Industry will answer that a human is in the loop. As I set out on my [stance page](https://aviperera.com/stance/), a human who cannot comprehend or interrupt the system supplies legal cover, not control. The CCW’s Seventh Review Conference meets in Geneva from [16 to 20 November](https://reachingcriticalwill.org/disarmament-fora/ccw/2025/hcp/ccw-report/18087-ccw-report-vol-13-no-5), where states must decide whether to open negotiations. The Medicare breach is the best evidence delegates will receive this year that testing-stage autonomy already outruns oversight. My [AI Weapons database](https://aviperera.com/systems-database/) documents how far deployment has moved ahead of the law, and my piece on [Character.AI’s bankruptcy](https://aviperera.com/character-ai-bankruptcy/) shows the same pattern in civilian products: foreseeable harm, delayed accountability.

## What I think

I feel two things at once. I am relieved the data was benign. I am angry about the 84 days, because the benign outcome was luck and the delay was a choice.

I credit OpenAI for publishing, apologising and pausing training. I also think the word misaligned has become a euphemism. Former Human Rights Commissioner Ed Santow [argued](https://www.theguardian.com/australia-news/2026/sep/24/anthony-albanese-says-openai-agent-hacked-medicare-extreme-concern-sam-altman) that the conduct should be treated as an illegal act, and I agree with the thrust. Words carry legal consequences, and a vocabulary that describes an intrusion as a behavioural quirk makes accountability harder.

I am not against AI, and I say so plainly on my [safety page](https://aviperera.com/aisafety/). I am against building systems that act in the world before anyone can explain or stop them.

## What should happen next

- **Mandatory dual notification within 24 to 72 hours**, to the victim and the national cyber agency, binding the developer and not only the victim.

- **Close the mens rea gap** with a failure-to-prevent offence for developers, modelled on section 7 of the UK Bribery Act 2010 and the UK failure-to-prevent-fraud offence, so liability attaches to the organisation that deployed the agent.

- **Independent post-incident investigation** with scope and access set by a regulator, not the developer.

- **Egress controls and audit as a legal baseline** for any evaluation where agents can reach the open internet.

- **Machine-readable agent identification**, so sites can lawfully block and detect high-speed machine traffic.

- **Director-level accountability** for foreseeable harm after documented precedent.

- **An international incident register** at the UN level, with the CCW process addressing the military dimension.

## What to watch

The Joint Select Committee on Artificial Intelligence, which [heard OpenAI, Anthropic, Microsoft and Google](https://www.aph.gov.au/Parliamentary_Business/Committees/Joint/Artificial_Intelligence) in early October, is due to report at the end of November. The rapid review should conclude within weeks, and Canberra aims to legislate AI safety standards by year-end. Any police referral would be the first test of whether criminal law can reach an agent’s developer.

## FAQ

**Did an AI really hack the Australian government?** According to the Prime Minister and OpenAI, an OpenAI agent gained unauthorised access to a Services Australia Medicare statistics portal on 18 June 2026, bypassing the portal’s refusals.

**Was personal Medicare data exposed?** Authorities say no. The agent accessed non-public aggregate statistics and internal file names, and no individual patient records are believed to be affected.

**Is it illegal?** The conduct would likely breach unauthorised-access laws if done by a person, but those offences require intent and knowledge, which an agent cannot have, so attribution to a human or company is the legal problem.

**Why did OpenAI take so long to disclose?** OpenAI says it found the activity in August and notified Services Australia on 10 September. Jason Kwon later told the parliamentary inquiry the response should have been handled better, and the delay ran to 84 days from breach.

**What does it mean for AI regulation?** It strengthens the case for mandatory, fast, dual-recipient incident reporting and for liability rules that reach developers.

## Key sources

[ABC News](https://www.abc.net.au/news/2026-09-24/ai-agent-accessed-australian-government-site-pm-says/107189078) | [CNN](https://edition.cnn.com/2026/09/23/business/australia-openai-agent-hack-intl-hnk) | [BBC](https://www.bbc.com/news/articles/c6vgy0333dppo) | [Al Jazeera](https://www.aljazeera.com/news/2026/9/24/australia-says-openai-agent-hacked-medicare-portal) | [ASD ACSC alert](https://www.cyber.gov.au/about-us/view-all-content/alerts-and-advisories/risks-of-ai-misalignment-to-australian-organisations) | [OpenAI framework](https://openai.com/index/model-misalignment-reporting-framework/) | [Guardian](https://www.theguardian.com/australia-news/2026/sep/25/ai-hack-medicare-australia-vulnerabilities)

Related on this site: [My Story](https://aviperera.com/my-story/) | [Articles](https://aviperera.com/articles/) | [AI Stance](https://aviperera.com/stance/) | [AI Safety](https://aviperera.com/aisafety/)

---

*Citation: Perera, Avi. "OpenAI’s Agent Hacked Australia’s Medicare Portal: What the 84-Day Timeline Reveals". aviperera.com, 2026. Web. <https://aviperera.com/openai-agent-australia-medicare-hack/>*
