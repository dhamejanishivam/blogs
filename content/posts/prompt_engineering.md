+++
date = '2025-08-17'
draft = false
title = 'Prompt Engineering'
+++


Prompt engineering is about wording your requests so the model actually does what you want. Here’s the simplest breakdown of the main types with examples.

## Types of prompting

### Zero-shot prompting  
You just ask directly, with no example. The system figures it out from training. Works for simple tasks.

```python
# zero-shot prompt
prompt = "Summarize the following text in one sentence: 
Apple releases a new iPhone with better battery life and camera."
```

### One-shot prompting  
You give exactly one example along with the instruction. That single example guides the model.

```python
# one-shot prompt
prompt = """Translate the sentence to French.

Example:
English: I like coffee
French: J'aime le café

English: I enjoy reading books
French:"""
```


### Few-shot / multi-shot prompting  
You feed multiple examples. More examples = more consistency in results.

```python
# few-shot prompt
prompt = """Classify the sentiment as Positive, Negative, or Neutral.

Example:
Text: "The food was amazing and the staff were friendly."
Sentiment: Positive

Text: "The service was slow and disappointing."
Sentiment: Negative

Text: "It was okay, nothing special."
Sentiment:"""
```

### Instruction prompting  
You simply state what you want in clear, direct terms. Think of it as zero-shot with sharper wording.

```python
# instruction prompt
prompt = "List three pros and three cons of electric cars."
```

## Refrences
[1] . Lilian Weng : <a href='https://lilianweng.github.io/posts/2023-03-15-prompt-engineering/'>Article on Prompt Engineering</a>
