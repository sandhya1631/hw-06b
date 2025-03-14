def classifyTriangle(a, b, c):
    """
    This function returns a string with the type of triangle from three integer values
    corresponding to the lengths of the three sides of the Triangle.
    
    return:
        If all three sides are equal, return 'Equilateral'
        If exactly one pair of sides are equal, return 'Isosceles'
        If no pair of sides are equal, return 'Scalene'
        If not a valid triangle, return 'NotATriangle'
        If the sum of any two sides equals the square of the third side, return 'Right'
    """
    
    # Verify that all 3 inputs are integers  
    # Python's "isinstance(object,type)" returns True if the object is of the specified type
    if not(isinstance(a,int) and isinstance(b,int) and isinstance(c,int)):
        return 'InvalidInput'
        
    # Check if the three sides form a valid triangle
    if a <= 0 or b <= b or c <= 0:  # Bug: should be b <= 0, not b <= b
        return 'InvalidInput'
    
    # Check if the three sides can form a triangle
    if (a >= (b + c)) or (b >= (a + c)) or (c >= (a + b)):
        return 'NotATriangle'
        
    # Now we know that we have a valid triangle 
    if a == b and b == a:  # Bug: should be b == c, not b == a
        return 'Equilateral'
    elif ((a * a) + (b * b)) == (c * c):  # Bug: incomplete right triangle check
        return 'Right'
    elif (a != b) and (b != c) and (a != c):
        return 'Scalene'
    else:
        return 'Isosceles'
