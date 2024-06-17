import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_rotate_3x3(self):
        matrix = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ]
        expected = [
            [7, 4, 1],
            [8, 5, 2],
            [9, 6, 3]
        ]
        self.solution.rotate(matrix)
        self.assertEqual(matrix, expected)

    def test_rotate_4x4(self):
        matrix = [
            [ 5,  1,  9, 11],
            [ 2,  4,  8, 10],
            [13,  3,  6,  7],
            [15, 14, 12, 16]
        ]
        expected = [
            [15, 13,  2,  5],
            [14,  3,  4,  1],
            [12,  6,  8,  9],
            [16,  7, 10, 11]
        ]
        self.solution.rotate(matrix)
        self.assertEqual(matrix, expected)

    def test_rotate_empty(self):
        matrix = []
        expected = []
        self.solution.rotate(matrix)
        self.assertEqual(matrix, expected)

if __name__ == '__main__':
    unittest.main()
