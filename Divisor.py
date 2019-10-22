import math

def countDivisors(n) : 
    cnt = 0
    for i in range(1, (int)(math.sqrt(n)) + 1) : 
        if (n % i == 0) : 
              
            # If divisors are equal, 
            # count only one 
            if (n / i == i) : 
                cnt = cnt + 1
            else : # Otherwise count both 
                cnt = cnt + 2
                  
    return cnt

count = 0
for i in range(1, 101):
    count += countDivisors(i)

print(count)

sum = 0
for i in range(1, 101):
    sum += int(100/i)
print(sum)

    
