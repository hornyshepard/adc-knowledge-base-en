---
id: DIG-064
title: 'Identity without cookies has three levels of reach: your own channels or a single "walled garden," data clean rooms and universal IDs'
type: zettel
kind: framework
skill: digital-marketing
also: [advertising-strategy]
level: 3
tags: [identity-management, data-clean-rooms, universal-id, walled-gardens, pair, uid2]
sources:
  - SRC-032 | ch. 1.3.5.2, pp. 31–34
status: growing
---

# Identity without cookies has three levels of reach: your own channels or a single "walled garden," data clean rooms and universal IDs

> **The idea in one sentence:** the more networks you want to recognize your customers on, the more complex the identity infrastructure you need, and each level has a different balance between reach and privacy.

## Explanation

Identity management aims to ensure that users can be recognized at any touchpoint, over time, in a technically and legally compliant way (through login, email address, DMP ID), so that a unique user profile can be built. The authors describe three levels:

| Level | Where you use the data | Reach |
|---|---|---|
| 1 | on your own touchpoints or in a single network (Meta, Google, Amazon) | low; the more you narrow the audience, the more you run into reach limitations |
| 2 | across multiple networks, through *data clean rooms* | medium |
| 3 | on many networks, through a universal ID | high |

**Data clean rooms** are cloud-based solutions in which several parties (advertisers, publishers) analyze their data sets together under strict data protection guidelines. Encrypted identifiers, for example *hashed* email addresses, link the data sets without revealing personal data, and the results come out only in aggregated form (cohorts, reports). There are *media clean rooms*, run by the walled gardens: Google's Ads Data Hub and PAIR, Amazon Marketing Cloud (which also aggregates Whole Foods and Twitch data); and *partner clean rooms*, individual collaborations through Snowflake or LiveRamp. Disney has built one that gives advertisers access to over 1,000 first-party data segments.

**The universal ID**: first-party data is synchronized with a unique identifier shared across publishers, stored in first-party cookies or persistent IDs. Providers: Unified ID, UID2.0, ID5, IdentityLink, SharedID and many more; the industry wants a single standard. If this vision is realized, advertising would look almost identical to the era of third-party cookies; cookie blockers can still stop it.

## Application

- For a small client: your own channels + one large network. For a large FMCG brand with a retail partner: a clean room.
- Ask the vendor what data leaves the clean room: only aggregates, or user lists too?

## Example

Disney opens over 1,000 segments from its own data to advertisers without handing over the raw data, and Amazon combines its purchase data with Whole Foods and Twitch data in the same clean room.

## Questions

- If the universal ID practically rebuilds the world of cookies, has anything been gained for privacy?

## Links

- **extends** [[DIG-062-the-first-party-data-strategy-starts-from-the-question-what|DIG-062]]: first-party data is the raw material of the three levels.
- **see** [[DIG-057-third-party-cookies-made-retargeting-lookalikes-and-cross|DIG-057]]: why a new identity infrastructure became necessary.
- **see** [[DIG-050-programmatic-advertising-buys-every-impression|DIG-050]]: programmatic buying uses these identities for automated purchasing.
- **see** [[DIG-054-quality-settings-decide-whether-paid-impressions-count|DIG-054]]: the frequency cap requires deduplication through identity solutions.

## Sources

- [[SRC-032-digital-advertising-in-post-cookies-era|SRC-032]] Schwarz-Musch, Tauchhammer, Guetz, *Digital Advertising in the Post-cookie Era*, ch. 1.3.5.2 (pp. 31–34)

<!-- backlinks:start -->
## Backlinks

- [[DIG-050-programmatic-advertising-buys-every-impression|DIG-050]] _see_: Programmatic advertising buys every impression automatically, through real-time bidding: it gains efficiency but needs data, large budgets and control over placement
- [[DIG-062-the-first-party-data-strategy-starts-from-the-question-what|DIG-062]] _see_: The first-party data strategy starts from the question "What data can I use to drive sales?" and gets the data through invitation and value exchange, not hidden collection
- [[SRC-032-digital-advertising-in-post-cookies-era|SRC-032]]: Digital Advertising in the Post-cookie Era: Strategic Campaign Planning Across the Customer Journey
<!-- backlinks:end -->
