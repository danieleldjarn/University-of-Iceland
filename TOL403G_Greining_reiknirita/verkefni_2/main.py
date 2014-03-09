#!/usr/bin/env python
# -*- coding: utf-8 -*-

#from derpTree import DerpTree
from tree import Tree
import sys

def parseInput(input):
    t = Tree()
    for line in input:
        if line.startswith('+'):
            line = line.replace('+', '')
            insert(t, line)
        if line.startswith('-'):
            line = line.replace('-', '')
            remove(t, line)
        if line.startswith('?'):
            line = line.replace('?', '')
            search(t, line)

def insert(tree, line):
    value = map(int, line.split())
    tree.insert(value)
    #tree.printDerpTree()
    #print "MIXMIXMIX"

def remove(tree, line):
    value = map(int, line.split())
    tree.delete(value)
    #tree.printDerpTree()
    #print "DELEDLELDEL"

def search(tree, line):
    if line.startswith('o'):
        line = line.replace('o', '')
        value = map(int, line.split())
        tree.searchIntersect(value)

    if line.startswith('i'):
        line = line.replace('i', '')
        value = map(int, line.split())
        tree.searchInclusive(value)

    if line.startswith('p'):
        line = line.replace('p', '')
        value = int(line)
        tree.searchSingle(value)

    tree.printOutput()

if __name__=="__main__":
    parseInput(sys.stdin)
    '''t = DerpTree()
    t.insert([4,5])
    t.insert([2,6])
    t.insert([0,3])
    t.insert([2,6])
    t.searchInclusive([4,6])'''