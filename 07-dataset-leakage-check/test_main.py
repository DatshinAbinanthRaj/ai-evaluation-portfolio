import unittest
from main import evaluate

class EvaluationTests(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(evaluate({'train': ['A'], 'evaluation': [' a ']}), [{'evaluation_index': 0, 'train_indices': [0]}])

    def test_case_2(self):
        self.assertEqual(evaluate({'train': [''], 'evaluation': ['']}), [])

    def test_case_3(self):
        self.assertEqual(evaluate({'train': ['a', 'A'], 'evaluation': ['a']}), [{'evaluation_index': 0, 'train_indices': [0, 1]}])

if __name__ == "__main__":
    unittest.main()
