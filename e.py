def e(n):
    factorial = 1
    sum = 0
    for i in range(1, n + 1):
        sum += 1 / factorial
        factorial = factorial * i
    print(sum)

e(100)
