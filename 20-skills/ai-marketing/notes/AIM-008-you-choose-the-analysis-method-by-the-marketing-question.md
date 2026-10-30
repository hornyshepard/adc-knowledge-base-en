---
id: AIM-008
title: You choose the analysis method by the marketing question, not by technological fashion
type: zettel
kind: checklist
skill: ai-marketing
also: [consumer-insight, client-business]
level: 2
tags: [method-choice, research, prediction, project-planning]
sources:
  - SRC-038 | ch. 2 (At the beginning, Know what sensible goals might look like); ch. 8 (The tasks the methods do)
status: growing
---

# You choose the analysis method by the marketing question, not by technological fashion

> **The idea in one sentence:** each type of question has its fitting method; a complete tool-kit mixes new machine learning methods with classic ones.

## Explanation

In the summary chapter, Struhl reorganizes the book by **task**, not by method. Before any project, he asks six questions:

1. What can change, based on doing this analysis?
2. What do I need to know to help that change happen?
3. What data or which people do I need?
4. What is the most I can expect to get from this source?
5. How will I know if I reached a good answer?
6. Do the people who will use the result understand what they will get?

Then he matches the question with the method:

| Question | Recommended method |
|---|---|
| Who are the best prospects? What characterizes a group? | classification trees (+ random forests, boosting); clustering, discriminant analysis |
| Which item in a list (benefits, free gifts, messages) is the most valuable? | MaxDiff (with HB), Q-Sort/Case 5 for very long lists |
| What drives an outcome (share, intent to buy)? | Bayes Nets |
| What is the best combination for a message, an ad, a single product? | conjoint |
| What happens to a new or changed product in a competitive marketplace? | discrete choice + simulator |
| What hidden structures are in the data? | Bayes Nets, classification trees |
| Pattern recognition in huge volumes | neural networks, with caution |

Struhl adds a warning about expectations. It is sensible to use customer transactions to estimate how many will respond to a new offer similar to a recent one. It is not sensible to expect them to give you an idea for a new product.

## Application

- Use the six questions as a preamble to any research or data brief.
- When a client asks for "an AI model", translate the request into a row of the table. Often the answer is a classic method.
- Explain to stakeholders in advance what a reasonable result will look like. Busy people quickly forget what was agreed.

## Example

The cruise case shows the combination: the classification tree found *who* might buy the luxury cruise, but Struhl notes that the features and messages that would appeal to them had to be investigated separately, with trade-off methods.

## Questions

- Which method would you choose to decide between three positioning statements? Why not a focus group?
- Where do today's generative models fit into this 2017 table?

## Links

- **foundation** [[AIM-001-methods-for-predicting-choices-fall-into-four-classes-each|AIM-001]]: the four classes of methods.
- **see** [[AIM-009-classification-trees-turn-a-database-into-a-few-if-then|AIM-009]]: the method for "who".
- **see** [[AIM-012-trade-off-methods-discrete-choice-conjoint-maxdiff-q-sort|AIM-012]]: the methods for "what" and "what if".
- **see** [[AIM-007-validation-on-a-hold-out-sample-separates-real-patterns|AIM-007]]: question 5, how you judge the result.
- **see** [[INS-077-the-focus-group-is-good-for-language-and-for-detecting|INS-077]]: the focus group: good for language, not for choosing between options.

## Sources

- [[SRC-038-artificial-intelligence-marketing-and-predicting-consumer-choice|SRC-038]] Steven Struhl, *Artificial Intelligence Marketing and Predicting Consumer Choice*, ch. 2 and ch. 8

<!-- backlinks:start -->
## Backlinks

- [[AIM-001-methods-for-predicting-choices-fall-into-four-classes-each|AIM-001]] _see_: Methods for predicting choices fall into four classes, each with an implicit view of people
- [[AIM-009-classification-trees-turn-a-database-into-a-few-if-then|AIM-009]] _see_: Classification trees turn a database into a few "if-then" rules for targeting
- [[AIM-013-a-good-choice-study-is-built-before-the-questionnaire-a-ten|AIM-013]] _see_: A good choice study is built before the questionnaire: a ten-point checklist
- [[SRC-038-artificial-intelligence-marketing-and-predicting-consumer-choice|SRC-038]]: Artificial Intelligence Marketing and Predicting Consumer Choice: An Overview of Tools and Techniques
<!-- backlinks:end -->
