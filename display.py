from state import State
from utils import clear_screen, cprint
from utils import BLACK

class Screen:
    def render(self, state: State):
        clear_screen()
        m = state.matrix

        dmap = lambda c : 'X' if c == 1 else 'O' if c == 2 else ' '

        for i in [0, 3, 6]:
            line = [dmap(m[i]), dmap(m[i + 1]), dmap(m[i + 2])]
            cprint(' | '.join(line) + '\n')
            if i < 6:
                cprint('--+---+--\n')

        print('\n\n')
        cprint('moves:\n\n', BLACK)
        
        cprint(' 7 | 8 | 9\n', BLACK)
        cprint('---|---|---\n', BLACK)
        cprint(' 4 | 5 | 6\n', BLACK)
        cprint('---|---|---\n', BLACK)
        cprint(' 1 | 2 | 3\n\n', BLACK)
