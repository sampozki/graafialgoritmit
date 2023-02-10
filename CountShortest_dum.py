#! /usr/bin/env python
""" Breadth-first search example """

from graafi3 import Graph


def ReadSet(filename):
    ff = open(filename,'r')
    x = ff.readlines()[0].split()
    S = set([])
    for i in x:
        S.add(int(i))
    return S


# Counts shortest graph's route from startVertex to finalVertex by using most vertexes from subset
def CountShortest(graph, subset, startVertex, finalVertex):
    # Following code is pretty much just BFS but with small changes
    routeMembers = []
    visitedVertexes = set()
    vertexList = [(startVertex, [startVertex])]

    while vertexList:
        vertex, path = vertexList.pop(0)
        visitedVertexes.add(vertex)

        try: 
            for vertex in graph.AL[vertex]:

                # If vertex is finalVertex, then add it to routeMembers
                if vertex == finalVertex:
                    routeMembers.append(path + [finalVertex])

                # Else mark vertex as visited if algoritm hasn't visit it yet. Also add currenty path ito vertexList
                else:
                    if vertex not in visitedVertexes:
                        visitedVertexes.add(vertex)
                        vertexList.append((vertex, path + [vertex]))

        except Exception as e:
            return "Error happened: " + str(e)
    
    # Pretty ugly way to do this but oneliner and list comprehension are cool :D
    # Finds shortest routes based on their lenght and strips any longer paths out and overwrites the variable
    routeMembers = [i for i in routeMembers if len(i) == min([len(i) for i in routeMembers])]

    subSetVisitCount = []

    # Following files check how many subset vertexes are in shortest paths and sum their amounts together
    for i in routeMembers:
        n = 0
        for vertex in subset:
            if vertex in i:
                n += 1

        subSetVisitCount.append(n)
    
    # Check if there is a route from start to final vertexes
    if routeMembers == []:
        return "No path from startVertex to finalVertex"     
    
    # Check if there are any subset vertexes in the route
    # If there is/are then return biggest amount of them
    if subSetVisitCount != []:
        return max(subSetVisitCount)
    else:
        return "No subset vertexes in the shortest path"
