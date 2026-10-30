---
id: AIM-011
title: Bayesian networks start from the idea that when you change one variable, they all change
type: zettel
kind: concept
skill: ai-marketing
also: [consumer-insight, advertising-strategy]
level: 3
tags: [bayesian-networks, regression, drivers, conditional-probability, survey-and-behavior]
sources:
  - SRC-038 | ch. 7 (whole chapter); ch. 8 (Determining the effects of variables)
status: growing
---

# Bayesian networks start from the idea that when you change one variable, they all change

> **The idea in one sentence:** unlike regression, which measures the effect of one variable "holding the rest constant", a Bayesian network (Bayes Net) models how a change propagates through all the connected variables.

## Explanation

Bayes's idea, put simply: you start from a prior estimate, update it with the data you observe and get a new, more accurate posterior estimate. A Bayesian network is a diagram of variables linked by arrows ("parents", "children"), with no loops. Each node holds a table of conditional probabilities. The network can learn its structure from the data on its own, or an expert can build it.

Struhl compares it with the classic methods:

| | Regression | Classification tree | Bayesian network |
|---|---|---|---|
| Relationships | straight lines (correlations) | "if-then" situations | the whole pattern of values, including S-curves |
| Effect of a change | the rest stays constant | only in certain combinations | propagates through the whole network |
| Correlated variables | unstable coefficients, even with reversed signs | few variables kept | includes them all |

The result is a measure of the target's **sensitivity** to each variable, the correct term for what the industry calls "driver analysis". The network can also screen out irrelevant variables quickly (the "Markov blanket") and includes validation by default.

## Application

- Use the network when you want to link **survey answers to real behavior** (share, share of wallet), which is notoriously hard with regression.
- Check the diagram: if the structure does not make sense, do not accept the result.
- Remember the limit: the network tells you **what** needs to change (for example "the sales service"), not **how**. For the "how", you need an experiment.

## Example

In a study among customers of an IT product, the network correctly predicted 84% of the share of business signed for, with cross-folded validation. The best regression model (PLS) reached 11%. The Monty Hall problem (do you switch doors or not?) is solved exactly with a three-node network: if you switch, you win twice as often.

## Questions

- Why is it unrealistic, in marketing, to assume that "the rest stays constant"?
- Which audience would reject a model without equations?

## Links

- **alternative** [[AIM-009-classification-trees-turn-a-database-into-a-few-if-then|AIM-009]]: trees see local interactions, networks see the whole pattern.
- **foundation** [[AIM-007-validation-on-a-hold-out-sample-separates-real-patterns|AIM-007]]: validation, built into Bayesian networks.
- **see** [[ADV-008-tested-with-data-the-hierarchy-of-effects-came-out-in-a|ADV-008]]: the network applied to a theoretical model of advertising effects.
- **see** [[INS-084-the-importance-of-an-attribute-changes-with-life-stage-a|INS-084]]: the network applied to purchase drivers by life stage.

## Sources

- [[SRC-038-artificial-intelligence-marketing-and-predicting-consumer-choice|SRC-038]] Steven Struhl, *Artificial Intelligence Marketing and Predicting Consumer Choice*, ch. 7 and ch. 8

<!-- backlinks:start -->
## Backlinks

- [[ADV-008-tested-with-data-the-hierarchy-of-effects-came-out-in-a|ADV-008]] _foundation_: Tested with data, the hierarchy of effects came out in a different order from the theory: from "what they do" to "what I do"
- [[AIM-007-validation-on-a-hold-out-sample-separates-real-patterns|AIM-007]] _see_: Validation on a hold-out sample separates real patterns from overfitting
- [[AIM-009-classification-trees-turn-a-database-into-a-few-if-then|AIM-009]] _alternative_: Classification trees turn a database into a few "if-then" rules for targeting
- [[INS-084-the-importance-of-an-attribute-changes-with-life-stage-a|INS-084]] _foundation_: The importance of an attribute changes with life stage: "a brand I trust" matters hugely at ages 4–8 and hardly at all for pre-teens
- [[SRC-038-artificial-intelligence-marketing-and-predicting-consumer-choice|SRC-038]]: Artificial Intelligence Marketing and Predicting Consumer Choice: An Overview of Tools and Techniques
<!-- backlinks:end -->
