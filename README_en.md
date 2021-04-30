# Minimax Agent for TicTacToe

This is a basic example of using the `minimax` search algorithm in the `TicTacToe` game. The agent selects the move that maximizes his chances of winning, however he does not take into account the number of moves to win (if there are 2 or more ways to win, he could select the longest one). In addition, it assumes that the opponent will always play optimally.

## Build

```bash
python3 main.py
```

## Implementation details

> All the agent logic was implemented in the `agent.py` file, allowing the user to be able to create an agent by himself to play this game, the agent created by you must implement the `choice(state, turn)`, which receives the current status and the agent's turn and returns an integer in the range `[0..9]` with the position of the box to be played, the boxes for this case are numbered as follows.

```
 0 | 1 | 2
---|---|---
 3 | 4 | 5
---|---|---
 6 | 7 | 8
```

> Also, the `state.py` file contains useful functions to handle the current state.

> (See examples of `RandomAgent` and `MinimaxAgent` in `agent.py`)