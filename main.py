from display import Screen
from utils import cprint, GREEN, RED, YELLOW
from state import State
from agent import Agent
from argparse import ArgumentParser


map_move = {
    7: 0, 8: 1, 9: 2,
    4: 3, 5: 4, 6: 5,
    1: 6, 2: 7, 3: 8,
}
imap_move = {
    0: 7, 1: 8, 2: 9,
    3: 4, 4: 5, 5: 6,
    6: 1, 7: 2, 8: 3,
}


def start(player_turn=1):
    state = State()
    screen = Screen()
    agent = Agent()
    agent_turn = 3 - player_turn
    while not state.winner():
        screen.render(state)
        if state.turn == agent_turn:
            choice = agent.choice(state, agent_turn)
            try:
                state.move(choice)
            except ValueError:
                cprint('Invalid position, AI is broken!', RED)
                input()
                continue
        else:
            inp = input()
            if inp == '':
                continue
            inp = int(inp)
            if inp < 1 or inp > 9:
                cprint('Invalid position', RED)
                input()
                continue
            pos = map_move[inp]
            try:
                state.move(pos)
            except ValueError:
                cprint('Invalid position', RED)
                input()
                continue

    screen.render(state)
    winner = state.winner()

    if winner == -1:
        cprint(f'Tie!\n', YELLOW)
    else:
        cprint(f'Player {winner} wins!\n', GREEN)


if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument(
        '--turn', default='1', type=int, help='Your turn (1 or 2)')
    args = parser.parse_args()

    start(player_turn=int(args.turn))
