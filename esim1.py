#! /usr/bin/env python
from graafi3 import Graph
from CountShortest_dum import CountShortest

def ReadSet(filename):
    ff = open(filename,'r')
    x = ff.readlines()[0].split()
    S = set([])
    for i in x:
        S.add(int(i))
    return S


# Helper function for running simple tests.
def runSimpleTest(graphFile, setFile, startVertex, endVertex):
    G = Graph('tests/simple/' + graphFile)
    B = ReadSet('tests/simple/' + setFile)
    x = CountShortest(G, B, startVertex, endVertex)

    print("Test: " + graphFile + " with " + setFile + ": " + str(x))


if __name__ == "__main__":
    print("Simple tests: ")


    # These simple test cases are spaghetti
    print("First two tests should output errors as testgraph_sensible0 is malformatted")
    runSimpleTest("testgraph_sensible0", "testset_sensible0", 0, 1)
    runSimpleTest("testgraph_sensible0", "testset_sensible0_b", 0, 1)
    print()

    print("This test should output: 10")
    runSimpleTest("testgraph_sensible1", "testset_sensible1_a", 1, 10)
    print()

    print("This test should output: 0, because 0 isn't in graph")
    runSimpleTest("testgraph_sensible1", "testset_sensible1_b", 1, 10)
    print()

    print("There shouldn't be route from start to finish vertexes")
    runSimpleTest("testgraph_sensible2", "testset_sensible2_a", 2, 5)
    print()

    print("Should output: 1")
    runSimpleTest("testgraph_sensible2", "testset_sensible2_b", 1, 10)
    print()

    # This test data is formatted [startVertex, finalVertex, expected value]:
    testData = [[1,10,3], [1,20,2], [1,30,2], [1,40,2], [1,50,3], [1,60,4], [1,70,4], [1,80,4], [1,90,3], [1,100,3]]

    print("Ten tests:")

    # Run all different test situations in a for loop
    for i in range(len(testData)):
        G = Graph('tests/ten/testgraph_' + str(i + 1))
        B = ReadSet('tests/ten/testset_' + str(i + 1))
        x = CountShortest(G, B, testData[i][0], testData[i][1])
        
        print("Test case " + "[" + str(testData[i][0]) + ", " 
        + str(testData[i][1]) + ", " + str(testData[i][2]) + "]: Actual value: " 
        + str(x) + ", Expected value: " + str(testData[i][2]))
