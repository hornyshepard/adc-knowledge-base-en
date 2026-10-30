---
id: DIG-036
title: In AI-driven email, send time and frequency are optimized for the individual, not for the list
type: zettel
kind: method
skill: digital-marketing
also: [ai-marketing]
level: 2
tags: [email-marketing, send-time-optimization, automation, customer-journey]
sources:
  - SRC-037 | ch. 7 (7.2–7.6)
  - SRC-040 | section 4, ch. 2 (Contact Strategy)
status: growing
---

# In AI-driven email, send time and frequency are optimized for the individual, not for the list

> **The idea in one sentence:** besides personalized content, AI changes two variables that classic email fixed for the whole list: the send time and the pace.

## Explanation

The email chapter of Noil's book describes five AI levers:

| Lever | What it does |
|---|---|
| AI-powered segmentation | fine, dynamic groups (e.g., viewed expensive products, did not buy) |
| Predictive personalization | estimates which product will interest the person and when they will buy |
| Dynamic content generation | subject line, recommendations and text blocks change with the profile |
| Timing optimization (*send time optimization*) | each person gets the message at the time they usually open emails |
| Frequency optimization | the pace adjusts to engagement, to avoid fatigue and unsubscribes |

The book applies them to four lifecycle emails: **welcome** (recommendations based on what the person browsed before signing up), **abandoned cart** (the item left behind + related products, possibly low stock), **post-purchase** (complementary products, tutorials) and **re-engagement** (an offer for those inactive for several months).

Two warnings: over-personalization (the message feels too intrusive, as if it knows too much) and losing the brand voice in automation. Noil recommends that a person check the generated content.

Richards and McLean ([[SRC-040-intelligent-customer-engagement|SRC-040]]) add the layer of rules above the algorithm: a written **contact strategy** (maximum frequency by channel and by product, time windows) that product managers eager to send their campaigns cannot override.

## Application

- Write email flows as **scenarios** (trigger → message → continuation rule), not as isolated newsletters.
- A/B test subject lines and CTAs, but leave send time and frequency to the algorithm only once you have enough data.
- The copywriter defines the tone and the limits of the brand voice; tools such as Phrasee (subject lines generated through NLG) work inside them.

## Example

A fitness subscription service, in the book's example, sends each subscriber the weekly workout plan at the time that person usually opens emails, not at the same time for everyone.

## Questions

- What happens to the "campaign moment" (a simultaneous launch) if everyone gets the message at a different time?
- When is a lower frequency more profitable than a high one, even if the number of clicks drops?

## Links

- **extends** [[DIG-034-a-good-promotional-email-has-one-offer-a-time-deadline-and|DIG-034]]: the rules of the promotional email, with send time and frequency left to the algorithm.
- **application** [[AIM-017-ai-built-segments-are-dynamic-customers-move-between-them|AIM-017]]: email flows activate the dynamic segments.
- **application** [[AIM-016-ai-personalization-works-in-four-registers-real-time|AIM-016]]: email combines the behavioral and predictive registers.
- **see** [[DIG-069-personalization-works-only-with-relevance-respect-and|DIG-069]]: over-personalization, the risk Noil also names.
- **see** [[AIM-019-offer-what-the-customer-is-most-likely-to-accept-not-what|AIM-019]]: the contact strategy and offer arbitration in automated systems.

## Sources

- [[SRC-037-ai-driven-marketing|SRC-037]] Karen Noil, *AI-Driven Marketing*, ch. 7 (7.2–7.6)
- [[SRC-040-intelligent-customer-engagement|SRC-040]] Aly Richards & Scott McLean, *Intelligent Customer Engagement*, section 4, ch. 2

<!-- backlinks:start -->
## Backlinks

- [[AIM-003-martech-has-seven-use-cases-across-the-customer-path-from|AIM-003]] _see_: Martech has seven use cases across the customer path: from advertising and content to service CRM
- [[AIM-017-ai-built-segments-are-dynamic-customers-move-between-them|AIM-017]] _see_: AI-built segments are dynamic: customers move between them as their behavior changes
- [[AIM-019-offer-what-the-customer-is-most-likely-to-accept-not-what|AIM-019]] _see_: Offer what the customer is most likely to accept, not what brings the highest margin: one "yes" leads to another
- [[CPY-029-brand-voice-does-not-come-from-a-prompt-but-from-a-cycle|CPY-029]] _see_: Brand voice does not come from a prompt but from a cycle: examples → draft → human editing → feedback → final check
- [[DIG-034-a-good-promotional-email-has-one-offer-a-time-deadline-and|DIG-034]] _see_: A good promotional email has one offer, a time deadline and a subject line under 50 characters
- [[DIG-035-in-email-the-click-to-open-rate-says-more-than-the-open-rate|DIG-035]] _see_: In email, the click-to-open rate says more than the open rate
- [[SRC-037-ai-driven-marketing|SRC-037]]: AI-Driven Marketing: Harnessing Artificial Intelligence to Personalize Customer Experiences
- [[SRC-040-intelligent-customer-engagement|SRC-040]]: Intelligent Customer Engagement: The Future of Content Marketing
<!-- backlinks:end -->
