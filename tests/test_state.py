import unittest
from state import State

class TestStates(unittest.TestCase):
    def test_initial_state(self):
        s = State()
        self.assertEqual(s.matrix, [0 for _ in range(9)])
    
    def test_move(self):
        s = State()
        correct = [0 for _ in range(9)]
        turn = 1

        for i in [1, 0, 4, 5, 6, 8, 7, 3, 2]:
            s.move(i)
            correct[i] = turn
            turn = 3 - turn
            self.assertEqual(s.matrix, correct)

    def test_choices(self):
        s = State()
        correct = [i for i in range(9)]

        self.assertEqual(s.choices(), correct)

        s.move(3)
        correct.remove(3)

        self.assertEqual(s.choices(), correct)

    def test_winner(self):
        """
         0 | 1 | 2
        ---|---|---
         3 | 4 | 5
        ---|---|---
         6 | 7 | 8
        """

        w = [
            [0, 4, 8],
            [2, 4, 6],
            [0, 1, 2],
            [3, 4, 5],
            [6, 7, 8],
            [0, 3, 6],
            [1, 4, 7],
            [2, 5, 8]
        ]

        for moves in w:
            s1, s2 = State(), State()
            s1.matrix, s2.matrix = [0 for _ in range(9)], [0 for _ in range(9)]

            for m in moves:
                s1.matrix[m] = 1
                s2.matrix[m] = 2
            
            self.assertEqual(s1.winner(), 1)
            self.assertEqual(s2.winner(), 2)


if __name__ == '__main__':
    unittest.main()
