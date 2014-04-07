import fileinput
import sys
import copy
import heapq


def main(noNodes, edges, neighbors):
    mstPrim = {}
    priQueue = []

    graph = initializeGraph()

    heapq.heappush(priQueue, [0, 0]) #key, node

    while graph:
        lowestNode = getLowestNode(priQueue, graph)
        vertex = graph.pop(lowestNode) #vertex = {'parent': integer/None, 'key': integer}
        mstPrim[lowestNode] = vertex
        if mstPrim[lowestNode]['parent'] != None:
            parent = mstPrim[lowestNode]['parent']
            if parent < lowestNode:
                edges[(parent, lowestNode)]['partOfMST'] = True
            else:
                edges[(lowestNode, parent)]['partOfMST'] = True
        
        adjacentNodes = neighbors[lowestNode]
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

    primWeight = 0
    for node in mstPrim:
        primWeight += mstPrim[node]['key']

    result = []
    for edge in edges:
        tmpResult = []
        if edges[edge]['partOfMST']:
            edges[edge]['partOfSolution'] = False
            
            neighborsOriginal1 = copy.deepcopy(neighbors[edge[0]])
            neighborsOriginal2 = copy.deepcopy(neighbors[edge[1]])
        
            neighborsNew1 = copy.deepcopy(neighborsOriginal1)
            neighborsNew2 = copy.deepcopy(neighborsOriginal2)
            neighborsNew1.remove(edge[1])
            neighborsNew2.remove(edge[0])
            
            neighbors[edge[0]] = neighborsNew1
            neighbors[edge[1]] = neighborsNew2
            
            weight = primLite(noNodes, edges, neighbors)
            tmpResult.append(edge[0])
            tmpResult.append(edge[1])
            tmpResult.append(weight)
            
            neighbors[edge[0]] = neighborsOriginal1
            neighbors[edge[1]] = neighborsOriginal2

            edges[edge]['partOfSolution'] = True
            
        if tmpResult:
            result.append(tmpResult)
    print primWeight
    result = sorted(result, key=lambda line: (line[0],line[1]))
    for line in result:
        print line[0], line[1], line[2]

def initializeGraph():
    graph = {}
    for i in xrange(0, noNodes):
        graph[i] = {'key': sys.maxint, 'parent': None}
    graph[0]['key'] = 0
    return graph

def getLowestNode(priQueue, graph):
    lowestNode = heapq.heappop(priQueue)[1]
    while True:
        if lowestNode in graph:
            break
        else:
            lowestNode = heapq.heappop(priQueue)[1]
    return lowestNode

def primLite(noNodes, edges, neighbors):
    mstPrim = {}
    priQueue = []

    graph = initializeGraph()

    heapq.heappush(priQueue, [0, 0]) #key, node
    
    while graph:
        lowestNode = getLowestNode(priQueue, graph)
        
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