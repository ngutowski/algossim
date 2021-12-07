# MAB and CMAB Algorithms simulations in several datasets

This repository aims at learning most popular MAB and CMAB algorithms and watch how they run. It is interesting for
those wishing to start learning these topics.

## Algorithms

In this version I have implemented most popular MAB and CMAB algorithms (to be completed): UCB1, EXP3, epsilon-Greedy,
Thompson Sampling, LinUCB, and Linear Thompson Sampling (also known as Contextual Thompson Sampling).

## Datasets

Algorithms can be simulated over several datasets that I found in Kaggle, and UCI Machine Learning: Control (artifically
generated in full features and sparse features), Mushrooms, Statlog, Students Academic Performance, Recommendation
System Angers Smart City (RSASM), CNAE-9, contextfree (which is contexte free CNAE-9 version). Since Covertype and Poker
Hand are high volume datasets please contact me for getting them https://www.researchgate.net/profile/Nicolas_Gutowski.

## Graphic drawing mode

If you want to observe accuracy convergence in real-time (for you or your students) thus you can choose the dynamic
mode. Otherwise, choose static (it will run faster)

## List of parameters

**Algorithms**: String

- linucb
- egreedy
- ucb1
- ts
- lints
- exp3
- random

**Dataset**: String

- control
- controlsp
- mushrooms
- statlog
- students
- rsasm
- cnae9
- contextfree
- pokerhand
- covertype

**Horizon**: Integer in [1;T] T=whatever you want ;-) (100,1000,1000,10000, etc.)

**Graphic drawing mode** : String

- static
- dynamic

## How to simulate ?

For example :

- to simulate LinUCB algorithm in Control dataset up to horizon 2100 and watch dynamic graphic drawing you need to open
  a terminal and enter:
  python execute.py control linucb 2100 dynamic

- to simulate epsilon Greedy algorithm in Mushrooms dataset up to horizon 3000 and only watch the final graphic (not
  dynamically) you need to open a terminal and enter:
  python execute.py mushroom egreedy 3000 static

- to simulate UCB1 algorithm in Statlog dataset up to horizon 10000 and watch dynamic graphic drawing you need to open a
  terminal and enter:
  python execute.py statlog ucb1 10000 dynamic

- to simulate Thompson Sampling algorithm in Mushrooms dataset up to horizon 2000 and watch dynamic graphic drawing you
  need to open a terminal and enter:
  python execute.py statlog ts 10000 dynamic


