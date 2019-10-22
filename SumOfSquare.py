for m in range(2, 10000):
    listOfSquare = []
    for n in range(1, int(m / 2 + 1)):
        sumOfSquare = str(n**2 + (m - n)**2)
        for i in listOfSquare:
            if sumOfSquare == i[0][::-1]:
                print(i, (sumOfSquare, n, m - n))
        listOfSquare.append((sumOfSquare, n, m - n))
    
    
