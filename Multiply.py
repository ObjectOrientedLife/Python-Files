def multiply(iter):
    numbers = list(map(str, list(range(1, 10))))
    multiplied = numbers[:]
    for i in range(iter - 1):
        temp = []
        for p in multiplied:
            for q in numbers:
                temp.append(p + q)
        multiplied = temp
    print(multiplied)

multiply(3)
        
