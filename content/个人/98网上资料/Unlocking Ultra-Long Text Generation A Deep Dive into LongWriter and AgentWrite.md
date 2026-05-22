---
title: "Unlocking Ultra-Long Text Generation: A Deep Dive into LongWriter and AgentWrite"
source: "https://medium.com/@hitesh.hinduja/unlocking-ultra-long-text-generation-a-deep-dive-into-longwriter-and-agentwrite-01632c2edfa7"
author:
  - "[[Hitesh Hinduja]]"
published: 2024-08-21
created: 2025-03-01
description: "It’s been quite some time (almost 3 months) since my last blog post. But finally, I’m back, and let’s get started! Moving forward, my blogs will primarily focus on interesting research papers in the…"
tags:
  - "clippings"
---
[

![Hitesh Hinduja](https://miro.medium.com/v2/resize:fill:88:88/1*7PJz69zWv1NFmb7It9YMdw.jpeg)

](https://medium.com/@hitesh.hinduja?source=post_page---byline--01632c2edfa7---------------------------------------)                                                                                                                                                                                                                                                                                                                                                                                                                                                      

![](https://miro.medium.com/v2/resize:fit:1400/1*jQl-ug86ZA3nvmdByvZS6Q.jpeg)

Hello Folks,                                                                                              

It’s been quite some time (almost 3 months) since my last blog post. But finally, I’m back, and let’s get started! Moving forward, my blogs will primarily focus on interesting research papers in the LLM and GenAI space. I’ll be discussing problem statements that I encounter in my day-to-day life, in what we like to call **“story time,”** as many of you might remember from my past blogs. This will be followed by a deep dive into the technical aspects of those problem statements. In addition to explaining the research papers, I’ll share experiences and practical examples, and I’ll also elaborate on technical details that the papers might skip, assuming the reader already knows them. So, let’s dive in!          

Just a few days ago, one of my family friends visited our place. They have a lovely 8-year-old daughter. It was August 15th, India’s Independence Day, and her school had given her an assignment to write an essay on Independence Day with a strict requirement of **“at least 10000 words”.** Now that’s really a lot! I really don’t know if I should call this an essay or a mini-book for an 8-year-old child! As usual, the parents started drafting it on behalf of their child. The first thing that comes to everyone’s mind is ChatGPT or something similar. At first, the parents were very relaxed and thought, ***“Let’s start drafting this on August 14th, just a day before, since it’s just a matter of ‘prompting the LLM model’ and getting the output.”*** On the night of August 14th, they did just that, but any guesses what happened? The model, though it gave a good output, struggled to maintain the following: *Relevance, Accuracy, Coherence, Clarity, Breadth and Depth, and Reading Experience*. Additionally, when the model is asked to output strictly 10k words, it repeats the context and significantly goes out of context.              

Now, you all might be wondering, what are these six dimensions? For that, let’s continue with the further reading and dive into the problem statement of ***“limitations of current long-context large language models (LLMs) in generating ultra-long outputs.”*** In this blog, we’ll explore an interesting research paper titled [**“LONGWRITER: UNLEASHING 10,000+ WORD GENERATION FROM LONG CONTEXT LLMS.”**](https://arxiv.org/pdf/2408.07055v1) Even though these models can process inputs up to 100,000 tokens, they typically struggle to produce outputs longer than 2,000 words. The primary reason for this limitation is attributed to the supervised fine-tuning (SFT) datasets, which lack examples of long outputs, capping the models’ ability to generate extended text. So in this blog, let’s understand the intriguing technique the authors have used to improve long output responses and make sure parents’ lives become easier in the future! And what about the kids? These days, I leave that up to their destiny with the advancements in AI and the way life has become easier for them with limited use of their mental capabilities! Anyway, let’s get started.                                                                                                                                                                                                                                                                                          

## **Introduction  **    

Now, let’s get into the borderline understanding of the paper. It kicks off by highlighting an interesting challenge with long context LLMs. These models, which can process over 100,000 tokens of input, still struggle to generate outputs longer than 2,000 words. This is a significant issue because, in some cases, more than 1% of user requests actually need longer responses.    

The core problem? The supervised fine-tuning (SFT) datasets that train these models just don’t include enough examples of long outputs. So, even though the models are capable of handling long inputs, they haven’t been trained to produce long outputs effectively. This limitation has stuck around because many LLMs rely on these same datasets.    

To tackle this, the authors introduce ***AgentWrite*** — a new approach that helps these models generate longer texts by breaking down the task into smaller parts. This method can push output lengths up to 20,000 words, far beyond what’s usually possible.    

The paper also brings in ***LongWriter-6k*** and ***LongBench-Write***, a dataset and benchmark created to train and test models on their ability to generate these ultra-long texts. The idea is to push the boundaries of what LLMs can do, making them more capable of handling tasks that require extended output.  

## Now let’s understand what is Agentwrite and how it works:  

**Step I: Plan    
**First things first, *AgentWrite* starts with a plan — just like how you’d outline an article before diving into writing. The model creates a detailed outline based on the given instructions, laying out the main content and specifying word counts for each section. Think of it as the model’s roadmap. For instance, if tasked with writing a 30,000-word piece on the Roman Empire, the plan might look something like this:  

> **Paragraph 1**: Introduction to the origins of the Roman Empire (700 words)  
> 
> **Paragraph 2**: Founding of the Roman Empire (800 words)  
> 
> …  
> 
> **Paragraph 15**: Summary of the Roman Empire’s history (500 words)  

This structured approach ensures the model knows exactly where it’s headed, making it easier to manage the task of generating lengthy outputs. Here you can look below how the author’s structure the input:  

![](https://miro.medium.com/v2/resize:fit:1400/0*awTWR09cu_UEcbwA)

This detailed outline ensures that the model has a clear structure to follow, making it easier to manage the generation of long outputs.                    

![](https://miro.medium.com/v2/resize:fit:1400/0*rAiIW76IcOy8i0Y0)

**Step II: Write    
**Next up, the model gets down to writing. Following the outline from Step I, the model generates the text in a serial manner — paragraph by paragraph. This sequential method ensures that each paragraph builds on the previous one, maintaining **coherence** throughout. By using earlier paragraphs as context, the model avoids common pitfalls like **repetition** or **incoherence**, which can be a real issue when generating longer texts. The results? Outputs extending over 20,000 words, all while keeping the quality intact. Here you see below how they motivate the input text with clear standing instructions. Imagine a pitch-perfect training to someone in their early stages of life so that they learn better for the future!  

![](https://miro.medium.com/v2/resize:fit:1400/0*sJ7vgmu-8FxXBnCH)

*Hope you all are clear with what exactly AgentWrite method does. We will soon see the validations and results of incorporating AgentWrite method in the LongWriter-6k and LongBench-Write. But before that, let’s see how these datasets are created and how are the models fine-tuned with this dataset that has AgentWrite methodology.  *

## LONGWRITER: TEACHING MODELS TO GENERATE ULTRA-LONG OUTPUTS  

After understanding how *AgentWrite* works, the next big question is — can we actually teach large language models (LLMs) to generate ultra-long outputs consistently? This paper dives into just that by constructing specialized datasets, fine-tuning models, and using Direct Preference Optimization (DPO) to fine-tune their performance. Don’t worry, we will be going into each and everything in detail! Let’s start with the first step **“DATA”, “DATA”, “DATA”!  **

## 4.1 Data Construction  

**Selection of Instructions:    
**The first step in this process was to handpick instructions that would naturally require long outputs. The team selected 6,000 such instructions — 3,000 from GLM-4’s SFT data (in Chinese) and another 3,000 from WildChat-1M (in English). GPT-4o automated this selection process, with additional rule-based filtering to weed out toxic or irrelevant instructions. After some manual verification, over 95% of these instructions were confirmed to genuinely need long outputs.  

**Generating Responses:    
**Once the instructions were set, it was time to generate responses using the *AgentWrite* pipeline powered by GPT-4o. The outputs underwent a strict post-processing phase, where any responses that were too short or that resulted from failed planning steps were filtered out. To ensure clarity, irrelevant identifiers like “paragraph 1,” “paragraph 2,” etc., were removed. The outcome was a dataset named *LongWriter-6k*, which offers a broad range of output lengths between 2,000 and 10,000 words — just what’s needed to supplement the general SFT data.  

**Combining Data:    
**The next move was to combine *LongWriter-6k* with the general SFT data, which includes 180k chat entries from GLM-4’s SFT dataset. This combination effectively addresses the scarcity of long outputs in the existing datasets, ensuring the models have ample examples to learn from.  

*Now once we have understood how data is getting constructed, lets understand how is the data being used in the model training.  *

## 4.2 Model Training  

**Supervised Fine-Tuning  **

**Models Used:    
**The team focused on fine-tuning two open-source models: GLM-4–9B and Llama-3.1–8B. Both of these models are capable of handling a context window of up to 128k tokens — perfect for the ultra-long outputs we’re aiming for.  

**Training Process:    
**To fine-tune these models, a loss weighting strategy was employed. Instead of averaging the loss by sequence, the loss was averaged by token. This approach ensures that longer outputs contribute more effectively to the training process. The training setup included 8xH800 80G GPUs using DeepSpeed+ZeRO3+CPU offloading, with a batch size of 8, a learning rate of 1e-5, and a packing length of 32k. The training spanned 4 epochs, totaling approximately 2,500–3,000 steps.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      

> Are you confused about the loss weighting strategy? If yes, let me explain it to you in detail. Else you may skip to the next section.    

## Token-Level Loss Averaging    

## **How It Works**:    

- Instead of averaging the loss at the sequence level, the model averages the loss across all tokens within the batch. This ensures that every token, regardless of its position in a short or long sequence, contributes equally to the learning process.  
-该模型不是在序列级别对损失进行平均，而是对批内所有令牌的损失进行平均。这确保了每个令牌，无论其在短序列或长序列中的位置如何，都对学习过程做出了同样的贡献。 

## **Example**:  

- Assume Sequence 1 has 9 tokens and Sequence 2 has 100 tokens.  
- If Sequence 1 has a loss of 0.2 per token and Sequence 2 has a loss of 0.3 per token:  

![](https://miro.medium.com/v2/resize:fit:1400/0*1rEeZQWcObwUmQn0)

- This approach means that the model’s learning process is more influenced by the longer sequence because it contains more tokens contributing to the loss.  

## **Why This Matters for Long Outputs**:  

- In the context of fine-tuning models for generating ultra-long outputs, token-level loss averaging ensures that the model pays more attention to longer sequences during training. Each token in these longer outputs contributes to the loss, encouraging the model to improve its performance on generating long, coherent text.  

**Resulting Models:    
**The fine-tuning process led to the creation of two models: *LongWriter-9B* (derived from GLM-4–9B) and *LongWriter-8B* (from Llama-3.1–8B).  

**Alignment (DPO)  **

**Objective:    
**To further refine the quality and adherence to length constraints, the team applied Direct Preference Optimization (DPO) to the *LongWriter-9B* model. I will explain this to you in detail shortly. Its important for us to first understand DPO and then dive into how it is used in the paper!  

## **Understanding Direct Preference Optimization (DPO)  **

**Direct Preference Optimization (DPO)** is a technique used to fine-tune language models by optimizing them based on preference data. The core idea is to improve the model’s ability to generate outputs that align with human preferences or specific criteria, such as following instructions closely or producing high-quality content.  

## 1\. Practical Example of DPO — For simplistic understanding  

Imagine you’re building an AI that generates short stories. You want the AI to produce stories that are not only creative but also coherent and engaging.  

**Step 1: Generate Multiple Outputs**: The AI generates several versions of a story based on the same prompt.  

> **Version A**: A highly creative but slightly confusing story.  
> 
> **Version B**: A less creative but very clear and engaging story.  
> 
> **Version C**: A story that is both creative and coherent but slightly lacks depth.  

**Step 2: Rank the Outputs**: Human reviewers or another evaluation system rank these outputs based on how well they meet the desired criteria (creativity, coherence, engagement).  

> **Ranking**: Version C > Version B > Version A  

**Step 3: Optimize Based on Preferences**: The AI is fine-tuned to generate outputs more like Version C, which best balances creativity, coherence, and engagement. This process helps the AI learn what makes a “good” story according to the given criteria.  

## 2\. Technical Explanation of DPO — Not specific to paper but in real how DPO works.  

DPO involves several steps:  

- **Data Collection**: Collect pairs of outputs generated by the model. For each pair, a preference label is assigned, indicating which output is better according to specific criteria (e.g., clarity, relevance, creativity).  
- **Preference Data**: The model is trained on this preference data, where the goal is to maximize the likelihood that the model will generate the preferred output in future generations.  
- **Objective Function**: The model’s objective function is adjusted to give higher probabilities to preferred outputs. This is typically done using techniques like pairwise ranking loss or a reward model that scores outputs based on how well they align with the preferences*(Please feel free to reach out to me for understanding more about pairwise ranking loss understanding)*  
- **Fine-Tuning**: The model is then fine-tuned using this adjusted objective function, making it more likely to generate outputs that align with the preferences in similar future scenarios.  

## 3\. How DPO is Used in the Paper

So, we’ve talked about what Direct Preference Optimization (DPO) is, but how exactly is it applied in this research? In the context of the paper, DPO comes into play after the initial fine-tuning with the *LongWriter-6k* dataset. The goal here is to sharpen the model’s ability to generate long-form content that aligns more closely with user instructions.

Here’s a breakdown of how DPO is used:

**Generating Outputs:  
**Once the model has been fine-tuned with the *LongWriter-6k* dataset, it’s time to see what it can produce. The model generates multiple outputs for prompts that require lengthy responses. For instance, if the prompt asks for a detailed 10,000-word article, the model will produce several versions of that output.

**Creating Preference Data:  
**Next, these outputs are evaluated and ranked based on how well they meet the desired criteria — think of metrics like length adherence, coherence, and overall quality. For example, if the prompt asks for a 10,000-word piece, outputs that come closest to this length, while also maintaining coherence and quality, are ranked higher.

**Optimizing the Model:  
**Now, using these rankings, the model is further fine-tuned. This step is where the magic of DPO really kicks in — the model’s parameters are adjusted so that it learns to favor outputs similar to the ones ranked highest by the preference model. Essentially, the model is being trained to understand, “These are the kinds of outputs you should aim for.” But please don’t confuse here with the objective function. Here its making sure that the model learns among the best of the best outputs when it gets fine-tuned the second time! So its not like any objective function or loss function getting optimised in this paper for DPO. I am sure you might be wondering why there is so much of manual intervention? — Bdw my boss used to tell me **“Sometimes hardwork is better than smart work”**

**Final Evaluation:  
**After applying DPO, the model goes through another round of evaluation using benchmarks like *LongBench-Write*. This final step is crucial to ensure the model isn’t just generating long texts, but high-quality, length-appropriate content.

## 4\. How AgentWrite Uses DPO

Now, let’s tie this back to *AgentWrite* and how it leverages DPO to enhance its performance.

**Improving Length Adherence:  
**One of the main challenges *AgentWrite* addresses is getting the model to stick to specific length requirements — say, producing that elusive 10,000-word article without falling short. DPO helps by optimizing the model to prefer outputs that meet these length requirements more accurately. So, after going through DPO, the model is more likely to hit the length targets dead-on.

**Enhancing Content Quality:  
**But it’s not just about hitting the word count. *AgentWrite*, with the help of DPO, also refines the model’s ability to produce content that is coherent, relevant, and clear. By focusing on the highest-quality outputs during DPO, *AgentWrite* ensures that the model isn’t just verbose but also produces text that’s worth reading — long, but also strong.

So finally, we come to an end where we understand how DPO is used additionally to improve the quality of outputs and have better version of next fine-tuned model. In the article till here, we see that there are six dimensions that have been talked about very often. Now before moving to the next section where I explain you about these 6 metrics and how are they evaluated, I would like to give you a brief understanding of those. So let’s understand this in a funny way:

> *Picture this: Your boss has just asked you to draft a 1,000-word report on “The Impact of Remote Work on Team Productivity.” Naturally, you turn to your trusty AI to help you out. Now, let’s see how you’d evaluate whether the AI’s output is actually going to impress the boss or get you a stern “we need to talk” email.*

**Relevance:  
**First off, the report needs to stay on point. You don’t want the AI wandering off into unrelated territory, like the benefits of beach vacations or why cats make great office companions (unless, of course, your boss is a cat enthusiast).

**Accuracy:  
**Next, the report has to be factually correct. You’re hoping to present solid insights on how remote work affects productivity, not accidental claims like “working from home increases productivity by 200% — especially if you have Netflix on in the background.”

**Coherence:  
**The report should be logically structured. It should flow like a well-organized meeting agenda, not like a chaotic brainstorming session where everyone’s talking at once. Each section should lead smoothly into the next, making it easy for your boss to follow along without needing a coffee break halfway through.

**Clarity:  
**The language should be crystal clear — no jargon that requires a decoder ring or overly complex sentences that sound like they belong in a legal contract. Your boss should be able to skim through it and instantly get the main points, without scratching their head or wondering if you’ve secretly hired a lawyer to write it.

**Breadth and Depth:  
**The report should cover all the critical angles — like how remote work affects team collaboration, productivity metrics, and maybe even the impact on employee morale. You want to make sure the report is thorough enough to avoid that dreaded “Could you add more detail here?” feedback.

**Reading Experience:  
**Finally, the report should be engaging and easy to read. You don’t want your boss yawning halfway through or worse, feeling the need to rewrite half of it. The writing should be smooth and professional, giving your boss the impression that you’ve really put in the effort (even if you had a little help from AI on the side).

But now, you might be wondering — how do we actually evaluate these metrics? After all, your AI doesn’t come with a built-in “Boss Approval Gauge” or a “Clarity-O-Meter.” So, let’s dive into how this all works:

## How Are These Metrics Calculated? Enter LLM-as-a-Judge

So, after understanding the six key dimensions for evaluating text quality, the next question that naturally comes up is, “How on earth does the AI figure all this out?” After all, the model itself doesn’t inherently “know” these metrics. That’s where the LLM-as-a-Judge method comes into play.

**LLM-as-a-Judge Overview  
**Instead of relying on human evaluators for every single piece of content, the researchers cleverly used the LLM itself to assess the quality of the generated outputs. By leveraging the model’s extensive knowledge and contextual understanding, it can provide objective evaluations across the six dimensions we’ve discussed. Bdw my boss also used to tell me **“Sometimes smart work is better than hard work”** 😂

**Scoring Process: How It Works  
**The way it works is pretty straightforward. The researchers designed specific prompts to instruct GPT-4o to evaluate the outputs. For example, the model might be asked to rate how relevant the output is to the original prompt or assess the clarity of the writing. The prompts might look something like this:

> *“You are an expert in evaluating text quality. Please rate the AI assistant’s response across six dimensions: Relevance, Accuracy, Coherence, Clarity, Breadth and Depth, and Reading Experience. Provide a score from 1 to 5 for each dimension.”*

The model then analyzes the text based on these prompts and provides a score, usually outputting its evaluation in a structured format like JSON, which includes both the scores and brief explanations.

**Use of Pre-Defined Metrics  
**For specific metrics like output length, the model uses something a bit more technical — a piecewise linear function. This function adjusts the score based on how closely the actual length of the output matches the required length. For example:

> If the output is exactly 1,000 words when the prompt asks for 1,000, the score might be a perfect 100.
> 
> If it’s a bit off — say, 10% longer or shorter — the score will decrease slightly.
> 
> And if it’s way off, like 50% longer or shorter, the score drops significantly.

This method ensures that the model is incentivized to produce text that fits the expected length, penalizing outputs that deviate too much.

**No Built-in Metrics During Training  
**It’s important to note that these metrics aren’t baked into the model during its initial training. The model doesn’t inherently “know” it’s being judged on Relevance or Coherence — it’s just generating text based on its training data. The evaluation happens externally, using a separate model (in this case, GPT-4o) that’s prompted to act as a judge.

**Tools and Techniques  
**While some models can be fine-tuned on datasets labeled by human annotators, this paper primarily relies on GPT-4o’s existing capabilities to evaluate the text without additional fine-tuning. The idea is to mimic how a human would assess the quality of the writing, using the model’s vast knowledge and understanding of language.

## Experiment Results: Model Evaluation on LongBench-Write

The research team evaluated a set of models — 4 proprietary and 5 open-source — using the LongBench-Write benchmark. This evaluation also included the newly trained *LongWriter* models. Among the existing models, the only other one specifically aligned for long-form text generation is Suri-IORPO, which is based on Mistral-7B-Instruct-v0.2 and fine-tuned using LoRA.

For the evaluation, the team configured each model with a temperature setting of 0.5 and set the maximum tokens parameter to the highest allowed by the model’s API. For open-source models, this was set at 32,768 tokens.

The key results, summarized in Table 3, include average and median response lengths, while Figure 6 visualizes how well each model’s output length aligns with the required length across 120 different instructions.

## Key Findings from the Experiment Results

Let’s take a look at this table carefully!

![](https://miro.medium.com/v2/resize:fit:1400/0*tN_B7Jbx9fvYqd6b)

## **Output Length Performance:**

- **Previous Models’ Limitations:** Most existing models struggle to meet the length requirement of over 2,000 words. For instance, in the \[2k, 4k) word range, the majority scored below 70, with only *Claude 3.5 Sonnet* performing decently **(see Table 3 above).**
- **Severe Shortcomings in Longer Outputs:** For prompts requiring 4,000 to 20,000 words, almost all previous models failed to reach the target output length, with many scoring 0 (indicating output lengths were less than one-third of the required length) (refer to Figure 6 below).

![](https://miro.medium.com/v2/resize:fit:1400/0*Afb28Ir3mfA_wqh_)

- **LongWriter Models’ Success:** In contrast, the *LongWriter* models, enhanced with training data from *LongWriter-6k*, consistently met the required output lengths while maintaining good quality, as evidenced by the Si (output length score) and Sq (quality score) in the \[2k, 20k) range (refer to Table 3 and Figure 6).

## **Coherence of Long Outputs:**

- **NLL Testing for Coherence:** The cumulative average negative log-likelihood (NLL) test was used to ensure that the long outputs from the *LongWriter* models were coherent and logically connected (see Figure 7).

![](https://miro.medium.com/v2/resize:fit:1400/0*PpglCCNgV49eYGHz)

> Scratching your head or confused on what exactly is NLL? Don’t worry, let me explain this to you in a funny way!

![](https://miro.medium.com/v2/resize:fit:1400/0*Tfwn6xp3rTOqytNA.jpg)

## Negative Log Likelihood (NLL) Test Explained: The Manager-Employee Review

Imagine you’re a manager, and you have an employee (let’s call them Hitesh) who is supposed to prepare a long report. As Hitesh writes the report, you’re checking in at different points — say, after the introduction, the first section, halfway through, and so on. You want to see how well Hitesh is sticking to the topic and making logical points as the report progresses.

Now, if Hitesh is doing a great job, you’ll find it easier to predict what comes next in the report because it’s all flowing logically. You’re nodding along thinking, “Yes, this makes sense,” and you’re happy because Hitesh is making your life easier. This means the “Negative Log-Likelihood” (NLL) score is low — Hitesh is doing well, and your surprise at what comes next is low because it all fits together smoothly.

But if Hitesh starts rambling, throwing in random unrelated points, or the report starts falling apart in terms of structure, your ability to predict what’s coming next decreases. You’re now scratching your head, trying to figure out what on earth is happening. This would result in a higher NLL score — indicating that the coherence of the report is dropping.

![](https://miro.medium.com/v2/resize:fit:1400/0*PpglCCNgV49eYGHz)

Now, let’s look at **Figure 7 above**:

- The **red line** (GLM-4–9B) and the **blue line** (Llama-3.1–8B) represent how two different “Hitesh’s” (or models) are doing as they write their reports (generate text).
- As the report gets longer (moving along the x-axis), you (the manager) are checking to see if it’s still making sense.
- A **lower line** on the graph means the report is staying coherent, and you’re less surprised (lower NLL) as you read along. So, in this case, Hitesh(Llama-3.1–8B) in the blue line is doing a slightly poor job at keeping things coherent compared to Hitesh in the red line (GLM-4–9B).

## **Impact of Direct Preference Optimization (DPO)**

- **Improved Quality and Length Adherence:** The application of DPO resulted in a 4% improvement in the output length score (Sl) and a 3% improvement in the quality score (Sq) across all ranges when comparing *LongWriter-9B* and *LongWriter-9B-DPO* (see Table 3 and Figure 8).
- **Human Preference:** In manual evaluations, humans preferred the outputs of the DPO-trained model over the non-DPO model in 58% of the cases. Despite having fewer parameters, *LongWriter-9B-DPO* achieved a performance level on par with GPT-4o (as shown in Figure 9).

![](https://miro.medium.com/v2/resize:fit:1084/1*sZ6o_jgyOI57wQKMFcyN8g.png)

**Color Coding:** Blue indicates lower win rates (less than 50%), red indicates higher win rates (more than 50%). *LongWriter-9B-DPO* has higher win rates (more red), meaning it generally outperforms other models.

## Ablation Study: Understanding the Impact of Different Data Approaches

The ablation study in the paper examines how different data configurations impact the performance of the *LongWriter-9B* model. The key findings are summarized below, based on the results reported in **Tab 4**:

![](https://miro.medium.com/v2/resize:fit:1400/1*b3M9BHPLAe3UwlupYtrwZw.png)

**Ablation on LongWriter-6k Dataset:**

- **Without LongWriter-6k Data:**  
When the *LongWriter-9B* model was trained without the *LongWriter-6k* dataset (using only general SFT data), its performance dropped significantly. The overall output length score (Sl) decreased to 48.1, and the quality score (Sq) fell to 77.1. ***See table 4 above***
- **With LongWriter-6k Data:**  
Adding the *LongWriter-6k* dataset resulted in a marked improvement. The model’s ability to generate longer outputs improved significantly, especially in the \[2k, 4k) word range, where **Sl increased to 76.0 and Sq to 80.2**. The overall **quality score (Sq)** improved by 5%, with a notable 18% improvement in the **“Breadth and Depth”** dimension. ***See table 4 above***

## Blog Conclusion: Wrapping It Up with a Smile 🙂

## **The 2,000-Word Ceiling:**

- We found that current LLMs hit a “glass ceiling” at around 2,000 words — like trying to write a novel but running out of ink halfway through.

## **AgentWrite to the Rescue:**

- Enter *AgentWrite*, our superhero sidekick! This agent-based pipeline comes in to help LLMs break through that ceiling and churn out extended, coherent content — think of it as giving the model an extra-large coffee to keep it going through those longer reports.

## **LongWriter-6k: The Training Power-Up:**

- With the help of *LongWriter-6k* (our model’s secret weapon), we managed to stretch those output lengths to over 10,000 words. It’s like turning a short story writer into a best-selling author overnight.

## **Ablation Studies: Proving It Works:**

- Our ablation studies confirmed that *AgentWrite* isn’t just a one-hit wonder. It consistently boosts the model’s performance, proving that a little extra data can go a long way.

## **Future Adventures:**

- **Longer Outputs:** Next, we’re aiming to stretch those word counts even further — because who doesn’t love a good sequel?
- **Higher Quality:** We’ll be refining *AgentWrite* to make sure the extra words don’t turn into unnecessary rambling (nobody likes a chatty coworker).
- **Efficiency Challenges:** As outputs get longer, we’ll need to keep an eye on efficiency — because even the best authors need a good editor to keep things concise.

So that’s it for the day. Before wrapping up, I would like to provide special thanks to all the writers of this paper for working on a real problem in this space and coming up with such insightful results. **Authors and Affiliations** : Yushi Bai† , Jiajie Zhang† , Xin Lv , Linzhi Zheng , Siqi Zhu , Lei Hou , Yuxiao Dong , Jie Tang , Juanzi Li . ***Tsinghua University, Zhipu AI***

## Hope you all enjoyed reading the blog. Stay tuned for the next!