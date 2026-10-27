import unittest
from main import evaluate

class EvaluationTests(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(evaluate({'sources': {'a': 'hello  world'}, 'claims': [{'id': '1', 'source_id': 'a', 'quote': 'hello world'}]}), [{'id': '1', 'status': 'quote_present'}])

    def test_case_2(self):
        self.assertEqual(evaluate({'sources': {}, 'claims': [{'id': '2', 'source_id': 'x', 'quote': 'x'}]}), [{'id': '2', 'status': 'missing_source'}])

    def test_case_3(self):
        self.assertEqual(evaluate({'sources': {'a': 'abc'}, 'claims': [{'id': '3', 'source_id': 'a', 'quote': ''}]}), [{'id': '3', 'status': 'quote_missing'}])

if __name__ == "__main__":
    unittest.main()
