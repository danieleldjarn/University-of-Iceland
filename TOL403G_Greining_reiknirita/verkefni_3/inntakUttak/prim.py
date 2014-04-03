import fileinput
import sys


def main():
    weight = {}
    mstPrim = {}
    graph = {}
    count = 0

    for line in fileinput.input():
        line = line.split()
        if not fileinput.isfirstline():
            weight[(int(line[0]), int(line[1]))] = int(line[2])
            weight[(int(line[1]), int(line[0]))] = int(line[2])
        else:
            count = int(line[0])

    for i in xrange(0, count):
        graph[i] = {'key': sys.maxint, 'parent': None}
    graph[0]['key'] = 0

    while graph:
        lowestKey = getLowestKey(graph) #lowestKey = integer
        vertex = graph.pop(lowestKey) #vertex = {'parent': integer, 'key': integer}
        mstPrim[lowestKey] = vertex
        adjacentNodes = getAllNeighbors(weight, lowestKey) #adjacentNodes = [node, ...] node=integer
        for node in adjacentNodes:
            if node in graph.keys() and weight[(lowestKey, node)] < graph[node]['key']:
                graph[node]['parent'] = lowestKey
                graph[node]['key'] = weight[(lowestKey, node)]

    primWeight = 0
    for node in mstPrim:
        #print node, mstPrim[node]
        primWeight += mstPrim[node]['key']
    print "RESULT:"
    print primWeight
    

def getLowestKey(tempGraph):
    lowestKey = 0
    lowestKeyWeight = sys.maxint
    for key in tempGraph.keys():
        if tempGraph[key]['key'] < lowestKeyWeight:
            lowestKeyWeight = tempGraph[key]['key']
            lowestKey = key
    return lowestKey

# weight is a dictionary that stores the weight of a path between two vertexes.
# u is a given vertex
# getAllNeighbors returns all adjacent vertixes of u
def getAllNeighbors(weight, u):
    neighbors = []
    for path in weight:
        if path[0] == u and path[1] not in neighbors:
            neighbors.append(path[1])
    return neighbors

    '''print weight
    print weight.keys()
    keys = weight.keys()
    #print count
    i = 0
    span = []
    while i < count:
        lowestWeight = sys.maxint
        for k in keys:
            if k[0] == i:
                if weight[k] < lowestWeight:
                    lowestWeight = weight[k]
                    span.append(k)
        #print i
        i += 1

    print span
    shortestPath = 0
    for i in span:
        shortestPath += weight[i]
    print shortestPath'''

if __name__ == '__main__':
    main()