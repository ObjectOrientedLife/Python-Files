import random
import time

def monteCarlo(n):
    count = 0
    target = 0
    startTime = time.time()
    while count < n:
        x, y = random.random() + 1, random.random()
        if y < 1 / x:
            target += 1
        count += 1
    endTime = time.time()
    print(2**(n / target))
    print(endTime - startTime)

def lattice(n):
    area = n**2
    count = 0
    for i in range(n, 2 * n):
        for j in range(0, n):
            x = i / n
            y = j / n
            if y < 1 / x:
                count += 1
    print(2**(area / count))
