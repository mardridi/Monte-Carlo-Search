# 🎮 Connect Four Monte Carlo Search

## 🚀 Introduction

### 📚 Project description
This project is an implementation of  the Monte Carlo search algorithm for the game of "Connect Four". 

Connect Four is a turn-based board game in which two players take turns dropping colored discs into a vertical grid alternatively.

The Monte Carlo search algorithm is a decision-making algorithm that uses random sampling and statistical analysis to find the best possible move in a game.

Connect Four is a great game for Monte Carlo search algorithms because it has a relatively simple set of rules and a finite number of possible game states. In fact,  this algorithm can be used to analyze the best possible moves for a player given the current game state. It does this by simulating many random games from the current state, and analyzing the outcomes of those simulations to determine the best possible move. This makes it a useful tool for creating AI opponents that can play Connect Four at a high level.

###  🎯 Project goals and objectives

In this project we will try to let an AI agent learn to play Connect 4 using Monte Carlo Search algorithms and evaluate its performance with a random agent.

## ⚡️ Connect four
Connect Four is a classic game that has been around for over a century. However, it wasn't until 1974 that the game was officially licensed by Milton Bradley.

In October of 1988, James Dow Allen officially found a way for the first player to win the game every single time using his strategy. Other people and technologies have also solved this game.


### 📝 Rules of the game
Playing Connect Four requires following a simple set of rules:

1. Two players take turns dropping colored discs into a vertical grid.
2. The discs fall to the bottom of the grid or on top of other discs.
3. The objective is to connect four of the same colored discs vertically, horizontally, or diagonally.
4. Players can only drop one disc at a time.
5. The game ends if there is a four-in-a-row, which means that a player needs to place their colored discs in a consecutive line of four either vertically, horizontally, or diagonally on the game board.
6. The game ends too if there is no more moves can be made.
7. Players should alternate who goes first each game. For example, the first player of the first game will go second during the second game.

### 🏷️ Strategies of the game
There are several strategies that players can use to improve their chances of winning at Connect Four, including:

1. Select the middle column for a first move to maintain a strong central position.
2. Choose another bottom row slot with the second move.
3. Blocking the opponent's potential four-in-a-row while working towards your own.
4. Trying to create multiple threats at the same time to force the opponent to choose which to block.
5. Avoiding placing discs in the bottom row as this can limit future moves.

## 📂 Monte Carlo Search
Monte Carlo Tree Search (MCTS) is an algorithm used to find optimal decisions in a domain by building a search tree using random simulations to estimate the value of actions. It has had a profound impact on AI approaches for games and planning problems.

The algorithm progressively builds a partial game tree, guided by the results of previous exploration, until a predefined computational budget is reached. Each node in the tree represents a state of the domain, and directed links to child nodes represent actions leading to subsequent states.

The estimates of the most promising moves become more accurate as the tree is built, leading to a best-first strategy.

During each search iteration of the Monte Carlo Tree Search algorithm, the following four steps are applied:
1. "Selection:" Starting from the root node, traverse the tree by selecting the most promising child nodes, using a tree policy that balances exploration and exploitation.
2. "Expansion:" Once a leaf node is reached, expand it by adding one or more child nodes to represent possible moves from that state.
3. "Simulation:" Perform a simulated playout from the newly added child node, by making random moves until a terminal state is reached.
4. "Backpropagation:" Update the statistics of all nodes visited during the selection and expansion phases, based on the outcome of the simulated playout. This information is used to improve the estimates of the values of different moves, and ultimately guide the selection of moves in future iterations.

![Image](MCTS_steps.png)

### 🔖 Monte Carlo Tree Search

The Monte Carlo Tree Search (MCTS) is a technique used to identify the best decision in a given problem domain by sampling the decision space randomly and constructing a search tree based on the outcomes. 

MCTS has had a significant impact on AI methods for domains that can be represented as sequential decision trees, such as games and planning problems. 

In simple terms, MCTS is a way to explore possible decisions in a problem space by simulating outcomes and selecting the best path forward based on those simulations.

### 💬 Nested Monte Carlo Search

Nested Monte-Carlo Search is an algorithm used to guide search towards better states when there is no heuristic available to order moves. This is achieved by using random games to score positions and evaluate their interest. 

The algorithm uses nested levels of random games to guide the search. At each level of the search, all possible moves are tried, and a nested search is played at the lower level after each move. 

It memorizes the move associated with the best score of the lower level searches. If none of the moves improve on the best sequence found by a previous search, the move of the best sequence is played, otherwise, the best sequence is updated with the newly found sequence and the best move is chosen.

## 💻 Technical Overview
### 📦 libraries and packages

#### kaggle-environments>=0.1.6
It is a Python package that provides a simulation environment for various games and competitions hosted on Kaggle. This package allows users to define agents that can interact with the game environment and play against other agents. It also provides tools for visualizing the game states and actions taken by the agents. In this project, the kaggle-environments package is used to simulate and evaluate the performance of the Monte Carlo search algorithm for the game of Connect Four.

#### Random
The random library is a standard Python library that provides a suite of functions for generating random numbers, as well as other random operations like shuffling and selecting random elements from a list. It is often used in simulations, games and other applications that require random behavior.

#### Math
The math library in Python provides various mathematical functions for performing mathematical operations in Python. It includes functions for basic operations like addition, subtraction, multiplication and division, as well as more advanced functions like logarithms, trigonometric functions, and statistical functions.

#### Time
The time library in Python provides various time-related functions. It allows the Python interpreter to pause or delay execution of code for a certain period of time, measure the time taken by a block of code to execute and retrieve the current time and date. 

## 🛠️ Algorithm and Implementation
In this project,  We implemented two agents for the "ConnectX" game using the Monte Carlo Tree Search (MCTS) algorithm and Nested Monte Carlo Search.

### 🕹️ Monte Carlo Tree Search algorithm implementation
In our project, we implemented several classes and functions to create an intelligent agent using the Monte Carlo Tree Search (MCTS) algorithm for the game "ConnectX."

We utilized three main files to facilitate the implementation of our intelligent agent.

These files are the mcts_agent.py, state.py, and connect_4.ipynb.

#### mcts_agent.py file
The mcts_agent.py file contains the agent_mcts class, which is responsible for handling the MCTS algorithm and its related functionalities. It contains methods such as play to make a move on the board, check_win to determine if a winning condition is met, and check_tie to check for a tie game. 

The agent_mcts class also includes a default_policy_simulation method that performs random simulations to evaluate the outcome of the game.

#### state.py file
The state.py file contains the State class, which represents a state in the game. It stores the current board configuration, the player's mark, and other relevant information.

The State class keeps track of child states, calculates UCT scores using the uct_score function, and performs simulations and backpropagation to update the node statistics during the MCTS search.

In this file, we will find the uct_score function, which calculates the UCT score for a node based on its total score, total visits, and the number of visits of its parent node. It uses the formula that balances the exploitation of high-scoring nodes with the exploration of unexplored nodes, incorporating a constant value Cp that controls the level of exploration.

#### connect_4.ipynb file
The connect_4.ipynb file is the Jupyter Notebook where we bring everything together.

In fact, the combination of the agent_mcts class, the State class, and the uct_score function provides the necessary components to implement the MCTS algorithm and create a competitive game-playing agent.

We begin by setting up the environment using the "kaggle-environments" library and extracting the game configuration. Then, a Connect Four game is initialized and run using the environment, and the game board is rendered.

The Monte Carlo Tree Search (MCTS) implementation is defined in the "run_mcts_agent" function. It initializes the MCTS agent and performs iterations until a time limit is reached. 

The agent uses the "mcts_agent.py" and "state.py" files, which contain the necessary classes and functions for the MCTS algorithm.
### 🧠 Monte Carlo algorithm implementation




## 📈 Results and Performance 

###  Monte Carlo Tree Search evaluation
In the evaluation of the Monte Carlo Tree Search (MCTS) agent against a random agent, 50 episodes of the Connect Four game were played. The agent's performance was assessed based on the rewards obtained from these episodes.

The mean reward achieved by the MCTS agent was calculated to be 0.4. This indicates that, on average, the agent achieved a positive outcome in the game. A mean reward of 0.0 would suggest a neutral performance, while negative values would indicate a suboptimal performance. 

Therefore, the obtained mean reward of 0.4 indicates a reasonably good performance by the MCTS agent.

Additionally, the win rate of the MCTS agent was determined to be 0.7. This means that the agent won approximately 70% of the games played against the random agent.

A higher win rate signifies a stronger performance, indicating that the MCTS agent demonstrated a significant advantage over the random agent.

These evaluation results highlight the effectiveness of the MCTS algorithm in playing Connect Four. The agent's ability to consistently achieve positive outcomes and a high win rate demonstrates its proficiency in strategic decision-making and efficient exploration of the game tree.

## 💡 Conclusion



## 🗺️ References and Resources
* [Monte Carlo search - Tristan Cazenave](https://www.lamsade.dauphine.fr/~cazenave/MonteCarlo.pdf)
* [Game AI: Learning to play Connect 4 using Monte Carlo Tree Search](https://pranav-agarwal-2109.medium.com/game-ai-learning-to-play-connect-4-using-monte-carlo-tree-search-f083d7da451e)
* [How to Play Connect Four (Rules and Instructions)](https://groupgames101.com/connect-four-rules/)
* [A Survey of Monte Carlo Tree Search Methods](https://www.lamsade.dauphine.fr/~cazenave/A+Survey+of+Monte+Carlo+Tree+Search+Methods.pdf)
* [Nested Monte-Carlo Search-Tristan Cazenave](https://www.lamsade.dauphine.fr/~cazenave/papers/nested.pdf)






