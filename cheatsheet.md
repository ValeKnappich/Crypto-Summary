---
geometry: margin=1in
numbersections: true
title: "Introduction to Modern Cryptography - CheatSheet"
subtitle: "WS20/21"
documentclass: scrartcl
toc-depth: 2
toc: true
author:
- Valentin Knappich
- Jan-Nicolai Geistler 
date: \today{}
lang: en
include-before: |
    \begin{centering}
    \textbf{Disclaimer:} This document was created for exam preparation and has not been corrected by any of the lecturers/tutors. Therefore there is no guarantee for the correctness and/or comprehensiveness of the content.
    \end{centering}
header-includes: |
    \usepackage{graphicx}

    \newcommand\dummy[1]{#1}
    \let\Begin\begin
    \let\End\end
    \newcommand{\colEnd}[0]{\End{minipage}}
    \newcommand{\colBegin}[2][]{\dummy{\Begin{minipage}[#1]{#2\linewidth}}}

    \usepackage{setspace}
    \onehalfspace  

    \usepackage{tabto}
    \TabPositions{2cm, 4cm, 6cm, 8cm, 10cm, 12cm, 14cm, 16cm}

    \newcommand{\sample}{\overset{\$}{\leftarrow}}
---

# Block-Cipher

## Definition

Let $l: \mathbb{N} \rightarrow \mathbb{N}$ be a polynomial. Then the block-cipher is defined like this

$B = (\{0,1\}^{l}, Gen(1^\eta), E, D)$

Where $Gen(1^\eta)$ = probabilistic key generation

E = deterministic encrpytion

D = deterministic decryption

Only secure for scenario 2 (constant length no duplicated plaintext)

## (Shortend) security game

\begin{minipage}{.55\linewidth}
\centering
\includegraphics[width=.7\linewidth]{img/BC_SG}
\end{minipage}

## Advantage

\begin{align*}
Adv_{U, B}(\eta) &= 2 \cdot (Pr[\mathbb{E}^{B}_{U}(1^\eta) = 1]- \frac{1}{2})\\
&= Pr[\mathbb{S}_{U}^{B}\langle b=1\rangle (1^\eta)=1] - Pr[\mathbb{S}_{U}^{B}\langle b=0\rangle(1^\eta)=1]
\end{align*}

# PRNG Game

## Number Generator
Let $\eta\in\mathbb{N}$, p a polynomial and G a deterministic polynomial-time algorithm.

$G: (s:\{0, 1\}^\eta):\{0, 1\}^{p(\eta)}$

p is expansion factor of G

## PRNG-Distinguisher

Let $\eta\in\mathbb{N}$, p a polynomial and U is ppt algorithm.  
$U(1^\eta, x: \{0, 1\}^{p(\eta)}): \{0, 1\}$

## (Shortend) Game

\begin{minipage}{.55\linewidth}
\centering
\includegraphics[width=.7\linewidth]{img/prng-dist-shrt}
\end{minipage}

## Advantage

\begin{align*}
Adv_{U, G}(\eta) &= 2 \cdot (Pr[\mathbb{E}^{PRNG}_{U, G}(1^\eta) = 1]- \frac{1}{2})\\
&= Pr[\mathbb{S}_{U, G}^{PRNG}\langle b=1\rangle (1^\eta)=1] - Pr[\mathbb{S}_{U, G}^{PRNG}\langle b=0\rangle(1^\eta)=1]
\end{align*}

# CPA Security

## Security game

\begin{minipage}{.55\linewidth}
\centering
\includegraphics[width=.7\linewidth]{img/cpa}
\end{minipage}

## Adversary

Let $\eta\in\mathbb{N}$ and the adversary being a ppt algorithm

$A(1^\eta, H:\{0, 1\}^* \leftarrow \{0, 1\}^*): \{0, 1\})$

$(AF(1^\eta, H), AG(1^\eta, H, y: \{0, 1\}^*))$

AF = finder

AG = guesser

H = encryption oracle

## Advantage

\begin{align*}
Adv_{U, G}(\eta) &= 2 \cdot (Pr[\mathbb{E}_{A, S}(1^\eta) = 1]- \frac{1}{2})\\
&= Pr[\mathbb{S}_{A, S}\langle b=1\rangle (1^\eta)=1] - Pr[\mathbb{S}_{A, S}\langle b=0\rangle(1^\eta)=1]
\end{align*}

## Proof

By security game switching from success game to failure game proofing that the distingusiher stays the same, but it is possible to change the Gen function to a pseudo-random function.

\begin{minipage}{\linewidth}
\centering
\includegraphics[width=\linewidth]{img/cpa-switch}
\end{minipage}

# CCA

## Security game

\begin{minipage}{.55\linewidth}
\centering
\includegraphics[width=\linewidth]{img/cca}
\end{minipage}

## Adversary

Let $\eta\in\mathbb{N}$ and the adversary being a ppt algorithm

$A = (AF(1^\eta, H, H^{-1}), AG(1^\eta, H, y: \{0, 1\}^*))$

AF = finder

AG = guesser

H = encryption oracle

$H^{-1}$ = decryption oracle

## Advantage

\begin{align*}
Adv_{U, G}(\eta) &= 2 \cdot (Pr[\mathbb{E}^{S-CCA}_{A, S}(1^\eta) = 1]- \frac{1}{2})\\
&= Pr[\mathbb{S}^{S-CCA}_{A, S}\langle b=1\rangle (1^\eta)=1] - Pr[\mathbb{S}^{S-CCA}_{A, S}\langle b=0\rangle(1^\eta)=1]
\end{align*}


# Asymmetric encryption scheme

## Definition

\begin{minipage}{\linewidth}
\centering
\includegraphics[width=\linewidth]{img/asym-shm}
\end{minipage}

## Security game

\begin{minipage}{.55\linewidth}
\centering
\includegraphics[width=.7\linewidth]{img/asym-shm-game}
\end{minipage}

## Advantage

\begin{align*}
Adv^{A-CPA}_{U, G}(\eta) &= 2 \cdot (Pr[\mathbb{E}^{A-CPA}_{A, S}(1^\eta) = 1]- \frac{1}{2})\\
&= Pr[\mathbb{S}^{A-CPA}_{A, S}\langle b=1\rangle (1^\eta)=1] - Pr[\mathbb{S}^{S-CCA}_{A, S}\langle b=0\rangle(1^\eta)=1]
\end{align*}

# RSA

## Definition

\begin{minipage}{\linewidth}
\centering
\includegraphics[width=\linewidth]{img/rsa-df}
\end{minipage}

## Security game

\begin{minipage}{\linewidth}
\centering
\includegraphics[width=\linewidth]{img/rsa}
\end{minipage}

## Advantage / RSA-Assumption

$|Adv^{RSA}_{I,S}(\eta)| = Pr[\mathbb{E}^{RSA}_{I,S}(1^\eta) = 1]$

The function of the RSA encryption considered not invertable, because it is a trap-door function

# ElGamal

\newpage
## Definition
ElGamal is CPA secure.

\begin{minipage}{\linewidth}
\centering
\includegraphics[width=\linewidth]{img/elgamal-df}
\end{minipage}

## Advantage

TODO (DH-Assumption)

# Hashes

## Definition

\begin{minipage}{\linewidth}
\centering
\includegraphics[width=\linewidth]{img/hashes}
\end{minipage}

## Security Game

\begin{minipage}{0.7\linewidth}
\centering
\includegraphics[width=\linewidth]{img/hash_game}
\end{minipage}


## Advantage

$Adv_{A, \mathbb{H}}^{Coll} = Pr[\mathbb{E}^{Coll}_{A, \mathbb{H}}(1^\eta) = 1]$.

# MAC

## Definition

\begin{minipage}{\linewidth}
\centering
\includegraphics[width=\linewidth]{img/mac}
\end{minipage}

## Security game

\begin{minipage}{0.7\linewidth}
\centering
\includegraphics[width=\linewidth]{img/mac_game}
\end{minipage}

## Advantage

$Adv_{A, \mathcal{M}}^{MAC}(\eta) = Pr[\mathbb{E}_{A, \mathcal{M}}^{MAC}(1^\eta) = 1]$
