import copy, math
graph2 = {('a', 'b') : 2,
          ('a', 'c') : 3,
          ('b', 'd') : 5,
          ('b', 'e') : 2,
          ('c', 'e') : 5,
          ('d', 'e') : 1,
          ('d', 'z') : 2,
          ('e', 'z') : 4}

graph3 = {('a', 'b') : 4,
          ('a', 'c') : 3,
          ('b', 'c') : 2,
          ('b', 'd') : 5,
          ('c', 'd') : 3,
          ('c', 'e') : 6,
          ('d', 'e') : 1,
          ('d', 'f') : 5,
          ('e', 'g') : 5,
          ('f', 'g') : 2,
          ('f', 'z') : 7,
          ('g', 'z') : 4}

graph4 = {('a', 'b') : 2,
          ('a', 'c') : 4,
          ('a', 'd') : 1,
          ('b', 'c') : 3,
          ('b', 'e') : 1,
          ('c', 'e') : 2,
          ('c', 'f') : 2,
          ('d', 'f') : 5,
          ('d', 'g') : 4,
          ('e', 'h') : 3,
          ('f', 'h') : 3,
          ('f', 'i') : 2,
          ('f', 'j') : 4,
          ('f', 'g') : 3,
          ('g', 'k') : 2,
          ('h', 'o') : 8,
          ('h', 'l') : 1,
          ('i', 'l') : 3,
          ('i', 'm') : 2,
          ('i', 'j') : 3,
          ('j', 'm') : 6,
          ('j', 'n') : 3,
          ('j', 'k') : 6,
          ('k', 'n') : 4,
          ('k', 'r') : 2,
          ('l', 'o') : 6,
          ('l', 'm') : 3,
          ('m', 'o') : 4,
          ('m', 'p') : 2,
          ('m', 'n') : 5,
          ('n', 'q') : 2,
          ('n', 'r') : 1,
          ('o', 's') : 6,
          ('o', 'p') : 2,
          ('p', 's') : 2,
          ('p', 't') : 1,
          ('p', 'q') : 1,
          ('q', 't') : 3,
          ('q', 'r') : 8,
          ('r', 't') : 5,
          ('s', 'z') : 2,
          ('t', 'z') : 8}

airline = {('s', 'n') : 245,
           ('s', 'c') : 175,
           ('s', 'd') : 140,
           ('s', 'l') : 75,
           ('d', 'c') : 130,
           ('d', 'l') : 120,
           ('l', 'n') : 230,
           ('c', 'b') : 130,
           ('c', 'n') : 110,
           ('c', 'a') : 100,
           ('n', 'b') : 50,
           ('n', 'a') : 115,
           ('a', 'm') : 90,
           ('n', 'm') : 165}

network = {('s', 'c') : 1855,
           ('s', 'd') : 957,
           ('s', 'l') : 349,
           ('d', 'c') : 908,
           ('d', 'a') : 645,
           ('l', 'c') : 1736,
           ('l', 'a') : 1235,
           ('c', 'a') : 798,
           ('c', 'b') : 860,
           ('c', 'n') : 722,
           ('b', 'n') : 191,
           ('a', 'n') : 1372}

network2 = {('s', 'c') : 1500,
           ('s', 'd') : 1000,
           ('s', 'l') : 400,
           ('d', 'c') : 500,
           ('d', 'a') : 600,
           ('l', 'c') : 1400,
           ('l', 'a') : 1100,
           ('c', 'a') : 800,
           ('c', 'b') : 900,
           ('c', 'n') : 700,
           ('b', 'n') : 300,
           ('a', 'n') : 1200}
           
           
          
        

def dijkstra(graph, start, end):
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
        u = min(L2, key = L.get)
        S.add(u)
        for v in Q - S:
            if (u, v) in graph.keys():
                if L[u] + graph[(u, v)] < L[v]:
                    L[v] = L[u] + graph[(u, v)]
                    previous[v] = u
        del L2[u]

    S2 = []
    u = end
    while u in previous.keys():
        S2 = [u] + S2
        u = previous[u]
                
    print(L[end], S2)
                
    
