import unittest
from main import evaluate

class EvaluationTests(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(evaluate({'reference': 1, 'reference_unit': 'm', 'candidate': 1000, 'candidate_unit': 'mm', 'tolerance': 0}), {'status': 'pass', 'absolute_error': 0.0})

    def test_case_2(self):
        self.assertEqual(evaluate({'reference': 1, 'reference_unit': 'kg', 'candidate': 1, 'candidate_unit': 'm', 'tolerance': 0}), {'status': 'incompatible_units'})

    def test_case_3(self):
        self.assertEqual(evaluate({'reference': 10, 'reference_unit': 'kg', 'candidate': 9, 'candidate_unit': 'kg', 'tolerance': 0.5}), {'status': 'fail', 'absolute_error': 1.0})

    def test_boundary(self):
        with self.assertRaises(ValueError):
            evaluate({'reference':1,'candidate':1,'tolerance':-1,'reference_unit':'m','candidate_unit':'m'})

if __name__ == "__main__":
    unittest.main()
