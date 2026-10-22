---
title: "Vision 60 Q-UGV"
slug: "vision-60-q-ugv"
date: "2026-10-10T07:10:00"
author: "Avi Perera"
canonical_url: "https://aviperera.com/vision-60-q-ugv/"
source: "https://aviperera.com"
---

<link rel="canonical" href="https://aviperera.com/vision-60-q-ugv/" />

# Vision 60 Q-UGV

> [!NOTE]
> **Canonical Source**: This dossier was authored by [Avi Perera](https://aviperera.com) and originally published at **[https://aviperera.com/vision-60-q-ugv/](https://aviperera.com/vision-60-q-ugv/)**.
> Published on `2026-10-10`.

---

## Vision 60 Q-UGV: Technical Dossier and Legal Analysis

The **Vision 60** is a four-legged unmanned ground vehicle built by Ghost Robotics of Philadelphia. The company describes it as a mid-sized, high-endurance, all-weather ground drone for unstructured urban and natural environments, serving defense, homeland and enterprise customers. In its standard form it is a patrol and reconnaissance robot. It becomes a weapons system when a customer bolts a weapon to it, and several customers have. In 2021 it appeared at the Association of the US Army convention carrying the SPUR, a ten-shot 6.5 mm Creedmoor rifle with a 30x thermal and electro-optical scope. I have included it in this database because it shows how autonomy enters warfare: by modular integration, one payload at a time, with the legal burden quietly shifting from the manufacturer to whoever fits the weapon. [dronenerds](https://enterprise.dronenerds.com/vision-60), [aljundi](https://aljundi.ae/?p=21408)

### Key takeaways

- The base Vision 60 is not a weapon. Its armed variants are, so legal responsibility depends on the payload and on who integrates it.

- Ghost Robotics’ CEO has said the SPUR rifle is fully controlled by a remote operator, with no autonomy or AI. An AI-enabled, rifle-armed variant shown at the US Army’s Operation Hard Kill reportedly aimed autonomously. The line between those two claims is where the legal question sits. [siliconcanals](https://siliconcanals.com/ghost-robotics-robot-gets-rifle/)[thedefensepost](https://gecici.thedefensepost.com/?p=82860)

- Ghost Robotics declined to sign the industry pledge not to weaponise general-purpose robots, which sets it apart from most of its competitors. [billypenn](https://billypenn.com/?p=198807)

- A South Korean defence group, LIG Nex1, now holds 60 percent of the company. [technical](https://technical.ly/startups/ghost-robotics-acquisition-lig-nex-1/)

- The CCW Seventh Review Conference meets in Geneva from 16 to 20 November 2026. Ground robots like this one are part of what it must decide. [reachingcriticalwill](https://reachingcriticalwill.org/disarmament-fora/ccw/2025/hcp/ccw-report/18087-ccw-report-vol-13-no-5)

*

### Basic Weapon Facts

#### I. Background

FieldDetailManufacturerGhost Robotics Corporation (Philadelphia, USA). LIG Nex1 acquired a 60 percent controlling stake in a $240 million deal that valued the company at $400 million.SuppliersNVIDIA (Xavier compute module), SWORD Defense Systems (SPUR rifle), Teledyne FLIR (thermal camera in the SPUR). Full supplier list: UnknownCountry of originUnited States. Controlling ownership: South KoreaDevelopmental stageOperational and commercially available. The manufacturer reports more than 25 national security customers and more than 1,000 robots shipped.System versionVision 60 Version 5.4 (model VS60-R5400). Armed variant: SPUR MOD 0 integrationSystem typeQuadrupedal unmanned ground vehicle (Q-UGV). Modular platform for ISR, perimeter security and, in some configurations, weapons [technical](https://technical.ly/startups/ghost-robotics-acquisition-lig-nex-1/)[ghostrobotics](https://ghostrobotics.io/robots)

#### II. General Specifications

ParameterSpecificationSystem dimensionsUnknown (not stated in the sources I could verify)Weight51 kg (112 lb)Max payload10 kg (22 lb) per the manufacturer, with user-selectable payload compensation. Early press coverage in 2021 cited about 31 lbMax operating timeAbout 3.15 hours of continuous walking at 0.9 m/s, or about 21 hours on standbyMax operating distance/reach10 km, dependent on terrain and payload. Control link range: UnknownMax speedSprint of 3 m/s (about 6.7 mph) in earlier specifications. The current manufacturer page states up to 2.5 m/s (5.6 mph), dependent on payload and terrain.Environmental ratingIP67, with an operating range of about minus 40 to 55 degrees CelsiusUnit costReported figures vary from about $100,000 to about $200,000 depending on configuration [Vision 60 statistics +5](https://ghostrobotics.io/robots)

Two data quality notes for the database. Some trade coverage lists a “max power runtime of 15 minutes”, but the manufacturer’s figures show 15 minutes as the assembly and disassembly time, so I have treated the runtime figure as a transcription error. Speed and payload figures have also moved between 2021 and today, which suggests either design changes or more conservative marketing.*

*

### Origins and operational history

Ghost Robotics is a University of Pennsylvania spinout founded in 2015. The Vision 60 is its flagship, and its commercial pitch rests on a locomotion controller that the company calls blind mode, designed so the robot keeps moving when its vision sensors degrade or when it slips or falls.

The deployment record is mostly mundane, which is part of why it matters.

**Base security.** Four Vision 60s joined security patrols at Tyndall Air Force Base in Florida, where airmen train them on routes and can take over through a virtual reality headset. The Air Force later bought them to monitor base perimeters, and the Department of Homeland Security tested them for border use. [freethink](https://www.freethink.com/articles/robot-dogs?amp=1)[billypenn](https://billypenn.com/?p=198807)

**Allied customers.** Japan’s Ministry of Defence secured funding in its 2023 budget for six units for perimeter security, and South Korea is another customer. Reporting also records deployment by the British and US governments. The US and Australian armies have tested the armed configuration. [gbp.com.sg +2](https://gbp.com.sg/?p=46907)

**Training and exercises.** The US Army used a Ghost Robotics quadruped in urban assault training at Fort Irwin in March 2024. [billypenn](https://billypenn.com/?p=198807)

**The armed variants.** At Operation Hard Kill at Fort Drum in 2024 the Army showed a Vision 60 with an AR-15-type rifle on a small turret and an electro-optical targeting system, reportedly as an anti-drone system. The same report says the demonstration came nearly three months after China showed its own weapon-carrying robot dog at the start of a joint exercise with Cambodia. I treat that sequencing as an arms race signal, with the caveat that both were demonstrations and neither is evidence of combat use. [thedefensepost](https://gecici.thedefensepost.com/?p=82860), [thedefensepost](https://gecici.thedefensepost.com/?p=82860)

**Corporate and political events.** The LIG Nex1 acquisition coincided with protests against Ghost Robotics’ sales to government militaries including Israel. Boston Dynamics sued Ghost over patents, and the dispute was reported settled in 2025. [technical](https://technical.ly/startups/ghost-robotics-acquisition-lig-nex-1/)

### Autonomy: a forensic analysis

**Sensors.** The standard configuration includes a 32-beam LiDAR and a low-light camera. The manufacturer’s Mission Control platform supports fully autonomous operation in GPS-enabled and GPS-denied environments using real-time 3D LiDAR SLAM mapping. The compute module is an NVIDIA Xavier, a processor class built for onboard machine vision. The SPUR payload adds a Teledyne FLIR Boson thermal camera with 30x zoom, and a remote safe, chamber, clear and fire capability so the operator can load and make the weapon safe at a distance. [umbc](https://cypress.umbc.edu/testbed/trace/trace-testbed-design/ghostrobotics-vision60-qugv)[siliconcanals](https://siliconcanals.com/ghost-robotics-robot-gets-rifle/)

**Algorithms.** The autonomy that is publicly documented concerns movement: route following, obstacle avoidance, terrain assessment and mapping. Targeting autonomy is where the record is thinner and more contested. Reporting on the Hard Kill demonstration says the rifle-armed robot manoeuvred and aimed its AI-enabled weapon autonomously. That report does not say who or what authorised firing. Early commentary on the SPUR drew the same line: a system like this could line up a shot and compute a firing solution without being able to open fire. I regard that distinction as thin in practice. An aiming system that selects and tracks a target has done most of the cognitive work, and the human is left to confirm. [thedefensepost](https://gecici.thedefensepost.com/?p=82860)[Yahoo News](https://news.yahoo.com/welp-now-robo-dogs-sniper-130800576.html)

**Human intervention in the kill chain.** For the SPUR, the maker and integrator state that a trained service member must operate it from a ground control station over a secured wireless link, and that it cannot engage without a human in the loop. I have no basis to doubt that account for the configuration they describe. I would still ask the questions I put to any system claiming human control. How much time does the operator have? Can they see enough to judge distinction? What does the interface recommend before they decide? None of that is public. [mobilityengineeringtech](https://www.mobilityengineeringtech.com/component/content/article/40865-robotic-rifle)

**Classification.** On the public record the Vision 60 is a remotely operated platform with autonomous mobility, and it is not a lethal autonomous weapon system as the CCW process uses the term. I list it because it has everything a successor would need. It has mobility that works without GPS, compute capable of onboard perception, a standard payload interface and a customer base already weaponising it. The only missing ingredient is a policy decision to remove the operator, and as I argue on my [stance page](https://aviperera.com/stance/), policy decisions of that kind tend to be made under operational pressure. Compare the aerial case in my [MQ-28 Ghost Bat entry](https://aviperera.com/mq-28-ghost-bat/), and the Korean and Chinese ground systems in the database, [Hanwha Arion-SMET](https://aviperera.com/hanwha-arion-smet/) and [Norinco Sharp Claw](https://aviperera.com/norinco-sharp-claw/). For a rifle fire control comparison see [SMASH 2000](https://aviperera.com/smash-2000/).

### Legal analysis

#### Weapons review and the modular problem

[Article 36 of Additional Protocol I](https://ihl-databases.icrc.org/en/ihl-treaties/api-1977) requires states parties to determine whether a new weapon, means or method of warfare would be prohibited. The United States is not a party to the Protocol but conducts its own legal reviews as a matter of policy, and Department of Defense Directive 3000.09 (updated January 2023) sets senior review requirements for autonomous and semi-autonomous weapon systems. The Vision 60 exposes a structural weakness in this model. The manufacturer ships a legal, general-purpose robot, and the integrator mounts a weapon. Each party can point to the other. No public review of any armed Vision 60 configuration exists, and a review of the platform alone would miss the point. The ICRC’s [guide to weapons reviews](https://shop.icrc.org/a-guide-to-the-legal-review-of-new-weapons-means-and-methods-of-warfare-measures-to-implement-article-36-of-additional-protocol-i-of-1977-pdf-en.html) is clear that the reviewed object is the weapon as configured and used.

#### Distinction, proportionality and precautions

A rifle-armed legged robot is built for ground combat at close range, and that is the setting where [Articles 48, 51 and 57](https://ihl-databases.icrc.org/en/ihl-treaties/api-1977) are hardest to apply. A sniper platform engages from a distance through a scope, with a narrow field of view and no peripheral awareness, so the operator sees the target and little else. Article 41 protects anyone who is hors de combat, including those who have clearly surrendered, and signs of surrender are subtle, contextual and easily missed on a screen. The risk compounds if an algorithm cues the operator to a target before human judgment engages. I explain the general problem with automation bias in my piece on [meaningful human control](https://aviperera.com/meaningful-human-control-autonomous-weapons/).

#### Case law that frames the problem

**Prosecutor v. Galić (ICTY, 2003).** The Tribunal convicted a Bosnian Serb corps commander for a campaign of sniping and shelling against civilians in Sarajevo. I raise it because sniping is the archetype of precise, deliberate fire where responsibility is easy to assign, and a robot sniper tests whether it still is. Command responsibility under Article 28 of the Rome Statute would still apply to superiors, but the attribution chain gets longer.

**Public Committee Against Torture in Israel v. Government of Israel, HCJ 769/02 (2006).** The Israeli Supreme Court’s targeted killing judgment applied strict conditions to attacks on individuals, including verification and proportionality. It matters here because it shows courts accepting that remote precise force is lawful only under demanding evidentiary standards.

**Legality of the Threat or Use of Nuclear Weapons, ICJ Advisory Opinion (1996).** The Court confirmed that distinction and the prohibition on unnecessary suffering are cardinal principles of humanitarian law, which constrain every means of warfare whatever its novelty.

**R (Campaign Against Arms Trade) v. Secretary of State for International Trade [2019] EWCA Civ 1020.** The Court of Appeal found a UK arms export licensing process unlawful for failing to assess past violations of humanitarian law. It is relevant because Vision 60 exports, with a Korean parent and US manufacturing, will face the same scrutiny under the [Arms Trade Treaty](https://thearmstreaty.org), whose Articles 6 and 7 require export assessments. South Korea is a party. The United States is not.

#### Law enforcement and border use

The robots’ homeland security uses engage human rights law and the UN [Basic Principles on the Use of Force and Firearms by Law Enforcement Officials](https://www.ohchr.org/en/instruments-mechanisms/instruments/basic-principles-use-force-and-firearms-law-enforcement), which require necessity and proportionality for any use of force against a person. The 2016 Dallas incident, where police used a bomb disposal robot to kill a suspect, showed how quickly a tool bought for one purpose can be repurposed. As of mid 2026 no armed robot dogs are reported deployed in US policing, but I regard that as a policy position and not a legal barrier. [robozaps](https://blog.robozaps.com/b/police-military-robot-dogs)

#### Corporate responsibility

The 2022 open letter by several robotics firms pledged not to weaponise their advanced mobility robots or support others in doing so. Ghost Robotics did not sign. A pledge is voluntary, but the [UN Guiding Principles on Business and Human Rights](https://www.ohchr.org/en/publications/reference-publications/guiding-principles-business-and-human-rights) expect companies to prevent adverse human rights impacts linked to their products. I discuss the wider accountability gap in AI companies on my [stance page](https://aviperera.com/stance/). [taskandpurpose](https://taskandpurpose.com/tech-tactics/dont-arm-robot-dogs.md), [billypenn](https://billypenn.com/?p=198807)

### International relations implications

**Allied supply chains and control.** A US-designed system is now majority owned by a South Korean defence group and sold to Japan, with US forces as the anchor customer. That is a useful case study in how autonomy-related technology moves among allies faster than the control regimes meant to govern it. Questions of who sets end-use conditions, who audits them and which export law applies are unresolved in public.

**Proliferation and cost.** The Vision 60 costs roughly a hundred to two hundred thousand dollars. Chinese quadrupeds from Unitree and Deep Robotics are reported to cost around a tenth as much, although that comes from a lower quality secondary source and I would verify it before relying on it. Cheap, mass-produced legged platforms are within reach of any state and many non-state actors, and weaponising them requires only a rifle mount and a link. [robozaps](https://blog.robozaps.com/b/police-military-robot-dogs)

**Normalisation.** The robot dog is an unusually effective piece of public relations. It looks friendly, it appears at base gates and in exercises, and it habituates the public and the military to ground robots operating among people. I do not think the aesthetic is accidental, and I do not think it is harmless. Normalisation precedes regulation, and the weapons that follow arrive in a world already used to the platform.

**Contested norms at the CCW.** On 5 September 2026 the CCW Group of Governmental Experts reached consensus among 128 states on a document addressing lethal autonomous weapons, though critics argue major military powers weakened it. France says the text clarifies human control and judgment and that the Review Conference must decide next steps. The UN Secretary General and the ICRC jointly called on 25 August for the November conference to begin binding negotiations, and the ICRC argues the Review Conference should launch negotiations on a new protocol. Modular ground robots are exactly the case a definition based on “fully autonomous” systems would miss, because they become autonomous by software update, and that is why I press for a standard centred on human control over individual engagements, as I set out in [my AI stance](https://aviperera.com/stance/). [States reach agreement on autonomous weapons regulations in Geneva +3](https://cryptobriefing.com/autonomous-weapons-agreement-geneva/)

**Sovereignty and the Global South.** Ground robots are designed for urban combat, so their human cost will fall on cities. I return again to the point I make in my research on the Anticipatory Objection Registry: states likely to host such conflicts should record their legal objections early, before permissive norms form around practice they had no part in shaping.

### My assessment

I find the Vision 60 harder to write about than a missile, because the system is so ordinary. It patrols fences. It walks stairs. It was built to spare people from dangerous work, and I accept that this is a real benefit. It is also the cleanest example in this database of how responsibility dissolves in modular design. The manufacturer built a general platform, the integrator mounted a rifle, the customer wrote the rules of engagement, and a software update can move the operator out of the loop. At every step someone can say the decision belonged elsewhere.

My position, set out on my [stance page](https://aviperera.com/stance/), is that meaningful human control has to be designed in, specified by law and attached to identifiable people, and that it cannot be retrofitted onto a platform whose whole commercial logic is adaptability. I write about this from experience of the CCW process in Geneva, and I explain how I came to this work in [my story](https://aviperera.com/my-story/). For the wider risk picture see my [AI safety page](https://aviperera.com/aisafety/), my [research](https://aviperera.com/research/) and the [AI Policy Tracker](https://aviperera.com/ai-policy-tracker/).

### Frequently asked questions

**Is the Vision 60 an autonomous weapon?****The standard robot is not a weapon. Armed versions integrate weapons such as the SPUR rifle, which its makers say requires a human operator to fire. The platform has autonomous mobility and onboard compute, which is why it is relevant to the autonomy debate.

Who makes the Vision 60?****Ghost Robotics of Philadelphia, which has been majority owned by South Korea’s LIG Nex1 since 2024.

Who uses it?****The US Air Force and Army, Japan and South Korea among others, mostly for perimeter security, reconnaissance and training. The US and Australian armies have tested armed configurations.

Are armed robot dogs legal?****Neither the platform nor a remotely operated armed version is banned by any treaty. Use is governed by international humanitarian law in armed conflict and by human rights law elsewhere, and a legal weapons review is required of any state fielding one.

What is the SPUR?****The Special Purpose Unmanned Rifle, a 6.5 mm Creedmoor or 7.62 mm remotely operated rifle developed by SWORD Defense Systems that can be mounted on ground robots including the Vision 60.

### Sources

Manufacturer website:** [Ghost Robotics, Vision 60](https://www.ghostrobotics.io/vision-60) and [robot specifications](https://ghostrobotics.io/robots)

**News reports**

- [The Defense Post, South Korea’s LIG Nex1 to Acquire American Firm Ghost Robotics (December 2023)](https://thedefensepost.com/2023/12/15/south-korea-ghost-robotics/)

- [Korea JoongAng Daily, LIG Nex1 acquires Ghost Robotics in $240 million deal](https://www.koreajoongangdaily.com/business/lig-nex1-acquires-ghost-robotics-in-240-million-deal/10482814)

- [Technical.ly, Ghost Robotics acquired by a South Korean company](https://technical.ly/startups/ghost-robotics-acquisition-lig-nex-1/)

- [The Robot Report, LIG Nex1 intends to acquire stake in Ghost Robotics](https://www.therobotreport.com/lig-nex1-announces-intent-to-acquire-quadruped-maker-ghost-robotics/)

- [Billy Penn, Ghost Robotics and Israel (April 2024)](https://billypenn.com/2024/04/22/israel-palestine-gaza-robot-dogs-ghost-robotics/)

- [Task & Purpose, Companies behind robot dogs ask countries not to arm them](https://taskandpurpose.com/tech-tactics/dont-arm-robot-dogs)

- [Popular Mechanics via Yahoo, Robo-dogs with sniper rifles (2021)](https://news.yahoo.com/welp-now-robo-dogs-sniper-130800576.html)

- [Mobility Engineering Technology, SWORD Robotic Rifle](https://www.mobilityengineeringtech.com/component/content/article/40865-robotic-rifle)

- [The Defense Post, US Army rifle armed Q-UGV at Operation Hard Kill](https://gecici.thedefensepost.com/?p=82860)

- [Freethink, Robot dogs are being deployed at a US military base](https://www.freethink.com/articles/robot-dogs)

- [GBP, Japan nears Ghost Robotics Vision 60 ground drone buy](https://gbp.com.sg/stories/japan-nears-ghost-robotics-vision-60-ground-drone-buy/)

**Military, regulatory and diplomatic documentation**

- Department of Defense Directive 3000.09, Autonomy in Weapon Systems (updated January 2023)

- [ICRC, Autonomous Weapons advocacy paper (June 2026)](https://www.icrc.org/sites/default/files/2026-08/4937_002_Autonomous_weapons_advocacy_paper_EN.pdf)

- [France, GGE communiqué (10 September 2026)](https://www.diplomatie.gouv.fr/en/presse-et-ressources/decouvrir-et-informer/actualites/organisations-internationales-reunion-du-groupe-d-experts-gouvernementaux-sur-les-systemes-d-armes)

- [UNODA, CCW GGE LAWS briefing](https://disarmament.unoda.org/en/updates/briefing-chair-ccw-gge-laws-margins-first-committee)

- [Reaching Critical Will, CCW Report (January 2026)](https://reachingcriticalwill.org/disarmament-fora/ccw/2026/laws/reports/18145-ccw-report-vol-14-no-1)

- [Reaching Critical Will, CCW Meeting of High Contracting Parties (November 2025)](https://reachingcriticalwill.org/disarmament-fora/ccw/2025/hcp/ccw-report/18087-ccw-report-vol-13-no-5)

**Treaties, statute and case law**

- [Additional Protocol I, Arts 36, 41, 48, 51, 57 (ICRC database)](https://ihl-databases.icrc.org/en/ihl-treaties/api-1977)

- [Arms Trade Treaty, Arts 6 and 7](https://thearmstreaty.org)

- Rome Statute, Arts 8(2)(b)(i) and (iv) and 28

- UN Basic Principles on the Use of Force and Firearms by Law Enforcement Officials (1990)

- UN Guiding Principles on Business and Human Rights (2011)

- UNGA Resolution 78/241 (2023) on lethal autonomous weapons systems

- Prosecutor v. Galić*, IT-98-29-T (ICTY, 2003)

- *Public Committee Against Torture in Israel v. Government of Israel*, HCJ 769/02 (2006)

- *Legality of the Threat or Use of Nuclear Weapons*, ICJ Advisory Opinion (1996)

- *R (Campaign Against Arms Trade) v. Secretary of State for International Trade* [2019] EWCA Civ 1020

---

*Citation: Perera, Avi. "Vision 60 Q-UGV". aviperera.com, 2026. Web. <https://aviperera.com/vision-60-q-ugv/>*
