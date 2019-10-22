mathList = [('Aristotle', -384, -322),
            ('Boole', 1815, 1864),
            ('De Morgan', 1806, 1871),
            ('Lovelace', 1815, 1852),
            ('Dodgson', 1832, 1898),
            ('Decartes', 1596, 1650),
            ('Stirling', 1692, 1770),
            ('Al-Khowarizmi', 780, 850),
            ('Gauss', 1777, 1855),
            ('Eratosthenes', -276, -194),
            ('Mersenne', 1588, 1648),
            ('Euclid', -325, -265),
            ('Bezout', 1730, 1783),
            ('Fermat', 1601, 1665)]
matchedList = []
for i in mathList:
    for j in mathList:
        if i != j and set(range(i[1], i[2] + 1)) & set(range(j[1], j[2] + 1)) != set() and (j[0], i[0]) not in matchedList:
            matchedList.append((i[0], j[0]))
            print(i[0], j[0])
