list = []

def makeBit(n, bitString = ''):
    global list
    if n == 0:
        list.append(bitString)
    else:
        makeBit(n - 1, bitString + '0')
        makeBit(n - 1, bitString + '1')

makeBit(8)

count = 0

for i in list:
    if '1111' in i and '000' in i:
        count += 1

print count
        
