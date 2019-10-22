import math
g = {('a', 'b') : 4,
     ('a', 'c') : 2,
     ('b', 'd') : 5,
     ('b', 'c') : 1,
     ('c', 'd') : 8,
     ('c', 'e') : 10,
     ('d', 'e') : 2,
     ('d', 'z') : 6,
     ('e', 'z') : 3}

def floyd(graph):
    
    graph2 = {}
    for edge in graph.keys():
        graph2[(edge[1], edge[0])] = graph[edge]
    graph.update(graph2)
    
    Q = set([])
    edge = list(graph.keys())
    for i in edge:
        Q.update(i[0], i[1])

    d = {}
    for i in Q:
        for j in Q:
            if (i, j) in graph.keys():
                d[(i, j)] = graph[(i, j)]
            elif i == j:
                d[(i, j)] = 0
            else:
                d[(i, j)] = math.inf
                

    for i in Q:
        for j in Q:
            for k in Q:
                if d[(j, i)] + d[(i, k)] < d[(j, k)]:
                    d[(j, k)] = d[(j, i)] + d[(i, k)]
    print(d)

                
            
