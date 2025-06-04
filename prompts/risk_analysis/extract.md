# Medical Risk Analysis

### Step 1: Basic Prompt (Initial version)

```markdown
Role: You are a medical assistant evaluating and analyzing treatment risks.

Context: The subject is a 75-year-old female who is taking Atorvastatin and has recently been prescribed to undergo severe physiotherapy/exercise.

Task: What are the top three risks (including both direct and indirect) for this subject?
```

#### Design Principles

- Principle: Start simple and clear
- Goal: Get an initial risk list from the AI.

#### Expected Issues

- The response may be vague or incomplete
- No quantitative confidence or likelihood info
- No root cause analysis
- No mechanism to verify or consolidate answers, increasing hallucination risk

------

### Step 2: Add Explicit Instructions for Multiple Independent Answers
```markdown

Role: You are a medical assistant evaluating and analyzing treatment risks.

Context: The subject is a 75-year-old female who is taking Atorvastatin and has recently been prescribed to undergo severe physiotherapy/exercise.

Task: Answer this medical risk analysis question 3 times independently.  
“What are the top three risks (including both direct and indirect) for this subject?”
```

#### Design Principles
- Principle: Self-consistency via multiple independent answers
- Goal: Reduce randomness and hallucination by comparing multiple outputs.

#### Improvement:
- Allows cross-checking consistency.
- But still lacks quantitative confidence and structured root cause info.

------

### Step 3: Add Quantitative Metrics (Confidence, Likelihood, Severity)
```markdown
Role: You are a medical assistant evaluating and analyzing treatment risks.

Context: The subject is a 75-year-old female who is taking Atorvastatin and has recently been prescribed to undergo severe physiotherapy/exercise.

Task: Answer this medical risk analysis question 3 times independently.  
“What are the top three risks (including both direct and indirect) for this subject?”

Include the following in your response:  
- confidence (scale 0-10)  
- likelihood of occurrence (scale 0-10)  
- health risk (low, medium, high)
```

#### Design Principles

- Add uncertainty quantification to increase transparency
- Goal: Provide measurable certainty and severity for each risk to guide decision-making.

#### Improvement:

- AI must evaluate its confidence, helping doctors weigh answers.
- Still missing the root cause, so less actionable.
