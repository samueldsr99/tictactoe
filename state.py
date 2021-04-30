class State:
    def __init__(self, matrix: [] = None):
        if matrix is None:
            self.matrix = [0 for _ in range(9)]
            self.turn = 1
        else:
            self.matrix = matrix

            # Check player turn from matrix info
            self.turn = 1
            for row in matrix:
                for cell in matrix:
                    if cell != 0:
                        self.turn = 3 - self.turn

    def move(self, pos: int):
        if self.matrix[pos] != 0:
            raise ValueError('Invalid position')
        self.matrix[pos] = self.turn
        self.turn = 3 - self.turn

    def winner(self):
        """
         0 | 1 | 2
        ---|---|---
         3 | 4 | 5
        ---|---|---
         6 | 7 | 8
        winner id if there is a winner
        -1 if not
        0 if game has not ended
        """

        m = self.matrix
        # Horizontal
        for i in [0, 3, 6]:
            if self._equal(m[i], m[i + 1], m[i + 2]):
                return m[i]

        # Vertical
        for i in [0, 1, 2]:
            if self._equal(m[i], m[i + 3], m[i + 6]):
                return m[i]

        # Diagonals
        if self._equal(m[0], m[4], m[8]):
            return m[0]
        if self._equal(m[2], m[4], m[6]):
            return m[2]

        if len(self.choices()) > 0:
            return 0

        return -1

    def choices(self):
        return [i for i, v in enumerate(self.matrix) if v == 0]

    def clone(self):
        s = State()
        s.matrix = [self.matrix[i] for i in range(9)]
        s.turn = self.turn
        return s

    def _equal(self, x: int, y: int, z: int):
        return x != 0 and x == y and y == z and x == z

    @staticmethod
    def encode(row: int, col: int):
        return row * 3 + col

    @staticmethod
    def decode(pos: int):
        pos = pos - 1
        return pos // 3, pos % 3 # row, col

    def __str__(self):
        m = self.matrix

        dmap = lambda c : 'X' if c == 1 else 'O' if c == 2 else ' '

        ret = ""

        for i in [0, 3, 6]:
            line = [dmap(m[i]), dmap(m[i + 1]), dmap(m[i + 2])]
            ret += ' | '.join(line) + '\n'
            if i < 6:
                ret += '--+---+--\n'

        return ret
