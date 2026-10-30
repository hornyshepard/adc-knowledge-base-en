---
id: AIM-032
title: "Bias in AI marketing has two sources: the data the model learns from and people's blind trust in the recommendation"
type: zettel
kind: concept
skill: ai-marketing
also: [consumer-insight, advertising-strategy, digital-marketing]
level: 2
tags: [algorithmic-bias, automation-bias, ai-ethics, audit, inclusion, discrimination, david-dao]
sources:
  - SRC-037 | ch. 12 (12.1.2, 12.3.1–12.3.2)
  - SRC-039 | ch. 2 ("Addressing Bias in AI-Driven Campaigns", "Frameworks for Bias Mitigation", pp. 20–22)
  - SRC-005 | ch. 4 "Digital Divide" (the behavioral side effects); ch. 7 "The New CX" (the David Dao case)
  - SRC-038 | ch. 1 ("Implicit views of people and biases")
status: growing
---

# Bias in AI marketing has two sources: the data the model learns from and people's blind trust in the recommendation

> **The idea in one sentence:** a model repeats the injustices in its data and in the objective it optimizes, and people amplify them when they accept the recommendation without judgment; that is why bias is looked for in the results by group, not in intentions.

## Explanation

The sources in the library describe three different mechanisms, which add up.

| Source of the bias | What happens | The example in the book |
|---|---|---|
| **The training data** (Noil, Najafov) | the model learns the patterns in the history, inequalities included, and can exacerbate them | a real estate platform whose ads pass over certain groups by race, gender or socioeconomic status; fashion recommendations based on gender stereotypes; a language model that underrepresents some groups |
| **The optimized objective** (Kotler 5.0) | the algorithm does exactly what it was asked and ignores what it does not see | United (2017): a revenue-maximization algorithm picked David Dao as a "least valuable" passenger by frequent flyer tier and fare class, without knowing he was a doctor who needed to see his patient the following day |
| **Automation bias** (Kotler 5.0) | people ignore their own judgment and rely on what the algorithm suggests | the same story: nobody contradicted the recommendation |

Struhl adds a deeper level: every prediction method carries an implicit view of people ([[AIM-001-methods-for-predicting-choices-fall-into-four-classes-each|AIM-001]]). The idea that you are "likely to buy what people somehow similar to you have bought" is already an assumption that can put someone in the wrong group.

The proposed remedies converge. Noil asks for an audit of the data sources (representative, diverse) and regular testing of the models for unintended bias. Najafov adds bias detection tools, diverse review teams, continuous monitoring, training and written policies. Kotler asks that people be able to override the machine's decision.

## Application

- Before launch, ask: who is excluded or over-targeted? Read the results by group (age, gender, region), not only the total.
- Write down what the model optimizes and what it is not allowed to sacrifice (for example, equal access to an offer).
- For high-stakes decisions (price, credit, exclusion), keep a clear rule for human intervention.

## Example

The David Dao case shows how objective bias and automation bias combine: a revenue rule, applied without empathy, produced an image crisis that no model had "priced in".

## Questions

- Is optimizing creative work for CTR also a bias, toward what is easy to click? What does the brand lose?
- Who audits bias in an agency: the data team, the strategist or the creative who chooses the images?

## Links

- **foundation** [[AIM-001-methods-for-predicting-choices-fall-into-four-classes-each|AIM-001]]: the implicit view of people in each method is the first form of bias.
- **see** [[AIM-030-data-ethics-in-ai-marketing-has-four-basic-rules-consent|AIM-030]]: explainability and accountability, the ethical rules that make bias visible.
- **see** [[AIM-010-accuracy-or-transparency-ensembles-and-neural-networks|AIM-010]]: opaque models are the hardest to audit.
- **see** [[AIM-004-in-the-new-cx-machines-are-cool-but-humans-are-warm-ai|AIM-004]]: the David Dao case, in the argument about human wisdom.
- **see** [[STO-040-the-responsibility-checklist-for-representation-stereotypes|STO-040]]: the representation checklist applies the same vigilance to images and copy.
- **see** [[ADV-051-inclusive-advertising-is-checked-on-three-axes-tone|ADV-051]]: an inclusive ad is checked for tone, language and representation.

## Sources

- [[SRC-037-ai-driven-marketing|SRC-037]] Karen Noil, *AI-Driven Marketing*, ch. 12 (12.1.2, 12.3.1–12.3.2)
- [[SRC-039-chatgpt-for-marketing|SRC-039]] Eldar Najafov, *ChatGPT for Marketing*, ch. 2, pp. 20–22
- [[SRC-005-marketing-5-0-philip-kotler|SRC-005]] Kotler, Kartajaya & Setiawan, *Marketing 5.0*, ch. 4 and ch. 7
- [[SRC-038-artificial-intelligence-marketing-and-predicting-consumer-choice|SRC-038]] Steven Struhl, *Artificial Intelligence Marketing and Predicting Consumer Choice*, ch. 1

<!-- backlinks:start -->
## Backlinks

- [[AIM-004-in-the-new-cx-machines-are-cool-but-humans-are-warm-ai|AIM-004]] _see_: In the new CX, machines are "cool" but humans are "warm": AI takes data and convergent thinking, humans keep insight, wisdom and empathy
- [[AIM-030-data-ethics-in-ai-marketing-has-four-basic-rules-consent|AIM-030]] _see_: Data ethics in AI marketing has four basic rules: consent, access and erasure, transparency, minimization
- [[AIM-034-the-real-digital-divide-is-between-the-advocates-and-the|AIM-034]] _see_: The real digital divide is between the advocates and the critics of digitalization: technology earns trust when it is personal, social and experiential
- [[MAP-003-ethics-regulation-and-responsibility-in-advertising|MAP-003]]: Ethics, regulation and responsibility in advertising
<!-- backlinks:end -->
