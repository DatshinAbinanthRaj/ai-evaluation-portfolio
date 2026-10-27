import unittest
from main import evaluate

class EvaluationTests(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(evaluate({'k': 2, 'retrieved': ['x', 'a'], 'relevant': ['a']}), {'precision_at_k': 0.5, 'recall_at_k': 1.0, 'reciprocal_rank_at_k': 0.5})

    def test_case_2(self):
        self.assertEqual(evaluate({'k': 1, 'retrieved': [], 'relevant': []}), {'precision_at_k': 0.0, 'recall_at_k': None, 'reciprocal_rank_at_k': 0})

    def test_case_3(self):
        self.assertEqual(evaluate({'k': 2, 'retrieved': ['a', 'a'], 'relevant': ['a']}), {'precision_at_k': 0.5, 'recall_at_k': 1.0, 'reciprocal_rank_at_k': 1.0})

    def test_boundary(self):
        with self.assertRaises(ValueError):
            evaluate({'k':0,'retrieved':[],'relevant':[]})

if __name__ == "__main__":
    unittest.main()
