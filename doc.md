---
geometry: margin=1in
numbersections: true
title: "Introduction to Modern Cryptography Summary"
subtitle: WS20/21
documentclass: scrartcl
author:
- Valentin Knappich 
date: \today{}
lang: en
filter:
- pandoc-eqnos
latex-engine-opt: -shell-escape
header-includes: |
    \usepackage{placeins}
    \usepackage{graphicx}

    \let\Begin\begin
    \let\End\end

    \usepackage{setspace}
    \onehalfspace  

    \usepackage{tabto}
    \TabPositions{2cm, 4cm, 6cm, 8cm, 10cm, 12cm, 14cm, 16cm}
---

\tableofcontents
\newpage

# Symmetric encryption

**Kerkhoffs Principle**: The security of a system should only depend on whether the actual key is secret, not on the system itself. The whole system is assumed to be public. No "Security by obscurity".

## Scenario 1

**One message with constant length**

### Cryptosystems

A cryptosystem is a tuple $S = (X, K, Y, e, d)$ with

- X: set of plaintexts
- K: finite set of keys
- Y: set of ciphertexts
- e: encryption function
- d: decryption function

Perfect correctness: \tab\tab $d(e(x, k), k) \forall x \in X, k \in K$

No unnecessary ciphertexts: \tab $Y = \{e(x,k) | x \in X, k \in K\}$ 


### Vernam system

The Vernam cryptosystem of length $l$ is defined as $(\{0, 1\}^l, \{0, 1\}^l, \{0, 1\}^l, e, d)$ where 

$e(x, k) = x \oplus k$ and $d(y, k) = y \oplus k$.

A vernam system of length $l>0$ provides perfect secrecy for every uniform $P_K$. It is the perfect system for Scenario 1.

### Perfect Secrecy

A cryptosystem with key distribution $V = S[P_k]$  provides perfect secrecy if for all plaintext distributions $P_X$, the probability of every plaintext remains the same, i.e.: $$P(x) = P(x | y) \quad \forall x \in X, y \in Y, P(y) > 0$$

**Example Proof**:

We need to show the criteria above for all plaintext distributions $P_X$. Therefore we use variable probabilities for the plaintexts $P_X(a) = p, P_X(b) = 1-p$ (for 2 plaintexts, else $p_1, ..., p_n$).
\begin{minipage}{.35\linewidth}
    \centering
    \includegraphics[width=\linewidth]{img/perfect_secrecy_example}
\end{minipage}
\begin{minipage}{.63\linewidth}
    \begin{align}
        P(a | A) &= \frac{P(a, A)}{P(A)} &= \frac{\frac{1}{2} * p}{\frac{1}{2} * p + \frac{1}{2} * (1-p)} &= p = P(a)\\
        P(a | B) &= \frac{P(a, B)}{P(B)} &= \frac{\frac{1}{2} * p}{\frac{1}{2} * p + \frac{1}{2} * (1-p)} &= p = P(a)\\
        P(b | A) &= \frac{P(b, A)}{P(A)} &= \frac{\frac{1}{2} * (1-p)}{\frac{1}{2} * (1-p) + \frac{1}{2} * p} &= 1-p = P(b)\\
        P(b | B) &= \frac{P(b, B)}{P(B)} &= \frac{\frac{1}{2} * (1-p)}{\frac{1}{2} * (1-p) + \frac{1}{2} * p} &= 1-p = P(b)
    \end{align}
\end{minipage}
\newline

**Theorem**: 

Let $S = (X,K,Y,e,d)$ be a cryptosystem providing perfect secrecy, then it holds $|K| \geq |Y| \geq |X|$.

**Shannons Theorem**:

Let $V = S[P_k] be a cryptosystem with key distribution $P_K$ and $|K| = |Y| = |X|$. The system provides perfect secrecy if and only if

1. $P_K$ is a uniform distribution
2. $\forall x \in X, y \in Y \exists k \in K with e(x, k) = y$ (There must be a key for every plaintext/ciphertext pair)

## Scenario 2 

**Multiple messages with constant length, no repetition**

### Vernam in Scenario 2

Vernam is not a secure cryptosystem anymore, since from 2 ciphertexts, Eve can learn non-trivial information about the plaintexts:
$$y_0 \oplus y_1 = x_0 \oplus k \oplus x_1 \oplus k = x_0 \oplus x_1$$

Also with 1 plaintext-ciphertext pair (CPA), the key can be calculated as $k = x \oplus y$.

### Substitution Cryptosystem

Let $X$ be a non-empty finite set. A substitution cryptosystem over X is a tuple $(X, P_X, X, e, d)$ where $P_X$ is the set of all permutations of $X$.
$$e(x, \pi) = \pi(x) \quad d(y, \pi) = \pi^{-1}(y) \quad \forall x,y \in X, \pi \in P_X$$

Substitution cryptosystems provide "perfect security" in scenario 2, BUT they are impractical because the permutation table ($\pi$) has a size of $2^l * l$.

Therefore, we need a weaker security definition that takes into account, that attackers are resource bound.

### l-Block Cipher

Let $l : \mathbb{N} \rightarrow \mathbb{N}$ be a polynomial. An l-block cipher $B$ is a cryptosystem of the form 
$$\bigg(\{0,1\}^{l(\eta)}_{\eta \in \mathbb{N}},\; Gen(1^\eta),\; \{0,1\}^{l(\eta)}_{\eta \in \mathbb{N}},\; E,\; D \bigg)$$

\begin{center}
or simplified:
\end{center}

$$\bigg(\{0,1\}^l,\; Gen(1^\eta),\; \{0,1\}^l,\; E,\; D \bigg)$$

### Substitution-Permutation Cryptosystem (SPCS)

**Notation**: 

- plaintexts are split into $m$ words with length $n$ with $l = m*n$, $x^{(i)}$ denotes the $i$'th word
- $[r] = \{0, 1, ..., r-1\}$
- $\beta \in P_{[l]}$, then $x^\beta(i) = x(\beta(i))$

**General Principle**: Over $r$ rounds, (round) key additions, word substitutions and bit permutations are applied, including an initial step that just applies key addition and shortened last round without bit permutation.

\begin{minipage}{.6\linewidth}
    \includegraphics[width=\linewidth]{img/spcs}
\end{minipage}
\begin{minipage}{.35\linewidth}
    \includegraphics[width=\linewidth]{img/spcs_vis}
\end{minipage}

**Known Attacks**: 

- Brute Force Attack
- Linear Cryptanalysis
- Differential Cryptanalysis

**Linear Cryptanalysis**: 

- Relies on a set $T$ of plaintext-ciphertext pairs
- Instead of brute forcing the whole key, get small parts of the key at a time
- TODO

**AES (Advanced encryption standard)**: basically SPCS with modifications


