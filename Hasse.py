import itertools
import copy

S = ['A', 'B', 'C', 'D', 'E', 'F']
result = []

def hasse(R, order = ''):
    global result
    if len(R) == 1:
        order = order + R[0][0] + R[0][1]
        result.append(order)
        return
    availableElement = copy.deepcopy(S)
    
    for element in R:
        if element[1] in availableElement:
            availableElement.remove(element[1])
        
    for element in R:
        if element[0] in availableElement:
            hasse([x for x in R if x[0] != element[0]], order + element[0])

hasse([('A', 'B'), ('C', 'B'), ('B', 'D'), ('B', 'F'), ('E', 'F'), ('D', 'G'), ('F', 'G')])
result = list(set(result))
for i in result:
    print(i)
