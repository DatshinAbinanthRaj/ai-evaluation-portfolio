import unittest
from main import evaluate

class EvaluationTests(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(evaluate({'votes': []}), {'A': 0, 'B': 0, 'ties': 0, 'invalid': 0, 'A_win_rate_excluding_ties': None})

    def test_case_2(self):
        self.assertEqual(evaluate({'votes': ['A', 'B']}), {'A': 1, 'B': 1, 'ties': 0, 'invalid': 0, 'A_win_rate_excluding_ties': 0.5})

    def test_case_3(self):
        self.assertEqual(evaluate({'votes': ['tie', 'x']}), {'A': 0, 'B': 0, 'ties': 1, 'invalid': 1, 'A_win_rate_excluding_ties': None})

if __name__ == "__main__":
    unittest.main()
