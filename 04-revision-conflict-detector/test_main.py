import unittest
from main import evaluate

class EvaluationTests(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(evaluate({'old': [], 'new': [{'id': 'x'}]}), [{'id': 'x', 'status': 'added'}])

    def test_case_2(self):
        self.assertEqual(evaluate({'old': [{'id': 'x'}], 'new': []}), [{'id': 'x', 'status': 'removed'}])

    def test_case_3(self):
        self.assertEqual(evaluate({'old': [{'id': 'x', 'v': 1}], 'new': [{'id': 'x', 'v': 1}]}), [])

    def test_boundary(self):
        with self.assertRaises(ValueError):
            evaluate({'old':[{'id':'x'},{'id':'x'}],'new':[]})

if __name__ == "__main__":
    unittest.main()
