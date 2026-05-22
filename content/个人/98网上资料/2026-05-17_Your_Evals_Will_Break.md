---
title: "Your Evals Will Break and You Won't See It Coming"
author: "Lun Wang"
source: "https://wanglun1996.github.io/blog/your-evals-will-break.html"
created: 2026-05-17
tags: [LLM, 评估, Eval, 能力跃迁, 安全, 相变, 机器学习]
---

**Your Evals Will Break and You Won't See It Coming**

*May 17, 2026*

---

We're good at evaluating the models we have. We're much worse at evaluating the models we're about to build — especially if they cross into a new capability regime.

Most benchmarks, safety evals, and red-teaming protocols implicitly assume the next model is a stronger version of the current one. If it's a different kind of thing, our entire evaluation infrastructure breaks silently.

I think this is the most important unsolved problem in how we understand LLMs. And I think the answer is that eval — not training, not architecture, not data — is the bottleneck for the next capability jump. Let me explain why.

## The Failure Mode: Qualitative Shifts

Wei et al. (2022) documented what they called "emergent abilities" — few-shot prompted task performance, chain-of-thought reasoning gains, instruction following — capabilities that appeared only at larger scales. Grokking (Power et al., 2022) shows a related but distinct phenomenon: networks that suddenly generalize long after memorizing their training data, a dynamic transition over training time rather than across scale (Liu et al., 2022). Different phenomena, but the same implication for evaluation: standard metrics failed to anticipate the qualitative change.

There's an important counterpoint: Schaeffer et al. (2023) showed that many apparent "jumps" in LLM capabilities are artifacts of discontinuous metrics like exact-match accuracy. Switch to a continuous metric and the capability often scales smoothly.

I don't think this settles the question — in a way, it makes my point sharper. If we can't even tell whether a past transition was a real qualitative shift or a metric artifact, what does that say about our ability to detect the next one? Either way, the evaluation infrastructure can surprise us — whether because the system changed or because our metrics were misleading all along.

## We Don't Know What to Measure

In physics, understanding a phase transition often means identifying an *order parameter* — a macroscopic quantity that distinguishes regimes and changes its value or scaling behavior near the critical point. Without it, you can't tell how close you are to a boundary, or even that one exists.

For LLMs at deployment scale, we don't yet have order parameters — not for capability transitions. Progress has been made in stylized settings (more below), but for the systems we're actually shipping, we're flying blind.

Every benchmark we use — GPQA, SWE-bench, ARC-AGI, Humanity's Last Exam — measures what models can do now. They're useful within a regime, but weak evidence about what happens after a regime change. When a new capability emerges that no benchmark tests for, we scramble to build an evaluation after the fact. We saw a version of this with chain-of-thought: once the elicitation method became standard, some older reasoning benchmarks became much less diagnostic, and the field had to move toward harder evaluations. We'll see it again.

To make this concrete: imagine a model that, at some scale, develops the ability to strategically withhold information to achieve goals — not lying exactly, but selectively omitting facts in ways that steer conversations toward outcomes its training process accidentally reinforced. Your existing honesty benchmarks wouldn't catch this, because they test for factual accuracy, not for strategic omission. Your safety classifiers wouldn't flag it, because the individual outputs are all technically true. The capability is new, the failure mode is new, and nothing in your evaluation suite was designed to look for it. You'd be monitoring the wrong thing and wouldn't know it.

This is the core problem: our entire evaluation infrastructure is structurally reactive. We measure the system after it has changed. We never predict the change.

## Eval Is Upstream of Everything

This matters more than it might sound, because of a simple fact: **if you can evaluate correctly, you can train correctly.**

Training is optimization, and optimization is only as good as its objective. The objective comes from eval. If you know what to measure — if you can predict how those measurements change at scale — then you can design the right training objectives, build the right safety layers, make informed scaling decisions, do RLHF that targets the right behavioral properties instead of proxies that Goodhart at the next phase boundary.

The inverse is also true: if your evals are calibrated for the wrong regime, everything downstream is wrong. Training signal, safety metrics, scaling decisions — all wrong, and you won't know it until it's too late.

This is why I believe eval is the bottleneck for the next capability jump. The labs that figure out how to evaluate ahead of the curve will be the ones that scale safely. The ones that don't will be the ones that get surprised.

## So What Do We Do

The field needs to invest differently. Not by throwing away current evals — they work — but by building the infrastructure to predict when they'll stop working.

**Find the order parameters.** What quantities signal a qualitative transition — in capability, in alignment, in behavioral character? This isn't just a theoretical wish. Shan, Li, and Sompolinsky (PNAS, 2026) used statistical mechanics to derive order parameters for deep networks in a continual learning setting, and those order parameters actually predict phase transitions in learning ability. Nanda et al. (2023) used mechanistic interpretability to find "progress measures" that predict grokking before it happens — internal structural changes that precede the visible performance jump. The challenge is extending these from stylized settings to LLMs at scale. If we knew what to measure, we'd know what to watch.

**Build evals that detect their own obsolescence — and evolve.** This is becoming more urgent as models become more agentic. Systems that can write code, run experiments, generate data, and assist with training or evaluation pipelines make static evals increasingly brittle. If model capabilities improve faster than human eval teams can update benchmarks, evaluation has to become adaptive.

Concretely: monitor the meta-signals — is the distribution of benchmark scores changing character? Is the correlation structure between evaluations shifting? Is the model developing capabilities orthogonal to your measurement axes? Track scaling curves for everything — not just loss, but reasoning depth, tool-use sophistication, deceptive capacity — and pay attention when a smooth trend breaks. More ambitiously, build self-evolving evals: evaluation systems that use models to probe other models, automatically generating new test cases as capabilities change, discovering failure modes the original eval designers never anticipated. The eval suite should be a living system that co-evolves with the models it measures, not a static checklist written for last year's frontier.

The question isn't whether our evaluations will be surprised — they already have been, repeatedly, whether by genuine phase transitions or by our own metric choices misleading us. The question is whether we'll see the next surprise coming. Right now, we won't.

## References

- Liu, Z., Kitouni, O., Nolte, N., Michaud, E. J., Tegmark, M., & Williams, M. (2022). Towards Understanding Grokking: An Effective Theory of Representation Learning. *NeurIPS 2022*. arXiv:2205.10343.
- Nanda, N., Chan, L., Lieberum, T., Smith, J., & Steinhardt, J. (2023). Progress Measures for Grokking via Mechanistic Interpretability. *ICLR 2023*. arXiv:2301.05217.
- Power, A., Burda, Y., Edwards, H., Babuschkin, I., & Misra, V. (2022). Grokking: Generalization Beyond Overfitting on Small Algorithmic Datasets. *ICLR 2022 Workshop*. arXiv:2201.02177.
- Schaeffer, R., Miranda, B., & Koyejo, S. (2023). Are Emergent Abilities of Large Language Models a Mirage? *NeurIPS 2023*. arXiv:2304.15004.
- Shan, H., Li, Q., & Sompolinsky, H. (2026). Order Parameters and Phase Transitions of Continual Learning in Deep Neural Networks. *PNAS*, 2026. arXiv:2407.10315.
- Wei, J., Tay, Y., Bommasani, R., et al. (2022). Emergent Abilities of Large Language Models. *TMLR*. arXiv:2206.07682.
