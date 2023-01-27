#! /usr/bin/env python
""" Breadth-first search example """

from graafi3 import Graph



def ReadSet(filename):
    ff = open(filename,'r')
    x = ff.readlines()[0].split()
    S =set([])
    for i in x:
        S.add(int(i))
    return S




# CountShortest(G, B, 6,4)
def CountShortest(graph, subset, startVertex, finalVertex):

    # print("Graph members: " + str(graph.V))
    # print("Graph: " + str(graph.AL))
    # print("Set: " + str(subset))

    routeMembers = []

    queue = [(startVertex, [startVertex])]
    visited = set()

    while queue:
        vertex, path = queue.pop(0)
        visited.add(vertex)

        try: 
            for node in graph.AL[vertex]:

                if node == finalVertex:
                    routeMembers.append(path + [finalVertex])

                else:
                    if node not in visited:
                        visited.add(node)
                        queue.append((node, path + [node]))
        except Exception as e:
            return e

    routeMembers = [i for i in routeMembers if len(i) == min([len(i) for i in routeMembers])]
    

    subSetVisitCount = []

    for i in routeMembers:
        n = 0
        for vertex in subset:
            if vertex in i:
                n += 1

        subSetVisitCount.append(n)
    
    return max(subSetVisitCount)
