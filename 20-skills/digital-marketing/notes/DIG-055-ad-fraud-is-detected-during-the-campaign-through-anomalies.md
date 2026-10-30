---
id: DIG-055
title: Ad fraud is detected during the campaign, through anomalies, not after it, and paying only for verified sales makes it unattractive
type: zettel
kind: checklist
skill: digital-marketing
also: [client-business]
level: 2
tags: [ad-fraud, bots, domain-spoofing, programmatic, verification, anomalies]
sources:
  - SRC-032 | ch. 2.3.4.2, p. 78; ch. 5.1.1.2, p. 162; ch. 5.2.3, pp. 175–177
status: growing
---

# Ad fraud is detected during the campaign, through anomalies, not after it, and paying only for verified sales makes it unattractive

> **The idea in one sentence:** in programmatic advertising, some of the impressions and clicks can be produced by bots; the advertiser defends itself by checking vendors, tracking anomalies in real time and using billing models that are hard to fake.

## Explanation

**Types of fraud** (after Sadeghpour and Vlajic): *placement fraud* (ads on fraudulent sites or in invisible sections of legitimate sites), *traffic fraud* (bots and "click farms" that inflate impressions and clicks), *action fraud* (fake form submissions and purchases, generated to claim revenue). Programmatic campaigns tend to have a higher rate of ad fraud than traditional digital ones. *Domain spoofing*: traffic is redirected to a domain that looks like a legitimate one, sometimes to recreated copies of trusted websites.

**Recommended measures:**

- ask the programmatic platforms and real-time bidding vendors for their anti-fraud precautions and certificates;
- whitelists of publishers and ad verification of the placement;
- a performance KPI with a billing model that only charges for verified purchases in your own store, because those do not interest fraudsters (but this fits only campaigns with a sales goal);
- watch for anomalies: unusually high click-through rates, traffic from distant countries at suspicious times, impressions that last 1 second on average, "views" with no human interaction; a bot can even falsify the viewability rate by scrolling;
- randomly test touchpoints: legitimate ones have an imprint (publisher identification) and are listed in trustworthy advertising lists;
- use automated detection during the campaign, not analysis afterwards.

## Application

- Set alarm thresholds (click-through rate, geography, time of day) before launch and check weekly.
- When a report shows "too good" results, treat it as a signal to check, not as a success.

## Example

With your own ad server, the anomaly is easy to spot: 1,000 clicks at 4 a.m. on 10,000 ad impressions, when on a normal day only 50 impressions with 2 clicks are served at that time.

## Questions

- Who pays for the fraudulent impressions discovered after the campaign: the advertiser, the agency or the platform?

## Links

- **see** [[DIG-054-quality-settings-decide-whether-paid-impressions-count|DIG-054]]: the campaign's other quality settings.
- **see** [[DIG-042-the-media-billing-model-is-chosen-by-objective-and-customer|DIG-042]]: the CPA payment model as protection.
- **see** [[DIG-050-programmatic-advertising-buys-every-impression|DIG-050]]: why programmatic buying is more exposed.
- **see** [[SOC-029-an-influencer-s-audience-is-checked-before-any-contract|SOC-029]]: fraud signals are also checked before signing with an influencer.
- **see** [[ADV-085-the-effectiveness-of-digital-advertising-remains-unproven|ADV-085]]: fraud is one of the reasons the effectiveness of digital advertising remains disputed.

## Sources

- [[SRC-032-digital-advertising-in-post-cookies-era|SRC-032]] Schwarz-Musch, Tauchhammer, Guetz, *Digital Advertising in the Post-cookie Era*, ch. 2.3.4.2 (p. 78), 5.1.1.2 (p. 162), 5.2.3 (pp. 175–177)

<!-- backlinks:start -->
## Backlinks

- [[ADV-085-the-effectiveness-of-digital-advertising-remains-unproven|ADV-085]] _see_: The effectiveness of digital advertising remains unproven, and the book sees social media as a "negotiated" medium, hit by fraud and poor visibility
- [[DIG-042-the-media-billing-model-is-chosen-by-objective-and-customer|DIG-042]] _see_: The media billing model is chosen by objective and customer journey stage: CPM for awareness, CPV/CPE for appeal, CPC/CPL for ask, CPA for purchase
- [[DIG-054-quality-settings-decide-whether-paid-impressions-count|DIG-054]] _see_: Quality settings decide whether paid impressions count: brand safety, viewability and the frequency cap
- [[SOC-029-an-influencer-s-audience-is-checked-before-any-contract|SOC-029]] _see_: An influencer's audience is checked before any contract: fraud signals, engagement authenticity and audience fit, manually or with AI
- [[SRC-032-digital-advertising-in-post-cookies-era|SRC-032]]: Digital Advertising in the Post-cookie Era: Strategic Campaign Planning Across the Customer Journey
<!-- backlinks:end -->
