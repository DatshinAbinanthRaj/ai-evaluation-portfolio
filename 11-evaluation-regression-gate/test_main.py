import unittest
from main import evaluate

class EvaluationTests(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(evaluate({'baseline': {}, 'candidate': {}}), {'regressions': [], 'improvements': [], 'gate': 'no_data'})

    def test_case_2(self):
        self.assertEqual(evaluate({'baseline': {'a': True}, 'candidate': {'a': False}}), {'regressions': ['a'], 'improvements': [], 'gate': 'fail'})

    def test_case_3(self):
        self.assertEqual(evaluate({'baseline': {'a': False}, 'candidate': {'a': True}}), {'regressions': [], 'improvements': ['a'], 'gate': 'pass'})

    def test_boundary(self):
        with self.assertRaises(ValueError):
            evaluate({'baseline':{'a':True},'candidate':{}})

if __name__ == "__main__":
    unittest.main()
