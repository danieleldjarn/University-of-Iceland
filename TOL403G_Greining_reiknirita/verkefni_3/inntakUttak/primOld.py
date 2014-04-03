import fileinput
import sys


w = {}
w[(0,1)] = 4

extract all the things from the weight function


def prim():
    graph = {}
    for line in fileinput.input():
        if not fileinput.isfirstline():
            #print line
            line = line.split()
            try:
                graph[line[0]].append([line[1], line[2]])
            except:
                graph[line[0]] = [[line[1], line[2]]]
    #print graph

    mst = {}

    for u in graph:
        mst[u] = [sys.maxint,sys.maxint]
        for v in xrange(0, len(graph[u])):
            #print graph[u][v][1]
            #print mst[u][1]
            print type(graph[u][v][1])
            print type(mst[u][1])
            #print int(graph[u][v][1]) < int(mst[u][1]) 
            if int(graph[u][v][1]) < int(mst[u][1]):
                #print "herpaderp"
                mst[u] = [graph[u][v][0], graph[u][v][1]]

    print mst

if __name__ == '__main__':
    prim()



'''
def prim():
    graph = {}
    emptyGraph = {}
    for line in fileinput.input():
        if fileinput.isfirstline():
            line = line.split()
            for i in xrange(0, int(line[0])-1):
                emptyGraph[i] = [[sys.maxint,sys.maxint]]
        else:
            #print line
            line = line.split()
            try:
                graph[line[0]].append([line[1], line[2]])
            except:
                graph[line[0]] = [[line[1], line[2]]]
    print graph
    print emptyGraph'''