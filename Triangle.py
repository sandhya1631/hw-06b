def classifyTriangle(a, b, c):
    """Classify a triangle based on its side lengths."""
    
    if a <= 0 or b <= 0 or c <= 0:
        return "Invalid Input"

    if (a + b <= c) or (a + c <= b) or (b + c <= a):
        return "Not a Triangle"

    if a == b and b == c:
        return "Equilateral"
    
    if (a**2 + b**2 == c**2) or (b**2 + c**2 == a**2) or (a**2 + c**2 == b**2):
        return "Right Triangle"

    if a == b or b == c or a == c:
        return "Isosceles"

    return "Scalene"
