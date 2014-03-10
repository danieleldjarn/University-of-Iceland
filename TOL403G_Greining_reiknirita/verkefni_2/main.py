#!/usr/bin/env python
# -*- coding: utf-8 -*-

#from derpTree import DerpTree
from tree import Tree
import sys

# Notkun: parseInput(i)
# Fyrir: i er inntak af staðalinntaki
# Eftir: Búið er að greina gögnin í i og senda þau á réttan stað.
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

# Notkun: insert(t, l)
# Fyrir: t er tré. l er lína af upplýsingum
# Eftir: Búið er að setja gildi úr l í tréð t.
def insert(tree, line):
    value = map(int, line.split())
    tree.insert(value)
    #tree.printDerpTree()
    #print "MIXMIXMIX"

# Notkun: remove(t, l)
# Fyrir: t er tré. l er lína af upplýsingum
# Eftir: Búið er að fjarlægja gildi úr l í trénu t
def remove(tree, line):
    value = map(int, line.split())
    tree.delete(value)
    #tree.printDerpTree()
    #print "DELEDLELDEL"

# Notkun: search(t, l)
# Fyrir: t er tré. l er lína af upplýsingum
# Eftir: Búið er að finna allar nóður í t sem uppfylla skilyrðin sem eru listuð í l
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