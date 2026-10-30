---
id: AIM-010
title: "Accuracy or transparency: ensembles and neural networks predict but do not explain"
type: zettel
kind: debate
skill: ai-marketing
also: [consumer-insight, client-business]
level: 3
tags: [black-box, explainability, ensembles, random-forests, neural-networks, human-control]
sources:
  - SRC-038 | ch. 6 (Random forests, Boosted decision stumps); ch. 8 (Now about neural networks, Thinking about thinking)
status: growing
---

# Accuracy or transparency: ensembles and neural networks predict but do not explain

> **The idea in one sentence:** the more opaque an AI model is, the harder it is to check whether it does a good job or only a middling one; Struhl openly prefers methods you can test against common sense.

## Explanation

A key finding of machine learning, Struhl explains, is that **the average of many weak models typically performs better than any of the individual models**. This is how **ensembles** work: random forests run hundreds of trees, randomly swapping people and predictors in and out, then average them or take votes. Boosting reruns the model with more weight on the cases it got wrong. The price is opacity: you cannot see what 500 trees did. In the cruise case, Struhl used the random forest only to pick out the definitely important variables, then built **a single tree** that could be studied and applied.

Neural networks, touted as the future of artificial intelligence, are the extreme case. In the author's test (1,800 cases, 70 variables), the network produced an unintelligible diagram and coefficients whose signs seemed backward about half the time. It predicted worse than the other methods and overfitted the data. Struhl grants that such networks can shine with huge volumes of data and long training, but he raises an awkward question: a bad self-driving car is easy to spot, because it crashes. How do you tell that an automated recommendation system is doing only a middling job?

## The tension

Kotler, Kartajaya and Setiawan explicitly hold the opposite position: a model beyond human comprehension is "a good thing", because marketers are no longer restricted to their own biases ([[AIM-006-predictive-analytics-estimates-who-will-buy-what-will-sell|AIM-006]]).

| The "accuracy" position (Kotler 5.0) | The "transparency" position (Struhl) |
|---|---|
| all that matters is how well it predicts | you have to be able to check whether the model makes sense |
| complex models capture fine patterns | opaque models hide basic mistakes |
| automation frees people | you have to decide explicitly where you cede control to the computer and to the vendor |

## Application

- When a vendor sells a "black box", ask for validation on new data and an explanation of the main variables.
- Use opaque models for selection and exploration, then explainable models for the decision and for the presentation to the client.
- Remember the author's conclusion: no analysis of transactions gives you a new product idea.

## Example

Psoriasis and depression: a simple tree, which any doctor could score with pencil and paper, was complemented by boosting, which highlighted two thresholds (over 10% and over 20% of body surface area affected). The ensemble served the transparent model; it did not replace it.

## Questions

- Would a marketing director accept a budget recommendation that nobody can explain?
- How does the debate change in the era of generative models?

## Links

- **extends** [[AIM-009-classification-trees-turn-a-database-into-a-few-if-then|AIM-009]]: ensembles start from classification trees.
- **contradicts** [[AIM-006-predictive-analytics-estimates-who-will-buy-what-will-sell|AIM-006]]: Marketing 5.0 sees the opacity of the "black box" as an advantage.
- **see** [[AIM-030-data-ethics-in-ai-marketing-has-four-basic-rules-consent|AIM-030]]: explainability as an ethical and regulatory obligation.
- **see** [[AIM-007-validation-on-a-hold-out-sample-separates-real-patterns|AIM-007]]: overfitting, the classic problem of neural networks.
- **see** [[AIM-029-can-ai-create-a-brand-s-identity-the-promise-of-ai|AIM-029]]: the same question, "where does the human stay?", applied to brand creation.
- **see** [[DIG-050-programmatic-advertising-buys-every-impression|DIG-050]]: programmatic advertising makes the same trade: automated efficiency against control and transparency.

## Sources

- [[SRC-038-artificial-intelligence-marketing-and-predicting-consumer-choice|SRC-038]] Steven Struhl, *Artificial Intelligence Marketing and Predicting Consumer Choice*, ch. 6 and ch. 8

<!-- backlinks:start -->
## Backlinks

- [[AIM-006-predictive-analytics-estimates-who-will-buy-what-will-sell|AIM-006]] _contradicts_: Predictive analytics estimates who will buy, what will sell and what will work: a cycle that is checked continuously, not a report
- [[AIM-009-classification-trees-turn-a-database-into-a-few-if-then|AIM-009]] _see_: Classification trees turn a database into a few "if-then" rules for targeting
- [[AIM-032-bias-in-ai-marketing-has-two-sources-the-data-the-model|AIM-032]] _see_: Bias in AI marketing has two sources: the data the model learns from and people's blind trust in the recommendation
- [[MAP-003-ethics-regulation-and-responsibility-in-advertising|MAP-003]]: Ethics, regulation and responsibility in advertising
- [[SRC-038-artificial-intelligence-marketing-and-predicting-consumer-choice|SRC-038]]: Artificial Intelligence Marketing and Predicting Consumer Choice: An Overview of Tools and Techniques
<!-- backlinks:end -->
