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
        
        # If the node has no interval we set it's interval to the new interval.
        if node.interval == None:
            node.interval = interval
            node.max = interval[1]
            self.setMaxInsert(node)

        # To put the new interval in the correct position we start by
        # comparing the lower end of the interval and then the 
        # higher end of the interval.
        # If the exact same interval is in the tree nothing will happen.
        elif interval[0] < node.interval[0]:
            if node.left == None:
                node.left = Node(interval, node)
                node.left.max = interval[1]
                self.setMaxInsert(node.left)
                #self.splay(node.left)
                #self.root = node.left
            else:
                self._insert(interval, node)
        elif interval[0] > node.interval[0]:
            if node.right == None:
                node.right = Node(interval, node)
                node.right.max = interval[1]
                self.setMaxInsert(node.right)
                #self.splay(node.right)
                #self.root = node.right
            else:
                self._insert(interval, node.right)
        elif interval[0] == node.interval[0]:
            if interval[1] < node.interval[1]:
                if node.left == None:
                    node.left = Node(interval, node)
                    node.left.max = interval[1]
                    self.setMaxInsert(node.left)
                    #self.splay(node.left)
                    #self.root = node.left
                else:
                    self._insert(interval, node.left)
            elif interval[1] > node.interval[1]:
                if node.right == None:
                    node.right = Node(interval, node)
                    node.right.max = interval[1]
                    self.setMaxInsert(node.right)
                    #self.splay(node.right)
                    #self.root = node.right
                else:
                    self._insert(interval, node.right)

    def setMaxInsert(self, node):
        newMax = node.max
        parent = node.parent
        #print newMax
        while parent != None and parent.max < newMax:
            grandParent = parent.parent
            #if parent.max < newMax:
             #   parent.max = newMax
            parent.max = newMax
            parent = grandParent

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
        if node.left != None and interval[1] <= node.left.max:
            self._searchInclusive(interval, node.left)
        if node.right != None and interval[1] <= node.right.max:
            self._searchInclusive(interval, node.right)

    def searchSingle(self, value):
        self._searchSingle(value, self.root)

    def _searchSingle(self, value, node):
        if node.interval[0] <= value and value <= node.interval[1]:
            self.resultToPrint.append(node.interval)
        if node.left != None and value <= node.left.max:
            self._searchSingle(value, node.left)
        if node.right != None and value <= node.right.max:
            self._searchSingle(value, node.right)

    def searchIntersect(self, interval):
        self._searchIntersect(interval, self.root)

    def _searchIntersect(self, interval, node):
        if interval[0] <= node.interval[1] and node.interval[0] <= interval[1]:
            self.resultToPrint.append(node.interval)
        if node.left != None and interval[1] <= node.left.max:
            self._searchIntersect(interval, node.left)
        if node.right != None and interval[1] <= node.right.max:
            self._searchIntersect(interval, node.right)

    def printOutput(self):
        stringToPrint = ""
        if self.resultToPrint == []:
            print "[]" #þetta verður að vera. Return dugar ekki.
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

    def max(self, node):
        if node.interval == None:
            return None
        else:
            tmpNode = node
            while tmpNode.right != None:
                tmpNode = tmpNode.right
            return tmpNode


    '''def delete(self, interval):
        self._delete(interval, self.root)

    # This version of delete is much simpler because it uses the Splay
    # command to bring the node to be deleted to the root. Therefore
    # There is only one case that needs to be considdered when deleting
    def _delete(self, interval, root):
        node = self.search(interval, root)
        if node:
            self.setMaxDelete(node)
            self.splay(node)

            if interval != node.interval:
                raise "Interval not in tree"

            if node.left == None:
                node = node.right
                node.parent = None
            if node.right == None:
                node = node.left
                node.parent = None
            else:
                temp = node.right
                node = node.left
                node.splay(node.left.max()) #hvað er þetta?
                node.right = temp
                node.parent = None
        else:
            raise "Node not in tree"
'''
    def setMaxDelete(self, node):
        parent = node.parent
        if parent != None:
            oldMax = node.max
            childMax = -1
            siblingMax = -1
            biggestRelativeMax = -1
            if node.left:
                childMax = node.left.max
            if node.right and childMax <= node.right.max:
                childMax = node.right.max

            if parent.left and parent.left.max != oldMax:
                siblingMax = parent.left.max
            if parent.right and siblingMax <= parent.right.max:
                siblingMax = parent.right.max

            if siblingMax <= childMax:
                biggestRelativeMax = childMax
            else:
                biggestRelativeMax = siblingMax

            if childMax < oldMax and siblingMax < oldMax:
                while parent != None and parent.max <= oldMax:
                    grandParent = parent.parent
                    parent.max = biggestRelativeMax
                    if parent.max <= parent.left.max:
                        parent.max = parent.left.max
                    if parent.max <= parent.right.max:
                        parent.max = parent.right.max
                    parent = grandParent


    def delete(self, interval):
        self._delete(interval, self.root)

    # This is the old binary tree delete. It does not work properly.
    # It has been replaced by the splay delete function
    def _delete(self, interval, nodeToDelete):
        node = self.search(interval, nodeToDelete)

        if node != None:
            children = self.count_children(node)
            if children == 0:
                if node.parent.left == node:
                    node.parent.left = None
                else:
                    node.parent.right = None

            elif children == 1:
                if node.parent.left == node:
                    if node.left != None:
                        node.parent.left = node.left
                    elif node.right != None:
                        node.parent.left = node.right
                elif node.parent.right == node:
                    if node.left != None:
                        node.parent.right = node.left
                    elif node.right != None:
                        node.parent.right = node.right

            elif children == 2:

                # We find the in-order predecessor of the node being
                # deleted and replace the node being deleted with it
                successor_parent = node
                successor = node.right
                while successor.left != None:
                    successor_parent = successor
                    successor = successor.left

                node.interval = successor.interval

                if successor_parent.left == successor:
                    successor_parent.left = successor.right

                if successor_parent.right == successor:
                    successor_parent.right = successor.right
   

    def in_order_tree_walk(self, node):
    # Walks trhough the tree and returns all the intervals in accending order
        if(node.left != None):
            self.in_order_tree_walk(node.left)
        return node.interval
        if(node.right != None):
            self.in_order_tree_walk(node.right)


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

            self.setMaxValue(node.left)
            self.setMaxValue(node)

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

            self.setMaxValue(node.right)
            self.setMaxValue(node)

    def setMaxValue(self, node):
        leftMax = -1
        rightMax = -1
        childMax = -1
        selfMax = node.interval[1]
        if node.left:
            leftMax = node.left.max
        if node.right:
            rightMax = node.right.max
        
        if leftMax <= rightMax:
            childMax = rightMax
        else:
            childMax = leftMax
        if selfMax <= childMax:
            node.max = childMax
        else:
            node.max = selfMax


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
                    self.rotate_left(parent)
                    self.rotate_right(node)
                    self.splay(node)
            else:
                if node == parent.left:     # Zakk Zikk
                    self.rotate_right(parent)
                    self.rotate_left(node)
                    self.splay(node)
                else:                       # Zakk Zakk
                    self.rotate_left(parent)
                    self.rotate_left(node)
                    self.splay(node)
