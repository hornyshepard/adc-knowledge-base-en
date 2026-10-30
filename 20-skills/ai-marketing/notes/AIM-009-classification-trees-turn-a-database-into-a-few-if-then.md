---
id: AIM-009
title: Classification trees turn a database into a few "if-then" rules for targeting
type: zettel
kind: method
skill: ai-marketing
also: [digital-marketing, consumer-insight]
level: 2
tags: [chaid, classification-trees, targeting, lift, interactions, segmentation]
sources:
  - SRC-038 | ch. 6 (whole chapter)
status: growing
---

# Classification trees turn a database into a few "if-then" rules for targeting

> **The idea in one sentence:** a classification tree (CHAID, CART) repeatedly splits the population into groups that differ more and more on a target behavior, and produces simple rules that reveal combinations of factors you would not have thought of.

## Explanation

The tree starts from the whole database and looks for the variable that best splits it into groups with different levels of the target behavior. Then it splits each group again, and so on, until it reaches a significance threshold or a minimum group size. Struhl names several strengths:

- **Visible interactions**: the tree shows when two factors together produce more than each one separately (CHAID = chi-squared automatic interaction detector).
- **Optimal recoding**: the tree finds on its own how to group the categories; the testing is so advanced that it was first presented at an AI conference.
- **Simple rules**, easy to program into a database: "IF suburbs AND five or more kids THEN 27.5% buy".
- **Gains analysis** (also called lift or leverage analysis): it ranks the groups by their concentration of buyers and helps you choose the cut-off point for targeting.

The limit: the tree is a **greedy algorithm**. At each step it picks the locally best option, and small variations in the data can produce very different trees. Struhl's advice: let the program grow the tree, then check it and guide it toward what is strategically useful.

## Application

- Use the tree to find **whom** to talk to and which combinations of traits define a segment. Then test **what** to tell them with trade-off methods.
- Ask for the final rules, not only the "accuracy": a model that is easy to explain to the client is worth more than one more point on the score.

## Example

**SoggyOs vs. Kardboard Krunchies** (fictional names): from a chain's household data, the tree showed that 28% of suburban families with five or more children buy the competitor, nearly three times as many as suburban families with 1–3 children. The insight led to a giant "economy gunny-sack size" package. At a luxury cruise company (base rate 0.6%), 15 rules with only 10 variables classified over 340,000 people. The first 11 groups held 20% of the database and 70% of the buyers, which makes targeting some 17.5 times as efficient.

## Questions

- Why might a model that describes hundreds of thousands of people with 10 variables look suspicious to a client?
- What does the tree not tell you about the message that will persuade the segment it found?

## Links

- **application** [[AIM-017-ai-built-segments-are-dynamic-customers-move-between-them|AIM-017]]: the tree is a concrete micro-segmentation tool.
- **see** [[AIM-010-accuracy-or-transparency-ensembles-and-neural-networks|AIM-010]]: random forests and boosting, the ensemble extensions.
- **alternative** [[AIM-011-bayesian-networks-start-from-the-idea-that-when-you-change|AIM-011]]: Bayesian networks see the whole pattern, not only "if-then" situations.
- **see** [[AIM-008-you-choose-the-analysis-method-by-the-marketing-question|AIM-008]]: the tree answers the question "who are the best prospects?".
- **see** [[INS-085-personas-not-segments-ozzy-osbourne-and-prince-charles-have|INS-085]]: the segment the tree finds tells you whom you reach; the persona tells you how to talk to them.

## Sources

- [[SRC-038-artificial-intelligence-marketing-and-predicting-consumer-choice|SRC-038]] Steven Struhl, *Artificial Intelligence Marketing and Predicting Consumer Choice*, ch. 6

<!-- backlinks:start -->
## Backlinks

- [[AIM-008-you-choose-the-analysis-method-by-the-marketing-question|AIM-008]] _see_: You choose the analysis method by the marketing question, not by technological fashion
- [[AIM-010-accuracy-or-transparency-ensembles-and-neural-networks|AIM-010]] _extends_: Accuracy or transparency: ensembles and neural networks predict but do not explain
- [[AIM-011-bayesian-networks-start-from-the-idea-that-when-you-change|AIM-011]] _alternative_: Bayesian networks start from the idea that when you change one variable, they all change
- [[AIM-017-ai-built-segments-are-dynamic-customers-move-between-them|AIM-017]] _see_: AI-built segments are dynamic: customers move between them as their behavior changes
- [[SRC-038-artificial-intelligence-marketing-and-predicting-consumer-choice|SRC-038]]: Artificial Intelligence Marketing and Predicting Consumer Choice: An Overview of Tools and Techniques
<!-- backlinks:end -->
