---
id: AIM-025
title: A marketing prompt is a mini-brief, and the model's answer is a draft, not a deliverable
type: zettel
kind: method
skill: ai-marketing
also: [copywriting, creative-brief, art-direction]
level: 1
tags: [prompting, generative-ai, chatgpt, midjourney, brief, draft, variants, curation]
sources:
  - SRC-039 | ch. 1 (Real-World Use Cases, pp. 10–14); ch. 2 (Tailoring Content for Target Audiences, Conducting A/B Testing for Messaging, pp. 26–27); ch. 4 (Case Studies, pp. 80–81; Demystifying Analytics, p. 94)
  - SRC-025 | ch. 6 "The North Star" (the Jardim Sonoro "Blended with Nature" case)
status: growing
---

# A marketing prompt is a mini-brief, and the model's answer is a draft, not a deliverable

> **The idea in one sentence:** a good prompt for a marketing task contains the same elements as a brief (purpose, content, audience, tone, examples), and what comes out has to be reviewed, selected and adapted by a person.

## Explanation

The library is thin on this topic, and it is worth saying openly: the only book about ChatGPT (Najafov) does not propose a prompting method, only five simple scenarios. All of them, though, share the same three-step structure: **initial prompt → review and edit → use**. From his examples you can extract the elements of a marketing prompt:

| Element | The example in the book |
|---|---|
| The **purpose** of the communication | an email informing a client about a delay in their product shipment |
| The **key points** | an apology + the assurance of expedited shipping |
| The **product details** | an eco-friendly water bottle made from recycled materials that keeps drinks cold for 24 hours |
| The **format and number of variants** | "a series of three social media posts" |
| The **audience and tone** | a tech blog about AI; the desired tone given for social posts |
| **Examples of existing content** | past content given to the model, because the first drafts lacked the brand's unique tone |

The author also recommends multiple variants for A/B tests and analytical questions in natural language, with the reservations in [[AIM-027-a-language-model-summarizes-text-well-but-does-not-prove|AIM-027]].

A case from *Shareworthy* shows what the prompt looks like in a creative team. For the Jardim Sonoro festival, Dentsu Creative Portugal input the names of top festival performers into Midjourney, along with words like birds, butterflies, leaves and trees. The team then refined the output. The prompt's ingredients came from the "Blended with Nature" concept, and the credits list an "A.I. prompt master" next to the art directors and the copywriter. The prompt is therefore a craft within the team, not a substitute for the idea.

## Application

- Write the prompt like a short brief: *what* (the task and the format), *for whom*, *why* (objective), *what it must contain* (facts, benefits), *how it should sound* (tone, approved examples).
- Put the concept's words in the prompt, not only the product description. The idea comes before the prompt.
- Ask for several variants, then select and combine. Check the facts: the model can invent product features.

## Example

The posts generated in the book for the eco-friendly bottle are correct but predictable: emoji, generic hashtags ("#EcoFriendly"), listed benefits. They are a draft that needs an idea and the brand's voice to become communication.

## Questions

- Which element of a creative brief (the insight, the single-minded proposition) is missing from almost all the prompt examples in the book?
- When is it faster to write the copy yourself than to correct a generated draft?

## Links

- **foundation** [[BRF-016-the-get-to-by-brief-puts-the-whole-strategy-into-one|BRF-016]]: Get/To/By, the shortest skeleton of a brief, and so of a prompt.
- **see** [[CPY-029-brand-voice-does-not-come-from-a-prompt-but-from-a-cycle|CPY-029]]: the cycle of human oversight of the voice, which follows the prompt.
- **see** [[AIM-027-a-language-model-summarizes-text-well-but-does-not-prove|AIM-027]]: the limit of analytical "and why?" questions put to the model.
- **see** [[AIM-026-in-award-winning-ai-campaigns-the-idea-comes-from-human|AIM-026]]: the award-winning cases in which the AI executes an idea formulated by people.
- **see** [[AIM-024-the-human-forms-the-hypothesis-the-ai-runs-it-the-human|AIM-024]]: the human-AI division of labor in testing and lead generation.

## Sources

- [[SRC-039-chatgpt-for-marketing|SRC-039]] Eldar Najafov, *ChatGPT for Marketing*, ch. 1, pp. 10–14; ch. 2, pp. 26–27; ch. 4, pp. 80–81, 94
- [[SRC-025-shareworthy|SRC-025]] Robin Landa, *Shareworthy*, ch. 6 "The North Star" (Jardim Sonoro, Dentsu Creative Portugal)

<!-- backlinks:start -->
## Backlinks

- [[AIM-026-in-award-winning-ai-campaigns-the-idea-comes-from-human|AIM-026]] _see_: In award-winning AI campaigns, the idea comes from human insight and the AI gives it scale: Cadbury, Nike "Never Done Evolving", Jardim Sonoro
- [[AIM-027-a-language-model-summarizes-text-well-but-does-not-prove|AIM-027]] _see_: A language model summarizes text well but does not prove causes: "why did conversion go up?" is not a question for a chatbot
- [[BRF-001-the-creative-brief-is-the-blueprint-for-the-execution-a|BRF-001]] _see_: The creative brief is the blueprint for the execution: a road map for the creative work and a criterion for evaluating it
- [[CPY-029-brand-voice-does-not-come-from-a-prompt-but-from-a-cycle|CPY-029]] _foundation_: Brand voice does not come from a prompt but from a cycle: examples → draft → human editing → feedback → final check
- [[SRC-039-chatgpt-for-marketing|SRC-039]]: ChatGPT for Marketing: Learn Practical Applications of ChatGPT for Marketing
<!-- backlinks:end -->
