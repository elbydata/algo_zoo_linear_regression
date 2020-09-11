import numpy as np

def digit_sum(number):
    
    """Calculates digit sum of a number"""

    while len(str(number)) > 1:
        digit_sum = 0
        for d in str(number):
            digit_sum += int(d)
            number = digit_sum        
    return number