#!/usr/bin/env python
# -*- coding: utf-8 -*-

from node import Node
''' An implementation of splay tree in python '''

import sys
sys.setrecursionlimit(10000)

class Tree:

    def __init__(self):
        self.root = Node()
        self.resultToPrint = []
    
    # Notkun:   t.insert(i)
    # Fyrir:    t er hlutur af gerð tree og i er bil.
    # Eftir:    Búið er að bæta bilinu i inn í tréið t á réttan stað
    def insert(self, interval):
        self._insert(interval, self.root)

    def _insert(self, interval, node):
        leftInsert = False
        rightInsert = True
        # If the node has no interval we set it's interval to the new interval.
        if node.interval == None:
            node.interval = interval


        # To put the new interval in the correct position we start by
        # comparing the lower end of the interval and then the 
        # higher end of the interval.
        # If the exact same interval is in the tree nothing will happen.

        elif interval[0] < node.interval[0]:
            if node.left == None:
                self.placeNewNode(interval, node, leftInsert)
            else:
                self._insert(interval, node.left)
        elif interval[0] > node.interval[0]:
            if node.right == None:
                self.placeNewNode(interval, node, rightInsert)
            else:
                self._insert(interval, node.right)
        elif interval[0] == node.interval[0]:
            if interval[1] < node.interval[1]:
                if node.left == None:
                    self.placeNewNode(interval, node, leftInsert)
                else:
                    self._insert(interval, node.left)
            elif interval[1] > node.interval[1]:
                if node.right == None:
                    self.placeNewNode(interval, node, rightInsert)
                else:
                    self._insert(interval, node.right)

    def placeNewNode(self, interval, node, rightInsert):
        if rightInsert:
            node.right = Node(interval, node)
            self.splay(node.right)
            self.setRoot()
        else:
            node.left = Node(interval, node)
            self.splay(node.left)
            self.setRoot()

            

    def setRoot(self):
        oldRoot = self.root
        rootParent = self.root.parent
        rootGrandParent = self.root.parent.parent
        if rootGrandParent != None:
            if rootParent == rootGrandParent.left:
                self.root = rootGrandParent
                self.root.left = rootParent
                if rootGrandParent.right:
                    rootGrandParent.right.parent = self.root
                rootParent.parent = self.root
                rootParent.left = oldRoot
            elif rootParent == rootGrandParent.right:
                self.root = rootGrandParent
                self.root.right = rootParent
                if rootGrandParent.left:
                    rootGrandParent.left.parent = self.root
                rootParent.parent = self.root
                rootParent.right = oldRoot
        else:
            if self.root == rootParent.left:
                self.root = rootParent
                self.root.left = oldRoot
                oldRoot.parent = self.root
            elif self.root == rootParent.right:
                self.root = rootParent
                self.root.right = oldRoot
                oldRoot.parent = self.root

    # Usage:    n = t.search(i)
    # Before:   t is an object of type tree and i is an interval.+
    # After:    If i was in the tree, n is the node containing i. If i is not in the tree n is None
    def search(self, interval, node):
        if interval == node.interval:
            return node
        elif interval[0] != node.interval[0]:
            if interval[0] > node.interval[0]:
                if node.right == None:
                    return None
                else:
                    return self.search(interval, node.right)
            elif interval[0] < node.interval[0]:
                if node.left == None:
                    return None
                else:
                    return self.search(interval, node.left)
        else:
            if interval[1] > node.interval[1]:
                if node.right == None:
                    return None
                else:
                    return self.search(interval, node.right)
            elif interval[1] < node.interval[1]:
                if node.left == None:
                    return None
                else:
                    return self.search(interval, node.left)

    def searchInclusive(self, interval):
        self._searchInclusive(interval, self.root)

    def _searchInclusive(self, interval, node):
        if node.interval[0] <= interval[0] and interval[1] <= node.interval[1]:
            self.resultToPrint.append(node.interval)
        if node.left != None:
            self._searchInclusive(interval, node.left)
        if node.right != None:
            self._searchInclusive(interval, node.right)

    # Usage:    t.searchSingle(p)
    # Before:   t is an object of type tree, p is an integer (point)
    # After:    All intervals in t that include p have been added to resultToPrint
    def searchSingle(self, value):
        self._searchSingle(value, self.root)

    def _searchSingle(self, value, node):
        if node.interval[0] <= value and value <= node.interval[1]:
            self.resultToPrint.append(node.interval)
        if node.left != None:
            self._searchSingle(value, node.left)
        if node.right != None:
            self._searchSingle(value, node.right)

    def searchIntersect(self, interval):
        self._searchIntersect(interval, self.root)

    # Usage:    t.searchIntersect(i)
    # Before:   t is an object of type tree, i is an interval
    # After:    All intervals in t that intersect i have been added to resultToPrint
    def _searchIntersect(self, interval, node):
        if interval[0] <= node.interval[1] and node.interval[0] <= interval[1]:
            self.resultToPrint.append(node.interval)
        if node.left != None:
            self._searchIntersect(interval, node.left)
        if node.right != None:
            self._searchIntersect(interval, node.right)

    # Usage:    t.printOutput()
    # Before:   t is an object of type tree
    # After:    The contents of the global variable resultToPrint have been printed
    #           onto standar output
    def printOutput(self):
        stringToPrint = ""
        if self.resultToPrint == []:
            print "[]"
        else:
            self.resultToPrint.sort()
            for interval in self.resultToPrint:
                stringToPrint += str(interval)

            print stringToPrint
            self.resultToPrint = []

    def count_children(self, node):
        children = 0
        if node.left != None:
            children += 1
        if node.right != None:
            children += 1
        return children

    def delete(self, interval):
        self._delete(interval, self.root)

    def _delete(self, interval, root):
        if root == None:
            return False
        else:
            node = self.search(interval, root)
            if node != None and node.interval == interval:
                children = self.count_children(node)
                if children == 0:
                    self.zeroLeafs(node)
                elif children == 1:
                    self.oneLeaf(node)
                elif children == 2:
                    self.twoLeafs(node)

    def zeroLeafs(self, node):
        parent = node.parent
        if parent != None:
            if node == parent.left:
                parent.left = None
            else:
                parent.right = None
        else:
            self.root = None
            node = None

    def oneLeaf(self, node):
        parent = node.parent
        if parent != None:
            if node.left != None:
                if node == parent.left:
                    node.left.parent = parent
                    parent.left = node.left
                else:
                    node.left.parent = parent
                    parent.right = node.left
            else:
                if node == parent.right:
                    node.right.parent = parent
                    parent.right = node.right
                else:
                    node.right.parent = parent
                    parent.left = node.right
        else:
            #Node is the root of the tree
            if node.left != None:
                self.root = node.left
                node = None
            else:
                self.root = node.right
                node = None

    def twoLeafs(self, node):
        successor = self.treeMin(node.right)
        node.interval = successor.interval

        if successor.right != None:
            self.oneLeaf(successor)
        else:
            self.zeroLeafs(successor)

    def treeMin(self, node):
        while node.left != None:
            node = node.left
        return node

#   Notkun: node.rotate_left()
#   Fyrir : node er hlekkur i Splay tre
#   Eftir : Buid er ad faera node upp um eitt saeti eins og sest eftirfarandi mynd
#       (n = node)
#
#       p          n
#      / \   =>   / \
#     A   n      p   C
#        / \    / \
#       B   C  A   B 
    def rotate_left(self, node):
        parent = node.parent
        if parent != None:
            grand_parent = parent.parent
            if grand_parent != None:
                if parent == grand_parent.left:
                    grand_parent.left = node
                else:
                    grand_parent.right = node
                if node.left != None:
                    node.left.parent = parent
                parent.right = node.left
                parent.parent = node
                node.left = parent
                node.parent = grand_parent
            else:
                root_parent = parent.parent
                if node.left != None:
                    node.left.parent = parent
                parent.right = node.left
                parent.parent = node
                node.left = parent
                node.parent = root_parent

#   Notkun: node.rotate_right()
#   Fyrir : node er hlekkur i Splay tre
#   Eftir : Buid er ad faera node upp um eitt saeti eins og sest eftirfarandi mynd
#       (n = node)
#
#         p        n
#        / \  =>  / \
#       n   C    A   p
#      / \          / \
#     A   B        B   C
    def rotate_right(self, node):
        parent = node.parent
        if parent != None :
            grand_parent = parent.parent
            if grand_parent != None:
                if parent == grand_parent.left:
                    grand_parent.left = node
                else:
                    grand_parent.right = node
                if node.right != None:
                    node.right.parent = parent
                parent.left = node.right
                parent.parent = node
                node.right = parent
                node.parent = grand_parent
            else:
                root_parent = parent.parent
                if node.right != None:
                    node.right.parent = parent
                parent.left = node.right
                parent.parent = node
                node.right = parent
                node.parent = root_parent

    def splay(self, node):
        if node.parent == None:
            return
        elif node.parent.parent == None:
            parent = node.parent
            if node == parent.left:    # Zikk
                self.rotate_right(node)
                self.splay(node)
            else:                           # Zakk
                self.rotate_left(node)
                self.splay(node)
        else:
            parent = node.parent
            grand_parent = node.parent.parent

            if parent == grand_parent.left:
                if node == parent.left:     # Zikk Zikk
                    self.rotate_right(parent)
                    self.rotate_right(node)
                    self.splay(node)
                else:                       # Zikk Zakk
                    self.rotate_left(node)
                    self.rotate_right(node)
                    self.splay(node)
            else:
                if node == parent.left:     # Zakk Zikk
                    self.rotate_right(node)
                    self.rotate_left(node)
                    self.splay(node)
                else:                       # Zakk Zakk
                    self.rotate_left(parent)
                    self.rotate_left(node)
                    self.splay(node)
