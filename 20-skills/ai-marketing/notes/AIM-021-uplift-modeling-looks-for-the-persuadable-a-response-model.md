---
id: AIM-021
title: "Uplift modeling looks for the persuadable: a response model also takes credit for sales that would have come anyway"
type: zettel
kind: concept
skill: ai-marketing
also: [advertising-strategy, digital-marketing, consumer-insight]
level: 3
tags: [uplift-modelling, persuadables, attribution, incrementality, obama-2012, response-models]
sources:
  - SRC-040 | section 2, ch. 3 (Moving From Level 4 to Level 5; Measuring the Right Things)
status: growing
---

# Uplift modeling looks for the persuadable: a response model also takes credit for sales that would have come anyway

> **The idea in one sentence:** what matters is not who is likely to buy, but whom your message changes; the rest is wasted spend or, worse, irritation.

## Explanation

Richards and McLean arrive at this idea while explaining why contact-center Decision Engines look far more effective than outbound campaigns. Their explanation has two parts.

**1. Context, not only prediction.** The customer who calls in is already engaged; they are at the bottom of the funnel. Measured in isolation, the Decision Engine gets all the glory for the sale, even though the path there was prepared by a lot of other communication. Copying the model into outbound campaigns does not give the same results, because the customer is at a different point in the journey.

**2. The type of model.** A **response model** predicts who will say "yes". An **uplift model** predicts whom the contact *changes*. Any group divides into:

| Group | What the contact does |
|---|---|
| Already decided to buy | nothing; they would have bought anyway, but the response model counts them as a win |
| Dead set against buying | nothing |
| Turned off by the contact | a negative effect; they should be left alone |
| **Persuadable** | the only real effect of the campaign is here |

The book's example is Barack Obama's 2012 re-election campaign. The analysts built and tested models that identified voters leaning toward Mitt Romney but likely to be receptive to the Obama campaign's message in swing states. The models guided the online and TV ad buys, the doors canvassers knocked on, the calls and the mailings.

The authors also note the trade-offs: **the cost per conversion increases** (because "sure-thing customers" are no longer counted), and the analytical work costs more. The gain: the same results with less outbound communication. Their broader recommendation: "What you really should be thinking about is engagement, not response." Look for the people who will buy *only if* they get one more piece of suitable content.

## Application

- When a report says "the campaign generated X sales", ask: how many would have happened without the campaign? Ask for a control group.
- Leave out of retention or discount campaigns the customers who would stay anyway; you are giving them money for nothing.
- Identify the "do not disturb" segment (people whom contact annoys) and take it off the lists.

## Example

On the same principle, Noil (SRC-037) proposes a discount for customers at "risk of churn". Without uplift logic, part of the discounts goes to people who were not leaving anyway.

## Questions

- Why can a model that "predicts well" be useless for the decision to contact someone?
- How would you apply the idea of persuadables to media planning for a brand campaign?

## Links

- **contradicts** [[AIM-006-predictive-analytics-estimates-who-will-buy-what-will-sell|AIM-006]]: the standard uses of predictive analytics ignore incrementality.
- **see** [[AIM-020-o2-vision-the-decision-engine-took-conversion-from-under-2|AIM-020]]: the O2 results, read through this lens.
- **see** [[AIM-014-share-of-preference-is-not-market-share-the-forecast-has-to|AIM-014]]: another trap: confusing preference with the market.
- **see** [[INS-081-the-effect-of-an-ad-is-proved-by-experiment-not-by-the|INS-081]]: Fennis & Stroebe: the effect is proven only with a control group.
- **see** [[DIG-077-the-attribution-model-decides-which-channel-gets-credit-for|DIG-077]]: attribution models share out the credit, but do not show what would have come anyway.

## Sources

- [[SRC-040-intelligent-customer-engagement|SRC-040]] Aly Richards & Scott McLean, *Intelligent Customer Engagement*, section 2, ch. 3

<!-- backlinks:start -->
## Backlinks

- [[ADV-047-a-big-idea-is-not-enough-without-a-long-idea-the-audience|ADV-047]] _see_: A Big Idea is not enough without a "Long Idea": the audience must be met at the next step (Volvo Trucks, "Epic Split")
- [[AIM-006-predictive-analytics-estimates-who-will-buy-what-will-sell|AIM-006]] _see_: Predictive analytics estimates who will buy, what will sell and what will work: a cycle that is checked continuously, not a report
- [[AIM-019-offer-what-the-customer-is-most-likely-to-accept-not-what|AIM-019]] _see_: Offer what the customer is most likely to accept, not what brings the highest margin: one "yes" leads to another
- [[AIM-020-o2-vision-the-decision-engine-took-conversion-from-under-2|AIM-020]] _see_: O2 Vision: the Decision Engine took conversion from under 2% to over 70%, then audience fatigue set in
- [[DIG-077-the-attribution-model-decides-which-channel-gets-credit-for|DIG-077]] _alternative_: The attribution model decides which channel gets credit for the conversion, and after cookies, tracking becomes uncertain and the early stages lose out
- [[SRC-040-intelligent-customer-engagement|SRC-040]]: Intelligent Customer Engagement: The Future of Content Marketing
<!-- backlinks:end -->
