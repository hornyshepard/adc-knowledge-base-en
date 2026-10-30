---
id: DIG-035
title: In email, the click-to-open rate says more than the open rate
type: zettel
kind: concept
skill: digital-marketing
also: [advertising-strategy]
level: 2
tags: [email, open-rate, ctr, ctor, bounce-rate, unsubscribe, metrics]
sources:
  - SRC-029 | ch. 11, pp. 299, 312–315, 317
status: growing
---

# In email, the click-to-open rate says more than the open rate

> **The idea in one sentence:** the open rate is noisy and only directional; the click-to-open rate (CTOR), based on unique clicks, shows better how many people actually responded to the message.

## Explanation

Email service providers (MailChimp, HubSpot, Constant Contact) offer dashboards with six basic metrics:

| Metric | Formula | What it tells you |
|---|---|---|
| Open rate | opens ÷ emails delivered | directional; it also counts accidental or repeated opens |
| CTR | clicks ÷ emails sent | total engagement; inflated by multiple clicks, firewalls checking links, forwarding |
| CTOR | unique clicks ÷ opens | how many of those who opened took action: the metric many managers prefer |
| Unsubscribe rate | unsubscribes ÷ emails sent | a signal of relevance or of too high a frequency |
| Hard bounce | invalid address | the quality of the list |
| Soft bounce | temporarily undeliverable (a system problem) | technical problems |

The book's worked example: 8,000 subscribers, 2,570 open, 825 click → open rate 32.1%, CTR 10.3%, CTOR about 32%. An unsubscribe rate of 10.1% (808 people) should cause concern. The authors also note that most opens happen within the first 24 hours (down from 48 hours a few years earlier), so a fast reaction is essential. Industry averages are modest: around 21.5% open rate, 2.3% CTR and 10.5% CTOR (Campaign Monitor, 2022).

**A caution about the book:** CTR is defined in one place as "clicks ÷ opens" (p. 299) and in another as "clicks ÷ emails sent" (p. 315), and the example dashboard shows a CTOR of 26%, not 32%. Always check the definition your platform uses.

## Application

- Use the open rate to test the subject line, CTOR to test the content and the offer.
- Compare the unsubscribe rate after every change in frequency or tone.
- Always report to the client against the industry average, not in absolute figures.

## Example

The MailChimp dashboard with several campaigns (Fig. 11.16) compares segments that receive different messages; the difference between total and unique opens shows how many people come back to the same email, for example after a first hurried read.

## Questions

- Why has the open rate become even less reliable with email privacy protection (automatic opens)?
- Can an email with a low CTOR still be a brand success?

## Links

- **foundation** [[DIG-072-a-metric-is-just-a-number-it-becomes-a-kpi-when-it-is|DIG-072]]: metrics become KPIs only when tied to an objective.
- **application** [[DIG-034-a-good-promotional-email-has-one-offer-a-time-deadline-and|DIG-034]]: the design elements are evaluated through these metrics.
- **application** [[DIG-076-an-a-b-test-changes-a-single-variable-starts-from-a|DIG-076]]: subject lines and offers are compared through A/B tests.
- **see** [[DIG-036-in-ai-driven-email-send-time-and-frequency-are-optimized|DIG-036]]: send-time optimization relies on each subscriber's history of opens.

## Sources

- [[SRC-029-digital-marketing-foundations-and-strategy|SRC-029]] Zahay et al., *Digital Marketing: Foundations and Strategy*, ch. 11, pp. 299, 312–315, 317

<!-- backlinks:start -->
## Backlinks

- [[DIG-034-a-good-promotional-email-has-one-offer-a-time-deadline-and|DIG-034]] _see_: A good promotional email has one offer, a time deadline and a subject line under 50 characters
- [[DIG-076-an-a-b-test-changes-a-single-variable-starts-from-a|DIG-076]] _see_: An A/B test changes a single variable, starts from a hypothesis and waits for statistical significance
- [[SRC-029-digital-marketing-foundations-and-strategy|SRC-029]]: Digital Marketing: Foundations and Strategy (5th ed.)
<!-- backlinks:end -->
