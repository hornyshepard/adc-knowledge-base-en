---
id: AIM-006
title: "Predictive analytics estimates who will buy, what will sell and what will work: a cycle that is checked continuously, not a report"
type: zettel
kind: method
skill: ai-marketing
also: [digital-marketing, marketing-fundamentals, advertising-strategy]
level: 1
tags: [predictive-analytics, predictive-marketing, clv, churn, lead-scoring, next-best-action, recommendations, regression, neural-networks, moneyball]
sources:
  - SRC-037 | ch. 5 (5.1–5.6)
  - SRC-005 | ch. 9 "Predictive Marketing" (Fig. 9.1, 9.2)
status: growing
---

# Predictive analytics estimates who will buy, what will sell and what will work: a cycle that is checked continuously, not a report

> **The idea in one sentence:** descriptive analytics tells you what happened; predictive analytics learns from history to estimate what comes next, and it becomes useful only if its predictions are compared with reality all the time.

## Explanation

*Marketing 5.0* and Karen Noil describe the same tool from two angles. Kotler, Kartajaya and Setiawan start from *Moneyball*: the Oakland A's built a winning team on statistics, not intuition. They divide the applications into three areas; Noil gives the typical uses in each.

| Area (Kotler 5.0) | What it predicts | Typical uses (Noil) |
|---|---|---|
| **Customers** | customer lifetime value (CLV), upselling, cross-selling, churn risk | CLV, predictive lead scoring, churn prediction; a next-best-action plan for each customer (Kotler) |
| **Products** | which new product has a chance, what to offer each customer | product recommendations, propensity models (Kotler) |
| **Brands** | which combination of copy and visuals will work, for which audience | campaign optimization across channels and segments |

Noil adds the process, in five steps: data collection, data cleaning and preprocessing, model building, prediction generation, evaluation and optimization (the feedback loop). Kotler adds the techniques the marketer has to understand conceptually: **regression** (logistic regression gives the likelihood of a yes/no outcome), **collaborative filtering** (what people with the same preferences liked) and **neural networks** (accurate but hard to interpret).

Here the sources part ways. Kotler et al. see the opacity of the "black box" as an advantage: marketers are no longer restricted to their past biases and assumptions. Struhl argues the opposite ([[AIM-010-accuracy-or-transparency-ensembles-and-neural-networks|AIM-010]]). And neither Kotler nor Noil discusses validation on unseen data, or the sales that would have happened anyway.

## Application

- When a client says "we have data", ask about step 2: how clean are the data, and how well linked?
- Always ask for step 5: how do we check whether the prediction was right? Without it, the model is an automated opinion.
- Use prediction to choose **whom** and **when**, then let strategy and creative work decide **what** you tell them. In B2B and services, argue for the acquisition budget through CLV, not through the first sale.

## Example

Netflix decided to produce *House of Cards* based on a prediction that the combination of Kevin Spacey, David Fincher and a political drama would succeed (Kotler 5.0). On a small scale, the gym in Noil's book flags members whose attendance is declining as likely to cancel and offers them a free personal training session.

## Questions

- Does an accurate churn prediction guarantee that the retention offer is profitable? You may be paying some customers who would have stayed anyway.
- Can prediction discourage radically new ideas, for which there is no history?

## Links

- **foundation** [[DIG-061-data-driven-marketing-targets-segments-of-one-and-starts|DIG-061]]: predictive models are built on the data ecosystem of the "segment of one".
- **see** [[AIM-007-validation-on-a-hold-out-sample-separates-real-patterns|AIM-007]]: validation on unseen data, the step the cycle assumes but does not explain.
- **contradicts** [[AIM-010-accuracy-or-transparency-ensembles-and-neural-networks|AIM-010]]: Struhl rejects the idea that the model's opacity is an advantage.
- **see** [[AIM-021-uplift-modeling-looks-for-the-persuadable-a-response-model|AIM-021]]: uplift modeling: not who will buy, but whom the contact changes.
- **see** [[DIG-060-predictive-targeting-moves-the-question-from-who-the-person|DIG-060]]: predictive targeting applies the same principle in media.
- **see** [[AIM-016-ai-personalization-works-in-four-registers-real-time|AIM-016]]: predictive personalization is the end user of the predictions.

## Sources

- [[SRC-037-ai-driven-marketing|SRC-037]] Karen Noil, *AI-Driven Marketing*, ch. 5 "Predictive Analytics: Forecasting Customer Behavior" (5.1–5.6)
- [[SRC-005-marketing-5-0-philip-kotler|SRC-005]] Kotler, Kartajaya & Setiawan, *Marketing 5.0*, ch. 9 "Predictive Marketing: Anticipating Market Demand with Proactive Action" (Fig. 9.1, 9.2)

<!-- backlinks:start -->
## Backlinks

- [[AIM-003-martech-has-seven-use-cases-across-the-customer-path-from|AIM-003]] _see_: Martech has seven use cases across the customer path: from advertising and content to service CRM
- [[AIM-007-validation-on-a-hold-out-sample-separates-real-patterns|AIM-007]] _foundation_: Validation on a hold-out sample separates real patterns from overfitting
- [[AIM-010-accuracy-or-transparency-ensembles-and-neural-networks|AIM-010]] _contradicts_: Accuracy or transparency: ensembles and neural networks predict but do not explain
- [[AIM-016-ai-personalization-works-in-four-registers-real-time|AIM-016]] _see_: AI personalization works in four registers: real-time, behavioral, micro-segment and predictive
- [[AIM-017-ai-built-segments-are-dynamic-customers-move-between-them|AIM-017]] _application_: AI-built segments are dynamic: customers move between them as their behavior changes
- [[AIM-019-offer-what-the-customer-is-most-likely-to-accept-not-what|AIM-019]] _see_: Offer what the customer is most likely to accept, not what brings the highest margin: one "yes" leads to another
- [[AIM-021-uplift-modeling-looks-for-the-persuadable-a-response-model|AIM-021]] _contradicts_: Uplift modeling looks for the persuadable: a response model also takes credit for sales that would have come anyway
- [[DIG-060-predictive-targeting-moves-the-question-from-who-the-person|DIG-060]] _see_: Predictive targeting moves the question from "who the person was" to "what they will probably do" and can use context triggers such as weather, place and time
- [[DIG-061-data-driven-marketing-targets-segments-of-one-and-starts|DIG-061]] _application_: Data-driven marketing targets "segments of one" and starts with a narrow objective, not with an IT project
- [[SRC-005-marketing-5-0-philip-kotler|SRC-005]]: Marketing 5.0: Technology for Humanity
- [[SRC-037-ai-driven-marketing|SRC-037]]: AI-Driven Marketing: Harnessing Artificial Intelligence to Personalize Customer Experiences
<!-- backlinks:end -->
