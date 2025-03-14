import unittest
from Triangle import classifyTriangle

class TestTriangles(unittest.TestCase):
    def testRightTriangle(self): 
        self.assertEqual(classifyTriangle(3,4,5),'Right','3,4,5 is a Right triangle')
        
    def testEquilateralTriangle(self): 
        self.assertEqual(classifyTriangle(1,1,1),'Equilateral','1,1,1 should be equilateral')
        
    def testScaleneTriangle(self): 
        self.assertEqual(classifyTriangle(2,3,4),'Scalene','2,3,4 should be scalene')
        
    def testIsoscelesTriangle(self): 
        self.assertEqual(classifyTriangle(2,2,3),'Isosceles','2,2,3 should be isosceles')
        
    def testInvalidInput(self):
        self.assertEqual(classifyTriangle(-1,2,3),'InvalidInput','-1,2,3 should be invalid')

if __name__ == '__main__':
    unittest.main()
