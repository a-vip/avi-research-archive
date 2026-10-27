---
title: "Ethical AI in Recruitment: Ensuring Fair Hiring Practices"
slug: "ethical-ai-in-recruitment-ensuring-fair-hiring-practices"
date: "2024-10-24T07:26:56"
author: "Avi Perera"
canonical_url: "https://aviperera.com/ethical-ai-in-recruitment-ensuring-fair-hiring-practices/"
source: "https://aviperera.com"
---

<link rel="canonical" href="https://aviperera.com/ethical-ai-in-recruitment-ensuring-fair-hiring-practices/" />

# Ethical AI in Recruitment: Ensuring Fair Hiring Practices

> [!NOTE]
> **Canonical Source**: This dossier was authored by [Avi Perera](https://aviperera.com) and originally published at **[https://aviperera.com/ethical-ai-in-recruitment-ensuring-fair-hiring-practices/](https://aviperera.com/ethical-ai-in-recruitment-ensuring-fair-hiring-practices/)**.
> Published on `2024-10-24`.

---

Hiring is where algorithmic decisions touch people’s livelihoods most directly, and in 2026 it is also where the law has moved fastest. In the last twelve months, the United Kingdom replaced its main rule on automated decisions, the European Union pushed back its high-risk deadline, California’s hiring regulations came into force, a US federal court allowed a nationwide age-discrimination collective action against an AI hiring vendor to proceed, and the UK data regulator published a report on how employers really use automated tools. The 2024 version of this post no longer describes the legal position accurately, and it contained errors I have now corrected.

This is a rewrite from the ground up. I explain why recruitment is a high-risk use of AI, set out the rules in the EU, the UK and the United States as they stand in October 2026, describe what fair practice requires in operational terms, and end with a checklist and answers to the questions I am asked most. I have removed several citations and anecdotes from the original that I could not verify, and the update note at the end lists them.

## Key takeaways

- In the EU, AI used for recruitment and selection is high-risk under Annex III of the AI Act, with obligations now applying from 2 December 2027 after the AI Omnibus. Emotion recognition in the workplace has been banned since February 2025.

- In the UK, Article 22 of the UK GDPR was replaced on 5 February 2026 by Articles 22A to 22D, which permit more automated decision-making but require safeguards, including a way for candidates to contest decisions.

- In the United States, there is no federal rulebook for hiring AI. Obligations come from state and city rules (New York City, California, Illinois, Texas, and Colorado from 2027) and from litigation such as Mobley v. Workday.

- Removing names or protected characteristics from CVs does not remove bias, because models infer identity from other signals.

- The failure regulators describe most often is not biased code but the absence of meaningful human oversight, candidate transparency and testing.

## Why Recruitment AI Is a High-Risk Use

Three kinds of evidence explain why regulators treat hiring differently from most business uses of AI. The first is history. Reuters reported in 2018 that Amazon had abandoned an experimental recruiting engine after it learned to downgrade CVs containing the word “women’s”, because it had been trained on a decade of mostly male applications. I discuss that case in my article on [AI ethics failures](https://www.claudeusercontent.com/ai-ethics-case-studies-lessons-learned-from-real-world-failures/). The [original Reuters report](https://www.reuters.com/article/us-amazon-com-jobs-automation-insight/amazon-scraps-secret-ai-recruiting-tool-that-showed-bias-against-women-idUSKCN1MK08G) remains the clearest account.

The second is measurement. Modern tools are less transparent than rule-based screens, and they inherit bias from the language data they are built on. Researchers at the University of Washington tested three state-of-the-art language models on more than 550 real CVs, varying only the names. In their [peer-reviewed study](https://doi.org/10.1609/aies.v7i1.31748), the models favoured White-associated names in 85.1 percent of cases and female-associated names in only 11.1 percent. The [university’s summary](https://www.washington.edu/news/2024/10/31/ai-bias-resume-screening-race-gender/) adds that the systems never preferred Black male names over White male names. One of the authors also noted that simply removing names from CVs would not fix the problem, because the models can infer identity from education history, location and word choice.

The third is scale and opacity. A rejected candidate rarely knows that a machine was involved, let alone why. That asymmetry is why the law keeps returning to the same three ideas: tell people when automated tools are used, make a human genuinely accountable, and let people contest the outcome. In its 2026 report on recruitment, the UK Information Commissioner’s Office found that many organisations use tools with little or no meaningful human involvement and are not giving candidates clear information about how decisions are made. Employers who see these tools as neutral, or as a way to remove human prejudice, are usually relying on an assumption that has not been tested.

## European Union: AI Act and GDPR

### The AI Act

The [EU AI Act (Regulation (EU) 2024/1689)](https://eur-lex.europa.eu/eli/reg/2024/1689/oj) classifies employment AI as high-risk in Annex III, point 4. Point 4(a) covers systems used to recruit or select people, including placing targeted job advertisements, analysing and filtering applications, and evaluating candidates. Point 4(b) covers systems that decide on terms of employment, promotion or termination, allocate tasks based on individual behaviour or traits, or monitor and evaluate performance. Separately, Article 5 has banned AI that infers emotions in the workplace, with narrow medical and safety exceptions, since February 2025. That prohibition catches some video-interview products that claim to read candidates’ emotional states.

On timing, the [AI Omnibus (Regulation (EU) 2026/1744)](https://www.mondaq.com/uk/new-technology/1825722/eu-digital-omnibus-on-ai-enters-into-force), in force since 27 July 2026, moved the application date for Annex III high-risk systems, which includes recruitment tools, from 2 August 2026 to 2 December 2027. The delay changes when enforcement starts, not whether employers need to prepare. Documentation, vendor due diligence and testing take many months, and contracts signed now will still be running in 2028.

The obligations split between those who build and those who use. Providers must meet requirements in Articles 9 to 15 of the Act: a risk management system, data governance that includes examining the data for possible biases, technical documentation, logging, transparency to deployers, human oversight by design, and appropriate accuracy and robustness. Deployers, which means most employers, carry the duties in Article 26. They must use the system according to its instructions, assign human oversight to people with the competence, training and authority to do it, monitor the system, keep the logs they control for at least six months, and, before using such a system at work, inform workers’ representatives and the affected workers. Article 86 gives people affected by decisions based on the output of these systems a right to a clear explanation of the system’s role and the main elements of the decision. An employer that puts its own name on a tool, or modifies it substantially, can become a provider under Article 25 and take on the heavier duties.

One nuance deserves emphasis because it is often misreported: the fundamental rights impact assessment in Article 27 applies to public bodies, to private entities providing public services, and to certain credit and insurance deployers. It is not a blanket requirement for every private employer, although a data protection impact assessment under the GDPR will often still be needed.

### GDPR and automated decisions

In the EU, Article 22 of the GDPR still operates as a default prohibition on decisions based solely on automated processing that have legal or similarly significant effects, subject to narrow exceptions. A recruitment rejection fits that description. The Court of Justice’s decision in [*SCHUFA Holding* (C-634/21)](https://www.aoshearman.com/en/insights/ao-shearman-on-data/cjeu-rules-that-a-credit-score-constitutes-automated-decision-making-under-the-gdpr), decided on 7 December 2023, held that producing a credit score is itself an automated decision when a third party draws heavily on it to decide whether to enter a contract. My earlier version said the case established a right to explanations, which overstated it. The right to an explanation was developed in a later judgment, *Dun & Bradstreet Austria* (C-203/22), delivered on 27 February 2025, and [reported follow-on litigation in Germany](https://ppc.land/schufa-loses-blanket-trade-secret-defence-at-germanys-top-civil-court/) has since rejected a blanket trade-secret defence. The practical lesson for recruitment is that a tool whose score a recruiter follows without real scrutiny can itself count as the decision.

## United Kingdom: Equality Act and the New Automated Decision Rules

### Discrimination law

The Equality Act 2010 is the foundation. Indirect discrimination under [section 19](https://www.legislation.gov.uk/ukpga/2010/15/section/19) applies where a neutral provision, criterion or practice puts a protected group at a particular disadvantage and cannot be justified as a proportionate means of achieving a legitimate aim. [Section 39](https://www.legislation.gov.uk/ukpga/2010/15/section/39) protects job applicants. The Supreme Court’s decision in [*Essop v Home Office* [2017] UKSC 27](https://www.bailii.org/uk/cases/UKSC/2017/27.html) held that a claimant does not have to prove why a group is disadvantaged, only that it is, which is significant for opaque algorithms whose inner workings candidates cannot examine. Employers must also consider the duty to make [reasonable adjustments](https://www.legislation.gov.uk/ukpga/2010/15/section/20), which can be engaged by timed online tests, video interviews and gamified assessments that disadvantage disabled applicants.

### Data protection after the Data (Use and Access) Act 2025

My 2024 version pointed to the Data Protection and Digital Information Bill, which lapsed and was never enacted. What happened instead is the [Data (Use and Access) Act 2025](https://www.legislation.gov.uk/ukpga/2025/18/contents). Section 80, in force since 5 February 2026, [replaced Article 22 of the UK GDPR](https://www.traverssmith.com/knowledge/knowledge-container/uks-data-protection-reforms-take-effect-a-new-era-for-automated-decision-making/) with new Articles 22A to 22D. In outline, significant decisions based solely on automated processing are now permitted as a starting point where special category data is not involved, provided the Article 22C safeguards apply. Those safeguards include telling people about the decision, letting them make representations, giving them access to human intervention and a way to contest the outcome. Where special category data is involved, such as health, ethnicity or biometric data, the stricter conditions in Article 22B apply. Practitioners point out that this makes the UK noticeably more permissive than the EU, so a UK-compliant approach will not automatically satisfy EU law.

In March 2026, the ICO published [Recruitment Rewired](https://ico.org.uk/about-the-ico/what-we-do/recruitment-rewired/introduction-what-is-adm-and-why-are-we-focusing-on-it-in-recruitment/), a report based on work with more than 30 employers, alongside draft updated guidance on automated decision-making. The ICO’s central concerns are meaningful human involvement and clear information for candidates. A UK employer that uses a tool to reject applications outright should assume the new Article 22C safeguards apply to it, and that the regulator is paying attention to recruitment specifically.

## United States: State Rules and Litigation

There is still no comprehensive federal AI statute that I am aware of, and enforcement of existing discrimination law has shifted. The federal equal employment agency removed its earlier technical assistance on algorithmic hiring tools in 2025 and law firm commentary describes a move away from disparate impact enforcement, even as [states such as New York and New Jersey have codified disparate impact liability](https://www.jdsupra.com/topics/algorithms/employment-discrimination/artificial-intelligence) in their own laws. Employers cannot assume that reduced federal activity means reduced exposure.

The binding rules sit at city and state level. New York City’s Local Law 144, in force since July 2023, requires annual independent bias audits of automated employment decision tools, publication of a summary and notice to candidates. A [Consumer Reports-led study](https://arxiv.org/abs/2406.01399) of employers found very low compliance, with only 18 of those examined posting audit reports and 13 posting transparency notices, which tells you the law is lightly enforced, not that it is unimportant. California’s [Civil Rights Council regulations](https://www.akingump.com/en/insights/ai-law-and-regulation-tracker/california-civil-rights-council-approves-employment-regulations-regarding-automated-decision-systems), effective 1 October 2025, state that using an automated-decision system can violate state fair employment law, require employers to keep related records for at least four years, and confirm that assessments eliciting disability information may be unlawful medical inquiries. Illinois HB 3773, effective 1 January 2026, [requires notice when AI is used](https://law.washu.edu/ai-policy-and-regulation-resources/labor-employment/) in employment decisions and bars discriminatory use, including the use of zip codes as proxies. Texas’s TRAIGA also took effect on 1 January 2026. Colorado’s original AI Act was repealed and re-enacted by [SB 26-189](https://www.ebglaw.com/workforce-bulletin/tag/colorado), signed on 14 May 2026, with a new effective date of 1 January 2027 and a focus on automated decision-making technology.

Litigation is doing as much work as legislation. In [*Mobley v. Workday*](https://www.akingump.com/en/insights/ai-law-and-regulation-tracker/court-allows-discrimination-claims-against-ai-hiring-tool-to-proceed-or-mobley-v-workday-inc), the court accepted that Workday could plausibly be liable as an “agent” of the employers who delegated screening functions to its software. In May 2025 the court granted [preliminary certification of a nationwide age-discrimination collective action](https://www.fisherphillips.com/en/insights/insights/discrimination-lawsuit-over-workdays-ai-hiring-tools-can-proceed-as-class-action-6-things) on a disparate impact theory, and the case has continued through further rulings in 2026, including a [June 2026 decision](https://www.gunder.com/en/news-insights/insights/client-insight-quarterly-employment-law-update-spring-2026) that allowed some claims to proceed and dismissed others. A class certification hearing is [reportedly scheduled for March 2027](https://thegrio.com/2026/09/24/workday-ai-hiring-discrimination-lawsuit/). Workday denies wrongdoing, and nothing has been decided on the merits. A separate class action against Eightfold AI argues that an AI hiring platform operated as an unregistered consumer reporting agency under the Fair Credit Reporting Act. Both cases test who is accountable when the screening is done by a vendor’s software, and the early rulings suggest that vendors, not only employers, are in scope.

## International Standards

The International Labour Organization’s [Discrimination (Employment and Occupation) Convention, 1958 (No. 111)](https://normlex.ilo.org/dyn/nrmlx_en/f?p=NORMLEXPUB:12100:0::NO::P12100_ILO_CODE:C111) remains the global anchor. It requires states to pursue equality of opportunity and treatment in employment, and it applies to automated tools in the same way as to human decisions. On the management side, [ISO/IEC 42001](https://www.iso.org/standard/81230.html) sets requirements for an AI management system, and the [NIST AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework) offers a widely used risk vocabulary. My earlier draft attached specific section numbers to ISO/IEC 42001 for human resources. That standard is not organised around the use case, so I have removed those references. Neither framework is a legal safe harbour, though both help an employer show it took reasonable steps.

## Jurisdiction Snapshot

JurisdictionKey rule for hiring AIStatus in October 2026EUAI Act, Annex III point 4 (high-risk); Article 5 emotion recognition ban; GDPR Article 22Ban in force since Feb 2025. High-risk duties from 2 Dec 2027.UKEquality Act 2010; UK GDPR Articles 22A to 22DNew automated decision rules in force since 5 Feb 2026.New York CityLocal Law 144 bias audits and noticesIn force since July 2023.CaliforniaCivil Rights Council automated-decision regulationsIn force since 1 Oct 2025.IllinoisHB 3773 (Human Rights Act amendment)In force since 1 Jan 2026.ColoradoSB 26-189 (repealed and re-enacted)Effective 1 Jan 2027.US federalExisting discrimination statutesEnforcement posture shifting; litigation continuing.

## What Fair Practice Requires

Legal compliance and fairness are not identical, but they point the same way, and the practical steps overlap heavily. I group them into six commitments.

### 1. Decide whether you need the tool at all

Begin with the purpose and the evidence. What problem does the tool solve, what evidence shows it works for the role, and would a simpler, more transparent method do the job? Treat tools that claim to infer personality, emotion or potential from video or voice with particular scepticism. In the EU some of that is banned, and the scientific basis is widely disputed.

### 2. Do vendor due diligence that goes beyond the brochure

Ask the vendor what data the model was trained and validated on, how bias was tested and with which groups, what the results were, how often the model changes, and what logs and explanations you can obtain. Researchers who reviewed vendor claims found that many vendors say little about bias or use vague language such as “fairness” without defining it. Put your requirements in the contract: audit rights, notice of model changes, cooperation with regulators and candidates’ requests, and indemnities. If you are in the EU or the UK, ask who the provider is for the purposes of the AI Act and who is the controller for data protection.

### 3. Test outcomes, not just inputs

Removing protected characteristics from the data does not prevent discrimination, because proxies carry the same information. Measure outcomes by group at each stage of the funnel, compare them, investigate gaps, and repeat the tests after every material model or data change. The worked example below shows the standard first-pass check.

### 4. Make human oversight real

A human who clicks “approve” on a ranked list has not exercised oversight. Meaningful oversight needs a person with the competence, time, authority and information to disagree with the tool and to override it. Log overrides, and review whether recruiters are in practice agreeing with the tool almost every time, which is a sign the oversight is nominal.

### 5. Tell candidates and give them a route to challenge

Say clearly when automated tools are used, what they do, and what the candidate can do about it. Provide an accessible way to request human review and to ask for reasonable adjustments. Under the UK’s new Article 22C and the EU’s Article 86 this is a legal requirement in many cases, and it is also the most effective way to catch errors.

### 6. Keep records and keep monitoring

Record what the tool was, how it was configured, what testing was done and what decisions were made. California requires four years of relevant records, and the AI Act expects logs to be retained. Monitor outcomes after deployment, and have a defined process to suspend a tool that shows adverse impact. The tools I review in my guide to [AI compliance and governance platforms](https://www.claudeusercontent.com/best-ai-regulatory-compliance-tools-for-businesses-2024/) can help with inventory and evidence, but they do not replace these decisions.

## A Worked Bias-Testing Example

The four-fifths rule is a long-standing screening heuristic from US employment guidelines: if the selection rate for one group is less than 80 percent of the rate for the group with the highest rate, that is generally regarded as evidence of adverse impact that needs investigating. It is a trigger for further analysis, not a legal test of discrimination, and it is not a substitute for statistical testing or for applying the law of your own jurisdiction. The [US Uniform Guidelines](https://www.ecfr.gov/current/title-29/subtitle-B/chapter-XIV/part-1607) set out the rule, and New York City’s audit rules use a closely related impact ratio.

Here is a hypothetical illustration with invented numbers. Suppose a screening tool advances 80 of 200 applicants from group A (a selection rate of 40 percent) and 24 of 100 applicants from group B (24 percent). The impact ratio is 24 divided by 40, which is 0.60. That is well below 0.80, so the gap should be investigated: was it caused by the tool, by the applicant pool, or by something in the job requirements, and is it justified by a legitimate and proportionate aim? If the tool is the cause and the aim cannot be justified, the employer has a problem under US disparate impact doctrine, the UK’s indirect discrimination rules and, in the EU, the AI Act’s expectations on bias. Run the same calculation for each stage of the process, for intersections such as race and sex together, and again after every change to the tool.

## Compliance Checklist

- List every automated tool used in recruitment, including features inside your applicant tracking system, and record who is the provider and who is the controller or deployer.

- Classify each tool under the rules that apply to you: EU AI Act high-risk or prohibited, GDPR and UK GDPR automated decision rules, and any US city or state rule.

- Complete a data protection impact assessment and an equality impact assessment where a tool materially affects candidates.

- Obtain from vendors their bias testing results, validation data, logs and model change policy, and write audit rights into contracts.

- Test selection rates by group at each stage, including intersections, before launch and after every material change.

- Define meaningful human oversight: named reviewers, authority to override, training, and review of override rates.

- Notify candidates about automated tools in plain language and provide a route to human review and to reasonable adjustments.

- Inform workers’ representatives and affected staff where required, for example under Article 26 of the AI Act.

- Keep records for the periods the law requires, including four years in California.

- Set a review cycle and a suspension procedure for tools that show adverse impact.

## Frequently Asked Questions

### Is AI recruitment legal in the EU?

Yes, but it is regulated. AI used for recruitment and selection is classed as high-risk under Annex III of the EU AI Act, with obligations applying from 2 December 2027 after the AI Omnibus. Emotion recognition in the workplace has been banned since February 2025, and GDPR rules on automated decisions already apply.

### What changed in the UK in 2026?

On 5 February 2026, section 80 of the Data (Use and Access) Act 2025 replaced Article 22 of the UK GDPR with Articles 22A to 22D. Solely automated significant decisions are now permitted as a starting point where special category data is not involved, but employers must apply safeguards including informing candidates and letting them contest decisions.

### Can a company be sued over an AI hiring tool its vendor built?

Yes, and vendors can be sued too. In Mobley v. Workday, a US court accepted that a software provider could plausibly be liable as an agent of employers, and preliminarily certified a nationwide age-discrimination collective action in May 2025. The case has not been decided on its merits.

### Does removing names and photos from CVs prevent AI bias?

No. University of Washington researchers found that language models favoured White-associated names in 85.1 percent of cases, and warned that removing names does not fix the problem because models infer identity from education history, location and word choice.

### What is the four-fifths rule?

It is a US screening heuristic: if the selection rate for a group is below 80 percent of the highest group’s rate, this is regarded as evidence of adverse impact that warrants investigation. It is a trigger for analysis, not a conclusive legal test.

### Do I need a bias audit?

It is legally required in New York City for covered tools, and it is effectively expected elsewhere as evidence that you took reasonable steps. Even where it is not mandatory, testing outcomes by group before and after deployment is the most defensible control.

## Conclusion

The most useful change in my own thinking since the first version of this post is that the central question has shifted from whether AI can be fair in hiring to whether the organisation using it can prove it took fairness seriously. The law in all three jurisdictions converges on the same practical test: do you know what your tools do, have you measured their effects on different groups, can a human really overrule them, and can a candidate find out and challenge the outcome? Employers who can answer yes with evidence are in a strong position wherever they operate. Employers who cannot are relying on their vendors’ assurances, and the Workday litigation and the ICO’s findings show how little protection that offers. For my wider views on AI governance, see my [stance on AI](https://www.claudeusercontent.com/stance/), my [background](https://www.claudeusercontent.com/my-story/) and my other [articles](https://www.claudeusercontent.com/articles/).

*Legal information, not legal advice. Rules in this area are changing quickly, so check current legal advice for your specific jurisdiction and circumstances.*

**Update note, 27 October 2026.** This post was rewritten. Corrections to the 2024 version: the AI Act citation (Regulation (EU) 2024/1689); the description of the SCHUFA judgment (it concerned whether a credit score is itself an automated decision, not a right to explanations); the UK legal framework (the Data Protection and Digital Information Bill lapsed and was replaced by the Data (Use and Access) Act 2025); and several statutory references that were wrong or misapplied, including provisions of the Data Protection Act 2018, the Employment Rights Act 1996 and the public sector equality duty, which applies to public authorities rather than private employers. I also removed two case citations (*Bouamar v. Accenture* and *Smith v. Microsoft Corporation*) that I could not trace in any source, the ISO/IEC 42001 section numbers, an unsourced International Labour Organization statistic, and the first-person client anecdotes, which I could not verify.

## References

- European Union. (2024). [Regulation (EU) 2024/1689 (Artificial Intelligence Act)](https://eur-lex.europa.eu/eli/reg/2024/1689/oj).

- European Union. (2026). [Regulation (EU) 2026/1744 (AI Omnibus)](https://eur-lex.europa.eu/eli/reg/2026/1744/oj).

- Court of Justice of the European Union. (2023). *SCHUFA Holding (Scoring)*, Case C-634/21, judgment of 7 December 2023. See [A&O Shearman analysis](https://www.aoshearman.com/en/insights/ao-shearman-on-data/cjeu-rules-that-a-credit-score-constitutes-automated-decision-making-under-the-gdpr).

- Court of Justice of the European Union. (2025). *Dun & Bradstreet Austria*, Case C-203/22, judgment of 27 February 2025.

- UK Parliament. (2025). [Data (Use and Access) Act 2025](https://www.legislation.gov.uk/ukpga/2025/18/contents).

- UK Parliament. (2010). [Equality Act 2010, sections 19, 20 and 39](https://www.legislation.gov.uk/ukpga/2010/15/section/19).

- UK Supreme Court. (2017). [*Essop and others v Home Office (UK Border Agency)* [2017] UKSC 27](https://www.bailii.org/uk/cases/UKSC/2017/27.html).

- Information Commissioner’s Office. (2026). [Recruitment Rewired](https://ico.org.uk/about-the-ico/what-we-do/recruitment-rewired/introduction-what-is-adm-and-why-are-we-focusing-on-it-in-recruitment/).

- Dastin, J. (2018). [Amazon scraps secret AI recruiting tool that showed bias against women](https://www.reuters.com/article/us-amazon-com-jobs-automation-insight/amazon-scraps-secret-ai-recruiting-tool-that-showed-bias-against-women-idUSKCN1MK08G). Reuters.

- Wilson, K., & Caliskan, A. (2024). [Gender, race, and intersectional bias in resume screening via language model retrieval](https://doi.org/10.1609/aies.v7i1.31748). *Proceedings of the AAAI/ACM Conference on AI, Ethics, and Society*, 7(1), 1578-1590.

- Smith, A., et al. (2024). [Null compliance: NYC Local Law 144 and the challenges of algorithm accountability](https://arxiv.org/abs/2406.01399).

- California Civil Rights Council. (2025). [Employment regulations regarding automated-decision systems](https://www.akingump.com/en/insights/ai-law-and-regulation-tracker/california-civil-rights-council-approves-employment-regulations-regarding-automated-decision-systems) (summary).

- *Mobley v. Workday, Inc.*, No. 3:23-cv-00770 (N.D. Cal.). See [Akin Gump summary](https://www.akingump.com/en/insights/ai-law-and-regulation-tracker/court-allows-discrimination-claims-against-ai-hiring-tool-to-proceed-or-mobley-v-workday-inc) and [Fisher Phillips summary](https://www.fisherphillips.com/en/insights/insights/discrimination-lawsuit-over-workdays-ai-hiring-tools-can-proceed-as-class-action-6-things).

- US Equal Employment Opportunity Commission et al. [Uniform Guidelines on Employee Selection Procedures, 29 CFR Part 1607](https://www.ecfr.gov/current/title-29/subtitle-B/chapter-XIV/part-1607).

- International Labour Organization. (1958). [Discrimination (Employment and Occupation) Convention (No. 111)](https://normlex.ilo.org/dyn/nrmlx_en/f?p=NORMLEXPUB:12100:0::NO::P12100_ILO_CODE:C111).

- ISO/IEC. (2023). [ISO/IEC 42001:2023 Artificial intelligence management system](https://www.iso.org/standard/81230.html).

- NIST. (2023). [AI Risk Management Framework (AI 100-1)](https://www.nist.gov/itl/ai-risk-management-framework).

## Further reading

- [AI Ethics Case Studies: Lessons Learned from Real-World Failures](https://www.claudeusercontent.com/ai-ethics-case-studies-lessons-learned-from-real-world-failures/)

- [Best AI Regulatory Compliance Tools for Businesses (2026)](https://www.claudeusercontent.com/best-ai-regulatory-compliance-tools-for-businesses-2024/)

- [The Impact of AI on Employment: Navigating the Shifting Job Landscape](https://www.claudeusercontent.com/articles/)

---

*Citation: Perera, Avi. "Ethical AI in Recruitment: Ensuring Fair Hiring Practices". aviperera.com, 2024. Web. <https://aviperera.com/ethical-ai-in-recruitment-ensuring-fair-hiring-practices/>*
