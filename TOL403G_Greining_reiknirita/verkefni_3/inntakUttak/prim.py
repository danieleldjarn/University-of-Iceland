import fileinput
import sys
import time
import copy
import heapq


def main(noNodes, edges, neighbors):
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
        vertex = graph.pop(lowestNode) #vertex = {'parent': integer/None, 'key': integer}
        mstPrim[lowestNode] = vertex
        if mstPrim[lowestNode]['parent'] != None:
            parent = mstPrim[lowestNode]['parent']
            if parent < lowestNode:
                edges[(parent, lowestNode)]['partOfMST'] = True
            else:
                edges[(lowestNode, parent)]['partOfMST'] = True
        start = time.time()
        
        adjacentNodes = neighbors[lowestNode]
        
        end = time.time()
        adjacentNodesTime += end-start
        start = time.time()
        for node in adjacentNodes:
            if lowestNode < node:
                if node in graph and edges[(lowestNode, node)]['weight'] < graph[node]['key']:
                    graph[node]['parent'] = lowestNode
                    graph[node]['key'] = edges[(lowestNode, node)]['weight']
                    heapq.heappush(priQueue, [edges[(lowestNode, node)]['weight'], node])
            else:
                if node in graph and edges[(node, lowestNode)]['weight'] < graph[node]['key']:
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

    result = []
    tmpNeighbors = {}
    tmpEdges = {}
    counter = 0
    creationTime = 0
    neighborTime = 0
    restTime = 0
    startEverything = time.time()
    for edge in edges:
        tmpResult = []
        if edges[edge]['partOfMST']:
            start = time.time()
            #tmpEdges = dict(edges)
            edges[edge]['partOfSolution'] = False
            end = time.time()
            creationTime += end-start
            
            start = time.time()
            neighborsOriginal1 = copy.deepcopy(neighbors[edge[0]])
            neighborsOriginal2 = copy.deepcopy(neighbors[edge[1]])
        
            neighborsNew1 = copy.deepcopy(neighborsOriginal1)
            neighborsNew2 = copy.deepcopy(neighborsOriginal2)
            neighborsNew1.remove(edge[1])
            neighborsNew2.remove(edge[0])
            
            neighbors[edge[0]] = neighborsNew1
            neighbors[edge[1]] = neighborsNew2
            end = time.time()
            neighborTime += end-start

            
            
            #tmpEdges.pop(edge)

            

            start = time.time()
            
            weight = primLite(noNodes, edges, neighbors)
            #weight = 3
            tmpResult.append(edge[0])
            tmpResult.append(edge[1])
            tmpResult.append(weight)
            
            neighbors[edge[0]] = neighborsOriginal1
            neighbors[edge[1]] = neighborsOriginal2

            end = time.time()
            restTime += end-start
            edges[edge]['partOfSolution'] = True
            
        if tmpResult:
            result.append(tmpResult)
        counter += 1
    endEverything = time.time()
    print "NEWTIMEs"
    print "creationTime: ", creationTime
    print "neighborTime: ", neighborTime
    print "restTime: ", restTime
    print "everything: ", endEverything-startEverything
    print primWeight
    '''result = sorted(result, key=lambda line: (line[0],line[1]))
    for line in result:
        print line[0], line[1], line[2]'''

def primLite(noNodes, edges, neighbors):
    mstPrim = {}
    graph = {}
    priQueue = []

    for i in xrange(0, noNodes):
        graph[i] = {'key': sys.maxint, 'parent': None}
    graph[0]['key'] = 0

    heapq.heappush(priQueue, [0, 0]) #key, node
    

    while graph:
        
        lowestNode = heapq.heappop(priQueue)[1]
        
        while True:
            if lowestNode in graph:
                break
            else:
                lowestNode = heapq.heappop(priQueue)[1]
        
        vertex = graph.pop(lowestNode) #vertex = {'parent': integer/None, 'key': integer}
        mstPrim[lowestNode] = vertex
        
        adjacentNodes = neighbors[lowestNode]
        
        for node in adjacentNodes:
            
            if lowestNode < node:
                if node in graph and edges[(lowestNode, node)]['weight'] < graph[node]['key'] and edges[(lowestNode, node)]['partOfSolution']:
                    graph[node]['parent'] = lowestNode
                    graph[node]['key'] = edges[(lowestNode, node)]['weight']
                    heapq.heappush(priQueue, [edges[(lowestNode, node)]['weight'], node])
            else:
                if node in graph and edges[(node, lowestNode)]['weight'] < graph[node]['key'] and edges[(node, lowestNode)]['partOfSolution']:
                    graph[node]['parent'] = lowestNode
                    graph[node]['key'] = edges[(node, lowestNode)]['weight']
                    heapq.heappush(priQueue, [edges[(node, lowestNode)]['weight'], node])

    primWeight = 0
    for node in mstPrim:
        #print node, mstPrim[node]
        primWeight += mstPrim[node]['key']
    return primWeight

if __name__ == '__main__':
    start = time.time()
    edges = {}
    neighbors = {}
    noNodes = 0
    for line in fileinput.input():
        line = line.split()
        if not fileinput.isfirstline():
            edges[(int(line[0]), int(line[1]))] = {'weight': int(line[2]), 'partOfMST': False, 'partOfSolution': True}
            try:
                neighbors[int(line[0])].append(int(line[1]))
            except:
                neighbors[int(line[0])] = [int(line[1])]
            try:
                neighbors[int(line[1])].append(int(line[0]))
            except:
                neighbors[int(line[1])] = [int(line[0])]
        else:
            noNodes = int(line[0])
    main(noNodes, edges, neighbors)
    end = time.time()
    print end - start