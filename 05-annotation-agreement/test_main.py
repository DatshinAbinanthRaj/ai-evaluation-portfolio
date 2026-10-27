import unittest
from main import evaluate

class EvaluationTests(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(evaluate({'a': [], 'b': []}), {'n': 0, 'agreement': None, 'kappa': None})

    def test_case_2(self):
        self.assertEqual(evaluate({'a': ['x', 'y'], 'b': ['x', 'y']}), {'n': 2, 'agreement': 1.0, 'kappa': 1.0})

    def test_case_3(self):
        self.assertEqual(evaluate({'a': ['x'], 'b': ['x']}), {'n': 1, 'agreement': 1.0, 'kappa': None})

    def test_boundary(self):
        with self.assertRaises(ValueError):
            evaluate({'a':['x'],'b':[]})

if __name__ == "__main__":
    unittest.main()
