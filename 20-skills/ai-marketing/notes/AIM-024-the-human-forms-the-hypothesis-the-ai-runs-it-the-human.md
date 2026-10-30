---
id: AIM-024
title: "The human forms the hypothesis, the AI runs it, the human interprets it: the division of labor in testing and leads"
type: zettel
kind: principle
skill: ai-marketing
also: [digital-marketing, client-business]
level: 2
tags: [human-and-ai, ab-testing, lead-scoring, automation, human-oversight]
sources:
  - SRC-039 | ch. 4 (Lead Generation, Potential Pitfalls of Overly Automated Interactions, Blending AI and Human Interaction, A/B Testing, Combining AI-Driven A/B Testing with Human Insights, pp. 82–86)
status: growing
---

# The human forms the hypothesis, the AI runs it, the human interprets it: the division of labor in testing and leads

> **The idea in one sentence:** the AI takes the volume (variants, first contact, scoring, monitoring), and people keep both ends of the process: what is worth testing, what the result means, and the relationships that matter.

## Explanation

Najafov's chapter "Advanced Techniques for Marketing with ChatGPT" is, at bottom, a description of the **division of labor** between human and model in two processes.

**A/B testing**, in five stages:

1. **Human-led hypothesis**: marketers formulate it from their understanding of the audience and the market. The AI can suggest variables from historical data.
2. **Execution and monitoring** are automated: the model runs the variants and monitors them in real time.
3. **Interpretation is human**: people see context, external influences and biases that the model misses.
4. **Qualitative insights** (interviews, feedback) complement the numbers: emotional responses, cultural influences.
5. **Continuous training and monitoring**, with bias checks.

**Lead generation**, with the warning that overly automated interactions may come across as impersonal:

- the AI segments, makes the first personalized outreach, sends follow-ups and **scores** leads by their likelihood to convert;
- humans take the high-scoring leads, the meetings and the relationship building;
- the transition from bot to human has to be seamless, at the appropriate time.

## Application

- In a test plan, write down explicitly who does what: the hypothesis (strategist), the variants (copywriter + AI), the analysis (analyst), the decision (client).
- Set clear escalation thresholds: from which score or which signal a lead goes to a human.
- Do not let the variant generator decide alone what gets tested. Otherwise you test only what is easy to generate, not what matters.

## Example

The book describes the scenario: the model automates the first message and the follow-up, a human reviews the responses, identifies the most engaged prospects and writes to them personally, then schedules a direct call. The success figures in the book (for example, a 30% increase in response rates in a B2B campaign) are anonymous and cannot be verified.

## Questions

- What is lost if the interpretation of tests is also left to the AI?
- Where is the line between "automated personalization" and "polite spam"?

## Links

- **see** [[AIM-023-a-good-chatbot-knows-when-to-hand-the-conversation-over-to|AIM-023]]: the same principle of handing over to a human, applied in support.
- **alternative** [[ADV-080-the-elements-of-an-ad-can-be-tested-as-an-experiment|ADV-080]]: conjoint testing, more efficient than A/B for many variants.
- **see** [[AIM-027-a-language-model-summarizes-text-well-but-does-not-prove|AIM-027]]: why interpretation cannot be delegated to the model.
- **see** [[DIG-076-an-a-b-test-changes-a-single-variable-starts-from-a|DIG-076]]: the rules of the A/B test: one variable, one hypothesis, a threshold set in advance.
- **see** [[AIM-022-augmented-marketing-amplifies-people-instead-of-replacing|AIM-022]]: the tiered sales interfaces, the same handover logic.

## Sources

- [[SRC-039-chatgpt-for-marketing|SRC-039]] Eldar Najafov, *ChatGPT for Marketing*, ch. 4, pp. 82–86

<!-- backlinks:start -->
## Backlinks

- [[AIM-022-augmented-marketing-amplifies-people-instead-of-replacing|AIM-022]] _see_: Augmented marketing amplifies people instead of replacing them: tiered interfaces and digital tools for frontliners
- [[AIM-025-a-marketing-prompt-is-a-mini-brief-and-the-model-s-answer|AIM-025]] _see_: A marketing prompt is a mini-brief, and the model's answer is a draft, not a deliverable
- [[SRC-039-chatgpt-for-marketing|SRC-039]]: ChatGPT for Marketing: Learn Practical Applications of ChatGPT for Marketing
<!-- backlinks:end -->
