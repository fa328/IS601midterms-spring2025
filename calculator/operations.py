'''This functions is for addition, subtraction, multiplication and division '''

def add(a: float, b: float) -> float:
    '''Test that addition function works.'''    
    return a + b

def subtract(a: float, b: float) -> float:
    '''Test that subract function works.'''    
    return a - b

def multiply(a: float, b: float) -> float:
    '''Test that multiply function works.'''    
    return a * b

def divide(a: float, b: float) -> float:
    '''Test that divide function works. Raises an error if dividing by zero.'''    
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b
