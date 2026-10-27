import unittest
from main import evaluate

class EvaluationTests(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(evaluate({'budget': 1, 'events': []}), {'cost': 0.0, 'over_budget': False, 'flags': []})

    def test_case_2(self):
        self.assertEqual(evaluate({'budget': 1, 'events': [{'type': 'tool', 'tool': 'send', 'action_id': 'x', 'requires_approval': True}]}), {'cost': 0.0, 'over_budget': False, 'flags': [{'event': 0, 'issue': 'missing_approval'}]})

    def test_case_3(self):
        self.assertEqual(evaluate({'budget': 1, 'events': [{'type': 'approval', 'action_id': 'x'}, {'type': 'tool', 'tool': 'send', 'action_id': 'x', 'requires_approval': True}]}), {'cost': 0.0, 'over_budget': False, 'flags': []})

    def test_boundary(self):
        self.assertEqual(evaluate({'budget':1,'events':[{'type':'tool','action_id':'a','tool':'search','status':'error'}]*3})['flags'], [{'event':2,'issue':'three_failures_same_tool'}])

if __name__ == "__main__":
    unittest.main()
