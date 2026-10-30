---
id: AIM-001
title: Methods for predicting choices fall into four classes, each with an implicit view of people
type: zettel
kind: framework
skill: ai-marketing
also: [consumer-insight, marketing-fundamentals]
level: 1
tags: [prediction, research-methods, machine-learning, ai-definition, implicit-biases]
sources:
  - SRC-038 | preface; ch. 1 (Some definitions we need, The methods we will be discussing, Implicit views of people and biases); ch. 8
status: growing
---

# Methods for predicting choices fall into four classes, each with an implicit view of people

> **The idea in one sentence:** before you choose a method (or an AI tool), ask what it assumes about how people decide, because that is where the errors hide.

## Explanation

Struhl defines artificial intelligence pragmatically: anything a machine does to respond to its environment and maximize its chances of success. For marketing, the environment is **data**, and success means finding patterns in the data that we cannot perceive. The decision stays with the human. He also points out that we do not "predict" but **forecast**, as weather forecasters do. And AI has been "hiding in plain sight" for decades in research methods (classification trees, hierarchical Bayesian analysis).

The methods for predicting choices fall into four broad classes:

| Class | What it assumes about people | Typical limit |
|---|---|---|
| Experimental or trade-off (discrete choice, conjoint, MaxDiff) | a product is a bundle of attributes that can be weighed against each other | the measurable attributes are not always the important ones |
| Questions and answers (surveys) | people report accurately what they think | response biases, inflated ratings |
| Stored or historic data (data mining, machine learning) | you will do what you have done; you will buy what people similar to you buy | fails when the market changes or when you are assigned to the wrong group |
| Theoretical models (AIDA-type hierarchies) | people go through psychological stages | often without an empirical basis |

Struhl arranges them on two axes: the **effort of planning to interact with consumers** (inviolable) and **analytical complexity** (sometimes discretionary). Discrete choice is high on both axes; historical data call for a lot of analysis but little or no interaction with consumers.

## Application

- Ask of every source of "insight": what view of people lies behind it?
- Combine the classes: historical data tell you *who*, surveys suggest *why*, experiments show *what would happen if*.
- Be skeptical of methods supported only by a vendor's website. Struhl accepts only what has both a track record in practical applications and academic validation.

## Example

The assumption "you buy what people similar to you buy" underlies recommendation engines: if women in the last trimester of pregnancy buy a lot of cotton balls, the system assumes that Thisbe, who is in the same situation, will buy them too.

## Questions

- What view of people does a brief hold when it says "the target wants quality at a good price"?
- Which class does a social listening tool belong to? What can it tell you, and what can it not?

## Links

- **alternative** [[AIM-002-the-next-tech-consists-of-the-technologies-that-mimic-human|AIM-002]]: Kotler defines AI through the technologies that mimic humans; Struhl, pragmatically, through what the machine does with data.
- **see** [[AIM-005-historical-data-predict-repetition-not-novelty-they-do-not|AIM-005]]: the limit of the "historic data" class, developed.
- **see** [[AIM-012-trade-off-methods-discrete-choice-conjoint-maxdiff-q-sort|AIM-012]]: the experimental class in detail.
- **see** [[AIM-008-you-choose-the-analysis-method-by-the-marketing-question|AIM-008]]: the "which method for which question" matrix.
- **see** [[INS-078-asked-directly-what-matters-people-say-everything|INS-078]]: the ratings bias, the limit of the "questions and answers" class.
- **see** [[ADV-008-tested-with-data-the-hierarchy-of-effects-came-out-in-a|ADV-008]]: a theoretical model (the hierarchy of effects) tested with data.

## Sources

- [[SRC-038-artificial-intelligence-marketing-and-predicting-consumer-choice|SRC-038]] Steven Struhl, *Artificial Intelligence Marketing and Predicting Consumer Choice*, preface, ch. 1, ch. 8

<!-- backlinks:start -->
## Backlinks

- [[ADV-008-tested-with-data-the-hierarchy-of-effects-came-out-in-a|ADV-008]] _see_: Tested with data, the hierarchy of effects came out in a different order from the theory: from "what they do" to "what I do"
- [[AIM-002-the-next-tech-consists-of-the-technologies-that-mimic-human|AIM-002]] _alternative_: The next tech consists of the technologies that mimic human capabilities: AI, NLP, sensors, robotics, mixed reality, IoT and blockchain
- [[AIM-005-historical-data-predict-repetition-not-novelty-they-do-not|AIM-005]] _foundation_: Historical data predict repetition, not novelty: they do not answer "what if" and do not show perceptions
- [[AIM-008-you-choose-the-analysis-method-by-the-marketing-question|AIM-008]] _foundation_: You choose the analysis method by the marketing question, not by technological fashion
- [[AIM-032-bias-in-ai-marketing-has-two-sources-the-data-the-model|AIM-032]] _foundation_: Bias in AI marketing has two sources: the data the model learns from and people's blind trust in the recommendation
- [[SRC-038-artificial-intelligence-marketing-and-predicting-consumer-choice|SRC-038]]: Artificial Intelligence Marketing and Predicting Consumer Choice: An Overview of Tools and Techniques
<!-- backlinks:end -->
