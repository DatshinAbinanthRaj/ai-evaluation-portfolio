import unittest
from main import evaluate

class EvaluationTests(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(evaluate({'cases': []}), [])

    def test_case_2(self):
        self.assertEqual(evaluate({'cases': [{'id': 'a', 'severity': 'low', 'confidence': 0.9}]}), [])

    def test_case_3(self):
        self.assertEqual(evaluate({'cases': [{'id': 'a', 'severity': 'critical', 'confidence': 1}]}), [{'id': 'a', 'priority': 40, 'reasons': ['high_severity']}])

    def test_boundary(self):
        with self.assertRaises(ValueError):
            evaluate({'cases':[{'id':'a','confidence':1.1,'severity':'low'}]})

if __name__ == "__main__":
    unittest.main()
