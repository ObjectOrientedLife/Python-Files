import itertools
g = {('a', 'b') : 3,
     ('a', 'c') : 5,
     ('a', 'd') : 2,
     ('b', 'c') : 6,
     ('b', 'd') : 4,
     ('c', 'd') : 7}

o = list(itertools.permutations(['a','b', 'c', 'd'], 4))

airline = {('s', 'd') : 329,
           ('s', 'n') : 359,
           ('s', 'v') : 179,
           ('s', 'l') : 69,
           ('d', 'v') : 229,
           ('d', 'n') : 189,
           ('d', 'l') : 349,
           ('v', 'n') : 279,
           ('v', 'l') : 209,
           ('l', 'n') : 379}
airlineo = list(itertools.permutations(['s', 'd', 'n', 'l', 'v'], 5))

def salesman(graph, order):
    graph2 = {}
    for edge in graph.keys():
        graph2[(edge[1], edge[0])] = graph[edge]
    graph.update(graph2)
    
    result = {}
    for i in order:
        sum = 0
        for j in range(3):
            sum += graph[(i[j], i[j + 1])]
        result[i] = sum
    lowest = min(result, key = result.get)
    print(lowest)
        
