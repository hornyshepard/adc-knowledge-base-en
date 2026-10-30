---
id: AIM-012
title: Trade-off methods (discrete choice, conjoint, MaxDiff, Q-Sort) answer different questions
type: zettel
kind: framework
skill: ai-marketing
also: [consumer-insight, marketing-fundamentals]
level: 2
tags: [discrete-choice, conjoint, maxdiff, q-sort, experiment, hierarchical-bayes]
sources:
  - SRC-038 | ch. 3 (whole chapter); ch. 4 (The Bayesian advantage); ch. 8 (Finding what is most valuable in a list)
status: growing
---

# Trade-off methods (discrete choice, conjoint, MaxDiff, Q-Sort) answer different questions

> **The idea in one sentence:** they all make people choose between attributes, but each answers a different question; choosing the wrong method gives precise answers to the wrong question.

## Explanation

Trade-off methods start from the idea that a product, a service or a message is a bundle of attributes, each with **levels** (for example, prices of £2,000, £4,500, £6,800 and £9,000). The value of each level is measured in **utilities**, an abstract unit used as a kind of bookkeeping. The methods do not claim to reproduce how people think, only the **outcome** of the decision.

| Method | What the participant sees | Answers |
|---|---|---|
| Discrete choice modelling | simulated marketplaces with competing products + "none" | what happens to shares if I change the product, the price or the competition (including cannibalization) |
| Conjoint (full-profile) | a whole product or message, evaluated | the best configuration for a product with no direct competition or a small share; optimizing messages |
| MaxDiff | sets of 2–6 items from a list of 8–35; "most/least important" | the ranking of a list of benefits, messages, free gifts; data for each individual |
| Q-Sort / Thurstone Case 5 | a long list (up to about 100); you rank the top and the bottom items | the ranking of a very long list, at group level only |

Their strength comes from the **designed experiment**: the attributes vary with no correlation between them (an orthogonal design). So 18 profiles can estimate the value of 4,374 combinations, and 20 can cover 262,144.

The AI component is **Hierarchical Bayesian (HB) analysis**: it fills in each respondent's missing data by repeatedly borrowing estimates from other respondents, 20,000 or more times, until the values settle. With HB you can measure two to four times as many attributes without a larger sample, and you get results for each individual. People tire after 6–12 screens; engineers and farmers hold out up to about 21.

## Application

- A list of benefits for the brief? MaxDiff, not ratings.
- A launch in a crowded market, with possible reactions from competitors? Discrete choice.
- Which combination of headline, image and offer works? Conjoint.

## Example

Struhl gives the example of a floor-standing wine cooler with features proposed by the product team, some of them "slightly far-fetched": on rating scales, nearly all of them come out as highly important. A MaxDiff or a conjoint on the same features would have separated them clearly.

## Questions

- Why can MaxDiff not compare "shelf stable for three months" with "shelf stable for six months"?
- What do you lose if you test attributes separately rather than in the context of the whole product?

## Links

- **foundation** [[INS-078-asked-directly-what-matters-people-say-everything|INS-078]]: the failure of direct ratings is why these methods exist.
- **see** [[AIM-015-a-market-simulation-shows-when-a-price-cut-raises-share-but|AIM-015]]: discrete choice and the market simulator in action.
- **see** [[AIM-013-a-good-choice-study-is-built-before-the-questionnaire-a-ten|AIM-013]]: the practical rules for a well-built choice study.
- **see** [[ADV-080-the-elements-of-an-ad-can-be-tested-as-an-experiment|ADV-080]]: conjoint applied to advertising messages.
- **see** [[BRD-060-in-choice-models-the-brand-is-a-container-for-features-and|BRD-060]]: in the same models, brand value appears as the difference left after the attributes.
- **see** [[EXP-029-conjoint-service-optimization-shows-where-you-overdeliver|EXP-029]]: conjoint applied to the service package.

## Sources

- [[SRC-038-artificial-intelligence-marketing-and-predicting-consumer-choice|SRC-038]] Steven Struhl, *Artificial Intelligence Marketing and Predicting Consumer Choice*, ch. 3, 4 and 8

<!-- backlinks:start -->
## Backlinks

- [[ADV-080-the-elements-of-an-ad-can-be-tested-as-an-experiment|ADV-080]] _foundation_: The elements of an ad can be tested as an experiment: message conjoint beats the A/B test
- [[AIM-001-methods-for-predicting-choices-fall-into-four-classes-each|AIM-001]] _see_: Methods for predicting choices fall into four classes, each with an implicit view of people
- [[AIM-008-you-choose-the-analysis-method-by-the-marketing-question|AIM-008]] _see_: You choose the analysis method by the marketing question, not by technological fashion
- [[AIM-013-a-good-choice-study-is-built-before-the-questionnaire-a-ten|AIM-013]] _foundation_: A good choice study is built before the questionnaire: a ten-point checklist
- [[AIM-014-share-of-preference-is-not-market-share-the-forecast-has-to|AIM-014]] _foundation_: Share of preference is not market share: the forecast has to be adjusted for awareness, understanding and distribution
- [[AIM-015-a-market-simulation-shows-when-a-price-cut-raises-share-but|AIM-015]] _foundation_: A market simulation shows when a price cut raises share but lowers revenue
- [[BRD-059-the-brand-is-an-asset-not-an-expense-and-its-strength-is|BRD-059]] _see_: The brand is an asset, not an expense, and its strength is not its performance
- [[BRD-060-in-choice-models-the-brand-is-a-container-for-features-and|BRD-060]] _foundation_: In choice models the brand is a container for features, and its value shows in what remains after the features
- [[EXP-029-conjoint-service-optimization-shows-where-you-overdeliver|EXP-029]] _see_: Conjoint service optimization shows where you overdeliver and where you underdeliver
- [[INS-078-asked-directly-what-matters-people-say-everything|INS-078]] _extends_: Asked directly what matters, people say "everything": importance ratings do not predict behavior
- [[SRC-038-artificial-intelligence-marketing-and-predicting-consumer-choice|SRC-038]]: Artificial Intelligence Marketing and Predicting Consumer Choice: An Overview of Tools and Techniques
<!-- backlinks:end -->
