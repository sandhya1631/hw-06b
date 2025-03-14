import unittest
from Triangle import classifyTriangle

class TestTriangles(unittest.TestCase):
    # Test for valid equilateral triangles
    def testEquilateralTriangles(self):
        self.assertEqual(classifyTriangle(1, 1, 1), 'Equilateral', '1,1,1 should be equilateral')
        self.assertEqual(classifyTriangle(5, 5, 5), 'Equilateral', '5,5,5 should be equilateral')
        self.assertEqual(classifyTriangle(10, 10, 10), 'Equilateral', '10,10,10 should be equilateral')
    
    # Test for valid isosceles triangles
    def testIsoscelesTriangles(self):
        self.assertEqual(classifyTriangle(2, 2, 3), 'Isosceles', '2,2,3 should be isosceles')
        self.assertEqual(classifyTriangle(5, 5, 8), 'Isosceles', '5,5,8 should be isosceles')
        self.assertEqual(classifyTriangle(5, 8, 5), 'Isosceles', '5,8,5 should be isosceles')
        self.assertEqual(classifyTriangle(8, 5, 5), 'Isosceles', '8,5,5 should be isosceles')
    
    # Test for valid scalene triangles
    def testScaleneTriangles(self):
        self.assertEqual(classifyTriangle(2, 3, 4), 'Scalene', '2,3,4 should be scalene')
        self.assertEqual(classifyTriangle(7, 8, 9), 'Scalene', '7,8,9 should be scalene')
        self.assertEqual(classifyTriangle(3, 5, 7), 'Scalene', '3,5,7 should be scalene')
    
    # Test for valid right triangles (all three orientations)
    def testRightTriangles(self):
        self.assertEqual(classifyTriangle(3, 4, 5), 'Right', '3,4,5 should be right')
        self.assertEqual(classifyTriangle(5, 3, 4), 'Right', '5,3,4 should be right')
        self.assertEqual(classifyTriangle(4, 5, 3), 'Right', '4,5,3 should be right')
        self.assertEqual(classifyTriangle(5, 12, 13), 'Right', '5,12,13 should be right')
        self.assertEqual(classifyTriangle(8, 15, 17), 'Right', '8,15,17 should be right')
    
    # Test for invalid triangles (violating triangle inequality theorem)
    def testInvalidTriangles(self):
        self.assertEqual(classifyTriangle(1, 2, 3), 'NotATriangle', '1,2,3 should not be a triangle')
        self.assertEqual(classifyTriangle(1, 3, 2), 'NotATriangle', '1,3,2 should not be a triangle')
        self.assertEqual(classifyTriangle(3, 1, 2), 'NotATriangle', '3,1,2 should not be a triangle')
        self.assertEqual(classifyTriangle(10, 2, 7), 'NotATriangle', '10,2,7 should not be a triangle')
    
    # Test for invalid inputs - negative values
    def testNegativeInputs(self):
        self.assertEqual(classifyTriangle(-1, 2, 3), 'InvalidInput', '-1,2,3 should be invalid')
        self.assertEqual(classifyTriangle(1, -2, 3), 'InvalidInput', '1,-2,3 should be invalid')
        self.assertEqual(classifyTriangle(1, 2, -3), 'InvalidInput', '1,2,-3 should be invalid')
        self.assertEqual(classifyTriangle(-1, -2, -3), 'InvalidInput', '-1,-2,-3 should be invalid')
    
    # Test for invalid inputs - zero values
    def testZeroInputs(self):
        self.assertEqual(classifyTriangle(0, 2, 3), 'InvalidInput', '0,2,3 should be invalid')
        self.assertEqual(classifyTriangle(1, 0, 3), 'InvalidInput', '1,0,3 should be invalid')
        self.assertEqual(classifyTriangle(1, 2, 0), 'InvalidInput', '1,2,0 should be invalid')
        self.assertEqual(classifyTriangle(0, 0, 0), 'InvalidInput', '0,0,0 should be invalid')
    
    # Test for invalid inputs - non-integer values
    def testNonIntegerInputs(self):
        self.assertEqual(classifyTriangle(1.5, 2, 3), 'InvalidInput', '1.5,2,3 should be invalid')
        self.assertEqual(classifyTriangle(1, 2.5, 3), 'InvalidInput', '1,2.5,3 should be invalid')
        self.assertEqual(classifyTriangle(1, 2, 3.5), 'InvalidInput', '1,2,3.5 should be invalid')
        self.assertEqual(classifyTriangle("1", 2, 3), 'InvalidInput', '"1",2,3 should be invalid')
    
    # Test for boundary cases - large values
    def testLargeInputs(self):
        self.assertEqual(classifyTriangle(100, 100, 100), 'Equilateral', '100,100,100 should be equilateral')
        self.assertEqual(classifyTriangle(500, 500, 700), 'Isosceles', '500,500,700 should be isosceles')
        self.assertEqual(classifyTriangle(1000, 800, 600), 'Scalene', '1000,800,600 should be scalene')

    # Test right triangles that are also isosceles
    def testRightIsoscelesTriangles(self):
        self.assertEqual(classifyTriangle(1, 1, 2**0.5), 'Right', '1,1,sqrt(2) should be right (and isosceles)')
        # Note: This might fail due to the integer check in the function

if __name__ == '__main__':
    unittest.main()
