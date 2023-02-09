import unittest
from count_islands import Solution

class TestSolution(unittest.TestCase):
    
    def test_Solution_load_data(self):
        result = Solution('tests/test_file').load_data()
        self.assertIsNone(result, "Value should be none")
    
    def test_Solution_count_islands_none(self):
        result = Solution('tests/test_file_none')
        self.assertEqual(result, 0, "")
    
    def test_Solution_count_islands_medio(self):
        result = Solution('tests/test_file_medio')
        self.assertEqual(result, 12, "")

    
    def test_Solution_count_islands_medio(self):
        result = Solution('tests/test_file_medio')
        self.assertEqual(result, 12, "")
