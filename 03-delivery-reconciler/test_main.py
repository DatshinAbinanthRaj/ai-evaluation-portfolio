import unittest
from main import evaluate

class EvaluationTests(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(evaluate({'orders': [], 'tickets': []}), [])

    def test_case_2(self):
        self.assertEqual(evaluate({'orders': [{'zone': 'B', 'diameter_mm': 16, 'kg': 100}], 'tickets': []}), [{'zone': 'B', 'diameter_mm': 16, 'ordered_kg': 100.0, 'delivered_kg': 0.0, 'variance_kg': -100.0}])

    def test_case_3(self):
        self.assertEqual(evaluate({'orders': [], 'tickets': [{'id': 'x', 'zone': 'A', 'diameter_mm': 12, 'kg': 20}]}), [{'zone': 'A', 'diameter_mm': 12, 'ordered_kg': 0.0, 'delivered_kg': 20.0, 'variance_kg': 20.0}])

    def test_boundary(self):
        with self.assertRaises(ValueError):
            evaluate({'orders':[], 'tickets':[{'id':'x','zone':'A','diameter_mm':16,'kg':1}]*2})

if __name__ == "__main__":
    unittest.main()
