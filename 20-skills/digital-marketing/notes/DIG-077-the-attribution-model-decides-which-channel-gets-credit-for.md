---
id: DIG-077
title: The attribution model decides which channel gets credit for the conversion, and after cookies, tracking becomes uncertain and the early stages lose out
type: zettel
kind: debate
skill: digital-marketing
also: [advertising-strategy]
level: 2
tags: [attribution, last-click, first-touch, linear, multi-touch, utm, post-view, brand-lift, incrementality, roi]
sources:
  - SRC-030 | ch. 4, ch. 5
  - SRC-029 | ch. 9, pp. 262–263; ch. 13, pp. 381–382
  - SRC-032 | ch. 2.1, p. 39; ch. 3.3, pp. 108–109; ch. 3.4.3.1, pp. 119–120; ch. 4.3, p. 145
status: growing
---

# The attribution model decides which channel gets credit for the conversion, and after cookies, tracking becomes uncertain and the early stages lose out

> **The idea in one sentence:** when a person touches the brand five times before buying, the attribution model decides how much credit each touchpoint gets, and so where the budget moves; choosing it is a strategic decision, not a technical one.

## Explanation

Connors (SRC-030) calls attribution one of the biggest challenges in multi-channel marketing: a person sees an ad on Facebook, then a retargeting banner, gets a newsletter and buys after reading a review. Who "sold"?

| Model | How it allocates credit | What it favors |
|---|---|---|
| Last-touch / last-click | all of it to the final interaction | brand search, email, retargeting |
| First-touch | all of it to the first interaction | discovery channels (social, display) |
| Linear | equally among all of them | a balanced but naive picture |
| Multi-touch | by estimated contribution | for Connors, the most comprehensive |

Zahay et al. (SRC-029) supply the infrastructure: **UTM parameters** (source, medium, campaign; optionally term and content) make every click visible in analytics. In B2B, they show that leads from different channels have both different costs and different conversion rates.

**The tension.** Connors treats the multi-touch model as a solution. Schwarz-Musch et al. (SRC-032) show that in the post-cookie era, following a person from the first ad to the purchase becomes harder and harder, especially for the early stages. Last-touch overvalues search and retargeting, first-touch overvalues awareness. Their solution, separate KPIs per stage, sidesteps the problem without solving it: it does not say how much money an awareness campaign is worth. Firms still run traditional survey-based advertising performance studies (brand lift) in parallel. All the models measure correlation, not causation.

## Application

- Ask the client which model it uses before you accept the KPIs; an awareness campaign judged on last-click always "loses".
- Put UTMs on every link you distribute and report with at least two models, discussing the difference.
- Complete attribution with incrementality tests (areas or groups with no campaign) and with brand lift surveys.

## Example

A retargeting campaign looks spectacular in the last-touch report, because it catches people who have already decided. But those people entered the journey because of a video they saw two weeks earlier, which the model gives no credit at all.

## Questions

- Should creative agencies be paid according to an attribution model? Which one?
- How do you attribute the effect of a TV or outdoor campaign in a digital model?

## Links

- **foundation** [[DIG-072-a-metric-is-just-a-number-it-becomes-a-kpi-when-it-is|DIG-072]]: KPIs per channel depend on the attribution model.
- **see** [[DIG-074-each-stage-of-the-journey-has-its-own-kpis-net-reach-and|DIG-074]]: separate KPIs per stage, the partial answer of SRC-032.
- **see** [[DIG-052-retargeting-works-only-when-segmented-by-journey-stage|DIG-052]]: retargeting, the classic winner of last-click attribution.
- **alternative** [[AIM-021-uplift-modeling-looks-for-the-persuadable-a-response-model|AIM-021]]: uplift modeling looks for the incremental effect, not just who was reached.
- **foundation** [[INS-081-the-effect-of-an-ad-is-proved-by-experiment-not-by-the|INS-081]]: only a controlled experiment proves that the ad produced the effect.
- **see** [[SOC-039-valid-metrics-framework-success-on-social-media-ends-in|SOC-039]]: on social, too, the impact on sales is hard to attribute, which is why the framework stops at advocacy.

## Sources

- [[SRC-030-digital-marketing-strategies|SRC-030]] K. Connors, *Advanced Digital Marketing Strategies*, ch. 4, ch. 5
- [[SRC-029-digital-marketing-foundations-and-strategy|SRC-029]] Zahay et al., *Digital Marketing: Foundations and Strategy*, ch. 9, pp. 262–263; ch. 13, pp. 381–382
- [[SRC-032-digital-advertising-in-post-cookies-era|SRC-032]] Schwarz-Musch, Tauchhammer, Guetz, *Digital Advertising in the Post-cookie Era*, ch. 2.1 (p. 39), 3.3 (pp. 108–109), 3.4.3.1 (pp. 119–120), 4.3 (p. 145)

<!-- backlinks:start -->
## Backlinks

- [[ADV-082-continuous-tracking-measures-the-campaign-on-the-same-four|ADV-082]] _see_: Continuous tracking measures the campaign on the same four steps of the response sequence, and wearout is diagnosed from the plan down to the execution
- [[ADV-085-the-effectiveness-of-digital-advertising-remains-unproven|ADV-085]] _see_: The effectiveness of digital advertising remains unproven, and the book sees social media as a "negotiated" medium, hit by fraud and poor visibility
- [[AIM-021-uplift-modeling-looks-for-the-persuadable-a-response-model|AIM-021]] _see_: Uplift modeling looks for the persuadable: a response model also takes credit for sales that would have come anyway
- [[DIG-020-omnichannel-means-channels-that-reinforce-each-other-it-is|DIG-020]] _see_: Omnichannel means channels that reinforce each other: it is built on the critical purchase scenarios, with the silos broken, and measured by customer value, not by clicks per channel
- [[DIG-072-a-metric-is-just-a-number-it-becomes-a-kpi-when-it-is|DIG-072]] _see_: A metric is just a number; it becomes a KPI when it is chosen because it shows progress against an objective, and a KPI can combine several metrics
- [[DIG-074-each-stage-of-the-journey-has-its-own-kpis-net-reach-and|DIG-074]] _see_: Each stage of the journey has its own KPIs: net reach and frequency in Awareness, entry into the evoked set in Appeal, clicks and conversions in Ask, retention and CLV after purchase
- [[MAP-001-the-agency-workflow-from-the-business-problem-to-the-pitch|MAP-001]]: The agency workflow: from the business problem to the pitch and back
- [[MAP-002-effect-models-and-customer-journey-models-compared|MAP-002]]: Effect models and customer journey models, compared
- [[SRC-029-digital-marketing-foundations-and-strategy|SRC-029]]: Digital Marketing: Foundations and Strategy (5th ed.)
- [[SRC-030-digital-marketing-strategies|SRC-030]]: Advanced Digital Marketing Strategies: Mastering SEO, Social Media, Content Marketing, and AI for Maximum Online Growth
- [[SRC-032-digital-advertising-in-post-cookies-era|SRC-032]]: Digital Advertising in the Post-cookie Era: Strategic Campaign Planning Across the Customer Journey
<!-- backlinks:end -->
