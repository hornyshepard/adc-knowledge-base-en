---
id: AIM-030
title: "Data ethics in AI marketing has four basic rules: consent, access and erasure, transparency, minimization"
type: zettel
kind: checklist
skill: ai-marketing
also: [digital-marketing, brand-strategy]
level: 1
tags: [ethics, gdpr, privacy, explainability, accountability]
sources:
  - SRC-037 | ch. 12 (12.1-12.5)
  - SRC-039 | ch. 3 (Privacy-by-Design Principles for Personalized Marketing, pp. 73–74)
status: growing
---

# Data ethics in AI marketing has four basic rules: consent, access and erasure, transparency, minimization

> **The idea in one sentence:** AI personalization is paid for in trust; four data rules, plus explainability and accountability, make the difference between relevant and abusive.

## Explanation

Noil sums up the principles of regulations such as the GDPR (EU) and the CCPA (California) in four rules:

| Rule | What it means |
|---|---|
| Consent | explicit consent before personal data is collected or used for marketing |
| Right to access and erasure | people can see what data you hold about them and ask for it to be deleted |
| Transparency | you explain clearly what you collect and what you use it for |
| Data minimization | you collect only what you need |

On top of these, the chapter adds three obligations specific to AI:

- **Explainability**: complex models are "black boxes"; if you cannot explain why someone saw an ad or was refused a loan, you have a problem of trust and of compliance.
- **Accountability**: if a chatbot gives incorrect information, the company is responsible, not "the algorithm".
- **Anonymization** (tokenization, aggregation): you use the data for patterns without exposing individuals.

Algorithmic bias appears as a separate risk, covered in [[AIM-032-bias-in-ai-marketing-has-two-sources-the-data-the-model|AIM-032]].

Najafov ([[SRC-039-chatgpt-for-marketing|SRC-039]]) reaches the same list from the opposite direction, that of design. His **privacy-by-design** principles for personalization add three elements: anonymization, **user control** (view, edit, delete, opt out of personalized marketing) and regular audits of data practices. The convergence of the two books shows that the list is already an industry standard, not one author's opinion. The same list also appears in the work of the lawyer Raj Sachdev ([[DIG-065-ten-privacy-practices-for-marketers-from-consent-that-shows|DIG-065]]).

## Application

- Before a personalized campaign, go through the four rules like a checklist.
- Write a sentence you could say to the end customer: "You are seeing this because…". If it sounds embarrassing, rethink the mechanism.
- For brand strategy: transparency about data can itself be a differentiating message.

## Example

The example in the book: a real estate platform using AI to target ads has to audit its data and its output, so that the algorithm does not favor or exclude people based on race, gender or socioeconomic status.

## Questions

- Is consent obtained through a cookie banner that nobody reads real consent?
- Where does "useful personalization" end and manipulation begin?

## Links

- **see** [[AIM-016-ai-personalization-works-in-four-registers-real-time|AIM-016]]: over-personalization is the commercial version of the same problem.
- **see** [[AIM-033-disclose-when-you-use-ai-a-transparency-toolkit-and-an|AIM-033]]: transparency toward the public about content generated with AI.
- **see** [[AIM-032-bias-in-ai-marketing-has-two-sources-the-data-the-model|AIM-032]]: algorithmic bias, covered in depth.
- **see** [[AIM-023-a-good-chatbot-knows-when-to-hand-the-conversation-over-to|AIM-023]]: the chatbot is where accountability for AI errors becomes visible.
- **see** [[DIG-065-ten-privacy-practices-for-marketers-from-consent-that-shows|DIG-065]]: ten privacy practices for marketers, the same list seen by a lawyer.
- **see** [[DIG-063-valid-consent-is-asked-for-actively-and-can-be-withdrawn|DIG-063]]: what valid consent looks like in practice.

## Sources

- [[SRC-037-ai-driven-marketing|SRC-037]] Karen Noil, *AI-Driven Marketing*, ch. 12 (12.1-12.5)
- [[SRC-039-chatgpt-for-marketing|SRC-039]] Eldar Najafov, *ChatGPT for Marketing*, ch. 3, pp. 73–74

<!-- backlinks:start -->
## Backlinks

- [[AIM-010-accuracy-or-transparency-ensembles-and-neural-networks|AIM-010]] _see_: Accuracy or transparency: ensembles and neural networks predict but do not explain
- [[AIM-016-ai-personalization-works-in-four-registers-real-time|AIM-016]] _see_: AI personalization works in four registers: real-time, behavioral, micro-segment and predictive
- [[AIM-023-a-good-chatbot-knows-when-to-hand-the-conversation-over-to|AIM-023]] _see_: A good chatbot knows when to hand the conversation over to a human
- [[AIM-028-visual-listening-finds-the-brand-in-images-where-the-text|AIM-028]] _see_: Visual listening finds the brand in images, where the text does not name it
- [[AIM-032-bias-in-ai-marketing-has-two-sources-the-data-the-model|AIM-032]] _see_: Bias in AI marketing has two sources: the data the model learns from and people's blind trust in the recommendation
- [[AIM-033-disclose-when-you-use-ai-a-transparency-toolkit-and-an|AIM-033]] _extends_: Disclose when you use AI: a transparency toolkit and an eight-point ethical checklist
- [[DIG-062-the-first-party-data-strategy-starts-from-the-question-what|DIG-062]] _see_: The first-party data strategy starts from the question "What data can I use to drive sales?" and gets the data through invitation and value exchange, not hidden collection
- [[DIG-063-valid-consent-is-asked-for-actively-and-can-be-withdrawn|DIG-063]] _see_: Valid consent is asked for actively and can be withdrawn just as easily: equal buttons, unticked boxes, purposes explained, proof kept
- [[DIG-065-ten-privacy-practices-for-marketers-from-consent-that-shows|DIG-065]] _see_: Ten privacy practices for marketers, from consent that shows the value provided to data minimization
- [[HIS-020-political-advertising-learned-from-commercial-advertising|HIS-020]] _see_: Political advertising learned from commercial advertising: from the Eisenhower spots to "Daisy"
- [[MAP-003-ethics-regulation-and-responsibility-in-advertising|MAP-003]]: Ethics, regulation and responsibility in advertising
- [[SRC-037-ai-driven-marketing|SRC-037]]: AI-Driven Marketing: Harnessing Artificial Intelligence to Personalize Customer Experiences
- [[SRC-039-chatgpt-for-marketing|SRC-039]]: ChatGPT for Marketing: Learn Practical Applications of ChatGPT for Marketing
<!-- backlinks:end -->
