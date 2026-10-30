---
id: DIG-050
title: "Programmatic advertising buys every impression automatically, through real-time bidding: it gains efficiency but needs data, large budgets and control over placement"
type: zettel
kind: concept
skill: digital-marketing
also: [advertising-strategy, ai-marketing]
level: 2
tags: [programmatic, rtb, ad-server, ad-network, ad-exchange, dsp, ssp, dmp, ctv, context-matching]
sources:
  - SRC-029 | ch. 10, pp. 272–275
  - SRC-032 | ch. 2.3.4.1, pp. 76–77; ch. 5.1, pp. 159–171
status: growing
---

# Programmatic advertising buys every impression automatically, through real-time bidding: it gains efficiency but needs data, large budgets and control over placement

> **The idea in one sentence:** in programmatic advertising, algorithms decide in milliseconds, for each impression, whether to buy it and at what price, while the page is loading.

## Explanation

At first, banners were hard coded into web pages and every visitor saw the same ad. Both books then describe the same evolution:

- **The ad server** stores, serves and tracks ads. It allows *roadblocks* (one advertiser takes over the page), *frequency capping* and **sequencing** (ads shown to a user in a particular order).
- **The ad network** collects inventory from publishers and sells it to advertisers in categories. Prices are stable, but transparency is low, unsold inventory remains, and the same person sees the ad too many times across different networks.
- **The ad exchange** is an open marketplace with **real-time bidding** (RTB). The advertiser sets the maximum CPM, the publisher the floor price, and the system decides instantly.
- **The DSP** is the advertiser's software that bids across several exchanges, **the SSP** is the publisher's software, and **the DMP** stores audience data (first-, second- and third-party).

Schwarz-Musch et al. report that in 2022 the global share of programmatic advertising was around 87% (PwC/IAB). Creative work can be adapted to each profile through dynamic banners, billing can be tied to any measurable KPI, and the model extends to connected TV.

**Where the authors differ.** Zahay et al. treat programmatic as the operating standard; their cascade of objectives includes the target "100% Programmatic in Two Years." Schwarz-Musch et al. add Lammenett's critique. Programmatic is only effective with a very large amount of data and five- to six-figure budgets. It optimizes toward click-through rates and impressions, although the setting in which the ad appears matters (*context matching*). And it brings a loss of control.

## Application

- Before you recommend programmatic, check the client's budget and data volume.
- Ask for the list of websites and the brand safety and anti-fraud settings, not only the CPM achieved.
- Define the goals and KPIs yourself; unlike Meta or Google, programmatic platforms do not select them for you at the start.
- Think of the creative work as a series: sequencing and frequency capping are also narrative tools.

## Example

The kitchen case in SRC-032 runs through the whole chain: real estate data in a DMP, a DSP for reach and dynamic banners that change the kitchen and the price to fit the profile.

## Questions

- If the algorithm chooses the placement, who is responsible for the setting in which the ad appears?
- What brand safety risks come with automated buying across thousands of websites?

## Links

- **foundation** [[DIG-046-display-advertising-has-moved-from-the-static-banner-to|DIG-046]]: display formats are the raw material of programmatic buying.
- **see** [[DIG-051-the-kitchen-case-anonymized-real-estate-data-a-dmp-a-dsp|DIG-051]]: the kitchen case, programmatic from start to finish.
- **see** [[DIG-054-quality-settings-decide-whether-paid-impressions-count|DIG-054]]: automation makes brand safety, viewability and frequency settings mandatory.
- **see** [[DIG-064-identity-without-cookies-has-three-levels-of-reach-your-own|DIG-064]]: the identity that programmatic targeting depends on after cookies.
- **contradicts** [[ADV-085-the-effectiveness-of-digital-advertising-remains-unproven|ADV-085]]: Percy and Rosenbaum-Elliott consider the effectiveness of digital advertising unproven, with fraud and doubtful viewability.

## Sources

- [[SRC-029-digital-marketing-foundations-and-strategy|SRC-029]] Zahay et al., *Digital Marketing: Foundations and Strategy*, ch. 10, pp. 272–275
- [[SRC-032-digital-advertising-in-post-cookies-era|SRC-032]] Schwarz-Musch, Tauchhammer, Guetz, *Digital Advertising in the Post-cookie Era*, ch. 2.3.4.1 (pp. 76–77) and 5.1 (pp. 159–171)

<!-- backlinks:start -->
## Backlinks

- [[AIM-010-accuracy-or-transparency-ensembles-and-neural-networks|AIM-010]] _see_: Accuracy or transparency: ensembles and neural networks predict but do not explain
- [[DIG-046-display-advertising-has-moved-from-the-static-banner-to|DIG-046]] _see_: Display advertising has moved from the static banner to rich media and video, but the creative idea stays human
- [[DIG-051-the-kitchen-case-anonymized-real-estate-data-a-dmp-a-dsp|DIG-051]] _example_: The kitchen case: anonymized real estate data, a DMP, a DSP and dynamic banners turn a flyer for everyone into an offer for each household
- [[DIG-054-quality-settings-decide-whether-paid-impressions-count|DIG-054]] _see_: Quality settings decide whether paid impressions count: brand safety, viewability and the frequency cap
- [[DIG-055-ad-fraud-is-detected-during-the-campaign-through-anomalies|DIG-055]] _see_: Ad fraud is detected during the campaign, through anomalies, not after it, and paying only for verified sales makes it unattractive
- [[DIG-056-contextual-targeting-follows-the-page-behavioral-targeting|DIG-056]] _foundation_: Contextual targeting follows the page, behavioral targeting follows the person
- [[DIG-064-identity-without-cookies-has-three-levels-of-reach-your-own|DIG-064]] _see_: Identity without cookies has three levels of reach: your own channels or a single "walled garden," data clean rooms and universal IDs
- [[SRC-029-digital-marketing-foundations-and-strategy|SRC-029]]: Digital Marketing: Foundations and Strategy (5th ed.)
- [[SRC-032-digital-advertising-in-post-cookies-era|SRC-032]]: Digital Advertising in the Post-cookie Era: Strategic Campaign Planning Across the Customer Journey
<!-- backlinks:end -->
