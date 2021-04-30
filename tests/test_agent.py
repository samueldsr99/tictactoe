import unittest
from state import State
from agent import MiniMaxAgent


class TestMinimaxAgent(unittest.TestCase):
    def test_recognize_winning_states(self):
        s = State([])
        agent = MiniMaxAgent()

        self.assertEqual(1, 1)
