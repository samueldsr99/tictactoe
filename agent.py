from state import State
import random
from utils import cprint, clear_screen
from utils import (
    BLACK,
    RED,
    GREEN,
    YELLOW,
    BLUE,
    MAGENTA,
    CYAN,
    WHITE
)

class MiniMaxAgent:
    """
    TicTacToe agent that implements Minimax choice criteria
    """
    def choice(self, state: State, turn: int):
        # Minimax decision
        choices = state.choices()
        random.shuffle(choices)

        best_move, best_value = 0, -2
        percent = 0

        for i, choice in enumerate(choices):
            new_state = state.clone()
            new_state.move(choice)
            
            child_value = self.min_value(new_state, turn)
            percent += 100 / len(choices)
            cprint(f'Thinking... {percent}%\n', CYAN)
            if child_value > best_value:
                best_value = child_value
                best_move = choice

        if best_value == 1:
            cprint('mmmm... I\'m about to win :)\n', YELLOW)
            input()
        return best_move

    def leaf_value(self, winner: int, turn: int):
        if winner == turn: # win
            return 1
        if winner == 3 - turn: # lose
            return -1
        return 0 # tie

    def min_value(self, state: State, turn: int):
        winner = state.winner()

        if winner != 0:
            return self.leaf_value(winner, turn)

        choices = state.choices()
        random.shuffle(choices)

        mn = 9999999
        o = []
        for choice in choices:
            new_state = state.clone()
            new_state.move(choice)

            child_value = self.max_value(new_state, turn)
            o.append((child_value, choice))

            mn = min(mn, child_value)
        return mn

    def max_value(self, state: State, turn: int):
        winner = state.winner()

        if winner != 0:
            return self.leaf_value(winner, turn)
        
        choices = state.choices()
        random.shuffle(choices)

        mx = -9999999
        for choice in choices:
            new_state = state.clone()
            new_state.move(choice)

            child_value = self.min_value(new_state, turn)

            mx = max(mx, child_value)
        return mx


class RandomAgent:
    def choice(self, state: State, turn: int):
        return random.choice(state.choices())


# 
Agent = RandomAgent
