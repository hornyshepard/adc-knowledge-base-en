---
id: AIM-027
title: 'A language model summarizes text well but does not prove causes: "why did conversion go up?" is not a question for a chatbot'
type: zettel
kind: debate
skill: ai-marketing
also: [consumer-insight, digital-marketing]
level: 2
tags: [data-analysis, llm, sentiment, causality, hallucinations, social-listening]
sources:
  - SRC-039 | ch. 4 (Analytics Tools, Demystifying Analytics, pp. 94–95); ch. 5 (Data Collection and Preprocessing, NLP, Summarization and Insights Generation, Case Studies, pp. 109–114)
  - SRC-038 | ch. 2 (These methods show what will happen but not why, Results and validation); ch. 8 (Thinking about thinking)
status: growing
---

# A language model summarizes text well but does not prove causes: "why did conversion go up?" is not a question for a chatbot

> **The idea in one sentence:** ChatGPT is useful for reading and synthesizing large volumes of unstructured text, but a fluent explanation of the numbers is not a validated causal analysis.

## Explanation

Najafov describes a four-step analysis workflow with ChatGPT: **data collection and preprocessing** (cleaning, transformation, integration), **natural language processing** (NLP: sentiment, topic identification, key phrase extraction), **summarization and insights generation**, then **visualization and reporting**. The solid part of the proposal is the work with text: reviews, comments, open-ended answers. For example, the model notices that a product is receiving positive feedback for its quality but negative feedback for its price.

The problem appears when the author extends the promise to numbers and causes. His "after integration" examples show the model saying that the blog pages have high traffic *because of* posts on trending topics, or that the conversion rate increased by 15% "primarily due to the new email marketing campaign." The case studies (an "ecommerce giant", a "financial services firm") are anonymous and give no method.

## The tension

| Najafov (SRC-039) | Struhl (SRC-038) |
|---|---|
| the model turns raw data into actionable conclusions, fast | a model has to be validated on new data, otherwise it overfits |
| it can say *why* a metric changed | even rigorous methods show *what* will happen more easily than *why* |
| patterns emerge from the data | patterns "discovered" by chance are often urban legends (diapers and beer) |

Struhl does not discuss generative models (his book is from 2017), but his criteria apply directly. A causal explanation requires a design (an experiment, a control group) or a validated model, not just a convincing sentence.

## Application

- Use the model for **text synthesis** (themes from 2,000 reviews, the summary of a transcribed focus group), then check it against a sample read by a person.
- For "what caused it?" questions, ask for a test (A/B, control group) or an analyst; treat the model's answer as a **hypothesis**.
- Do not let the model "clean" the customer database on its own without verifiable rules.

## Example

The anonymous case of the consumer goods manufacturer that "identified" a growing demand for eco-friendly products and launched a successful line illustrates the risk exactly: the story is plausible, but we do not know what data, what method and what alternatives there were.

## Questions

- How would you check whether the themes the model extracts from reviews are real and not invented?
- Which research questions can you safely delegate to a language model?

## Links

- **contradicts** [[AIM-005-historical-data-predict-repetition-not-novelty-they-do-not|AIM-005]]: Struhl: data does not produce insights or new ideas on its own.
- **see** [[AIM-007-validation-on-a-hold-out-sample-separates-real-patterns|AIM-007]]: validation, the step missing from the workflow Najafov proposes.
- **see** [[AIM-025-a-marketing-prompt-is-a-mini-brief-and-the-model-s-answer|AIM-025]]: analytical questions as a type of prompt.
- **see** [[INS-081-the-effect-of-an-ad-is-proved-by-experiment-not-by-the|INS-081]]: a causal effect is proven by an experiment with a control group.
- **see** [[AIM-028-visual-listening-finds-the-brand-in-images-where-the-text|AIM-028]]: automated sentiment analysis, on text and on images, has the same limits.

## Sources

- [[SRC-039-chatgpt-for-marketing|SRC-039]] Eldar Najafov, *ChatGPT for Marketing*, ch. 4, pp. 94–95; ch. 5, pp. 109–114
- [[SRC-038-artificial-intelligence-marketing-and-predicting-consumer-choice|SRC-038]] Steven Struhl, *Artificial Intelligence Marketing and Predicting Consumer Choice*, ch. 2 and ch. 8

<!-- backlinks:start -->
## Backlinks

- [[AIM-005-historical-data-predict-repetition-not-novelty-they-do-not|AIM-005]] _see_: Historical data predict repetition, not novelty: they do not answer "what if" and do not show perceptions
- [[AIM-007-validation-on-a-hold-out-sample-separates-real-patterns|AIM-007]] _see_: Validation on a hold-out sample separates real patterns from overfitting
- [[AIM-024-the-human-forms-the-hypothesis-the-ai-runs-it-the-human|AIM-024]] _see_: The human forms the hypothesis, the AI runs it, the human interprets it: the division of labor in testing and leads
- [[AIM-025-a-marketing-prompt-is-a-mini-brief-and-the-model-s-answer|AIM-025]] _see_: A marketing prompt is a mini-brief, and the model's answer is a draft, not a deliverable
- [[AIM-028-visual-listening-finds-the-brand-in-images-where-the-text|AIM-028]] _see_: Visual listening finds the brand in images, where the text does not name it
- [[DIG-075-the-conversion-funnel-shows-where-visitors-leave-the|DIG-075]] _see_: The conversion funnel shows where visitors leave; the marketer's job is to find out why
- [[SRC-039-chatgpt-for-marketing|SRC-039]]: ChatGPT for Marketing: Learn Practical Applications of ChatGPT for Marketing
<!-- backlinks:end -->
