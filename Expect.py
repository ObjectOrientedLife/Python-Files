import random

redFund = [0.05, 0.2, 1.0, 3.0, 3.0, 3.0]
whiteFund = [0.95, 1.0, 1.0, 1.0, 1.0, 1.1]
blueFund = [0.8, 0.9, 1.1, 1.1, 1.2, 1.4]
resultList = []
year = 1

def randomDice(n):
    spotList = []
    for i in range(n):
        spotList.append(random.randint(1, 6))
    return spotList

def benefit(dice, fund, capital):
    for spot in dice:
        capital = capital * fund[spot - 1]
    return capital

for i in range(100):
    redDice = randomDice(year)
    whiteDice = randomDice(year)
    blueDice = randomDice(year)
    resultList.append((benefit(redDice, redFund, 50) + benefit(whiteDice, whiteFund, 50)) / 100)

def mean(l):
    sum = 1
    for i in l:
        sum = sum * i
    average = sum ** (1 / len(l))
    print(sum)
    print(average)

mean(resultList)



        
