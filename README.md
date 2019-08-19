# MAB and CMAB Algorithms simulations in several datasets

## Algorithms
In this version I have implemented most popular MAB and CMAB algorithms (to be completed): UCB1, EXP3, epsilon-Greedy, Thompson Sampling, LinUCB, and Linear Thompson Sampling (also known as Contextual Thompson Sampling).

## Datasets
Algorithms can be simulated over several datasets that I found in Kaggle, and UCI Machine Learning: Control (artifically generated in full features and sparse features), Mushrooms, Statlog, Students Academic Performance, Recommendation System Angers Smart City (RSASM), CNAE-9, contextfree (which is contexte free CNAE-9 version),Covertype, Poker Hand 

## List of parameters
* Algorithms: String
- linucb
- egreedy
- ucb1
- ts
- lints
- exp3

* Dataset: String
-control
-controlsp
-mushrooms
-statlog
-students
-rsasm
-cnae9
-contextfree
-pokerhand
-covertype

## How to simulate ? 
For example :
- to simulate LinUCB algorithm in Control dataset up to horizon 2100 and watch dynamic graphic drawing you need to open a terminal and enter:
python main.py control linucb 2100 dynamic

- to simulate epsilon Greedy algorithm in Mushrooms dataset up to horizon 3000 and only watch the final graphic (not dynamically) you need to open a terminal and enter:
python main.py mushroom egreedy 3000 static

- to simulate UCB1 algorithm in Statlog dataset up to horizon 10000 and watch dynamic graphic drawing you need to open a terminal and enter:
python main.py statlog ucb1 10000 dynamic

- to simulate Thompson Sampling algorithm in Mushrooms dataset up to horizon 2000 and watch dynamic graphic drawing you need to open a terminal and enter:
python main.py statlog ts 10000 dynamic


