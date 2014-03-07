#!/usr/bin/env python
# -*- coding: utf-8 -*-

class DerpTree(object):
    def __init__(self):
        self.derpTree = []

    def insert(self, value):
        if value not in self.derpTree:
            self.derpTree.append(value)
        else:
            print "value already in derpTree"

    def delete(self, value):
        if value in self.derpTree:
            self.derpTree.remove(value)
        else:
            print "value not in list"

    #finnur öll bil sem inniheldur value
    def searchSingle(self, value):
        resultToPrint = []
        for node in self.derpTree:
            if value >= node[0] and value <= node[1]:
                resultToPrint.append(node)
        self.printOutput(resultToPrint)

    #finnur öll bil sem skarast við value
    def searchIntersect(self, value):
        resultToPrint = []
        for node in self.derpTree:
            if value[0] >= node[0] and value[0] <= node[1]:
                resultToPrint.append(node)
                continue
            if value[1] >= node[0] and value[1] <= node[1]:
                resultToPrint.append(node)
        self.printOutput(resultToPrint)

    #finnur öll bil [c,d] fyrir value [a, b] þar sem c<=a og b<=d
    def searchInclusive(self, value):
        resultToPrint = []
        for node in self.derpTree:
            if node[0] <= value[0] and value[1] <= node[1]:
                resultToPrint.append(node)
        self.printOutput(resultToPrint)

    def printOutput(self, output):
        stringToPrint = ""
        for value in output:
            stringToPrint += str(value)
            
        if output == []:
            print '[]'
        else:
            print stringToPrint

    def printDerpTree(self):
        for node in self.derpTree:
            print node
