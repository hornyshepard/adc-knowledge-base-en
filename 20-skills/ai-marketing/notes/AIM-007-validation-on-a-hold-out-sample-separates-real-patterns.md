---
id: AIM-007
title: Validation on a hold-out sample separates real patterns from overfitting
type: zettel
kind: method
skill: ai-marketing
also: [consumer-insight, digital-marketing]
level: 2
tags: [validation, overfitting, hold-out, predictive-models, evaluation]
sources:
  - SRC-038 | ch. 2 (How do I plan to evaluate the results?, Results and validation), ch. 7
status: growing
---

# Validation on a hold-out sample separates real patterns from overfitting

> **The idea in one sentence:** a predictive model always looks better on the data it was built on; only when it is tested on data it has not seen does it show what it is worth in the market.

## Explanation

Steven Struhl insists that every prediction project decide **from the start** how the result will be judged. The usual criteria: correct classification, explained variance (R²), the information criteria AIC and BIC (only for comparing models with each other) and the root-mean-squared error (RMSE).

The most important step is **validation**: you put part of the data aside (the hold-out sample), build the model on the rest and test it on the part you kept. Every model also fits random bumps and fluctuations found only in that data set; this is called **overfitting**. The validated result is almost always weaker, but more realistic. An example from the book: a Bayesian network predicted 93% of behavior correctly without validation and 84% with cross-folded validation.

Struhl adds three common-sense nuances:

- "All models are wrong but some are useful" (George E. Box): there is no universal threshold for "good enough"; organizations set arbitrary thresholds (70 percent explained variance, "two-thirds"), which you have to find out beforehand.
- **A weak result can be information.** At a pharmaceutical manufacturer, doctors' recall of the sales message explained no more than 28 percent of the variance in sales; management eventually accepted that the problem lay outside the sales force.
- The more data you have, the more validation is needed, and the easier it is to do.

## Application

- When an agency or an AI vendor presents a targeting model, ask: "How well does it predict on data it has not seen?"
- Agree with the client, before the analysis, on what a "good result" means and what decision is taken if the model is weak.
- Treat a model that "explains everything" on the old data as a warning sign, not a sign of success.

## Example

In the IT product study in chapter 7, a complex regression model (a partial least squares path model) correctly predicted only 11% of the share of business; the Bayesian network, with cross-folded validation, reached 84%. The comparison makes sense only because both were evaluated by the same rule.

## Questions

- Why can a model that fits the past perfectly be worse than an imperfect one?
- What would "validation" mean for a creative campaign tested in a single pre-test?

## Links

- **foundation** [[AIM-006-predictive-analytics-estimates-who-will-buy-what-will-sell|AIM-006]]: the simple predictive cycle needs this checking step.
- **see** [[INS-080-statistical-significance-does-not-mean-importance-with-lots|INS-080]]: statistical significance, the other criterion that is often misunderstood.
- **see** [[AIM-011-bayesian-networks-start-from-the-idea-that-when-you-change|AIM-011]]: Bayesian networks include validation by default.
- **see** [[DIG-076-an-a-b-test-changes-a-single-variable-starts-from-a|DIG-076]]: the A/B test applies the same discipline: a hypothesis, a sample, a threshold set in advance.
- **see** [[AIM-027-a-language-model-summarizes-text-well-but-does-not-prove|AIM-027]]: validation is the step missing from "conversational" analysis with language models.

## Sources

- [[SRC-038-artificial-intelligence-marketing-and-predicting-consumer-choice|SRC-038]] Steven Struhl, *Artificial Intelligence Marketing and Predicting Consumer Choice*, ch. 2 and ch. 7

<!-- backlinks:start -->
## Backlinks

- [[AIM-006-predictive-analytics-estimates-who-will-buy-what-will-sell|AIM-006]] _see_: Predictive analytics estimates who will buy, what will sell and what will work: a cycle that is checked continuously, not a report
- [[AIM-008-you-choose-the-analysis-method-by-the-marketing-question|AIM-008]] _see_: You choose the analysis method by the marketing question, not by technological fashion
- [[AIM-010-accuracy-or-transparency-ensembles-and-neural-networks|AIM-010]] _see_: Accuracy or transparency: ensembles and neural networks predict but do not explain
- [[AIM-011-bayesian-networks-start-from-the-idea-that-when-you-change|AIM-011]] _foundation_: Bayesian networks start from the idea that when you change one variable, they all change
- [[AIM-027-a-language-model-summarizes-text-well-but-does-not-prove|AIM-027]] _see_: A language model summarizes text well but does not prove causes: "why did conversion go up?" is not a question for a chatbot
- [[INS-080-statistical-significance-does-not-mean-importance-with-lots|INS-080]] _see_: Statistical significance does not mean importance: with lots of data, almost any difference becomes "significant"
- [[SRC-038-artificial-intelligence-marketing-and-predicting-consumer-choice|SRC-038]]: Artificial Intelligence Marketing and Predicting Consumer Choice: An Overview of Tools and Techniques
<!-- backlinks:end -->
