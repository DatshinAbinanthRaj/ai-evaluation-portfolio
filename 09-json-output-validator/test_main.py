import unittest
from main import evaluate

class EvaluationTests(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(evaluate({'schema': {'x': 'integer'}, 'value': {'x': True}}), {'valid': False, 'errors': ['x: wrong type']})

    def test_case_2(self):
        self.assertEqual(evaluate({'schema': {'x': 'string'}, 'value': {}}), {'valid': False, 'errors': ['x: missing']})

    def test_case_3(self):
        self.assertEqual(evaluate({'schema': {'x': 'number'}, 'value': {'x': 2.5}}), {'valid': True, 'errors': []})

if __name__ == "__main__":
    unittest.main()
