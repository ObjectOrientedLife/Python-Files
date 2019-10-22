def f(n):
    if n == 0:
        return 1

    result = 1
    
    for i in range(1, n + 1):
        result *= i
        
    return result

def p(n, r):
    return f(n) / f(n - r)

def c(n, r):
    return p(n, r) / f(r)

