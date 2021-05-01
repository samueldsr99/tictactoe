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

        if best_value > 1000:
            cprint('mmmm... I\'m about to win :)\n', YELLOW)
            input()
        return best_move

    def connection_value(self, arr: [], val: int):
        m = []
        for i in [0, 3, 6]:
            m.append([arr[i], arr[i + 1], arr[i + 2]])

        dr = [1, 0, -1, 0, 1, 1, -1, -1]
        dc = [0, 1, 0, -1, 1, -1, -1, 1]
        counter = 0
        for i in range(len(m)):
            for j in range(len(m[0])):
                if m[i][j] != val:
                    continue
                for d in range(8):
                    ni, nj = i + dr[d], j + dc[d]
                    if ni >= 0 and ni < 3 and nj >= 0 and nj < 3:
                        counter += (m[i][j] == m[ni][nj])
        return counter

    def leaf_value(self, state: State, winner: int, turn: int, moves_amount: int):
        BIAS = 1000
        if winner == turn: # win
            return BIAS + 1 / moves_amount
        if winner == 3 - turn: # lose
            return -1
        return self.connection_value(state.matrix, turn) # tie

    def min_value(self, state: State, turn: int, depth: int = 1):
        winner = state.winner()

        if winner != 0:
            return self.leaf_value(state, winner, turn, depth)

        choices = state.choices()
        random.shuffle(choices)

        mn = 9999999
        o = []
        for choice in choices:
            new_state = state.clone()
            new_state.move(choice)

            child_value = self.max_value(new_state, turn, depth + 1)
            o.append((child_value, choice))

            mn = min(mn, child_value)
        return mn

    def max_value(self, state: State, turn: int, depth: int = 1):
        winner = state.winner()

        if winner != 0:
            return self.leaf_value(state, winner, turn, depth)
        
        choices = state.choices()
        random.shuffle(choices)

        mx = -9999999
        for choice in choices:
            new_state = state.clone()
            new_state.move(choice)

            child_value = self.min_value(new_state, turn, depth + 1)

            mx = max(mx, child_value)
        return mx


class RandomAgent:
    def choice(self, state: State, turn: int):
        return random.choice(state.choices())


# Agent = RandomAgent
Agent = MiniMaxAgent

a = MiniMaxAgent()

print(a.connection_value([2, 1, 1, 1, 2, 2, 2, 1, 1], 1))

print(a.connection_value([2, 1, 2, 1, 1, 2, 1, 2, 1], 1))