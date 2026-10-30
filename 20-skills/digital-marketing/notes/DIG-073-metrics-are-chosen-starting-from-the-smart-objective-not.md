---
id: DIG-073
title: "Metrics are chosen starting from the SMART objective, not from what the platform offers: in a chain that runs from the baseline to the diagnosis"
type: zettel
kind: method
skill: digital-marketing
also: [advertising-strategy]
level: 2
tags: [metrics, smart-objectives, traffic, audience, campaign, ga4, engagement-rate, diagnosis]
sources:
  - SRC-029 | ch. 5, pp. 130, 137–142
status: growing
---

# Metrics are chosen starting from the SMART objective, not from what the platform offers: in a chain that runs from the baseline to the diagnosis

> **The idea in one sentence:** the only way to bring order to the mass of metrics is to map each SMART objective explicitly to the metrics that measure it, starting from a baseline and drilling down to the point where the process breaks.

## Explanation

Zahay et al. divide web metrics into three families:

| Family | Examples |
|---|---|
| Traffic | impressions, page views, sessions, click-throughs |
| Audience | unique or repeat visitors, unidentified or identified, entry and exit pages, bounce rate, shopping cart abandonment |
| Campaign | results by channel, by offer, by keyword |

All of them make sense only over a specified period of time. GA4 replaced the bounce rate with the **engagement rate**: someone who reads an article for 45 seconds and leaves is not a failure.

The decisive filter is **SMART objectives**: specific, measurable, achievable, realistic, with a time frame. For "Increase Number of Email Captures by 5% in Q1", the metrics climb a chain. They start from unique visitors and the referral source, go through registrations started and not completed, and arrive at the **last form box completed**, which shows where people get stuck. Each metric answers a decision question. The second filter is the stage of the journey, with metrics specific to each stage.

Branding objectives also require attitudinal research (perception, intention). Behavioral data from the platform cannot measure them on their own.

## Application

- Write the objective in SMART format before you open the dashboard.
- For each objective, build a chain: baseline → intermediate behavior → result → diagnosis (where it breaks).
- Do not compare campaigns on traffic metrics if they have different objectives.

## Example

"Reactivate 10,000 Lapsed Customers in Q4" calls for several measurements: emails sent, a reactivation message tested A/B, click-throughs on each variant, bounces from the landing page and incentive offers accepted (10 percent off, $5 off or a free gift).

## Questions

- Which metrics in the three families say something about the brand, and which only about activity?
- What do you do when the client's objective cannot be written in SMART form?

## Links

- **foundation** [[DIG-072-a-metric-is-just-a-number-it-becomes-a-kpi-when-it-is|DIG-072]]: the distinction between metric and KPI comes before choosing the metrics.
- **see** [[DIG-074-each-stage-of-the-journey-has-its-own-kpis-net-reach-and|DIG-074]]: the second filter, the metrics and KPIs specific to each stage of the journey.
- **application** [[DIG-075-the-conversion-funnel-shows-where-visitors-leave-the|DIG-075]]: the conversion funnel is the detailed diagnosis of the purchase stage.
- **application** [[DIG-076-an-a-b-test-changes-a-single-variable-starts-from-a|DIG-076]]: conversion and reactivation objectives are reached through A/B tests.
- **see** [[BRF-007-the-objective-in-the-brief-is-a-communication-objective|BRF-007]]: in the brief, too, the objective has to be specific and falsifiable.
- **see** [[ADV-078-numerical-goals-are-set-per-ad-for-exposure-and-processing|ADV-078]]: Percy and Rosenbaum-Elliott set numerical targets per ad and per campaign.

## Sources

- [[SRC-029-digital-marketing-foundations-and-strategy|SRC-029]] Zahay et al., *Digital Marketing: Foundations and Strategy*, ch. 5, pp. 130, 137–142

<!-- backlinks:start -->
## Backlinks

- [[DIG-023-a-website-is-built-in-seven-steps-and-marketing-leads-the|DIG-023]] _see_: A website is built in seven steps, and marketing leads the first ones: otherwise you get technology without an objective
- [[DIG-027-a-mobile-app-is-justified-only-if-it-does-something-a|DIG-027]] _see_: A mobile app is justified only if it does something a responsive website cannot do
- [[DIG-049-video-metrics-measure-time-the-brand-has-to-appear-before|DIG-049]] _application_: Video metrics measure time: the brand has to appear before the viewer leaves
- [[DIG-072-a-metric-is-just-a-number-it-becomes-a-kpi-when-it-is|DIG-072]] _application_: A metric is just a number; it becomes a KPI when it is chosen because it shows progress against an objective, and a KPI can combine several metrics
- [[DIG-075-the-conversion-funnel-shows-where-visitors-leave-the|DIG-075]] _extends_: The conversion funnel shows where visitors leave; the marketer's job is to find out why
- [[DIG-076-an-a-b-test-changes-a-single-variable-starts-from-a|DIG-076]] _application_: An A/B test changes a single variable, starts from a hypothesis and waits for statistical significance
- [[SOC-025-the-strategic-framework-of-an-influencer-campaign-starts|SOC-025]] _see_: The strategic framework of an influencer campaign starts from research and SMART objectives
- [[SRC-029-digital-marketing-foundations-and-strategy|SRC-029]]: Digital Marketing: Foundations and Strategy (5th ed.)
<!-- backlinks:end -->
