#! /usr/bin/env python
from coursecodes.graafi3 import Graph
from CountShortest_dum import CountShortest

def ReadSet(filename):
    ff = open(filename,'r')
    x = ff.readlines()[0].split()
    S =set([])
    for i in x:
        S.add(int(i))
    return S

if __name__ == "__main__":


    # Simple tests

    print("Simple tests: ")

    G = Graph('tests/simple/testgraph_sensible0')
    B = ReadSet('tests/simple/testset_sensible0')
    x = CountShortest(G, B, 0, 1)
    
    print(x)


    print()
    # Ten tests:

    # normal tests
    testData = [[1,10,3], [1,20,2], [1,30,2], [1,40,2], [1,50,3], [1,60,4], [1,70,4], [1,80,4], [1,90,3], [1,100,3]]

    print("Test syntax: value, (correct value)")

    for i in range(len(testData)):

        
        G = Graph('tests/ten/testgraph_' + str(i + 1))
        B = ReadSet('tests/ten/testset_' + str(i + 1))
        x = CountShortest(G, B, testData[i][0], testData[i][1])
        
        print("Test case " + "[" + str(testData[i][0]) + ", " + str(testData[i][1]) + ", " + str(testData[i][2]) + "]")
        print(str(x) + ", (" + str(testData[i][2]) + ")")

        print()
