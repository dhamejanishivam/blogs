+++
date = '2026-04-25'
draft = false
title = 'Self-Attention Mechanism'
+++

Self-attention is the core component of the Transformer architecture. It allows a model to weigh the importance of different words in an input sequence when processing a specific word.

### How it Works
Instead of processing tokens sequentially (like RNNs), self-attention computes three vectors for each token:
1. **Query (Q):** What I am looking for.
2. **Key (K):** What I contain.
3. **Value (V):** My actual content.

The attention score is calculated by taking the dot product of the Query of the current word with the Keys of all other words. This score dictates how much focus to place on other words' Values.

### The Formula
The scaled dot-product attention is defined as:

$$\text{Attention}(Q, K, V) = \text{softmax}\left(\frac{QK^T}{\sqrt{d_k}}\right)V$$

Where $d_k$ is the dimension of the key vectors. The scaling factor $\frac{1}{\sqrt{d_k}}$ prevents the dot products from growing too large and pushing the softmax function into regions with extremely small gradients.
