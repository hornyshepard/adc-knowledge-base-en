---
id: DIG-054
title: "Quality settings decide whether paid impressions count: brand safety, viewability and the frequency cap"
type: zettel
kind: checklist
skill: digital-marketing
also: [advertising-strategy, brand-strategy]
level: 2
tags: [brand-safety, viewability, frequency-capping, ad-server, whitelist, blacklist]
sources:
  - SRC-032 | ch. 2.3.4.2, pp. 78–79; ch. 5.1.1.2, p. 161; ch. 5.2.1, p. 172; ch. 5.2.3, pp. 174–177
status: growing
---

# Quality settings decide whether paid impressions count: brand safety, viewability and the frequency cap

> **The idea in one sentence:** an impression served next to toxic content, never seen or repeated too many times costs money and can also cost reputation.

## Explanation

**Brand safety**: the certainty that the ad will only be displayed in a brand-compliant environment. The authors cite eight key problematic content categories (Integral Ad Science): adult content, alcohol, hate speech, illegal downloads, illegal drugs, offensive language, controversial news, violence. Tools: whitelists (only verified sites), blacklists, category filters and services such as DoubleVerify, which crawl and semantically evaluate pages. In programmatic advertising there have been cases of ads displayed in a racist or sexual context.

**Viewability**: the MRC standard counts a display ad as viewed if at least 50% of its pixels are visible for one continuous second; for video, 50% for two consecutive seconds. A caution: in chapter 5 the same book gives a stricter criterion (more than 2 seconds and at least 80% visible), so the standard has to be written into the contract. Averages can mislead: look at the distribution, how many saw it for under a second and how many to the end.

**The frequency cap**: the maximum number of exposures per user. For it to work, all paid touchpoints have to be measured, including digital TV and radio. Without a central ad server, each publisher counts its "unique" users separately, the overlap stays invisible, the frequency of exposure is underestimated and costs rise. Capping relied on third-party cookies; identity solutions are now being built (email hashes, device IDs).

## Application

- Before launch: the exclusion list, the viewability standard, the frequency cap per user and per period.
- Ask for reports on these three dimensions, not only impressions and clicks.
- For clients with many campaigns a year, consider their own ad server: centralized reporting, real reach without audience overlap, data that stays with the client when it changes agencies.

## Example

In the awareness campaign for the AI video creation software, the company sets a limit of four exposures per person. Without deduplication across sites, the same person could have received many more, each one paid for separately.

## Questions

- A very strict whitelist reduces the risk, but also the reach. How do you find the balance?

## Links

- **see** [[DIG-055-ad-fraud-is-detected-during-the-campaign-through-anomalies|DIG-055]]: ad fraud, the fourth quality setting.
- **see** [[DIG-059-contextual-targeting-places-the-ad-next-to-the-topic|DIG-059]]: brand safety in contextual targeting.
- **see** [[DIG-050-programmatic-advertising-buys-every-impression|DIG-050]]: programmatic automation makes these settings mandatory.
- **see** [[ADV-054-a-media-plan-is-judged-by-reach-at-the-minimum-effective|ADV-054]]: the media plan is judged by reach at the minimum effective frequency.
- **see** [[ADV-085-the-effectiveness-of-digital-advertising-remains-unproven|ADV-085]]: poor viewability and fraud, the reasons why Percy and Rosenbaum-Elliott see digital effectiveness as unproven.
- **see** [[ADV-076-the-communication-budget-is-built-from-objectives-and-tasks|ADV-076]]: frequency is the "advertising pressure" in the budget calculation.

## Sources

- [[SRC-032-digital-advertising-in-post-cookies-era|SRC-032]] Schwarz-Musch, Tauchhammer, Guetz, *Digital Advertising in the Post-cookie Era*, ch. 2.3.4.2 (pp. 78–79), 5.1.1.2 (p. 161), 5.2.1 (p. 172), 5.2.3 (pp. 174–177)

<!-- backlinks:start -->
## Backlinks

- [[ADV-054-a-media-plan-is-judged-by-reach-at-the-minimum-effective|ADV-054]] _see_: A media plan is judged by reach at the minimum effective frequency, not by GRPs or average frequency, and when in doubt it is better to choose frequency
- [[DIG-047-on-mobile-an-ad-has-less-than-a-second-to-be-seen-faces|DIG-047]] _see_: On mobile, an ad has less than a second to be seen: faces, contrast and instant emotion
- [[DIG-050-programmatic-advertising-buys-every-impression|DIG-050]] _see_: Programmatic advertising buys every impression automatically, through real-time bidding: it gains efficiency but needs data, large budgets and control over placement
- [[DIG-055-ad-fraud-is-detected-during-the-campaign-through-anomalies|DIG-055]] _see_: Ad fraud is detected during the campaign, through anomalies, not after it, and paying only for verified sales makes it unattractive
- [[DIG-059-contextual-targeting-places-the-ad-next-to-the-topic|DIG-059]] _see_: Contextual targeting places the ad next to the topic already on the reader's mind, and the semantic version also reads the sentiment of the context
- [[DIG-064-identity-without-cookies-has-three-levels-of-reach-your-own|DIG-064]] _see_: Identity without cookies has three levels of reach: your own channels or a single "walled garden," data clean rooms and universal IDs
- [[SRC-032-digital-advertising-in-post-cookies-era|SRC-032]]: Digital Advertising in the Post-cookie Era: Strategic Campaign Planning Across the Customer Journey
<!-- backlinks:end -->
