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

When Microsoft’s AI chatbot [Tay](https://www.theverge.com/2016/3/24/11297050/tay-microsoft-chatbot-racist) descended into generating hate speech within 24 hours of its launch in 2016, it was viewed as a fascinating experiment gone wrong. Today, such a failure would be viewed as a corporate liability. As we venture further into the age of Generative AI, examining these failures is no longer just academically interesting—it is critical for legal survival.

Recent statistics from the [2025 AI Index Report](https://aiindex.stanford.edu/report/) reveal a disturbing trend: reported AI incidents have surged by over 50% year-over-year. We have moved beyond simple classification errors to an era of deepfake fraud, hallucinated policies, and systemic bias. These case studies provide invaluable lessons for researchers, developers, and policymakers who must now navigate a landscape of strict enforcement.

.kb-table-of-content-nav.kb-table-of-content-id2169_a2fe02-51 .kb-table-of-content-wrap{padding-top:var(--global-kb-spacing-sm, 1.5rem);padding-right:var(--global-kb-spacing-sm, 1.5rem);padding-bottom:var(--global-kb-spacing-sm, 1.5rem);padding-left:var(--global-kb-spacing-sm, 1.5rem);}.kb-table-of-content-nav.kb-table-of-content-id2169_a2fe02-51 .kb-table-of-contents-title-wrap{padding-top:0px;padding-right:0px;padding-bottom:0px;padding-left:0px;}.kb-table-of-content-nav.kb-table-of-content-id2169_a2fe02-51 .kb-table-of-contents-title{font-weight:regular;font-style:normal;}.kb-table-of-content-nav.kb-table-of-content-id2169_a2fe02-51 .kb-table-of-content-wrap .kb-table-of-content-list{font-weight:regular;font-style:normal;margin-top:var(--global-kb-spacing-sm, 1.5rem);margin-right:0px;margin-bottom:0px;margin-left:0px;}

## Legal Framework for AI Ethics (Updated for 2026)

As we enter 2026, the era of “voluntary codes” is over. We have transitioned from a phase of proposal to a phase of **enforcement**, with binding treaties and strict liability regimes now in effect across major jurisdictions.

#### International Instruments

*

**Council of Europe Framework Convention on AI (2024)** Opened for signature in September 2024, this is the world’s first [legally binding international treaty on AI](https://www.coe.int/en/web/artificial-intelligence/the-framework-convention-on-artificial-intelligence). Unlike EU law, which focuses on market safety, this Treaty focuses strictly on **Human Rights, Democracy, and the Rule of Law**.

- **Status:** Signed by the EU, UK, US, and others; currently in the ratification phase.

- **Key Impact:** It forces signatory nations to establish judicial remedies for victims of AI-related human rights violations.

**UN Global Digital Compact (2025)** Adopted at the [UN Summit of the Future](https://www.un.org/techenvoy/global-digital-compact) in late 2025, the Compact establishes the first truly global consensus on AI governance. It mandates the creation of an **International Scientific Panel on AI** (modelled on the IPCC for climate change) to provide impartial, scientific assessments of AI risks to guide global policy.

#### European Union

**The AI Act (Regulation (EU) 2024/1689)** Fully legally binding, with the “unacceptable risk” bans (e.g., social scoring, emotion recognition in workplaces) having entered into force in February 2025.

- **Official Text:** [Regulation (EU) 2024/1689](https://eur-lex.europa.eu/eli/reg/2024/1689/oj)

- **2026 Milestone:** From August 2026, the bulk of obligations for **“High-Risk” systems** (Annex III) apply. This includes mandatory conformity assessments, fundamental rights impact assessments (FRIA), and registration in the EU database.

**The “New” Liability Regime: Product Liability Directive (PLD)** Crucial Update:* The specific “AI Liability Directive” has largely been sidelined in favour of the revised **Product Liability Directive**, adopted in late 2024 (Directive (EU) 2024/2853).

- **Official Text:** [Directive (EU) 2024/2853](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32024L2853)

- **Software is a Product:** The PLD explicitly classifies software and AI systems as “products.”

- **Strict Liability:** Developers can now be held liable for damage caused by defective AI *without* the victim needing to prove negligence (fault). If the AI causes harm (including data loss or psychological harm), the producer is strictly liable.

#### National Legislation (United Kingdom)

**Data (Use and Access) Act 2025** Enacted in June 2025, this Act reforms the UK’s data landscape to support “Smart Data” schemes.

- **Source:** [Data (Use and Access) Bill](https://bills.parliament.uk/bills/3763)

- **AI Impact:** It creates a statutory footing for **Digital Verification Services**, essential for combating deepfakes. It also simplifies data reuse for scientific research, aiding AI model training in healthcare and science.

**Online Safety Act (Full Implementation)** Now fully operational, Ofcom has begun enforcing “Duties of Care” against platforms hosting illegal AI-generated content (CSAM, fraud).

- **Source:** [Online Safety Act 2023](https://www.legislation.gov.uk/ukpga/2023/50/contents)

- **Deepfake Liability:** Platforms face fines of up to 10% of global turnover if they fail to prevent the proliferation of non-consensual deepfake pornography or AI-enabled fraud.

#### United States

**Executive Order 14110 & Agency Rulemaking** While federal legislation remains gridlocked, enforcement has moved to the agency level. The **FTC** has successfully applied “Algorithmic Disgorgement” (forcing companies to delete models trained on illegal data) in cases like *Rite Aid*, effectively creating a common-law precedent for AI compliance based on [Executive Order 14110](https://www.google.com/search?q=https://www.whitehouse.gov/briefing-room/presidential-actions/2023/10/30/executive-order-on-the-safe-secure-and-trustworthy-development-and-use-of-artificial-intelligence/).

## Case Study 1: Microsoft’s Tay Chatbot (2016)

*

**Background**: Microsoft launched [Tay](https://blogs.microsoft.com/blog/2016/03/25/learning-tays-introduction/) on Twitter as an experiment in conversational understanding. Within 24 hours, the system was corrupted by user interactions, producing hate speech and necessitating an immediate shutdown.

**The Story**: In March 2016, Microsoft released Tay, a chatbot designed to learn from user interactions to mimic the “voice” of a 19-year-old American girl. The goal was to showcase advances in Natural Language Processing (NLP). However, the model lacked sufficient filters for malicious input. Trolls on Twitter quickly discovered they could manipulate the bot by feeding it offensive prompts (“repeat after me…”). Within 16 hours, Tay transitioned from posting friendly greetings to generating virulent racist, misogynistic, and extremist content. Microsoft suspended the account and issued an apology, citing a “coordinated attack.”

**The Lesson**: Tay remains the textbook example of **Data Poisoning** and the failure of “naïve” learning in public spaces. It demonstrated that AI operating in the wild cannot blindly accept user input as training data. It also highlighted the reputational risk of deploying models without robust content moderation “guardrails.”

**Legal Implications**

- **Intermediary Liability:** In 2016, platforms were largely shielded by “Safe Harbor” laws (like Section 230 in the US). Today, under the **UK Online Safety Act** and **EU Digital Services Act**, a platform that generates illegal content (rather than just hosting it) faces significantly higher liability.

- **Harassment:** The content generated raised potential violations under the **UK Equality Act 2010** regarding harassment and hate speech regulations.

**Relevant Regulation**

- **EU Digital Services Act (DSA):** Modern regulations now require risk assessments for systemic risks, including the amplification of illegal content.

- **GDPR Article 22:** Highlights the risks of automated profiling without human oversight.

## Case Study 2: Amazon’s Biased Recruitment AI (2018)

**Background**: Amazon attempted to build an automated tool to screen job applicants. The project was abandoned after it was discovered the AI penalised female candidates due to historical biases in the training data. **Source:** [Reuters Special Report](https://www.reuters.com/article/us-amazon-com-jobs-automation-insight-idUSKCN1MK08G/)

**The Story**: Between 2014 and 2017, Amazon engineers developed an AI engine to rate job applicants from one to five stars. The system was trained on 10 years of historical CVs submitted to the company—a dataset dominated by men. Consequently, the model “learned” that male candidates were preferable. It began systematically downgrading CVs containing the word “women’s” (e.g., “women’s chess club captain”) and penalising graduates of two all-female colleges. When the bias was discovered during internal testing, Amazon attempted to patch it, but ultimately scrapped the project in 2018 as they could not guarantee other forms of bias wouldn’t emerge.

**The Lesson**: This case illustrates **Historical Bias Encoding**. If the past data reflects a prejudiced reality (the “glass ceiling”), the AI will not only replicate that prejudice but automate and scale it. It set the precedent that “blind” algorithms can still produce discriminatory outcomes (Disparate Impact).

**Legal Implications**

- **Employment Discrimination:** Such a tool, if deployed, would likely violate **Title VII of the US Civil Rights Act** and **Section 39 of the UK Equality Act 2010**.

- **Disparate Impact:** The legal doctrine that a policy (or algorithm) can be illegal if it disproportionately hurts a protected group, even if there was no intent* to discriminate.

**Relevant Case Law**

- ***Griggs v. Duke Power Co.* (1971):** The foundational US Supreme Court case establishing the “Disparate Impact” doctrine, which is now applied to algorithmic fairness.

- **EU AI Act (Reference):** AI systems used for recruitment are now classified explicitly as **“High Risk”** (Annex III), requiring strict conformity assessments and human oversight.

## Case Study 3: Air Canada’s “Lying” Chatbot (2024)

*

**Background**: A Civil Resolution Tribunal ruled that a company is liable for negligent misrepresentation when its AI chatbot provides false information, rejecting the defence that the AI is a distinct legal entity. **Official Ruling:** [Moffatt v. Air Canada, 2024 BCCRT 149](https://www.google.com/search?q=https://www.canlii.org/en/bc/bccrt/doc/2024/2024bccrt149/2024bccrt149.html)

**The Story**: In 2022, Jake Moffatt, a passenger travelling for a funeral, asked Air Canada’s AI chatbot about bereavement fares. The chatbot explicitly stated he could apply for the discount retroactively* within 90 days of travel—a “hallucination” that directly contradicted the airline’s actual policy (which required pre-approval). When Moffatt applied for the refund, Air Canada denied it. In the resulting legal battle (Moffatt v. Air Canada), the airline attempted a novel defence: it argued that the chatbot was a “separate legal entity” responsible for its own actions, and the airline itself was not liable for the bot’s “misleading words.”

**The Lesson**: This case killed the “beta test” defence for corporate AI. It established that companies cannot decouple themselves from their automated agents. If a chatbot is placed on a commercial website to serve customers, the company is as responsible for its output as it would be for a static webpage or a human agent. Accuracy is a non-negotiable duty of care.

**Legal Implications**

- **Negligent Misrepresentation:** The tribunal found the airline failed to take “reasonable care” to ensure the accuracy of its chatbot.

- **Rejection of “Separate Entity” Defence:** The ruling clarified that an AI tool is part of the vendor’s service, not an independent agent with its own liability shield.

**Relevant Case Law**

- ***Moffatt v. Air Canada*, 2024 BCCRT 149** (Civil Resolution Tribunal)

*Key Holding:* Companies are liable for specific promises made by their AI agents, even if those promises contradict other Terms of Service.

## Case Study 4: Rite Aid’s Biometric Ban (2024)

*

**Background**: The US Federal Trade Commission (FTC) banned pharmacy chain Rite Aid from using facial recognition for five years after its system was found to disproportionately misidentify minorities as shoplifters. **Official Order:** [FTC Decision & Order (Docket No. C-4809)](https://www.ftc.gov/legal-library/browse/cases-proceedings/2023190-rite-aid-corporation-ftc-v)

**The Story**: Between 2012 and 2020, Rite Aid deployed facial recognition technology in hundreds of stores to identify “persons of interest” (suspected shoplifters). The system, however, was plagued by poor image quality and algorithmic bias. According to the FTC complaint, the system falsely flagged legitimate customers as criminals, leading to public humiliation and ejection from stores. Crucially, the technology generated false positive matches for Black, Asian, and Latino faces at a significantly higher rate than for White faces—a known issue in biometric training data that Rite Aid failed to test for or mitigate.

**The Lesson**: This case introduces the concept of **“Algorithmic Disgorgement.”** As part of the settlement, Rite Aid wasn’t just fined; it was ordered to delete* all the biometric data it had collected and any models trained on that data. It serves as a warning that using “off-the-shelf” AI for high-stakes surveillance without rigorous, demographic-specific testing is a violation of consumer protection laws.

**Legal Implications**

- **Unfair Trade Practices:** The FTC classified the deployment of untested, biased surveillance in retail settings as an “unfair” practice under Section 5 of the FTC Act.

- **Algorithmic Disgorgement:** A regulatory remedy requiring the deletion of ill-gotten data and the algorithms built upon it.

**Relevant Regulation**

- **FTC Order (Docket No. C-4809):** *In the Matter of Rite Aid Corporation*

- **EU AI Act (Reference):** This type of “real-time remote biometric identification” in publicly accessible spaces is now classified as **“Unacceptable Risk”** (Prohibited) or **“High Risk”** under the new EU framework (Article 5).

## Case Study 5: The Hong Kong Deepfake CFO (2024)

*

**Background**: A finance employee at a multinational firm (Arup) was tricked into transferring **$25.5 million** to scammers after attending a video conference where every other participant* was a deepfake. **Source:** [CNN Business Report](https://edition.cnn.com/2024/02/04/asia/deepfake-cfo-scam-hong-kong-intl-hnk/index.html)

**The Story**: The employee initially received a suspicious email from the company’s “CFO” requesting a secret transaction. Prudently, the employee requested a video call to verify. The scammers obliged. Using deepfake technology, they generated live video and audio of the CFO *and* several other colleagues, all of whom appeared to be present on the conference call. Seeing trusted faces and hearing familiar voices, the employee’s doubts vanished, and they authorised 15 transfers totalling HK$200 million ($25.5 million USD). The fraud was only discovered days later when the employee checked with the head office.

**The Lesson**: “Human-in-the-loop” is no longer a sufficient security control. If human senses (sight and sound) can be deceived by real-time generative AI, verification must move to the hardware level. Companies must now rely on **cryptographic verification** (FIDO2 keys, digital signatures) rather than video presence to authorise high-value actions.

**Legal Implications**

- **Duty of Care in Cybersecurity:** Raises new questions about what constitutes “reasonable security measures” for corporate finance.

- **Insurance Coverage:** Many “Cyber Insurance” and “Crime” policies have exclusions for “voluntary transfers” (social engineering), potentially leaving companies uncovered for deepfake fraud unless policies are specifically updated.

**Relevant Regulation**

- **UK Online Safety Act 2023:** While this case occurred in Hong Kong, under the UK’s new laws, platforms hosting the tools used to create non-consensual deepfakes or facilitate fraud face new “duties of care” to prevent such illegal content.

### Lessons Learned & Best Practices (Updated for 2026)

The failures of the last decade have taught us a harsh truth: technical fixes alone are insufficient. In 2026 and beyond, ethical and legal safeguards must be baked into the lifecycle of every system—from data collection through to post-market monitoring.

Below are actionable lessons grounded in current regulatory standards and the latest high-profile failures.

#### 1. Ethical Testing & Impact Assessment

- **Pre-deployment Ethical Impact Assessments (EIAs):** Use published methodologies to map harms, stakeholders, and mitigations *before* a single line of code is deployed. EIAs must be versioned documents that evolve with the system.

- **Adversarial “Red-Teaming”:** Do not rely on standard QA. Perform adversarial attacks, misuse scenarios, and input-manipulation tests (e.g., “jailbreaking”) to reveal failure modes early.

- **Hallucination Stress Testing:** Following the *Air Canada* ruling, systems must be tested for “policy invention.” Ensure your RAG (Retrieval-Augmented Generation) systems cannot override your Terms of Service.

- **Standards-Based Well-being Metrics:** Integrate practices from **IEEE 7010** (Recommended Practice for Assessing the Impact of Autonomous and Intelligent Systems on Human Well-being) to measure societal impact beyond mere accuracy.

#### 2. Bias Mitigation & “Disgorgement” Readiness

- **Data Lineage & Provenance:** Document datasets with **datasheets** that record origin, consent, and limitations.

- **Prepare for Algorithmic Disgorgement:** As seen in the *Rite Aid* case, regulators can order the destruction of models trained on biased or ill-gotten data. If you cannot segregate your data, you risk losing the entire model.

- **Regular Algorithmic Audits:** Combine internal checks with independent third-party audits focused on disparate impact, calibration, and fairness for protected groups.

- **Technical Mitigations:** Employ debiasing, differential privacy, and thresholding where appropriate; explicitly measure and document the tradeoffs between accuracy and fairness.

#### 3. Governance & Corporate Liability

- **Strict Liability for AI Agents:** Treat your AI’s output as legally binding. Companies can no longer claim a chatbot is a “separate legal entity.” If the AI promises a refund, you may be liable to pay it.

- **Multi-Stakeholder Ethics Boards:** Create governance bodies with technical, legal, and domain representation to review high-risk systems.

- **Clear Accountability Paths:** Assign specific “owners” for model risk. Who goes to jail or pays the fine if the model discriminates? This must be defined in the org chart.

- **Procurement Controls:** Require vendors to provide transparency artifacts (Model Cards, Audit Reports) and contractual indemnities for AI failures.

#### 4. Security & Deepfake Defense

- **Zero-Trust Verification:** The *Hong Kong Deepfake* case proves that “human-in-the-loop” visual verification is obsolete.

- **Hardware-Based Authentication:** For high-value transactions, move beyond video calls. Require cryptographic verification (such as FIDO2 hardware keys) or adopt content provenance standards like **[C2PA](https://c2pa.org/)** (Coalition for Content Provenance and Authenticity) to digitally sign authentic media.

- **Duty of Care in Cybersecurity:** Update insurance policies and internal protocols to recognize that social engineering now possesses “perfect” mimicry capabilities.

#### 5. Post-Market Monitoring & Redress

- **Continuous Runtime Monitoring:** Deploy drift detection and incident logging. Fairness and safety metrics must be measured in production, not just in the lab.

- **Rapid Remediation Lanes:** Define a “Kill Switch.” Operational teams must know exactly how to pause, rollback, or hard-code overrides for a model that begins generating harm in real-time.

- **Transparency and Redress:** Publish clear complaint mechanisms. Users must have a way to challenge an automated decision and reach a human who has the authority to overturn it.

### Quick Practical Checklist (For Product Teams)

- [ ] **Run an EIA and Red-Team** exercise before public launch.

- [ ] **Create a Model Card** and Datasheet; attach both to procurement docs.

- [ ] **Implement “Guardrails”** that prevent the AI from making financial or policy commitments (prevents *Air Canada* scenarios).

- [ ] **Check Insurance Coverage:** Ensure your policy covers “Strict Liability” for software products under the new EU Product Liability Directive (2024/2853).

- [ ] **Establish a “Kill Switch”** protocol for rapid remediation.

- [ ] **Commission an External Audit** annually for high-impact systems.

**Selected further reading & sources:** *IEEE 7010; ACM Code of Ethics; Alan Turing Institute “Understanding AI Ethics and Safety” (2019); ISO/IEC TR 24368:2022; EU AI Act post-market provisions; * *OSTP Blueprint for an AI Bill of Rights; **[C2PA Technical Standard](https://c2pa.org/specifications/specifications/1.3/explainer/Explainer.html)**.*

## Conclusion

The examination of AI ethics failures provides crucial insights for the road ahead. We have transitioned from the “Wild West” era of 2016 to the “Strict Liability” era of 2026. As demonstrated in the landmark *[Moffatt v. Air Canada](https://www.google.com/search?q=https://www.canlii.org/en/bc/bccrt/doc/2024/2024bccrt149/2024bccrt149.html)* ruling, the defense that an AI is a “separate entity” is no longer valid in a court of law.

For organizations today, ethical AI is no longer just a matter of conscience; it is a matter of compliance. The lessons learned from these case studies—specifically regarding data provenance, hallucination control, and human oversight—must be baked into the technical architecture of every system before it ever touches a real-world user.

## References

- **Civil Resolution Tribunal.** (2024). *Moffatt v. Air Canada*, 2024 BCCRT 149.

- **European Parliament.** (2024). *Regulation (EU) 2024/1689 (The AI Act)*. Official Journal of the European Union.

- **Federal Trade Commission.** (2024). *Rite Aid Corporation & Effecting an Algorithmic Disgorgement*. Docket No. C-4809.

- **Floridi, L., & Cowls, J.** (2019). “A Unified Framework of Five Principles for AI in Society.” *Harvard Data Science Review*, 1(1).

- **Mittelstadt, B. D., et al.** (2016). “The Ethics of Algorithms: Mapping the Debate.” *Big Data & Society*, 3(2).

- **NIST.** (2019). *Face Recognition Vendor Test (FRVT) Part 3: Demographic Effects*. U.S. Department of Commerce.

- **Stanford HAI.** (2025). *Artificial Intelligence Index Report 2025*. Stanford University.

- **UNESCO.** (2021). *Recommendation on the Ethics of Artificial Intelligence*. Paris: UNESCO.

### 📚 Further Reading

For those interested in exploring similar themes, consider:

- [“Superintelligence” – Nick Bostrom](https://aviperera.com/superintelligence-nick-bostrom-book-summary-notes-highlights/) – it’s one of my all-time favourites

- [7 Essential Books on AI](https://aviperera.com/7-essential-books-on-ai-governance-every-leader-should-read/) – by the pioneers at the forefront of AI

- [Ethical Implications of AI in Warfare and Defence](https://aviperera.com/the-ethical-implications-of-ai-in-warfare-and-defence-a-comprehensive-perspective/) – very interesting read

---

*Citation: Perera, Avi. "AI Ethics Case Studies: Lessons Learned from Real-World Failures". aviperera.com, 2024. Web. <https://aviperera.com/ai-ethics-case-studies-lessons-learned-from-real-world-failures/>*
