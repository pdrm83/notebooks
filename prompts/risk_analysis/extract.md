# Medical Risk Analysis

## Step 1: Basic Prompt (Initial version)

```markdown
Role: You are a medical assistant evaluating and analyzing treatment risks.

Context: The subject is a 75-year-old female who is taking Atorvastatin and has recently been prescribed to undergo severe physiotherapy/exercise.

Task: What are the top three risks (including both direct and indirect) for this subject?
```

### Design Principles

> **Principle**: Start simple and clear
> **Goal**: Get an initial risk list from the AI.

### Expected Issues

- The response may be vague or incomplete
- No quantitative confidence or likelihood info
- No root cause analysis
- No mechanism to verify or consolidate answers, increasing hallucination risk
