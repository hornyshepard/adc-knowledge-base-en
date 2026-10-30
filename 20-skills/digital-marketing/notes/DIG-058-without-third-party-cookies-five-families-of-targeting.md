---
id: DIG-058
title: Without third-party cookies five families of targeting remain, and the cookie profile described a device, not a person, anyway
type: zettel
kind: framework
skill: digital-marketing
also: [advertising-strategy, ai-marketing]
level: 2
tags: [targeting, post-cookie, contextual, semantic, predictive, cohorts, topics-api, first-party]
sources:
  - SRC-032 | ch. 1.2.3–1.3.4, pp. 19–26
status: growing
---

# Without third-party cookies five families of targeting remain, and the cookie profile described a device, not a person, anyway

> **The idea in one sentence:** losing cookies is not as big a loss as it seems, because the profiles were imprecise, and targeting without them has existed since the beginnings of advertising.

## Explanation

**The hidden limit of cookies.** The profile built from browsing behavior belongs to a client device (a mobile phone, tablet, smart TV), which several people can use. Without logging in, a person's browsing behavior cannot be measured across devices. So an accurate profile of an individual never existed. The authors argue that some campaigns based on targeting without profiles can even be more efficient.

**The five options**, used individually or in combination:

| Option | Principle | Limit |
|---|---|---|
| Contextual | the ad appears in a relevant thematic environment | homonyms, sensitive contexts, limited inventory |
| Semantic | AI understands the whole context (text, image, video, sentiment), in real time | needs technology and quality data |
| Predictive | machine learning on collected data predicts future actions | precision depends on the data and the algorithm |
| Cohort / interest | groups of users who share common characteristics, not individuals | privacy controversy, needs a very large database |
| First-party | data given voluntarily by customers | limited reach, needs a value exchange |

On cohorts: in 2022 Google discontinued FLoC (numeric IDs) and moved to the Topics API. Interests are determined locally, in the browser, grouped into themes and deleted periodically, without being sent to Google. The criticisms remain: very narrow cohorts can identify individuals, and with over 60% of the browser market Google can increase its market power in advertising.

Each option usually covers a single objective; that is why the authors propose a campaign process that combines them with personas and the customer journey.

## Application

- For each campaign objective, choose the combination: context for awareness, first-party and predictive for conversion.
- Do not buy "audiences" without asking what they are based on: context, cohort, own data or purchased data?

## Example

An e-bike online shop can use context (cycling websites), first-party data (existing buyers) and prediction (people who often read the blog are probably interested in touring backpacks), without a single third-party cookie.

## Questions

- If the profiles were so imprecise, why was the industry so dependent on them?

## Links

- **foundation** [[DIG-057-third-party-cookies-made-retargeting-lookalikes-and-cross|DIG-057]]: why third-party cookies are disappearing.
- **see** [[DIG-056-contextual-targeting-follows-the-page-behavioral-targeting|DIG-056]]: the basic distinction: targeting by the page or by the person.
- **see** [[DIG-059-contextual-targeting-places-the-ad-next-to-the-topic|DIG-059]]: contextual and semantic targeting in detail.
- **see** [[DIG-060-predictive-targeting-moves-the-question-from-who-the-person|DIG-060]]: predictive targeting and context triggers.
- **see** [[DIG-062-the-first-party-data-strategy-starts-from-the-question-what|DIG-062]]: the first-party data strategy.

## Sources

- [[SRC-032-digital-advertising-in-post-cookies-era|SRC-032]] Schwarz-Musch, Tauchhammer, Guetz, *Digital Advertising in the Post-cookie Era*, ch. 1.2.3–1.3.4 (pp. 19–26)

<!-- backlinks:start -->
## Backlinks

- [[DIG-056-contextual-targeting-follows-the-page-behavioral-targeting|DIG-056]] _see_: Contextual targeting follows the page, behavioral targeting follows the person
- [[DIG-057-third-party-cookies-made-retargeting-lookalikes-and-cross|DIG-057]] _see_: Third-party cookies made retargeting, lookalikes and cross-site profiles possible, and the law and browsers are taking them out of the game: power shifts to first-party data
- [[DIG-059-contextual-targeting-places-the-ad-next-to-the-topic|DIG-059]] _extends_: Contextual targeting places the ad next to the topic already on the reader's mind, and the semantic version also reads the sentiment of the context
- [[DIG-060-predictive-targeting-moves-the-question-from-who-the-person|DIG-060]] _extends_: Predictive targeting moves the question from "who the person was" to "what they will probably do" and can use context triggers such as weather, place and time
- [[DIG-062-the-first-party-data-strategy-starts-from-the-question-what|DIG-062]] _extends_: The first-party data strategy starts from the question "What data can I use to drive sales?" and gets the data through invitation and value exchange, not hidden collection
- [[SRC-032-digital-advertising-in-post-cookies-era|SRC-032]]: Digital Advertising in the Post-cookie Era: Strategic Campaign Planning Across the Customer Journey
<!-- backlinks:end -->
