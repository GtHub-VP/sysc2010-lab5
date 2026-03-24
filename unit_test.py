def factorial_unit_testing(base_number: int) -> int:
    """
    This function tests factorials by taking a base number and outputting it's respective factorial result
    
    >>> factorial_unit_testing(5)
        120
        
    >>> factorial_unit_testing(1)
        1
    
    >>> factorial_unit_testing(0)    
        1
    """
    
    result = 1
    while base_number > 1:
        result *= base_number
        base_number -= 1
        
    return result 