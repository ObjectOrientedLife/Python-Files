def intSum(string):
    sum = 0
    for i in range(len(string)):
        sum += int(string[i])
    return sum

count = 0

for i in range(1000000

               ):
    i = str(i)
    if intSum(i) == 19:
        count += 1

print count
