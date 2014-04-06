import fileinput
import sys
import time
import copy
import heapq


def main(noNodes, edges):
    mstPrim = {}
    graph = {}
    priQueue = []

    for i in xrange(0, noNodes):
        graph[i] = {'key': sys.maxint, 'parent': None}
    graph[0]['key'] = 0

    heapq.heappush(priQueue, [0, 0]) #key, node
    heapPopTime = 0
    checkIfNodeInGraphTime = 0
    adjacentNodesTime = 0
    findNextPathTime = 0

    while graph:
        #lowestKey = getLowestKey(graph) #lowestKey = integer
        #print graph
        #print "lowest key/node: ", lowestKey
        #print priQueue
        start = time.time()
        lowestNode = heapq.heappop(priQueue)[1]
        end = time.time()
        heapPopTime += end-start
        start = time.time()
        while True:
            if lowestNode in graph:
                break
            else:
                lowestNode = heapq.heappop(priQueue)[1]
        end = time.time()
        checkIfNodeInGraphTime += end-start
        #print "lowest Node: ", lowestNode
        #print "------------"
        #print "INTERVAL"
        #print "------------"
        vertex = graph.pop(lowestNode) #vertex = {'parent': integer/None, 'key': integer}
        mstPrim[lowestNode] = vertex
        if mstPrim[lowestNode]['parent'] != None:
            parent = mstPrim[lowestNode]['parent']
            if parent < lowestNode:
                edges[(parent, lowestNode)]['partOfMST'] = True
            else:
                edges[(lowestNode, parent)]['partOfMST'] = True
        start = time.time()
        adjacentNodes = getAllNeighbors(edges, lowestNode) #adjacentNodes = [node, ...] node=integer
        end = time.time()
        adjacentNodesTime += end-start
        start = time.time()
        for node in adjacentNodes:
            if lowestNode < node:
                if node in graph.keys() and edges[(lowestNode, node)]['weight'] < graph[node]['key']:
                    graph[node]['parent'] = lowestNode
                    graph[node]['key'] = edges[(lowestNode, node)]['weight']
                    heapq.heappush(priQueue, [edges[(lowestNode, node)]['weight'], node])
            else:
                if node in graph.keys() and edges[(node, lowestNode)]['weight'] < graph[node]['key']:
                    graph[node]['parent'] = lowestNode
                    graph[node]['key'] = edges[(node, lowestNode)]['weight']
                    heapq.heappush(priQueue, [edges[(node, lowestNode)]['weight'], node])
        end = time.time()
        findNextPathTime += end-start

    print "heapPopTime: ", heapPopTime
    print "checkIfNodeInGraphTime: ", checkIfNodeInGraphTime
    print "adjacentNodesTime: ", adjacentNodesTime
    print "findNextPathTime: ", findNextPathTime

    primWeight = 0
    for node in mstPrim:
        #print node, mstPrim[node]
        primWeight += mstPrim[node]['key']

    '''result = []
    for edge in edges:
        tmpEdges = edges.copy()
        tmpResult = []
        if edges[edge]['partOfMST']:
            tmpEdges.pop(edge)
            weight = primLite(noNodes, tmpEdges)
            tmpResult.append(edge[0])
            tmpResult.append(edge[1])
            tmpResult.append(weight)
        if tmpResult:
            result.append(tmpResult)'''
    print primWeight
    '''result = sorted(result, key=lambda line: (line[0],line[1]))
    for line in result:
        print line[0], line[1], line[2]'''

def primLite(noNodes, edges):
    mstPrim = {}
    graph = {}

    for i in xrange(0, noNodes):
        graph[i] = {'key': sys.maxint, 'parent': None}
    graph[0]['key'] = 0

    while graph:
        lowestKey = getLowestKey(graph) #lowestKey = integer
        vertex = graph.pop(lowestKey) #vertex = {'parent': integer, 'key': integer}
        mstPrim[lowestKey] = vertex
        adjacentNodes = getAllNeighbors(edges, lowestKey) #adjacentNodes = [node, ...] node=integer
        for node in adjacentNodes:
            if lowestKey < node:
                if node in graph.keys() and edges[(lowestKey, node)]['weight'] < graph[node]['key']:
                    graph[node]['parent'] = lowestKey
                    graph[node]['key'] = edges[(lowestKey, node)]['weight']
            else:
                if node in graph.keys() and edges[(node, lowestKey)]['weight'] < graph[node]['key']:
                    graph[node]['parent'] = lowestKey
                    graph[node]['key'] = edges[(node, lowestKey)]['weight']

    primWeight = 0
    for node in mstPrim:
        #print node, mstPrim[node]
        primWeight += mstPrim[node]['key']
    return primWeight
    '''print "removedEdge: "
    print removedEdge
    print "weight:"
    print primWeight'''
    

def getLowestKey(graph):
    lowestKey = 0
    lowestKeyWeight = sys.maxint
    for key in graph.keys():
        if graph[key]['key'] < lowestKeyWeight:
            lowestKeyWeight = graph[key]['key']
            lowestKey = key
    return lowestKey

# edges is a dictionary that stores the weight of a path between two vertexes.
# node is a given vertex
# getAllNeighbors returns all adjacent vertixes of node
def getAllNeighbors(edges, node):
    neighbors = []
    #print node
    for path in edges:
        #print path
        if path[0] == node:
            neighbors.append(path[1])
        if path[1] == node:
            neighbors.append(path[0])
    return neighbors

if __name__ == '__main__':
    start = time.time()
    edges = {}
    noNodes = 0
    for line in fileinput.input():
        line = line.split()
        if not fileinput.isfirstline():
            edges[(int(line[0]), int(line[1]))] = {'weight': int(line[2]), 'partOfMST': False}
        else:
            noNodes = int(line[0])
    main(noNodes, edges)
    end = time.time()
    print end - start