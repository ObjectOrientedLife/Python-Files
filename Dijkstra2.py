import copy, math

graph2 = {('a', 'b') : 2,
          ('a', 'c') : 3,
          ('b', 'd') : 5,
          ('b', 'e') : 2,
          ('c', 'e') : 5,
          ('d', 'e') : 1,
          ('d', 'z') : 2,
          ('e', 'z') : 4}

def dijkstra2(graph, start, end):
    graph2 = {}
    for edge in graph.keys():
        graph2[(edge[1], edge[0])] = graph[edge]
    graph.update(graph2)
    
    Q = set([])
    L = {}
    previous = {}
    
    edge = list(graph.keys())
    for i in edge:
        Q.update(i[0], i[1])
        
    for i in Q:
        if i == start:
            L[i] = 0
        else:
            L[i] = math.inf

    S = set([])
    L2 = copy.deepcopy(L)

    while end not in S:
        print(L)
        u = max(L2, key = L.get)
        S.add(u)
        for v in Q - S:
            if (u, v) in graph.keys():
                if L[v] == math.inf:
                    L[v] = L[u] + graph[(u, v)]
                elif L[u] + graph[(u, v)] > L[v]:
                    L[v] = L[u] + graph[(u, v)]
                    previous[v] = u
        del L2[u]

    S2 = []
    u = end
    while u in previous.keys():
        S2 = [u] + S2
        u = previous[u]
                
    print(L[end], S2)
