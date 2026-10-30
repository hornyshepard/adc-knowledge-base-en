---
id: ADV-008
title: 'Tested with data, the hierarchy of effects came out in a different order from the theory: from "what they do" to "what I do"'
type: zettel
kind: case
skill: advertising-strategy
also: [consumer-insight, ai-marketing, brand-strategy]
level: 3
tags: [aida, lavidge-steiner, hierarchy-of-effects, loyalty, bayesian-networks, b2b]
sources:
  - SRC-038 | ch. 7 (Bayes Nets confirm a theoretical model, mostly; Going the next step with Bayes Nets; Letting the data speak with a Bayes Net; What next?)
status: growing
---

# Tested with data, the hierarchy of effects came out in a different order from the theory: from "what they do" to "what I do"

> **The idea in one sentence:** step models (AIDA, Lavidge-Steiner) are useful as hypotheses; when you let the data test them, the real sequence may be different, and that changes what you measure and what you communicate.

## Explanation

Struhl recalls that hierarchical models dominate thinking about advertising: **AIDA** (Attention, Interest, Desire, Action), attributed to E St Elmo Lewis (1898), and the six-stage model of **Lavidge and Steiner** (1961), building from awareness to purchase and climbed like the rungs of a ladder. Many measurement systems (tracking awareness, then preference) implicitly assume such a hierarchy. For a long time, hierarchies also survived for technical reasons: regression could not link ratings to sales, because the relationships are not linear.

The case: a firm that provided services to commercial brokers had a theoretical model built by hand. The client's actions made up "satisfaction", the customer's feelings made up "relationship", both were supposed to predict "loyalty", and loyalty to predict share of business. The model (a PLS path model) predicted share with only **18%** accuracy. A Bayes Net allowed to learn from the same data found a different hierarchy, with **62%** correct prediction under cross-validation:

**What they do (objectively) → How they treat me → How I feel → What I do → Share**

So actions do not work separately from the relationship. The way customers *view* the actions informs their feelings, and their feelings explain how they act.

## Application

- Treat any textbook model of effects as a **hypothesis to test** on the client's data, not as a law.
- In B2B communication strategy, work on the "how they treat me" link. Operational actions matter through the way customers experience them.
- Tie brand measures to real behavior (share, share of wallet), not only to other ratings.

## Example

The same analysis brought out important concrete actions: a designated contact throughout the relationship, communications when updating, a voice menu system, a dedicated person for problem resolution. The client then tested *how* to improve them with a conjoint-based service optimization.

## Questions

- What would this hierarchy mean for a consumer brand rather than a B2B one?
- If people often act without going through stages, is AIDA still useful in a seminar? For what?

## Links

- **foundation** [[AIM-011-bayesian-networks-start-from-the-idea-that-when-you-change|AIM-011]]: the method that made the test possible.
- **contradicts** [[ADV-005-hierarchy-of-effects-models-aida-lavidge-steiner-dagmar|ADV-005]]: the theoretical order of the hierarchies was not confirmed by the data.
- **see** [[HIS-010-aida-was-invented-by-copywriters-not-psychologists-the|HIS-010]]: step models started as writing rules, not as a description of the decision.
- **see** [[AIM-001-methods-for-predicting-choices-fall-into-four-classes-each|AIM-001]]: theoretical models as the fourth family of prediction methods.
- **application** [[EXP-029-conjoint-service-optimization-shows-where-you-overdeliver|EXP-029]]: the next step: optimizing the services identified.

## Sources

- [[SRC-038-artificial-intelligence-marketing-and-predicting-consumer-choice|SRC-038]] Steven Struhl, *Artificial Intelligence Marketing and Predicting Consumer Choice*, ch. 7

<!-- backlinks:start -->
## Backlinks

- [[ADV-005-hierarchy-of-effects-models-aida-lavidge-steiner-dagmar|ADV-005]] _example_: Hierarchy-of-effects models (AIDA, Lavidge-Steiner, DAGMAR) order think-feel-do objectives, but their fixed order has no empirical support
- [[AIM-001-methods-for-predicting-choices-fall-into-four-classes-each|AIM-001]] _see_: Methods for predicting choices fall into four classes, each with an implicit view of people
- [[AIM-011-bayesian-networks-start-from-the-idea-that-when-you-change|AIM-011]] _see_: Bayesian networks start from the idea that when you change one variable, they all change
- [[HIS-010-aida-was-invented-by-copywriters-not-psychologists-the|HIS-010]] _see_: AIDA was invented by copywriters, not psychologists: the genealogy of effect models
- [[MAP-002-effect-models-and-customer-journey-models-compared|MAP-002]]: Effect models and customer journey models, compared
- [[SRC-038-artificial-intelligence-marketing-and-predicting-consumer-choice|SRC-038]]: Artificial Intelligence Marketing and Predicting Consumer Choice: An Overview of Tools and Techniques
<!-- backlinks:end -->
