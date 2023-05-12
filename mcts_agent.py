import random
import math
import time

EMPTY = 0
Cp_default=1

class agent_mcts:

    def __init__(self,board,mark,configuration):
        self.columns = configuration.columns
        self.rows = configuration.rows
        self.inarow = configuration.inarow
        self.timeout = configuration.timeout - 0.34
        

    
    def play(self,board,column,mark):
        """ Plays a move """
        row = max([i for i in range(self.rows) if board[column + (i * self.columns)] == EMPTY])
        board[column + (row * self.columns)] = mark
        

    def check_win(self,board, column, mark):
        """ Checks for a win. """
        columns = self.columns
        rows = self.rows
        inarow = self.inarow

        # Check for vertical win
        if (row := max((r for r in range(rows) if board[column + r * columns] == mark), default=-1)) - inarow + 1 >= 0:
            return True

        # Check for horizontal win
        for offset in (-1, 1):
            count = 1
            for i in range(1, inarow):
                c = column + offset * i
                if c < 0 or c >= columns or board[c + row * columns] != mark:
                    break
                count += 1
            if count >= inarow:
                return True

        # Check for top left diagonal win
        count = 1
        for i in range(1, inarow):
            r = row + i
            c = column - i
            if r >= rows or c < 0 or board[c + r * columns] != mark:
                break
            count += 1
        if count >= inarow:
            return True

        # Check for top right diagonal win
        count = 1
        for i in range(1, inarow):
            r = row + i
            c = column + i
            if r >= rows or c >= columns or board[c + r * columns] != mark:
                break
            count += 1
        if count >= inarow:
            return True

        return False


    def check_tie(self,board):
        for mark in board:
            if mark == EMPTY:
                return False
        return True

    def check_finish_score(self ,board, column, mark):
        if self.check_win(board,column,mark):
            return (True,1)
        if self.check_tie(board):
            return (True, 0.5)
        else:
            return (False, None)
        
    def active_mark(self,mark):
        return 3-mark
    
    def backpropagate_scores(self,score):
        return 1 - score
    
    def random_action(self,board):
        return random.choice([c for c in range(self.columns) if board[c] == EMPTY])



    def default_policy_simulation(self,board,mark):
        
        original_mark = mark
        board = board.copy()
        column = self.random_action(board)
        self.play(board,column,mark)
        is_finish, score = self.check_finish_score(board, column, mark)
        while not is_finish:
            mark = self.active_mark(mark)
            column = self.random_action(board)
            self.play(board,column,mark)
            is_finish, score = self.check_finish_score(board,column,mark)
        if mark == original_mark:
            return score
        return backpropagate_scores(score)
    

    def find_action_taken(self,new_board, old_board):
        
        for i, piece in enumerate(new_board):
            if piece != old_board[i]:
                return i % self.columns
        return -1 




