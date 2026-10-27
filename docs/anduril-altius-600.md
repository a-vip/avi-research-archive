---
title: "Anduril Altius 600"
slug: "anduril-altius-600"
date: "2026-01-08T17:51:19"
author: "Avi Perera"
canonical_url: "https://aviperera.com/anduril-altius-600/"
source: "https://aviperera.com"
---

<link rel="canonical" href="https://aviperera.com/anduril-altius-600/" />

# Anduril Altius 600

> [!NOTE]
> **Canonical Source**: This dossier was authored by [Avi Perera](https://aviperera.com) and originally published at **[https://aviperera.com/anduril-altius-600/](https://aviperera.com/anduril-altius-600/)**.
> Published on `2026-01-08`.

---

# Anduril ALTIUS-600: Networked Loitering Munition, Lattice Autonomy and the Law of the Kill Chain

The ALTIUS-600 began as an air-launched effects platform developed by Area-I, a Georgia company that Anduril acquired in 2021 [1][2]. In 2022 Anduril added the ALTIUS-600M and 700M, purpose-built loitering munitions with high-explosive warheads, which its strategy chief Chris Brose described as the company’s first weapon [4]. The pitch is range, endurance and modularity: one airframe, many payloads, many launch platforms, many missions. The question for lawyers is what happens to human judgment when that flexibility is wrapped in software designed to act faster than a person can follow. This report sets out the verified facts, separates them from marketing, and tests them against the law as it stands in October 2026.

**Key findings**

- The ALTIUS-600 is a tube-launched, modular unmanned aircraft built by Anduril Industries, sold both as a reusable ISR and electronic warfare platform and, in its ALTIUS-600M form, as a loitering munition. It is in service, not a concept.

- Its defining feature is not the airframe but Lattice, the software that lets one operator task teams of drones that find, fix and strike. The strike decision is where the legal problem sits.

- Anduril says a human is always in the loop. Its own founder also describes a system that finds and hits targets through jamming. Both statements cannot describe the same terminal engagement without qualification.

- Ukrainian forces reportedly abandoned the system in 2024 after it failed against electronic warfare, while Taiwan has ordered more than 2,000 variants. The weapon is spreading faster than the evidence for its reliability.

- The CCW Seventh Review Conference opens on 16 November 2026. Systems like this one are the reason that meeting matters.

*

## Basic Weapon Facts

### I. Background

- **Manufacturer:** Anduril Industries (United States), through its Area-I acquisition [2]

- **Suppliers:** Unknown. Production is reported to be concentrated at an Anduril facility in Atlanta, Georgia [5]

- **Country of origin:** United States

- **Developmental stage:** Operational. Delivered to Taiwan (291 ALTIUS-600M, completed March 2026) [6][7]; a further contract for 1,554 ALTIUS-700M and 478 ALTIUS-600ISR was signed in August 2026 [6][8]; a UK-funded order of roughly 30 million pounds for Ukraine was announced in March 2025 [5]; US Special Operations Command has placed orders [2]

- **System version:** ALTIUS-600 (ISR and effects), ALTIUS-600M (loitering munition); the larger ALTIUS-700 and 700M share the architecture

- **System type:** Tube-launched, modular unmanned aircraft system; networked air-launched effect; loitering munition (600M)

### II. General Specifications

Published figures differ by variant and source, which matters for any weapons review. I list the conflicts rather than smooth them.

ParameterSpecificationEvidential statusSystem dimensionsUnknown; tube-launched with folding wingsNo official figures locatedWeightUp to about 12.2 kg (27 lb) for the 600 depending on payload; up to 29.5 kg (65 lb) for the 700Trade press citing Anduril [5]Max payloadModular payload up to about 3.2 kg (7 lb) for the 600 [2]; 600M warhead reported between 1.4 and 4 kg [5][6]; 700M warhead about 15 kg (33 lb), with a 35 lb warhead demonstrated [4][6]Sources conflictMax operating timeOver 4 hours (ISR configuration) [3][4]; about 1.5 hours as 600M munition and 1.25 hours as 700M [6]Configuration dependentMax operating distanceUp to 440 km (276 miles) in ISR configuration [3][4]; about 160 km as a munition [6]Configuration dependentMax speedUnknownNot published in sources reviewedLaunch platformsGround vehicles, ships, AC-130, UH-60, XQ-58A Valkyrie, MQ-1C Gray EagleAnduril and trial reports [2][3]

The earlier version of this entry listed 29.5 kg, a two-hour endurance and 400 km together. Those figures belong to different variants, and I have corrected them here.*

### III. Autonomy

**Autonomous targeting capabilities**

The ALTIUS family is software-defined and built on an open architecture, so mission software and payloads are interchangeable [3]. A single operator can task several aircraft through Lattice, Anduril’s command and control platform. At the US Army’s EDGE 23 demonstration, Anduril showed one operator directing a hunter and killer pair: an ALTIUS-600 carrying an ISR payload searched for signals of interest and an ALTIUS-600M loitering munition acted on what was found [3]. Anduril states that the family has demonstrated autonomous coordinated strike, target recognition and collaborative teaming [10].

The sensor fit is documented for the Taiwan sale. The strike variant is described as carrying full motion video and an infrared seeker and tracker, with resilient positioning, navigation and timing and communications, and the reconnaissance variant carries an electro-optical and long-wave infrared camera [9]. Anduril has not published the classification algorithms, the training data, the confidence thresholds or the test results behind target recognition.

Three features of the public account warrant forensic attention.

**The jamming paradox.** Luckey has described the onboard Lattice software as able to look for targets, identify them and fly into them even when the aircraft is being jammed [11]. That is a capability for operating without a human link. Anduril’s executive Brian Schimpf says the technology is not about taking humans out of the loop [11], and Luckey says all of the company’s weapons have a kill switch [12] and that nothing makes life or death decisions without a directly responsible person [13]. These are reconcilable only if the human decision is taken before launch, on a target set, and the machine selects the individual object afterwards. If a link exists, a human may veto. If it is severed, which is the scenario the jamming resistance is designed for, there is no veto. I regard any claim of meaningful human control that fails to say which of these two situations it describes as incomplete.

**The Ukrainian lesson was learned backwards.** The Wall Street Journal reported in November 2025 that ALTIUS drones used by Ukraine’s SBU security service lost communications, crashed and missed targets under Russian electronic warfare, and were taken out of use in 2024 [15][16]. Anduril answered that it fails often as part of fast iteration, and in its words, “We do fail… a lot” [16]. The commercial response to jamming vulnerability is more onboard autonomy, because an aircraft that does not depend on a link cannot be jammed off it. That is a sound engineering instinct and the most legally dangerous design pressure in the field. Each increment of jamming resilience is an increment of removed human oversight.

**The control problem is a software update.** The Lieber Institute at West Point notes that Anduril’s autonomy stack, which on its Fury aircraft already classifies and prioritises targets under human supervision, could be shifted to engagement with minimal human input through software change, and that the company treats its machine learning weights as commercial crown jewels, which impedes outside legal review [14]. An architecture whose human involvement is a configuration setting offers no structural guarantee. I have said on my [AI stance page](https://aviperera.com/stance/) that meaningful human control is an architecture, not a button, and a firmware option is the opposite of architecture.

On evidence of performance, Taiwan reports a perfect hit rate for ALTIUS-600M against maritime targets in a June 2026 live-fire exercise [8]. A scripted exercise at sea against known targets in permissive conditions tells us almost nothing about misidentification risk in a contested littoral. Ukraine tells us more.

Under US policy, Directive 3000.09 treats homing munitions that engage targets selected by a human operator as semi-autonomous, and systems that select and engage targets without further operator intervention as autonomous, requiring senior review [29]. Which side of that line a given ALTIUS mission falls on depends on mission software settings that are not public. The Department does not publish what it has reviewed [29].

## Strategic and technological context

I compare this system with the P.S. Killer in my [earlier report](https://aviperera.com/p-s-killer-kamikaze-drone/) deliberately. The PSK is a prototype whose autonomy claims rest on a founder’s interviews. The ALTIUS is the finished version of the same idea, with funded contracts, combat use and a software ecosystem behind it. What has changed since the first generation of loitering munitions, such as the Harpy, is the move from a single-purpose weapon to a networked, reconfigurable one whose lethality is a matter of software and payload choice. The same fuselage is a reconnaissance asset in the morning and a munition in the afternoon. This undermines weapons review, which was designed to assess a weapon as a fixed object.

The model of development also differs. Anduril builds at its own financial risk, ships fast and iterates in the field [7][16]. That works for consumer software. The WSJ reported that during tests more than a dozen drone boats running Lattice shut down in a US Navy exercise and that a counter-drone trial caused a 22 acre fire [16]. These are the failures that became public. When the cost of a bug is a hospital, a ferry or a surrendering soldier, the culture of “fail often, learn quickly” transfers the learning cost to people who did not consent to the experiment.

Expansion continues regardless. Australia has tested launching ALTIUS drones from the Ghost Shark underwater vehicle [18], and the family is being fitted to platforms from helicopters to uncrewed aircraft [2]. Anduril’s position is also a political one. China imposed sanctions on the company in July 2024, including visa bans and asset freezes, over its role in arms sales to Taiwan [17].

## Legal analysis

### Baseline rules and weapons review

No treaty prohibits loitering munitions or autonomy as such. Their use is governed by the principles of distinction, proportionality and precaution in attack, set out in [Additional Protocol I](https://ihl-databases.icrc.org/en/ihl-treaties/api-1977) at Articles 48, 51, 52 and 57 [19] and recognised as [customary law](https://ihl-databases.icrc.org/en/customary-ihl/v1/rule15) [21]. The ICJ has called the distinction between combatants and civilians a cardinal principle of humanitarian law [22]. [Article 36](https://ihl-databases.icrc.org/en/ihl-treaties/api-1977/article-36) requires parties to review new weapons and methods [20]. The United States is not a party to the Protocol but reviews weapons under its own policy and the 2023 text of Directive 3000.09 [29]. Taiwan sits outside the United Nations treaty system and is not a CCW party, so the legal accountability of the supplier and the user falls back on customary law and domestic regimes.

The weakness of review is evident. It is classified, it assesses the weapon as delivered, and the weapon is software that can be updated after delivery. A review that blesses version 1.0 says little about the mission set loaded in the field.

### Distinction, proportionality and precautions

As an anti-armour munition the ALTIUS-700M raises conventional questions. The harder case is the maritime role for which Taiwan is buying the 600M. Warships are lawful objectives. Fishing boats, coast guard vessels, ferries and the so-called maritime militia are not so easily classified, and a requisitioned civilian roll-on roll-off ferry is a military objective only when its use makes an effective contribution to military action and its destruction offers a definite military advantage under Article 52(2) [19]. Infrared and visual classification can estimate hull shape and thermal signature. It cannot determine whether a vessel carries troops or families. Article 50(1) requires doubt to be resolved in favour of civilian status [19]. A system that must decide in seconds, possibly cut off from the operator, has no mechanism for doubt.

Proportionality under Article 51(5)(b) is assessed on the information reasonably available to the decision maker. The ICTY Trial Chamber in [Prosecutor v Galić](https://www.icty.org/en/case/galic) framed the test by reference to a reasonably well informed person in the circumstances of the perpetrator [23]. With a loitering munition the relevant moment is the strike, perhaps ninety minutes after launch. Article 57(2)(b) requires an attack to be cancelled or suspended if it becomes apparent that the target is not a military objective [19]. Cancellation requires a functioning link, and Anduril advertises resilience to the very jamming that severs it.

### Responsibility, transfer and the supplier

Criminal liability for an unlawful strike requires a human with the requisite intent and knowledge under the [Rome Statute](https://www.icc-cpi.int/sites/default/files/RS-Eng.pdf), at Articles 25, 28 and 30 [24]. An operator who selects a target class and launches may lack the knowledge of the specific engagement. Superior responsibility presupposes subordinates who are human. I have called this the accountability gap, and a drone team that hunts and strikes with one operator widens it.

Transfer law is the better available lever. Under Common Article 1 of the Geneva Conventions, states undertake to ensure respect for the Conventions, which the ICJ treated as reflecting a general principle in [Nicaragua v United States](https://www.icj-cij.org/case/70) [25]. The ILC Articles on State Responsibility, at Article 16, make a state responsible for knowingly aiding an internationally wrongful act [26]. The Arms Trade Treaty requires an assessment of the risk that arms will be used to violate humanitarian law before authorisation, at Articles 6 and 7 [28]. The United States signed the treaty in 2013 and later announced that it would not ratify. In domestic courts the leading authority is [R (Campaign Against Arms Trade) v Secretary of State for International Trade](https://www.bailii.org/ew/cases/EWCA/Civ/2019/1020.html) [2019] EWCA Civ 1020, where the Court of Appeal held UK licensing decisions unlawful because the government had not assessed past violations [27]. The UK-funded ALTIUS order for Ukraine [5] is exactly the type of transfer to which that reasoning applies.

Export control adds a complication. On the manufacturer’s published ISR range of 440 km, the unarmed ALTIUS-600 appears to exceed the 300 km threshold that brings uncrewed aircraft within Category II of the Missile Technology Control Regime, while the same airframe as a 160 km munition does not. A weapon whose legal category changes with its payload is a weapon that is hard to control by treaty.

## International relations and the state of play

The Taiwan sales are the centre of gravity. Taipei took delivery of its first ALTIUS-600M in August 2025 [7], completed delivery of 291 in March 2026 [6], and in August 2026 signed an approximately 26.9 billion New Taiwan dollar contract for 1,554 ALTIUS-700M and 478 reconnaissance aircraft, with deliveries running to June 2033 [6][8]. The logic is asymmetric: cheap, mass, expendable strike against a larger navy. I understand the strategic reasoning of a small democracy facing a state that openly refuses to renounce force. I also note that the weapon being relied on has a documented record of failure against a peer electronic warfare opponent [15][16]. China’s electronic warfare capability is no less developed than Russia’s. Taiwan is buying confidence and receiving an unproven kill chain, and the cost of misplaced confidence in a Strait crisis is escalation.

There is a second, regional effect. Every large transfer of a software defined, exportable strike drone normalises the category. States across Southeast Asia and the Indo-Pacific watch what Washington sells and what it tolerates, and procure accordingly. The strongest norm against autonomy is a norm of restraint among the main developers, and an American system showcased as a model of autonomous strike weakens it.

Multilateral law is at a decision point. The CCW Group of Governmental Experts on lethal autonomous weapons systems adopted a consensus report on 5 September 2026, which the chair called “the end of the beginning” [33]. Human Rights Watch reports that 70 High Contracting Parties, a majority, support moving to negotiations, though the final report does not fully reflect that progress [32]. The ICRC has urged the prohibition of unpredictable autonomous weapons and those that target people directly, citing the success of the 1995 Protocol IV on blinding lasers [35]. The EU Council has called for an ambitious negotiating mandate [37]. Over 160 states voted for UN General Assembly Resolution [79/62](https://docs.un.org/en/A/RES/79/62) in December 2024 [38]. The Seventh Review Conference meets in Geneva from 16 to 20 November 2026 [34]. The Lieber Institute describes the United States and Russia as leading states that maintain that existing humanitarian law and weapons review are enough [36], and press accounts suggest the final text was weakened under their pressure, a detail I would confirm against the official record.

Washington’s domestic course is moving in the other direction. National Security Presidential Memorandum 11 of 5 June 2026 ordered a rewrite of Directive 3000.09 within 90 days, with annual review [30]. Senator Ruben Gallego has warned that compressing testing and reducing safeguards risks friendly fire and civilian harm [31]. As far as I could establish on 27 October 2026, no revised directive has been published. A government that has told its own department to remove barriers to rapid deployment cannot also be trusted to lead a global effort to restrain deployment.

## My assessment

I do not dismiss the ALTIUS as a toy or a scam. It is a serious system built by a serious company, and parts of it, such as networked ISR, communications relay and counter-drone work, raise manageable questions. My objection is to the specific bundling of three things: a strike capability, an autonomy stack that is proprietary and unreviewable, and a business model that treats field failure as acceptable cost. Taken together they place a lethal decision inside software that nobody outside the company can audit, in a conflict where the consequence of error falls on third parties.

I take no comfort from the phrase “human in the loop”. I set out on my [stance page](https://aviperera.com/stance/) why presence without comprehension, time and authority is legal cover for autonomous action. The ALTIUS record shows why this is not abstract. Luckey tells the public that a person is responsible while describing a weapon that must function when that person cannot reach it. That is a contradiction at the heart of the marketing, and journalists, regulators and treaty negotiators should keep asking which of the two is true.

There is a serious counter-argument and I will state it fairly. Autonomous terminal guidance may reduce the death toll among soldiers, may defeat jamming that would otherwise render cheap weapons useless, and, against armour in an empty field, may be more precise than artillery. Anduril and its supporters say the alternative is that less scrupulous states build worse systems [13]. That argument has force against a ban on autonomy and none against rules. It does not answer the demand for published test data, independent legal review, a hard prohibition on autonomous selection of persons, an auditable record of every human decision in the engagement, and a requirement that no weapon be exported whose human control depends on a link the user expects to lose. I made this case at the [UNIDIR conference in Geneva](https://aviperera.com/my-story/) and in my work with the Campaign to Stop Killer Robots. The fact that a major supplier can tell me its weapon always has a human in the loop, while selling the feature that it works without one, is why we need a treaty and not a pledge. See also my analysis of [AI safety](https://aviperera.com/aisafety/) and the [AI Policy Tracker](https://aviperera.com/ai-policy-tracker/).

## Frequently asked questions

**What is the Anduril ALTIUS-600?** A tube-launched modular uncrewed aircraft made by Anduril Industries, used for reconnaissance, electronic warfare and communications relay, with an ALTIUS-600M loitering munition variant [3][4].

**Is the ALTIUS-600M autonomous?** It is autonomous in navigation and, according to Anduril, in target recognition and coordinated strike, with human supervision described as present. The extent of human control after launch in a jammed environment is not publicly specified [10][11].

**Who uses the ALTIUS?** Taiwan has taken delivery of 291 ALTIUS-600M and ordered 1,554 ALTIUS-700M, Ukraine received UK-funded systems, and US forces have placed orders [2][5][6].

**Did it work in Ukraine?** The Wall Street Journal reported that SBU units stopped using it in 2024 after failures under electronic warfare, which Anduril disputes as a complete picture [15][16].

**Is it legal?** No treaty bans it. Lawfulness depends on use and on compliance with distinction, proportionality and precautions [19][22].

**Will international law change?** The CCW Review Conference, 16 to 20 November 2026, can authorise negotiation of a binding instrument [34].

## Sources

**Manufacturer website:** [anduril.com/hardware/altius](https://www.anduril.com/hardware/altius/)

**News reports and technical documentation**

- Anduril, [Area-I, an Anduril Company, Unveils the ALTIUS 700](https://blog.anduril.com/area-i-an-anduril-company-unveils-the-altius-700-2b8e856d48b5).

- Andreas Parsch, [Directory of U.S. Military Rockets and Missiles: Anduril ALTIUS](https://designation-systems.net/dusrm/app4/altius.html), Designation-Systems.net.

- The War Zone, [Our First Look At The ALTIUS-700M Loitering Munition Obliterating A Target](https://twz.com/air/our-first-look-at-the-altius-700m-loitering-munition-obliterating-a-target).

- Breaking Defense, [Meet Anduril’s new loitering munitions, the firm’s first (but not last) weapons program](https://breakingdefense.com/2022/10/meet-andurils-new-loitering-munitions-the-firms-first-but-not-last-weapons-program/), October 2022.

- Euro-SD, [UK to supply Ukraine with Anduril ALTIUS loitering munitions](https://euro-sd.com/?p=42958), March 2025.

- The Defense Post, [Taiwan to Acquire More Than 2,000 Altius Drones From Anduril](https://thedefensepost.com/2026/08/28/taiwan-acquires-anduril-altius/), 28 August 2026.

- Janes, [Taiwan acquires first batch of Altius-600M loitering munitions](https://www.janes.com/osint-insights/defence-news/defence/taiwan-acquires-first-batch-of-altius-600m-loitering-munitions).

- Taiwan News, [Taiwan signs contract for Altius-700M and Altius-600ISR drones](https://www.taiwannews.com.tw/news/6428878), August 2026.

- NOWnews, [DSCA notification summary of the ALTIUS-700M and ALTIUS-600 sale to Taiwan](https://www.nownews.com/news/6766262).

- Anduril, [Anduril Announces Best In Class Loitering Munition](https://blog.anduril.com/anduril-announces-best-in-class-loitering-munition-8b00a72aba2a).

- NPR, [Interview with Palmer Luckey and Brian Schimpf on AI drones for Ukraine](https://www.npr.org/transcripts/1198912876).

- CBS News, [Palmer Luckey wants to remake the U.S. military with autonomous weapons](https://www.cbsnews.com/news/palmer-luckey-future-warfare-anduril-60-minutes), 60 Minutes.

- SmartCompany, [Anduril founder Palmer Luckey on military tech](https://www.smartcompany.com.au/startupsmart/news/anduril-founder-palmer-luckey-military-tech/).

- Lieber Institute, West Point, [Diverging Standards in the Legal Review of LAWS](https://lieber.westpoint.edu/?p=33983).

- Militarnyi, [SSU Abandons Altius Attack Drones after Failures at Front](https://militarnyi.com/en/news/ssu-abandons-altius-attack-drones-after-failures-at-front/).

- Sherwood News, [WSJ: Anduril’s weapons systems have failed during several tests](https://sherwood.news/tech/wsj-andurils-weapons-systems-have-failed-during-several-tests/), reporting The Wall Street Journal, November 2025.

- Militaer Aktuell, [Taiwan receives loitering ammunition from Anduril](https://militaeraktuell.at/en/taiwan-receives-loitering-ammunition-from-anduril/).

- Defence Network, [Ghost Shark launches Altius drones in sea test](https://defence-network.com/dsq0).

**Law, cases and legal documentation**

- [Additional Protocol I to the Geneva Conventions, 1977](https://ihl-databases.icrc.org/en/ihl-treaties/api-1977), Articles 1(2), 36, 48 to 52, 57.

- [Article 36, New weapons](https://ihl-databases.icrc.org/en/ihl-treaties/api-1977/article-36), ICRC IHL Databases.

- ICRC, [Customary IHL, Rule 15: Principle of precautions in attack](https://ihl-databases.icrc.org/en/customary-ihl/v1/rule15).

- ICJ, [Legality of the Threat or Use of Nuclear Weapons, Advisory Opinion](https://www.icj-cij.org/case/95), 1996, paragraph 78.

- ICTY, [Prosecutor v Galić](https://www.icty.org/en/case/galic), IT-98-29.

- [Rome Statute of the International Criminal Court](https://www.icc-cpi.int/sites/default/files/RS-Eng.pdf), Articles 8, 25, 28, 30.

- ICJ, [Military and Paramilitary Activities in and against Nicaragua (Nicaragua v United States)](https://www.icj-cij.org/case/70), Merits, 1986.

- International Law Commission, [Articles on Responsibility of States for Internationally Wrongful Acts](https://legal.un.org/ilc/texts/instruments/english/draft_articles/9_6_2001.pdf), 2001, Article 16.

- [R (Campaign Against Arms Trade) v Secretary of State for International Trade [2019] EWCA Civ 1020](https://www.bailii.org/ew/cases/EWCA/Civ/2019/1020.html).

- [Arms Trade Treaty](https://thearmstradetreaty.org), Articles 6 and 7.

- US Congressional Research Service, [Defense Primer: Lethal Autonomous Weapon Systems (IF11150)](https://www.congress.gov/crs-product/IF11150); DoD Directive 3000.09, 25 January 2023.

- The White House, [National Security Presidential Memorandum 11](https://www.whitehouse.gov/presidential-actions/2026/06/national-security-presidential-memorandum-nspm-11/), 5 June 2026.

- DefenseScoop, [Senator questions Pentagon’s plan to revise autonomous weapons policy](https://defensescoop.com/2026/06/15/lawmaker-questions-pentagons-plan-to-revise-autonomous-weapons-policy/), 15 June 2026.

- Human Rights Watch, [UN Talks on Killer Robots End with Calls for Negotiations Growing](https://www.hrw.org/news/2026/09/07/un-talks-on-killer-robots-end-with-calls-for-negotiations-growing), 7 September 2026.

- Opinio Juris, [Symposium on the CCW GGE LAWS: The End of the Beginning](https://opiniojuris.org/2026/10/05/symposium-on-the-ccw-gge-laws-the-end-of-the-beginning-an-introduction/), 5 October 2026.

- Janes, [Special Report: Autonomous weapons talks advance, but verification obstacles remain](https://www.janes.com/defence-intelligence-insights/defence-news/air/special-report-autonomous-weapons-talks-advance-but-verification-obstacles-remain), October 2026.

- ICRC, [Advocacy paper: A key opportunity to prevent the development of unacceptable autonomous weapons](https://www.icrc.org/en/article/advocacy-paper-key-opportunity-prevent-development-unacceptable-autonomous-weapons), June 2026.

- Lieber Institute, West Point, [No New Rules Needed: Russia’s Minimalist Vision of Human Oversight for LAWS](https://lieber.westpoint.edu/?p=37883), April 2026.

- Council of the European Union, [Council Conclusions on the Seventh Review Conference of the CCW](https://data.consilium.europa.eu/doc/document/ST-14436-2026-INIT/en/pdf), 13 October 2026.

- UN General Assembly, [Resolution 79/62 on lethal autonomous weapons systems](https://docs.un.org/en/A/RES/79/62), December 2024.

---

*Citation: Perera, Avi. "Anduril Altius 600". aviperera.com, 2026. Web. <https://aviperera.com/anduril-altius-600/>*
