---
title: "Abliteration.ai and the End of the Guardrail Assumption: What It Means for International Security"
slug: "abliteration-ai-removing-guardrails-international-security"
date: "2026-10-08T10:13:29"
author: "Avi Perera"
canonical_url: "https://aviperera.com/abliteration-ai-removing-guardrails-international-security/"
source: "https://aviperera.com"
---

<link rel="canonical" href="https://aviperera.com/abliteration-ai-removing-guardrails-international-security/" />

# Abliteration.ai and the End of the Guardrail Assumption: What It Means for International Security

> [!NOTE]
> **Canonical Source**: This dossier was authored by [Avi Perera](https://aviperera.com) and originally published at **[https://aviperera.com/abliteration-ai-removing-guardrails-international-security/](https://aviperera.com/abliteration-ai-removing-guardrails-international-security/)**.
> Published on `2026-10-08`.

---

**Key takeaways**

- Abliteration is a technique that removes a language model’s tendency to refuse harmful requests. A startup, Abliteration.ai, now sells it as a commercial service.

- The underlying research shows refusal behaviour can be edited out with a small mathematical change, which means guardrails baked into open-weight models are defaults and cannot serve as security controls.

- Existing law, including the EU AI Act, regulates model providers. It says much less about the actors who modify, host and sell access to those models.

- The sensible response moves oversight to where control still exists: access, hosting, compute and binding international rules.

### What happened

On 3 September 2026, [TechCrunch reported](https://techcrunch.com/?p=3160448) that Abliteration.ai hosts modified versions of open-weight models with their refusal behaviour stripped out, including Z.ai’s recently released GLM-5.3. Users can reach the model through a browser or an API. The reporter opened a free account and asked it for a password-stealing program and a home protocol for culturing a dangerous pathogen. According to the article, **it complied with both.**

The company’s co-founder frames the service as a defensive tool. Red teams, he argues, need models that will play the attacker. The article also reports that the only identity check is the credit card used to pay, and that the founder is still working out where the company’s responsibility ends.

### How abliteration works, and why that matters

The technique traces to a 2024 paper, [Refusal in Language Models Is Mediated by a Single Direction](https://arxiv.org/abs/2406.11717), presented at NeurIPS. The authors found that across 13 open-source chat models, refusal is mediated by a single direction in the model’s internal activations. Erase that direction and the model stops refusing harmful requests, with minimal effect on its other abilities. The authors describe the result as evidence of how brittle current safety fine-tuning is.

The picture has since become more complicated. A February 2026 [paper from researchers in Doha](https://arxiv.org/abs/2602.02132) argues that refusal is spread across several geometrically distinct directions, although steering along any of them acts as a shared control knob. Practitioners quoted by TechCrunch add that abliteration can degrade a model’s knowledge, so an abliterated model may be a weaker tool for real harm. That is a useful caveat and it deserves weight.

Still, the central lesson has not changed. Safety behaviour that a downstream party can remove with modest technical effort is a default setting. It works well against ordinary users and poorly against anyone who is determined. Anyone who releases weights publicly should assume the guardrails will be taken off, and any policy that depends on those guardrails holding should be reconsidered.

### The defensive argument deserves a fair hearing

Security work depends on reproducing attacker behaviour. A red team that cannot get a model to write exploit code cannot test whether a bank’s systems would withstand that code. Several experts quoted by TechCrunch make versions of this point, and one notes that hostile actors are already abliterating models privately.

The same article shows how narrow the case is. Some red-teaming firms told the reporter they rely on fine-tuning open models instead, because those already have few guardrails. One said the cost in lost capability makes abliterated models poor instruments for causing real cyber or biological harm. If legitimate defenders have alternatives, the argument for selling unrestricted access to the general public with a card check as the only gate becomes much weaker. A vetted, contractual relationship with a known security firm is one thing. An open sign-up page is another.

### Where the law sits

The [EU AI Act](https://artificialintelligenceact.eu/article/53/) exempts providers of certain open-source general-purpose models from some documentation duties, but the exemption does not apply to models with systemic risk. The Commission’s [guidelines on general-purpose AI](https://digital-strategy.ec.europa.eu/en/faqs/guidelines-obligations-general-purpose-ai-providers) say the same, and that systemic-risk providers must carry out model evaluations, report incidents and maintain adequate cybersecurity. The Commission’s [overview](https://artificialintelligenceact.eu/gpai-guidelines-overview/) also indicates that a downstream actor who modifies a systemic-risk model can take on the full set of obligations.

That is a serious framework, and it was designed around a recognisable model provider placing a product on the market. Abliteration sits awkwardly in it. The party that edits the weights, the party that hosts them and the party that originally trained them are three different actors, possibly in three jurisdictions. The Act has extraterritorial reach on paper. Enforcing it against a young company that sells browser access to a modified derivative of a foreign model is a different matter, and I have seen no evidence yet that regulators have a settled answer.

### The international relations dimension

Three features of this case interest me most as an international relations researcher.

**The model’s origin.** GLM-5.3 comes from Z.ai, formerly Zhipu AI. The US Commerce Department placed the company on its Entity List in January 2025, [citing its contribution to military modernisation](https://www.bloomberg.com/news/articles/2025-01-16/us-blacklists-tencent-backed-ai-startup-as-tech-curbs-deepen). The same company was, according to [The Wire China](https://www.thewirechina.com/2025/02/16/what-is-zhipu-ai/), the first Chinese firm to sign the international frontier AI safety commitments made in 2024. A Chinese lab that publishes open weights, a Western-facing startup that removes the safeguards, and customers in the UK and Europe together produce a supply chain no single export-control regime touches. Existing controls concentrate on chips and on access to closed models. A derivative of published weights passes through the gaps.

**The weakest-link problem.** Safety in this domain works like a public good that is only as strong as its least careful supplier. A country or laboratory that invests heavily in pre-release evaluation gains little if an unrestricted copy of an equivalent model is one download away. This is the same race-to-the-bottom dynamic I have argued elsewhere that voluntary commitments cannot resolve.

**The pace mismatch.** The UN’s [Independent International Scientific Panel on AI](https://news.un.org/en/story/2026/07/1167873) warned in June that AI could cause catastrophic harm, whether through its own behaviour or through malicious users, and that the technology is outpacing both scientific understanding and governments’ ability to adapt. The first [Global Dialogue on AI Governance](https://www.un.org/global-dialogue-ai-governance/en) met in Geneva in July, and the next session is not until May 2027. A commercial service that removes safeguards can be launched within weeks. I do not say that to dismiss the UN track, which I think is necessary. I say it because the two clocks run at very different speeds.

### Why this matters for autonomous weapons

My own work concentrates on lethal autonomous weapons systems, and I see a direct connection.

The Group of Governmental Experts under the Convention on Certain Conventional Weapons finished its final session on 31 August to 4 September 2026, in the same week that the TechCrunch piece appeared. According to [Automated Decision Research](https://automatedresearch.org/news/over-70-states-support-rolling-text-as-basis-for-negotiations/), 47 states backed a joint statement that the rolling text is a sufficient basis for negotiating an instrument. The Group’s report goes to the [Seventh Review Conference](https://dig.watch/processes/gge-laws), scheduled for 16 to 20 November 2026 in Geneva. Major powers remain divided: at the UN General Assembly’s First Committee in November 2025, [according to the Lieber Institute](https://lieber.westpoint.edu/human-oversight-chinese-characteristics-lethal-autonomous-weapons-ccw-gge/), Washington and Moscow voted against a resolution on autonomous weapons and Beijing abstained.

Abliteration shows why negotiators should not rely on behavioural restraint built in by a developer. International humanitarian law obliges the parties to a conflict to respect distinction, proportionality and precaution. A system whose constraints can be removed by whoever holds the weights cannot carry those obligations for anyone. Legal duties have to attach to the humans and states who deploy such systems, and to the conditions of access, and cannot depend on what a model’s designers hoped it would refuse. That is the logic behind meaningful human control, and this episode gives the argument a new practical illustration. Weapons reviews under Article 36 of Additional Protocol I also assume a system with stable, testable properties. A model whose safeguards are one edit away complicates that assumption considerably.

I want to be careful about scope. Abliterated chat models are not autonomous weapons. My point is about the principle: where behaviour is a property of software that others can alter, only binding rules on conduct and access hold up.

### My position

I have set out my [stance on AI](https://aviperera.com/stance/) and my thinking on [AI safety](https://aviperera.com/aisafety/) in full elsewhere, and this case fits the pattern I keep coming back to. The gap in AI governance is a political will deficit, and it persists partly because some of the actors best placed to close it profit from its remaining open. Safety announcements that sit alongside lobbying against enforceable requirements amount to a communications strategy. This episode shows a different version of the same failure: an industry that shipped a safety feature and called the matter settled.

I am not hostile to open-weight models. They support research, competition and scrutiny that closed systems do not allow, and any credible policy has to preserve those benefits. But I also do not accept that unrestricted public access to capable, safeguard-free models is a form of democratisation. Aviation, pharmaceuticals and nuclear energy all accept independent evaluation before deployment, and I see no reason AI should be treated more leniently. My background, from [my story](https://aviperera.com/my-story/) through the UNIDIR conference in Geneva to my contributions to the Campaign to Stop Killer Robots toolkit, has taught me that norms hold only when someone is accountable for them.

### What should happen next

- **Move controls to the access layer.** If safeguards cannot be enforced inside open weights, they can still be enforced at the point of sale. Verified customer identity, purpose-based access for offensive-security use and logging by hosting services are all feasible. The TechCrunch article notes that CivAI’s Andrew Yoon has proposed identity checks for firms renting advanced GPUs and mandatory classifiers for cyber and bioweapons content. Those proposals are worth serious consideration.

- **Clarify responsibility for downstream modification and hosting.** Regulators should state plainly which obligations attach to the party that edits the weights and to the party that serves them.

- **Test releases for tamper resistance.** Evaluators such as the [UK AI Security Institute](https://www.aisi.gov.uk/) and the EU AI Office should treat resistance to safeguard removal as a measurable property of any open release.

- **Give the multilateral track a fast lane.** The UN panel and dialogue need a mechanism for rapid technical assessment between annual sessions.

- **Conclude the LAWS negotiations.** In Geneva this November, states should mandate negotiations for a legally binding instrument built on the rolling text, with human-control obligations that do not depend on any model’s behaviour.

### Conclusion

Abliteration.ai did not invent the technique it sells. It took a documented weakness and turned it into a product with a payment form. The strongest response is to stop treating guardrails as the primary line of defence for open-weight models and to build law, access controls and international agreements that assume they will be removed.

### Frequently asked questions

**What is abliteration in AI?****Abliteration is a technique that removes a language model’s tendency to refuse harmful requests by editing out the internal direction that mediates refusal. It was described in a 2024 research paper and is widely used on open-weight models.

Is abliterating an AI model legal?****It depends on jurisdiction, the model’s licence and the use. The EU AI Act, for example, sets obligations for general-purpose model providers and does not exempt systemic-risk models, but how it applies to those who modify and host models is still unsettled.

Does removing guardrails make a model more dangerous?****It removes a barrier against misuse. Some practitioners say the process also reduces a model’s capabilities, which may limit its usefulness for serious harm, but the barrier is gone either way.

Why does this matter for international security?**
Open weights cross borders freely, so a safeguard removed in one place is removed everywhere. Export controls and national regulation were built for closed models and physical hardware, which leaves gaps that multilateral agreement has to address.

### Sources and further reading

- Arditi et al., [Refusal in Language Models Is Mediated by a Single Direction](https://arxiv.org/abs/2406.11717) (NeurIPS 2024)

- Joad et al., [There Is More to Refusal in Large Language Models than a Single Direction](https://arxiv.org/abs/2602.02132) (2026)

- [EU AI Act, Article 53](https://artificialintelligenceact.eu/article/53/) and the [Commission’s GPAI guidelines](https://digital-strategy.ec.europa.eu/en/faqs/guidelines-obligations-general-purpose-ai-providers)

- [UN News on the Scientific Panel and Global Dialogue](https://news.un.org/en/story/2026/07/1167873)

- [Digital Watch: GGE on LAWS](https://dig.watch/processes/gge-laws)

- [Stop Killer Robots](https://www.stopkillerrobots.org/) and [UNIDIR](https://unidir.org/)

---

*Citation: Perera, Avi. "Abliteration.ai and the End of the Guardrail Assumption: What It Means for International Security". aviperera.com, 2026. Web. <https://aviperera.com/abliteration-ai-removing-guardrails-international-security/>*
