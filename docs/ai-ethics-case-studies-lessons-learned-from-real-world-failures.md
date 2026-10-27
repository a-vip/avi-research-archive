---
title: "AI Ethics Case Studies: Lessons Learned from Real-World Failures"
slug: "ai-ethics-case-studies-lessons-learned-from-real-world-failures"
date: "2024-10-30T03:27:31"
author: "Avi Perera"
canonical_url: "https://aviperera.com/ai-ethics-case-studies-lessons-learned-from-real-world-failures/"
source: "https://aviperera.com"
---

<link rel="canonical" href="https://aviperera.com/ai-ethics-case-studies-lessons-learned-from-real-world-failures/" />

# AI Ethics Case Studies: Lessons Learned from Real-World Failures

> [!NOTE]
> **Canonical Source**: This dossier was authored by [Avi Perera](https://aviperera.com) and originally published at **[https://aviperera.com/ai-ethics-case-studies-lessons-learned-from-real-world-failures/](https://aviperera.com/ai-ethics-case-studies-lessons-learned-from-real-world-failures/)**.
> Published on `2024-10-30`.

---

In March 2016, Microsoft’s chatbot Tay lasted less than a day on Twitter before it was pulled offline for posting abusive content. At the time it read as an embarrassing experiment. Eight years later, a Canadian tribunal ordered Air Canada to stand behind what its chatbot had told a grieving customer, and rejected the airline’s argument that the bot was responsible for itself. Between those two events, the cost of an AI failure moved from reputation to liability.

That shift is the thread running through this article. I revisit five well-documented failures (Tay, Amazon’s recruiting tool, Air Canada’s chatbot, Rite Aid’s facial recognition programme and the Arup deepfake fraud), set each against the law as it stands in October 2026, and draw out what product teams, lawyers and policymakers should do differently. I also add a shorter sixth case, Amazon Rekognition, because it shows how a vendor default becomes a public-interest problem.

The numbers support the urgency. The [Stanford AI Index 2026](https://hai.stanford.edu/ai-index) reports 362 documented AI incidents in 2025, up from 233 in 2024, drawing on the [AI Incident Database](https://incidentdatabase.ai/). That database is curated by hand and skews towards high-profile incidents, so I treat the figure as a direction of travel rather than an exact count.

## Key takeaways

- Companies are being held to what their AI systems say and do. Moffatt v. Air Canada and the FTC’s Rite Aid order are the clearest examples, though neither is binding on every court.

- The EU’s high-risk AI obligations no longer apply in August 2026. The AI Omnibus moved them to 2 December 2027 (stand-alone systems) and 2 August 2028 (AI embedded in regulated products).

- The new EU Product Liability Directive treats software as a product, but it only applies to products placed on the market after 9 December 2026.

- US Executive Order 14110 was revoked in January 2025. Accountability in the United States now runs through the FTC, anti-discrimination law and private litigation.

- A video call is no longer proof of identity. High-value payments need out-of-band verification and dual authorisation.

## Legal Framework for AI Ethics (Updated for 2026)

The era of voluntary codes is over, but the picture is less tidy than a simple move from proposal to enforcement. Some instruments are binding and in force, some are binding and waiting for ratifications, and some deadlines have moved. The table below is a status snapshot as of 26 October 2026. The sections that follow explain what each item means in practice.

InstrumentStatus as of October 2026Why it mattersCouncil of Europe Framework Convention on AIOpened for signature September 2024. EU ratified 15 May 2026. Not yet in force.First binding international AI treaty. Requires remedies for rights violations. Excludes national defence.UN Global Digital Compact and A/RES/79/325Compact adopted September 2024. Scientific Panel and Global Dialogue created August 2025. First Dialogue held July 2026.Universal political and scientific forum on AI governance. Not binding.EU AI Act (Regulation 2024/1689), as amended by Regulation 2026/1744Prohibitions apply since February 2025. High-risk duties delayed to December 2027 and August 2028.Sets the global compliance reference point for employment, credit, biometrics and more.EU Product Liability Directive (2024/2853)Transposition deadline and start date 9 December 2026, for products placed on the market after that date.Software and AI become products under strict liability.UK Data (Use and Access) Act 2025 and Online Safety Act 2023Deepfake creation offence in force since 6 February 2026. Ofcom fines of up to 10% of qualifying worldwide revenue.Criminal and regulatory exposure for intimate deepfakes and platform failures.US federal positionExecutive Order 14110 revoked 20 January 2025. No comprehensive federal AI statute that I am aware of.Enforcement runs through the FTC, discrimination law and private suits.

#### International Instruments

*

The [Council of Europe Framework Convention on Artificial Intelligence](https://www.coe.int/en/web/artificial-intelligence/the-framework-convention-on-artificial-intelligence) was opened for signature on 5 September 2024. It concentrates on human rights, democracy and the rule of law rather than market safety, and it obliges parties to provide effective remedies for victims of rights violations linked to AI. The European Union [ratified it on 15 May 2026](https://www.coe.int/web/artificial-intelligence/-/european-union-ratifies-the-council-of-europe-framework-convention-on-artificial-intelligence), but as of early October 2026 it had not entered into force: that needs five ratifications, including three by Council of Europe member states, followed by a three-month waiting period. Like the EU AI Act, it excludes national defence. That carve-out is central to my own work on autonomous weapons, and I discuss it further on my [AI safety page](https://www.claudeusercontent.com/aisafety/).

At the United Nations, the Global Digital Compact was [adopted in September 2024](https://www.un.org/global-digital-compact/en/ai) as part of the Pact for the Future. Resolution [A/RES/79/325](https://www.un.org/pga/wp-content/uploads/sites/110/2025/12/A_RES_79_325-EN.pdf), adopted on 26 August 2025, then created the Independent International Scientific Panel on AI and the Global Dialogue on AI Governance. According to the [UN’s own Dialogue page](https://www.un.org/global-dialogue-ai-governance/en/faq), the Panel’s preliminary report was launched on 1 July 2026 and presented at the Dialogue’s first session. These bodies shape norms and evidence. They do not create enforceable duties.

### European Union

The [AI Act (Regulation (EU) 2024/1689)](https://eur-lex.europa.eu/eli/reg/2024/1689/oj) has banned certain practices, including social scoring and emotion recognition in workplaces and schools, since February 2025. The timetable for high-risk systems has since changed. [Regulation (EU) 2026/1744](https://eur-lex.europa.eu/eli/reg/2026/1744/oj), known as the AI Omnibus, was published on 24 July 2026 and entered into force on 27 July 2026. It moves the application date for stand-alone high-risk systems under Annex III, which cover AI used in employment, education, credit and law enforcement, [from 2 August 2026 to 2 December 2027](https://www.mondaq.com/uk/new-technology/1825722/eu-digital-omnibus-on-ai-enters-into-force), and moves AI embedded in regulated products to 2 August 2028. It also adds two new prohibited practices: systems designed to generate non-consensual intimate imagery and child sexual abuse material. Obligations for general-purpose AI models were not postponed, and breaches of high-risk requirements will still carry fines of up to 15 million euros or 3 percent of worldwide turnover once the dates arrive. Any source that still gives August 2026 as the high-risk deadline is out of date, including earlier versions of this article.

On liability, [Directive (EU) 2024/2853](https://eur-lex.europa.eu/eli/dir/2024/2853/oj) replaces the 1985 Product Liability Directive and expressly treats software, including AI systems, as a product. Member states must transpose it by 9 December 2026, and it applies to products placed on the market after that date, so claims about older products stay under the old regime. Liability remains strict, which means the claimant does not have to prove fault. The claimant must still show a defect, damage and a causal link, although the Directive introduces presumptions of defectiveness, for example where a defendant fails to disclose relevant evidence. The separate AI Liability Directive proposal was largely sidelined in favour of this route.

### United Kingdom

The [Data (Use and Access) Act 2025](https://www.legislation.gov.uk/ukpga/2025/18/contents) received Royal Assent in June 2025. Its section 138, in force since 6 February 2026, makes it a criminal offence to create or request the creation of an intimate deepfake image without consent. Under the [Online Safety Act 2023](https://www.legislation.gov.uk/ukpga/2023/50/contents), Ofcom can fine services up to 18 million pounds or 10 percent of qualifying worldwide revenue, whichever is greater, and in January 2026 it opened a formal investigation into X over Grok-generated intimate imagery. The investigation shows regulators now treat an AI tool that generates content differently from a platform that merely hosts it.

### United States

Executive Order 14110 on safe, secure and trustworthy AI was [revoked on 20 January 2025](https://www.govinfo.gov/content/pkg/FR-2025-01-28/html/2025-01901.htm) by Executive Order 14148. An earlier version of this article treated it as the foundation of federal AI enforcement, which was wrong even before its revocation: the FTC acts under Section 5 of the FTC Act, not under the order. With no comprehensive federal AI statute that I am aware of, accountability comes through three channels: the FTC’s power over unfair and deceptive practices, existing anti-discrimination law, and private litigation. In [Mobley v. Workday*](https://www.proskauer.com/blog/ai-bias-lawsuit-against-workday-reaches-next-stage-as-court-grants-conditional-certification-of-adea-claim), for instance, a federal court granted preliminary certification in May 2025 of an age-discrimination collective action against an AI hiring vendor, on the theory that the vendor acted as an agent of employers.

## Case Study 1: Microsoft’s Tay Chatbot (2016)

*

Microsoft launched Tay on Twitter in March 2016 as an experiment in conversational understanding, aimed at 18-to 24-year-olds in the United States. The bot learned from the people who talked to it, and that was the flaw. [Microsoft’s own post-mortem](https://blogs.microsoft.com/blog/2016/03/25/learning-tays-introduction/) says that within the first 24 hours a coordinated group of users exploited a vulnerability, and that the company had prepared for many kinds of abuse but made a critical oversight for this specific attack. **Tay went from friendly greetings to racist, misogynistic and extremist posts**, Microsoft took it offline and apologised, and a short relaunch days later also failed.

Tay is the textbook case of **data poisoning** and of **naive online learning**. A system that treats unfiltered public input as training signal hands control of its behaviour to the most motivated users. It also shows why the phrase **“coordinated attack”** is not a defence. If adversarial users are foreseeable, and on a public social platform they always are, then adversarial testing is part of the design duty, not a post-hoc excuse.

The legal position has moved since 2016. Intermediary immunities such as **Section 230** in the United States were designed for hosting other people’s speech, and whether they cover content a company’s own model generates is contested. The EU Digital Services Act requires very large platforms to assess systemic risks from illegal content, and the Online Safety Act’s duties reach some generative AI services. A bot that produces unlawful content on its own account is a much harder case for the operator than a platform hosting a user’s post. My original draft linked Tay to the Equality Act 2010, which I now think was a stretch: Tay was a US experiment, and the more useful comparison is how today’s regulators would treat a model that generates harassment or hate speech.

## Case Study 2: Amazon’s Biased Recruitment AI (2018)

Reuters reported in [October 2018](https://www.reuters.com/article/us-amazon-com-jobs-automation-insight/amazon-scraps-secret-ai-recruiting-tool-that-showed-bias-against-women-idUSKCN1MK08G) that Amazon’s machine-learning team had been building a recruiting engine since 2014 that scored candidates from one to five stars. The models were trained on ten years of CVs submitted to the company, a pool dominated by men, so the system learned to prefer male candidates. It penalised CVs containing the word “women’s”, as in a women’s chess club captain, and downgraded graduates of two all-women’s colleges. Reuters’ sources said engineers edited the system to neutralise those specific terms but could not be sure other forms of discrimination would not emerge, and the effort was ultimately abandoned. Amazon’s position was that the tool was never used by recruiters to evaluate candidates, while Reuters’ sources said recruiters looked at its recommendations without relying on them alone.

The lesson is historical bias encoding. If past decisions reflect a prejudiced reality, a model trained on them will reproduce that prejudice at scale, and removing the obvious proxy words does not remove the pattern, because the model can find new proxies. This is why the fix is testing outcomes across groups, not scrubbing a list of terms.

The legal doctrine that matters here is disparate impact: a neutral practice can be unlawful if it disproportionately disadvantages a protected group and cannot be justified. In the United States it comes from [Griggs v. Duke Power Co.* (1971)](https://supreme.justia.com/cases/federal/us/401/424/) and operates through Title VII of the Civil Rights Act. In Great Britain the equivalent is indirect discrimination under [section 19 of the Equality Act 2010](https://www.legislation.gov.uk/ukpga/2010/15/section/19), and employers’ duties toward applicants sit in [section 39](https://www.legislation.gov.uk/ukpga/2010/15/section/39). The vendor question is now live in court: *Mobley v. Workday*, discussed above, tests whether a software provider can be liable as an employer’s agent. In the EU, recruitment AI is a high-risk use under Annex III of the AI Act, with obligations now due from 2 December 2027.

## Case Study 3: Air Canada’s “Lying” Chatbot (2024)

*

After his grandmother died in November 2022, Jake Moffatt booked a flight with Air Canada and asked its website chatbot about bereavement fares. The chatbot told him he could book at the full price and apply for the reduced fare afterwards, within 90 days. That contradicted the airline’s actual policy, which sat on a linked page and did not allow retroactive claims. Air Canada refused the refund, and the dispute went to British Columbia’s Civil Resolution Tribunal.

In [Moffatt v. Air Canada*, 2024 BCCRT 149](https://decisions.civilresolutionbc.ca/crt/crtd/en/525448/1/document.do), decided on 14 February 2024, the tribunal found **negligent misrepresentation**. It held that Air Canada owed a duty of care, had not taken reasonable care to ensure the chatbot was accurate, and could not treat the chatbot as a separate legal entity responsible for its own actions: the chatbot was part of the airline’s website. It also rejected the idea that a customer should cross-check the chatbot against another page. Damages were C$650.88, the difference between the fare paid and the bereavement fare, plus interest and fees. The [American Bar Association](https://www.americanbar.org/groups/business_law/resources/business-law-today/2024-february/bc-tribunal-confirms-companies-remain-liable-information-provided-ai-chatbot/) and Canadian law firms have treated the reasoning as a useful signal for chatbot operators.

I want to be precise about its weight. This is a small-claims tribunal decision, so it is persuasive rather than binding, and commentators have noted that the tribunal said little about why the airline’s conduct was negligent because Air Canada offered it almost no information about how the chatbot worked. The money was trivial. The principle is not:** a company that puts an AI system in front of customers should expect to answer for what it says**, and linking to the real policy does not cure a wrong summary. Practically, that means constraining a customer-facing model to verified sources, logging what it says, and designing a path to a human with authority to correct it.

## Case Study 4: Rite Aid’s Biometric Ban (2024)

*

Between 2012 and 2020, Rite Aid used facial recognition in hundreds of stores to flag people it suspected of shoplifting. In December 2023 the [Federal Trade Commission announced](https://www.ftc.gov/news-events/news/press-releases/2023/12/rite-aid-banned-using-ai-facial-recognition-after-ftc-says-retailer-deployed-technology-without) a federal court complaint and a [proposed stipulated order](https://www.ftc.gov/system/files/ftc_gov/pdf/2023190_riteaid_stipulated_order_filed.pdf) alleging that the system generated thousands of false matches and that Rite Aid had **not taken reasonable steps to prevent harm**. The FTC said the company did not test or inquire about accuracy before deployment, did not prevent low-quality images from being used, did not adequately train staff who acted on match alerts, and did not track false positives afterwards. It also alleged the **harm fell disproportionately on people of colour and women**. Rite Aid, which was in Chapter 11 bankruptcy at the time, said it disagreed with the allegations and described the programme as a pilot in a limited number of stores.

The remedy is what made the case notable. Rite Aid was barred from using facial recognition for surveillance for five years and ordered to delete the images it had collected and any algorithms developed from them. Lawyers at [Mintz](https://www.mintz.com/insights-center/viewpoints/54731/2024-01-23-algorithmic-disgorgement-increasingly-important-part) describe it as the FTC’s first use of its Section 5 unfairness authority against an allegedly discriminatory use of AI. It was not the first use of model deletion, though. The FTC began using what is called algorithmic disgorgement with Cambridge Analytica in 2019 and applied it again in Everalbum, WW International and Kurbo, and Edmodo. I corrected this point because my earlier version said Rite Aid introduced the remedy, and it did not.

Two further corrections. First, an FTC order binds the company that signs it. It is not common law and it does not create precedent in the way a court judgment does, although it signals what the agency considers unreasonable. Second, the EU treatment of this kind of system is more nuanced than “banned”. The AI Act prohibits certain real-time remote biometric identification in publicly accessible spaces for law enforcement, with exceptions, while remote biometric identification more generally is a high-risk use, and biometric data also engages **GDPR Article 9**. A private retailer in the EU would be looking at high-risk obligations and data protection law rather than an outright Article 5 ban.

## Case Study 5: The Hong Kong Deepfake CFO (2024)

In January 2024, a finance employee in the Hong Kong office of the engineering firm Arup received what looked like a message from the company’s UK chief financial officer asking for a confidential transaction. He suspected phishing. He then joined a video call in which the CFO and other colleagues appeared and spoke, and every participant other than him was a deepfake. His doubts were put aside, and he made **15 transfers totalling HK$200 million, about US$25.6 million**. Arup notified Hong Kong police that month and confirmed the incident in [May 2024](https://edition.cnn.com/2024/05/16/tech/arup-deepfake-scam-loss-hong-kong-intl-hnk), saying its financial stability and operations were unaffected and that no internal systems were compromised.

An earlier version of this article said the employee requested the video call as a precaution. The public reporting does not support that. What it does support is a more uncomfortable point: the video call was the thing that overcame a correct suspicion. Seeing and hearing familiar colleagues is no longer evidence of identity, and any control that relies on it is broken.

I would not go as far as my earlier claim that human-in-the-loop oversight is obsolete. The failure here was weak, in-band verification: the employee checked the request through the same channel the attacker controlled. The remedy is out-of-band verification (calling back on a number you already hold), dual authorisation for large or unusual payments, transaction limits, and a rule that urgency and secrecy are triggers for more checking, not less. Hardware-bound approvals such as FIDO2 security keys can protect who is authorising a payment. Content provenance standards such as [C2PA](https://c2pa.org/specifications/) help establish where recorded media came from, but they do not authenticate a live call. On the legal side, whether crime or cyber insurance responds to a deepfake-enabled transfer depends on the policy wording, and it is a question to put to your broker before an incident, not after.

## Beyond the Five: Amazon Rekognition

A sixth case deserves a short place here because it is one of the most searched examples of facial recognition bias. In July 2018 the ACLU [reported](https://www.aclu.org/press-releases/amazon-facial-surveillance-technology-falsely-identifies-28-members-congress-mugshots) that Amazon’s Rekognition service falsely matched 28 members of Congress to a database of 25,000 arrest photos, using the service’s default settings, with people of colour disproportionately affected. Amazon disputed the test, arguing that a higher confidence threshold should have been used for law enforcement. That argument is itself the lesson: when a vendor’s default setting is not suitable for a high-stakes use, the burden falls on whoever configures it, and customers rarely know that. In June 2020 Amazon announced a [one-year moratorium](https://techcrunch.com/2020/06/10/amazon-rekognition-moratorium) on police use of the service. The US National Institute of Standards and Technology reported in 2019 that Amazon had not submitted its algorithm to its demographic testing programme.

## What Successful Bias Mitigation Looks Like

Readers often ask for success stories, and I think the honest answer is that the public record is thinner than vendor marketing suggests. The strongest independent evidence comes from testing, not from claims. NIST’s [demographic effects study (NISTIR 8280)](https://nvlpubs.nist.gov/nistpubs/ir/2019/nist.ir.8280.pdf) evaluated 189 algorithms from 99 developers and found that false positive rates often varied by factors of 10 to over 100 between demographic groups, but also that algorithms differ markedly, and some showed no dramatic differential. That finding is the practical basis for mitigation: the choice of system, and measuring it on the population you will actually serve, changes outcomes.

The most concrete checklist of what reasonable mitigation involves is, ironically, the list of failures in the Rite Aid complaint: test accuracy before deployment, ask vendors for evidence, control image quality, train the humans who act on alerts, and monitor false positives afterwards. In the cases in this article, the closest thing to a successful mitigation was Amazon’s decision to abandon a recruiting tool when it could not guarantee fairness. That is a legitimate outcome, and one that governance processes should make easier, not harder.

## Lessons Learned and Best Practice (Updated for 2026)

### 1. Test adversarially and test by group

Tay shows why red-teaming has to include hostile users, and Rite Aid and Rekognition show why accuracy must be measured per demographic group on realistic data. Run ethical impact assessments before launch and keep them current as the system changes. Test customer-facing language models for invented policy, the failure at the centre of the Air Canada case.

### 2. Know your data and be ready to lose your model

Document where training data came from, under what consent and with what limits. Algorithmic disgorgement means a regulator can order deletion of models built on data that should not have been collected, so if you cannot separate tainted data from clean data you may have to give up the whole model. Commission independent audits focused on disparate impact for any system that affects employment, credit, housing or access to services.

### 3. Assign accountability to named people

Treat your system’s outputs as statements the company has made. Give model risk a named owner, set up review by people with technical, legal and domain expertise, and write indemnities and transparency requirements (model cards, audit reports) into vendor contracts. The Workday* litigation is a reminder that vendors and customers both end up in the dock.

### 4. Verify identity outside the channel that is under attack

Use call-backs on known numbers, dual authorisation, payment limits and cooling-off periods for urgent or secret requests. Treat any request that arrives with unusual pressure as a prompt to verify, not a reason to hurry.

### 5. Monitor after launch and keep a way to stop

Measure fairness and safety in production, not just in the lab. Define in advance who can pause, roll back or override a model that starts causing harm, and give users a route to challenge an automated decision and reach a human who can change it. The [NIST AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework) and ISO/IEC TR 24368 offer structures for doing this.

### Quick checklist for product teams

- Run an ethical impact assessment and an adversarial red-team exercise before launch.

- Test accuracy and error rates for each demographic group you will serve.

- Create a model card and a datasheet, and attach both to procurement documents.

- Constrain customer-facing models to verified sources and prevent them from making financial or policy commitments.

- Confirm whether your insurance covers software and AI claims under the new EU Product Liability Directive for products placed on the EU market after 9 December 2026.

- Require out-of-band verification and dual approval for high-value payments.

- Define and rehearse a kill-switch and rollback procedure.

- Commission an independent audit at least annually for high-impact systems.

**Selected further reading & sources:** *IEEE 7010; ACM Code of Ethics; Alan Turing Institute “Understanding AI Ethics and Safety” (2019); ISO/IEC TR 24368:2022; EU AI Act post-market provisions; * *OSTP Blueprint for an AI Bill of Rights; **[C2PA Technical Standard](https://c2pa.org/specifications/specifications/1.3/explainer/Explainer.html)**.*

## Frequently Asked Questions

### Are companies legally liable for what their AI chatbots say?

In some circumstances, yes. In Moffatt v. Air Canada (2024 BCCRT 149), a British Columbia tribunal held the airline liable for negligent misrepresentation by its chatbot and rejected the argument that the bot was a separate entity. It is a small-claims decision, so persuasive rather than binding, but the reasoning is consistent with general principles of misrepresentation.

### When do the EU AI Act’s high-risk rules apply?

Following the AI Omnibus (Regulation (EU) 2026/1744), stand-alone high-risk systems under Annex III apply from 2 December 2027, and high-risk AI embedded in regulated products from 2 August 2028. Prohibited practices have applied since February 2025, and general-purpose AI model obligations were not postponed.

### What is algorithmic disgorgement?

It is a remedy that requires a company to delete not only improperly obtained data but also the models or algorithms built from it. The US FTC first used it against Cambridge Analytica in 2019 and again in the Everalbum, WW International and Kurbo, Edmodo and Rite Aid matters.

### Is the Council of Europe AI Convention in force?

Not as of October 2026. The treaty needs five ratifications, including three from Council of Europe member states, and a three-month waiting period. The European Union ratified it in May 2026.

### Can a video call still be trusted to verify someone’s identity?

Not on its own. In the 2024 Arup case, a finance employee was persuaded by a deepfaked video call to transfer about US$25.6 million. Organisations should verify high-value requests through an independent channel and require a second approver.

### Is the EU Product Liability Directive already in effect?

Not yet for practical purposes. Directive (EU) 2024/2853 must be transposed by 9 December 2026 and applies to products placed on the market after that date. It treats software, including AI systems, as a product subject to strict liability.

## Conclusion

Read together, these cases show a consistent pattern. The technical failures are different: poisoned input, biased training data, invented answers, untested deployment, defeated verification. The consequence is the same. Regulators and courts are moving towards holding the deploying organisation responsible for what its systems do, and the controls they find missing are mundane ones: testing, documentation, accountable owners and monitoring.

The picture is also less settled than headlines suggest. Key EU dates have moved, the main international treaty is not yet in force, US federal policy has changed direction, and some of the most cited decisions carry limited legal weight. Anyone relying on a compliance summary, including this one, should check the primary sources linked below and the date of the last update. For my wider position on AI governance, see my [stance on AI](https://www.claudeusercontent.com/stance/), my [background](https://www.claudeusercontent.com/my-story/) and my other [articles](https://www.claudeusercontent.com/articles/).

**Update note, 26 October 2026.** This article was substantially revised. Corrections to earlier versions: the EU high-risk date (previously August 2026), the status of US Executive Order 14110 (revoked in January 2025 and never the basis of FTC enforcement), the date of the Global Digital Compact (September 2024), the start of the new EU product liability regime (products placed on the market after 9 December 2026), the description of Rite Aid as the first algorithmic disgorgement case, the Rite Aid case citation (a federal court complaint and stipulated order, not an administrative docket), and the claim that the Arup employee requested the video call.

## References

- Civil Resolution Tribunal of British Columbia. (2024). [*Moffatt v. Air Canada*, 2024 BCCRT 149](https://decisions.civilresolutionbc.ca/crt/crtd/en/525448/1/document.do).

- Council of Europe. (2024). [Framework Convention on Artificial Intelligence and Human Rights, Democracy and the Rule of Law (CETS No. 225)](https://www.coe.int/en/web/artificial-intelligence/the-framework-convention-on-artificial-intelligence).

- European Union. (2024). [Regulation (EU) 2024/1689 (Artificial Intelligence Act)](https://eur-lex.europa.eu/eli/reg/2024/1689/oj).

- European Union. (2026). [Regulation (EU) 2026/1744 (AI Omnibus)](https://eur-lex.europa.eu/eli/reg/2026/1744/oj).

- European Union. (2024). [Directive (EU) 2024/2853 on liability for defective products](https://eur-lex.europa.eu/eli/dir/2024/2853/oj).

- Federal Trade Commission. (2023). [Rite Aid banned from using AI facial recognition after FTC says retailer deployed technology without reasonable safeguards](https://www.ftc.gov/news-events/news/press-releases/2023/12/rite-aid-banned-using-ai-facial-recognition-after-ftc-says-retailer-deployed-technology-without), and [stipulated order](https://www.ftc.gov/system/files/ftc_gov/pdf/2023190_riteaid_stipulated_order_filed.pdf).

- Dastin, J. (2018). [Amazon scraps secret AI recruiting tool that showed bias against women](https://www.reuters.com/article/us-amazon-com-jobs-automation-insight/amazon-scraps-secret-ai-recruiting-tool-that-showed-bias-against-women-idUSKCN1MK08G). Reuters.

- Lee, P. (2016). [Learning from Tay’s introduction](https://blogs.microsoft.com/blog/2016/03/25/learning-tays-introduction/). Microsoft.

- Magramo, K. (2024). [British engineering giant Arup revealed as victim of $25 million deepfake scam](https://edition.cnn.com/2024/05/16/tech/arup-deepfake-scam-loss-hong-kong-intl-hnk). CNN.

- ACLU. (2018). [Amazon facial surveillance technology falsely identifies 28 members of Congress with mugshots](https://www.aclu.org/press-releases/amazon-facial-surveillance-technology-falsely-identifies-28-members-congress-mugshots).

- Grother, P., Ngan, M., & Hanaoka, K. (2019). [Face Recognition Vendor Test (FRVT) Part 3: Demographic Effects (NISTIR 8280)](https://nvlpubs.nist.gov/nistpubs/ir/2019/nist.ir.8280.pdf). NIST.

- Stanford HAI. (2026). [Artificial Intelligence Index Report 2026](https://hai.stanford.edu/ai-index).

- United Nations General Assembly. (2025). [Resolution A/RES/79/325](https://www.un.org/pga/wp-content/uploads/sites/110/2025/12/A_RES_79_325-EN.pdf).

- United States. (2025). [Executive Order 14148, Initial Rescissions of Harmful Executive Orders and Actions](https://www.govinfo.gov/content/pkg/FR-2025-01-28/html/2025-01901.htm).

- Floridi, L., & Cowls, J. (2019). [A unified framework of five principles for AI in society](https://doi.org/10.1162/99608f92.8cd550d1). *Harvard Data Science Review*, 1(1).

- Mittelstadt, B. D., et al. (2016). [The ethics of algorithms: Mapping the debate](https://doi.org/10.1177/2053951716679679). *Big Data & Society*, 3(2).

- NIST. [AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework).

- UNESCO. (2021). [Recommendation on the Ethics of Artificial Intelligence](https://www.unesco.org/en/artificial-intelligence/recommendation-ethics).

### 📚 Further Reading

For those interested in exploring similar themes, consider:

- [“Superintelligence” – Nick Bostrom](https://aviperera.com/superintelligence-nick-bostrom-book-summary-notes-highlights/) – it’s one of my all-time favourites

- [7 Essential Books on AI](https://aviperera.com/7-essential-books-on-ai-governance-every-leader-should-read/) – by the pioneers at the forefront of AI

- [Ethical Implications of AI in Warfare and Defence](https://aviperera.com/the-ethical-implications-of-ai-in-warfare-and-defence-a-comprehensive-perspective/) – very interesting read

{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "Article",
      "headline": "AI Ethics Case Studies: Lessons Learned from Real-World Failures",
      "datePublished": "2024-10-30",
      "dateModified": "2026-10-26",
      "author": {
        "@type": "Person",
        "name": "Avi Perera",
        "url": "https://aviperera.com/my-story/",
        "sameAs": [
          "https://orcid.org/0009-0005-1903-6868",
          "https://www.linkedin.com/in/avi-perera"
        ]
      },
      "publisher": { "@type": "Person", "name": "Avi Perera" },
      "mainEntityOfPage": "https://aviperera.com/ai-ethics-case-studies-lessons-learned-from-real-world-failures/",
      "about": ["AI ethics", "AI governance", "EU AI Act", "Product liability", "Algorithmic bias"]
    },
    {
      "@type": "FAQPage",
      "mainEntity": [
        {
          "@type": "Question",
          "name": "Are companies legally liable for what their AI chatbots say?",
          "acceptedAnswer": { "@type": "Answer", "text": "In some circumstances, yes. In Moffatt v. Air Canada (2024 BCCRT 149), a British Columbia tribunal held the airline liable for negligent misrepresentation by its chatbot and rejected the argument that the bot was a separate entity. It is a small-claims decision, so persuasive rather than binding." }
        },
        {
          "@type": "Question",
          "name": "When do the EU AI Act's high-risk rules apply?",
          "acceptedAnswer": { "@type": "Answer", "text": "Following the AI Omnibus (Regulation (EU) 2026/1744), stand-alone high-risk systems under Annex III apply from 2 December 2027, and high-risk AI embedded in regulated products from 2 August 2028. Prohibited practices have applied since February 2025." }
        },
        {
          "@type": "Question",
          "name": "What is algorithmic disgorgement?",
          "acceptedAnswer": { "@type": "Answer", "text": "A remedy requiring a company to delete not only improperly obtained data but also the models or algorithms built from it. The US FTC first used it against Cambridge Analytica in 2019 and again in the Everalbum, WW International and Kurbo, Edmodo and Rite Aid matters." }
        },
        {
          "@type": "Question",
          "name": "Is the Council of Europe AI Convention in force?",
          "acceptedAnswer": { "@type": "Answer", "text": "Not as of October 2026. It needs five ratifications, including three from Council of Europe member states, and a three-month waiting period. The European Union ratified it in May 2026." }
        },
        {
          "@type": "Question",
          "name": "Can a video call still be trusted to verify someone's identity?",
          "acceptedAnswer": { "@type": "Answer", "text": "Not on its own. In the 2024 Arup case, a finance employee was persuaded by a deepfaked video call to transfer about US$25.6 million. Organisations should verify high-value requests through an independent channel and require a second approver." }
        },
        {
          "@type": "Question",
          "name": "Is the EU Product Liability Directive already in effect?",
          "acceptedAnswer": { "@type": "Answer", "text": "Not yet for practical purposes. Directive (EU) 2024/2853 must be transposed by 9 December 2026 and applies to products placed on the market after that date. It treats software, including AI systems, as a product subject to strict liability." }
        }
      ]
    }
  ]
}

---

*Citation: Perera, Avi. "AI Ethics Case Studies: Lessons Learned from Real-World Failures". aviperera.com, 2024. Web. <https://aviperera.com/ai-ethics-case-studies-lessons-learned-from-real-world-failures/>*
