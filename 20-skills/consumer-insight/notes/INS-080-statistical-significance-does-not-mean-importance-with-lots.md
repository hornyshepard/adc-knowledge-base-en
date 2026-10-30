---
id: INS-080
title: Statistical significance does not mean importance: with lots of data, almost any difference becomes "significant"
type: zettel
kind: principle
skill: consumer-insight
also: [ai-marketing, digital-marketing]
level: 2
tags: [statistical-significance, statistical-power, correlation, big-data, interpretation]
sources:
  - SRC-038 | ch. 2 (What is significant?, Power versus significance, Significance testing needs to make sense, On to correlations)
status: growing
---

# Statistical significance does not mean importance: with lots of data, almost any difference becomes "significant"

> **The idea in one sentence:** "significant" only says that you are probably not making a false claim; it does not say that the effect is large, useful or sensible.

## Explanation

Struhl clears up three common confusions in research reports:

1. **What "significant" means.** The 95% confidence threshold is a convention ("just because"). It says you are fairly sure you are not claiming an effect that does not exist (a Type I error). It does not measure whether you are missing a real effect; that is **statistical power** (a Type II error). The more certainty you demand, the more real effects you miss, like the bird watcher who, wanting to be 99% certain, lets real ducks fly by without calling them.
2. **Large samples break the test.** With enough data, almost any difference passes the threshold. In a survey of about 12,000 people, those born under the sign of Leo seemed to watch "significantly" more television. It is an artifact. With big data, significance is a **minimum threshold**, not a decision.
3. **Correlation measures only straight lines.** An S-shaped growth curve (the adoption of a brand) can have a correlation of 0.9 although it is not linear; other perfectly regular relationships can have a correlation of zero.

His basic rule: any result first has to **make sense**. A statistical test cannot judge that.

## Application

- When a report says "significant difference", ask for the **size** of the difference too, and ask which decision it changes.
- In digital dashboards with millions of impressions, ignore "winners" that differ by tenths of a percent and have no plausible explanation.
- Replace "significant correlation" with a better question: what shape does the relationship have, and how well does it predict on new data?

## Example

The Leo and television example makes a good seminar test: students have to explain why a statistically significant result can be absurd.

## Questions

- Why are A/B tests on very large volumes vulnerable to "winners" with no practical importance?
- What is worse for a campaign: believing in an effect that does not exist, or missing a real one?

## Links

- **see** [[INS-077-the-focus-group-is-good-for-language-and-for-detecting|INS-077]]: sampling error explodes with small samples.
- **see** [[INS-083-the-replication-crisis-calls-for-caution-but-theories-are|INS-083]]: Fennis and Stroebe: underpowered and "lucky" studies lie at the root of the replication crisis.
- **see** [[DIG-076-an-a-b-test-changes-a-single-variable-starts-from-a|DIG-076]]: A/B tests on large volumes easily produce "winners" with no practical importance.
- **see** [[AIM-007-validation-on-a-hold-out-sample-separates-real-patterns|AIM-007]]: validation on new data is the solid alternative to the significance test.

## Sources

- [[SRC-038-artificial-intelligence-marketing-and-predicting-consumer-choice|SRC-038]] Steven Struhl, *Artificial Intelligence Marketing and Predicting Consumer Choice*, ch. 2, "Getting the project going"

<!-- backlinks:start -->
## Backlinks

- [[AIM-007-validation-on-a-hold-out-sample-separates-real-patterns|AIM-007]] _see_: Validation on a hold-out sample separates real patterns from overfitting
- [[DIG-076-an-a-b-test-changes-a-single-variable-starts-from-a|DIG-076]] _foundation_: An A/B test changes a single variable, starts from a hypothesis and waits for statistical significance
- [[INS-077-the-focus-group-is-good-for-language-and-for-detecting|INS-077]] _see_: The focus group is good for language and for detecting disasters, not for the final decision
- [[INS-083-the-replication-crisis-calls-for-caution-but-theories-are|INS-083]] _see_: The replication crisis calls for caution, but theories are judged on research programs, not on isolated studies
- [[SRC-038-artificial-intelligence-marketing-and-predicting-consumer-choice|SRC-038]]: Artificial Intelligence Marketing and Predicting Consumer Choice: An Overview of Tools and Techniques
<!-- backlinks:end -->
