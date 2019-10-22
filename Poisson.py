import math

def poisson(lam, k):
    f = lam**k * math.exp(-lam) / math.factorial(k)
    return f
