import random
import numpy

def expect(n):
    count = 0
    
    result = []
    
    while count < n:
        money = 1
        while random.choice(['H', 'T']) == 'H':
            money = money * 2
        result.append(money)
        count += 1
        
    return numpy.mean(result)
        
        
