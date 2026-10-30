---
id: AIM-017
title: "AI-built segments are dynamic: customers move between them as their behavior changes"
type: zettel
kind: concept
skill: ai-marketing
also: [marketing-fundamentals, digital-marketing]
level: 2
tags: [segmentation, micro-segments, churn, predictive-segmentation]
sources:
  - SRC-037 | ch. 4 (4.1-4.6)
status: growing
---

# AI-built segments are dynamic: customers move between them as their behavior changes

> **The idea in one sentence:** in classic segmentation the customer "sits" in a segment; in AI segmentation the segment is a temporary state, recalculated as behavior changes.

## Explanation

Noil contrasts traditional segmentation, which treats customers as static entities (demographic data that is rarely updated), with AI-powered segmentation, which is **dynamic**: the algorithm keeps reassessing which segment each person belongs to. The book describes four types:

- **behavioral**: by interactions (purchases, email engagement, social media activity);
- **psychographic**: by values and lifestyle, inferred from reviews and posts (e.g., travelers who prioritize sustainable travel);
- **real-time**: someone browsing for gifts during a holiday season is placed at once in a real-time segment that triggers gift recommendations and holiday promotions;
- **predictive**: grouping by what people are likely to do, not by what they have done (e.g., customers of a subscription box service at risk of canceling, spotted through declining engagement with emails, fewer interactions with the website and negative feedback).

The central idea is the **dynamic hyper-segment**: a customer who frequently shops for athletic wear and starts showing interest in formal wear is moved automatically to a new hyper-segment, and the messages follow.

The book warns against **over-segmentation**: too many micro-segments produce fragmented campaigns that are hard to manage and to produce creative work for.

## Application

- Define segments as **entry and exit rules** ("joins if…, leaves if…"), not as fixed portraits.
- Set a practical limit on the number of segments for which you can produce different messages; the rest get the standard version.
- For churn, build a "high-risk" segment with clear signals and a dedicated retention message.

## Example

In the book's hypothetical example, an online streaming service like Netflix might isolate a micro-segment of users who enjoy both horror films and 1980s nostalgia, and recommend them a 1980s horror series.

## Questions

- If the segment changes every week, what is left of the idea of a brand campaign's "target"?
- When does fine segmentation cost more (production, testing) than it gains in relevance?

## Links

- **foundation** [[AIM-016-ai-personalization-works-in-four-registers-real-time|AIM-016]]: the micro-segment is one of the four registers of personalization.
- **application** [[AIM-006-predictive-analytics-estimates-who-will-buy-what-will-sell|AIM-006]]: predictive segmentation uses churn and CLV models directly.
- **see** [[AIM-009-classification-trees-turn-a-database-into-a-few-if-then|AIM-009]]: classification trees, a concrete tool for finding micro-segments.
- **see** [[DIG-061-data-driven-marketing-targets-segments-of-one-and-starts|DIG-061]]: the "segment of one" from Marketing 5.0, the same idea taken to its limit.
- **see** [[DIG-036-in-ai-driven-email-send-time-and-frequency-are-optimized|DIG-036]]: email is the channel where dynamic segments are activated most often.
- **see** [[INS-085-personas-not-segments-ozzy-osbourne-and-prince-charles-have|INS-085]]: the segment says whom you reach, the persona says how to talk to them.

## Sources

- [[SRC-037-ai-driven-marketing|SRC-037]] Karen Noil, *AI-Driven Marketing*, ch. 4 (4.1-4.6)

<!-- backlinks:start -->
## Backlinks

- [[AIM-009-classification-trees-turn-a-database-into-a-few-if-then|AIM-009]] _application_: Classification trees turn a database into a few "if-then" rules for targeting
- [[AIM-016-ai-personalization-works-in-four-registers-real-time|AIM-016]] _see_: AI personalization works in four registers: real-time, behavioral, micro-segment and predictive
- [[DIG-036-in-ai-driven-email-send-time-and-frequency-are-optimized|DIG-036]] _application_: In AI-driven email, send time and frequency are optimized for the individual, not for the list
- [[DIG-061-data-driven-marketing-targets-segments-of-one-and-starts|DIG-061]] _see_: Data-driven marketing targets "segments of one" and starts with a narrow objective, not with an IT project
- [[INS-084-the-importance-of-an-attribute-changes-with-life-stage-a|INS-084]] _see_: The importance of an attribute changes with life stage: "a brand I trust" matters hugely at ages 4–8 and hardly at all for pre-teens
- [[INS-085-personas-not-segments-ozzy-osbourne-and-prince-charles-have|INS-085]] _see_: Personas, not segments: Ozzy Osbourne and Prince Charles have the same demographic profile
- [[MKT-014-stp-is-done-in-five-steps-strategy-segmentation|MKT-014]] _contradicts_: STP is done in five steps: strategy, segmentation, attractiveness, choice of target, positioning
- [[SRC-037-ai-driven-marketing|SRC-037]]: AI-Driven Marketing: Harnessing Artificial Intelligence to Personalize Customer Experiences
<!-- backlinks:end -->
