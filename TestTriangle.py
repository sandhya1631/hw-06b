import unittest
from Triangle import classifyTriangle

class TestTriangle(unittest.TestCase):
    
    def test_equilateral(self):
        self.assertEqual(classifyTriangle(3, 3, 3), "Equilateral")
    
    def test_isosceles(self):
        self.assertEqual(classifyTriangle(5, 5, 3), "Isosceles")

    def test_scalene(self):
        self.assertEqual(classifyTriangle(4, 5, 6), "Scalene")

    def test_right_triangle(self):
        self.assertEqual(classifyTriangle(3, 4, 5), "Right Triangle")

    def test_invalid_triangle(self):
        self.assertEqual(classifyTriangle(1, 2, 3), "Not a Triangle")

    def test_negative_values(self):
        self.assertEqual(classifyTriangle(-1, 2, 3), "Invalid Input")

    def test_zero_values(self):
        self.assertEqual(classifyTriangle(0, 0, 0), "Invalid Input")

if __name__ == '__main__':
    unittest.main()
