from mcts_agent import agent_mcts
import random
import time
import numpy as np
import math


def uct_score(node_total_score, node_total_visits, parent_total_visits, Cp):
       
    if node_total_visits == 0:
        return math.inf
    return node_total_score / node_total_visits + Cp * math.sqrt(
            2 * math.log(parent_total_visits) / node_total_visits)


class State():


    def __init__(self,board,mark,configuration,parent =None,is_terminal=False, terminal_score=None, action_taken=None):
        self.board= board.copy()
        self.mark = mark
        self.configuration = configuration
        self.children = []
        self.parent = parent
        self.EMPTY = 0
        self.node_total_score = 0
        self.node_total_visits = 0
        self.available_actions = [i for i in range(configuration.columns) if self.board[i] == self.EMPTY]
        self.unexplored_actions = self.available_actions.copy()
        self.is_terminal = is_terminal
        self.terminal_score = terminal_score
        self.action_taken = action_taken
        self.Cp_default = 1
        self.agent = agent_mcts(board,mark,configuration)


    
    def has_unexplored_children(self):
        return (not self.is_terminal) and (len(self.unexplored_actions) > 0)

    def simulate(self,mark,board):
        if self.is_terminal:
            return self.terminal_score
        return  self.agent.backpropagate_scores(self.agent.default_policy_simulation(board,mark))
    
    def backpropagate(self, simulation_score):
        self.node_total_score += simulation_score
        self.node_total_visits += 1
        if self.parent is not None:
            self.parent.backpropagate(self.agent.backpropagate_scores(simulation_score))

     
    
    def expand_simulate_child(self,board,mark):
        column = random.choice(self.unexplored_actions)
        child_board = board.copy()
        self.agent.play(board,column,mark)
        is_terminal, terminal_score = self.agent.check_finish_score(board, column, mark)
        self.children.append(State(child_board, self.agent.active_mark(mark), self.configuration, parent=self, is_terminal=is_terminal, terminal_score=terminal_score, action_taken=column))
        simulation_score = self.children[-1].simulate(mark,board)
        self.children[-1].backpropagate(simulation_score)
        self.unexplored_actions.remove(column)



    def max_ucb1(self,Cp):
        scores = [uct_score(child.node_total_score, child.node_total_visits,self.node_total_visits,self.Cp_default) for child in self.children]
        max_score = max(scores)
        best_child_index = scores.index(max_score)
        return self.children[best_child_index]
    
    def choose_play_child(self):
        children_scores = [child.node_total_score for child in self.children]
        max_score = max(children_scores)
        best_child_index = children_scores.index(max_score)
        return self.children[best_child_index]

    def tree_single_run(self,board,mark):
     
        if self.is_terminal:
            self.backpropagate(self.terminal_score)
            return
        if self.has_unexplored_children():
            self.expand_simulate_child(board,mark)
            return
        self.max_ucb1(self.Cp_default).tree_single_run(board,mark)


    def choose_child_via_action(self, action):
       
        for child in self.children:
            if child.action_taken == action:
                return child
        return None



