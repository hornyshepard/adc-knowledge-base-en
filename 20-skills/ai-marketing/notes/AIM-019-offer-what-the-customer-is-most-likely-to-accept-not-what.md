---
id: AIM-019
title: 'Offer what the customer is most likely to accept, not what brings the highest margin: one "yes" leads to another'
type: zettel
kind: principle
skill: ai-marketing
also: [digital-marketing, client-business]
level: 2
tags: [decision-engine, next-best-action, propensity, arbitration, contact-strategy, interest-cloud]
sources:
  - SRC-040 | section 4, ch. 4 (Decision Engines: What They Do, arbitration, Technology Notes); ch. 2 (Contact Strategy); ch. 3 (Engagement Decision Engine: Build Persona Interest Clouds)
status: growing
---

# Offer what the customer is most likely to accept, not what brings the highest margin: one "yes" leads to another

> **The idea in one sentence:** in automated decisions about which offer to make, the "highest margin" rule loses in the long run to the "highest likelihood of acceptance" rule.

## Explanation

Richards and McLean explain, step by step, the anatomy of a contact-center **Decision Engine**, using the example of a bank:

1. **Propensity models**: one model per product predicts the likelihood of purchase.
2. **Actions by propensity segment**: for example, the offer is made only above 70%. A customer with low propensity would need an extra incentive.
3. **Eligibility rules**, checked first: before a mortgage you run a credit check, so you do not sell something the customer cannot get.
4. **Arbitration** between products: for example "propensity × margin", possibly divided by the time it takes to sell the product.
5. **Priority switch**: when the call queue is long, the products that are quicker to sell win.

After each response from the customer, the engine runs again and proposes the next-best action.

The counterintuitive observation comes from the authors' projects:

| | Product A | Product B |
|---|---|---|
| Propensity | 55% | 85% |
| Margin | £100 | £50 |

With the margin rule, the engine offers A, to which the customer says "no" more often. Without it, the engine offers B. The result: more accepted offers and, above all, **the first "yes" increases the propensity to buy the second product**. In the long run, you make more money.

Two complementary ideas from the book:

- **Contact strategy**: rules that prevent over-contacting (for example, at least six weeks between calls for insurance products, only on a Wednesday evening between 7 p.m. and 8.30 p.m.). The audience strategist needs authority over the product managers.
- **"Interest clouds"**: content is tagged automatically (NLP), and a person's interest in a topic increases when they keep going back to it and degrades when they do not. It anticipates today's content recommendations.

## Application

- In CRM briefs, ask explicitly for the arbitration rule and question optimization for immediate margin.
- Propose a written contact strategy, with maximum frequencies per channel, before any automated program.
- For the copywriter: next-best-action scenarios need short, modular copy for every offer and every possible response.

## Example

The sequence in the book: the customer calls for a quote on household buildings insurance (and buys it), is then offered household contents insurance (says no), then a credit card. Each offer is recalculated after the previous response.

## Questions

- What happens to the customer's trust if they feel every call turns into a sale?
- Does the "one yes leads to another" rule hold in e-commerce too, not only in the contact center?

## Links

- **foundation** [[AIM-018-the-ice-maturity-model-ten-principles-and-five-levels-from|AIM-018]]: the Decision Engine defines maturity level 4.
- **see** [[AIM-006-predictive-analytics-estimates-who-will-buy-what-will-sell|AIM-006]]: Kotler's Marketing 5.0 calls the same mechanism next-best action.
- **see** [[AIM-021-uplift-modeling-looks-for-the-persuadable-a-response-model|AIM-021]]: the type of model matters as much as the rules.
- **see** [[DIG-036-in-ai-driven-email-send-time-and-frequency-are-optimized|DIG-036]]: frequency optimization, a relative of the contact strategy.
- **see** [[DIG-052-retargeting-works-only-when-segmented-by-journey-stage|DIG-052]]: retargeting without limits becomes harassment: the same need for contact rules.

## Sources

- [[SRC-040-intelligent-customer-engagement|SRC-040]] Aly Richards & Scott McLean, *Intelligent Customer Engagement*, section 4, ch. 2, 3 and 4

<!-- backlinks:start -->
## Backlinks

- [[AIM-018-the-ice-maturity-model-ten-principles-and-five-levels-from|AIM-018]] _see_: The ICE maturity model: ten principles and five levels, from transactions to intelligent engagement
- [[AIM-020-o2-vision-the-decision-engine-took-conversion-from-under-2|AIM-020]] _see_: O2 Vision: the Decision Engine took conversion from under 2% to over 70%, then audience fatigue set in
- [[DIG-036-in-ai-driven-email-send-time-and-frequency-are-optimized|DIG-036]] _see_: In AI-driven email, send time and frequency are optimized for the individual, not for the list
- [[SRC-040-intelligent-customer-engagement|SRC-040]]: Intelligent Customer Engagement: The Future of Content Marketing
<!-- backlinks:end -->
