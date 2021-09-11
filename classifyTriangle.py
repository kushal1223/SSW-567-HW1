#Kushal Patel

import unittest     # this makes Python unittest module available
import math

def classify_triangle(a,b,c):
    """
    
    This function returns a string with the type of triangle from three  values
    corresponding to the lengths of the three sides of the Triangle.
    
    return:
        If all three sides are equal, return 'Equilateral'
        If exactly one pair of sides are equal, return 'Isoceles'
        If no pair of  sides are equal, return 'Scalene'
        If not a valid triangle, then return 'NotATriangle'
        If the sum of any two sides equals the squate of the third side, then return 'Right'
        
        
    """
    # Note: This code is completely bogus but demonstrates a few features of python
    if (a+b <= c) or (b+c <= a) or (a+c <= b):
        return 'NotATriangle'
    if ((a * a + b*b) == (c*c)) or ((a*a + c*c) == (b*b)) or ((c*c + b*b) == (a*a)):
        if a == b and b == c:
            return 'Equilateral & Right'
        elif (a != b) and (b != c) and (a != c):
            return 'Scalene & Right'
        elif (a != b and (b == c or a == c)) or (a != c and (a == b or c == b)) or (b != c and (a == c or b == a)):
            return 'Isosceles & Right'
    
    if a == b and b == c:
        return 'Equilateral'
    elif a != b and b != c and a != c:
        return 'Scalene'
    elif (a != b and (b == c or a == c)) or (a != c and (a == b or c == b)) or (b != c and (a == c or b == a)):
            return 'Isosceles'
    else:
        return 'NotATriangle'
    
        
        
def runClassifyTriangle(a, b, c):
    """ invoke classifyTriangle with the specified arguments and print the result """
    print('classify_triangle(',a, ',', b, ',', c, ')= ',classify_triangle(a,b,c))


# The remainder of this code implements the unit test functionality

# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TestTriangles(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin
    # with 'test'.  Each function may include multiple tests
    def testSet1(self): # test invalid inputs
        # your tests go here.  Include as many tests as you'd like
        self.assertEqual(classify_triangle(3,4,5),'Scalene & Right') #Testing for right
        
    def testMyTestSet2(self): 
        # define multiple test sets to test different aspects of the code
        self.assertEqual(classify_triangle(1,1,1),'Equilateral') #Equilateral
        self.assertNotEqual(classify_triangle(10,10,10),'Isosceles')
        self.assertEqual(classify_triangle(6,6,8),'Isosceles') #Isoceles
        self.assertEqual(classify_triangle(4,5,6),'Scalene') #Scalene
        self.assertEqual(classify_triangle(10,15,30),'NotATriangle') #Not a triangle
        

if __name__ == '__main__':
    # examples of running the code
    runClassifyTriangle(1,2,3)
    runClassifyTriangle(1,1,1)
    runClassifyTriangle(3,4,5)
    runClassifyTriangle(2,2,5)
    runClassifyTriangle(6,6,8)
    runClassifyTriangle(3,4,6)
   

    unittest.main(exit=False) # this runs all of the tests - use this line if running from Spyder
    unittest.main(exit=True) # this runs all of the tests - use this line if running from the command line
    
    