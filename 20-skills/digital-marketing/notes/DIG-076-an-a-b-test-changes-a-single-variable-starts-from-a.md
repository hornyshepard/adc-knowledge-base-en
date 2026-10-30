---
id: DIG-076
title: An A/B test changes a single variable, starts from a hypothesis and waits for statistical significance
type: zettel
kind: method
skill: digital-marketing
also: [copywriting, art-direction]
level: 2
tags: [ab-testing, experiment, hypothesis, multivariate, optimization, conversion]
sources:
  - SRC-030 | ch. 1
  - SRC-029 | ch. 5, p. 140
  - SRC-029 | ch. 8, p. 238
status: growing
---

# An A/B test changes a single variable, starts from a hypothesis and waits for statistical significance

> **The idea in one sentence:** the A/B test (split test) is a controlled experiment: you randomly show version A to one group and version B to another, changing a single element, and you declare a winner only after reaching the sample size and confidence level set in advance.

## Explanation

Zahay et al. (SRC-029) define the A/B test as a controlled experiment that helps optimize web content: two or more versions (email, promotion, landing page), randomly assigned groups, the proper statistical test. The chapter on paid search and social repeats the refrain test, test, test, because "testing is the lifeblood of all good digital marketing". Connors (SRC-030) gives the steps:

1. **Identify what to test**: the elements with the most significant impact on the desired outcome (the headline, the CTA, the form length; in email, the subject line, the copy, the send time).
2. **Create a hypothesis** that is specific, measurable and based on data ("a red button will increase click-through rates because red is a more attention-grabbing color"), not on a whim.
3. **Create version A (the control) and version B (the variation)**, which differ by **only one** element; otherwise you cannot attribute the difference.
4. **Determine the sample size and duration** with a statistical calculator; aim for a confidence level of at least 95%.
5. **Do not peek**: stopping the test midway produces false positives.
6. **Analyze** against the key metric; an inconclusive result is still information (the element matters less than you thought).
7. **Document and repeat**: the archive of tests becomes the team's memory.

Advanced variants: **multivariate testing** (combinations of headlines, images and buttons all at once; it needs a lot of traffic), **sequential testing** (analysis at set stages, so you can stop early without false positives) and tests by segment (what works for younger audiences may not work for older ones). Connors adds the ethics: transparency and GDPR compliance.

## Application

- Use tests to settle creative arguments that come down to taste: two good headlines, one test, a decision based on data.
- Write the hypothesis into the testing brief, with the psychological reason; otherwise you learn nothing even if B wins.
- Do not test minor details on low traffic; test offers and messages, which have a large impact.

## Example

The reactivation campaign in SRC-029 (fig. 5.7) tests the reactivation message A/B and the incentive (10 percent off vs. $5 off the first purchase vs. a free gift), measuring click-throughs, bounces from the landing page and the offers accepted for each variant.

## Questions

- Can an A/B test optimize a campaign toward a dull "local maximum" and kill bold ideas?
- Why is an A/B test on clicks no proof of the long-term effect on the brand?

## Links

- **application** [[DIG-073-metrics-are-chosen-starting-from-the-smart-objective-not|DIG-073]]: SMART conversion and reactivation objectives are reached through tests.
- **application** [[DIG-075-the-conversion-funnel-shows-where-visitors-leave-the|DIG-075]]: each abandonment hypothesis in the funnel becomes a test.
- **application** [[DIG-045-an-ad-is-only-as-good-as-its-landing-page-simplicity|DIG-045]]: optimizing the landing page is a series of tests.
- **foundation** [[INS-080-statistical-significance-does-not-mean-importance-with-lots|INS-080]]: with a lot of data, almost any difference becomes "significant", but not necessarily important.
- **contradicts** [[ADV-080-the-elements-of-an-ad-can-be-tested-as-an-experiment|ADV-080]]: message conjoint tests several elements at once and beats the A/B test.
- **see** [[DIG-035-in-email-the-click-to-open-rate-says-more-than-the-open-rate|DIG-035]]: the email subject line and offer are compared through email metrics.

## Sources

- [[SRC-030-digital-marketing-strategies|SRC-030]] K. Connors, *Advanced Digital Marketing Strategies*, ch. 1
- [[SRC-029-digital-marketing-foundations-and-strategy|SRC-029]] Zahay et al., *Digital Marketing: Foundations and Strategy*, ch. 5, p. 140; ch. 8, p. 238

<!-- backlinks:start -->
## Backlinks

- [[ADV-080-the-elements-of-an-ad-can-be-tested-as-an-experiment|ADV-080]] _alternative_: The elements of an ad can be tested as an experiment: message conjoint beats the A/B test
- [[AIM-007-validation-on-a-hold-out-sample-separates-real-patterns|AIM-007]] _see_: Validation on a hold-out sample separates real patterns from overfitting
- [[AIM-024-the-human-forms-the-hypothesis-the-ai-runs-it-the-human|AIM-024]] _see_: The human forms the hypothesis, the AI runs it, the human interprets it: the division of labor in testing and leads
- [[CPY-017-disrupt-then-reframe-a-small-oddity-in-how-the-price-is|CPY-017]] _see_: Disrupt, then reframe: a small oddity in how the price is stated, followed by a persuasive conclusion, increases sales
- [[CPY-025-the-mail-order-school-the-coupon-turned-copywriting-into-a|CPY-025]] _see_: The mail-order school: the coupon turned copywriting into a measurable experiment
- [[CPY-027-a-search-ad-is-written-as-a-set-of-interchangeable-pieces|CPY-027]] _see_: A search ad is written as a set of interchangeable pieces, and each one has to work on its own
- [[DIG-035-in-email-the-click-to-open-rate-says-more-than-the-open-rate|DIG-035]] _application_: In email, the click-to-open rate says more than the open rate
- [[DIG-044-a-paid-search-and-paid-social-campaign-has-five-stages-from|DIG-044]] _application_: A paid search and paid social campaign has five stages: from keyword research to testing
- [[DIG-073-metrics-are-chosen-starting-from-the-smart-objective-not|DIG-073]] _application_: Metrics are chosen starting from the SMART objective, not from what the platform offers: in a chain that runs from the baseline to the diagnosis
- [[DIG-075-the-conversion-funnel-shows-where-visitors-leave-the|DIG-075]] _application_: The conversion funnel shows where visitors leave; the marketer's job is to find out why
- [[INS-080-statistical-significance-does-not-mean-importance-with-lots|INS-080]] _see_: Statistical significance does not mean importance: with lots of data, almost any difference becomes "significant"
- [[INS-081-the-effect-of-an-ad-is-proved-by-experiment-not-by-the|INS-081]] _application_: The effect of an ad is proved by experiment, not by the "before and after" survey
- [[SRC-029-digital-marketing-foundations-and-strategy|SRC-029]]: Digital Marketing: Foundations and Strategy (5th ed.)
- [[SRC-030-digital-marketing-strategies|SRC-030]]: Advanced Digital Marketing Strategies: Mastering SEO, Social Media, Content Marketing, and AI for Maximum Online Growth
<!-- backlinks:end -->
