import unittest
from count_islands import Solution

class TestSolution(unittest.TestCase):
    
    def test_Solution_count_islands_none(self):
        result = Solution('tests/test_file_none').num_islands()
        self.assertEqual(result, 0, "Test_none Failed")
    
    def test_Solution_load_data(self):
        result = Solution('tests/test_file').num_islands()
        self.assertEqual(result, 4, "Value should be 4")
    
    def test_Solution_count_islands_medio(self):
        result = Solution("./tests/test_file_medio").num_islands()
        self.assertEqual(result, 12, "test_file_medio Failed")

    
    def test_Solution_count_islands_medio(self):
        result = Solution('tests/test_file_medio_2').num_islands()
        self.assertEqual(result, 598753, "test_file_medio_2 failed")
