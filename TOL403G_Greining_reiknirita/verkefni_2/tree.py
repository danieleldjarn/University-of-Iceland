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
        #print "NODE"
        #print node
        #print node.interval
        leftInsert = False
        rightInsert = True
        '''print type(self.root.interval)
        print type(self.root)
        print type(node)
        print type(node.interval)
        print type(None)
        print self.root.interval'''
        #print "derpaherp"
        #print self.root
        #print self.root.interval
        # If the node has no interval we set it's interval to the new interval.
        if node.interval == None:
            #print "herpaderp"
            #print self.root.interval
            node.interval = interval
            node.max = interval[1]
            self.setMaxInsert(node)


        # To put the new interval in the correct position we start by
        # comparing the lower end of the interval and then the 
        # higher end of the interval.
        # If the exact same interval is in the tree nothing will happen.

        # 0 er minna en 2
        elif interval[0] < node.interval[0]:
            #print "I should be here"
            # node.left er ekki tómt
            if node.left == None:
                #print "I should NOT be here"
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
        #print "then I went here"
        if rightInsert:
            #print "node right 1"
            #print node.right
            node.right = Node(interval, node)
            #print "node right 2"
            #print node.right
            node.right.max = interval[1]
            #print "node right 3"
            #print node.right
            self.setMaxInsert(node.right)
            #print "node right 4"
            #print node.right
            #print "node right value 1"
            #print node.right.interval
            #print "node value 1"
            #print node.interval
            #print "inorderbeforesplay"
            #self.in_order_tree_walk(self.root)
            self.splay(node.right)
            #print self.root.parent.interval
            #print "inorderaftersplay"
            #self.in_order_tree_walk(self.root)
            #print "node right 5"
            #print node.right
            #print "self root 1"
            #print self.root
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
                    #print "leftchild"
                    #print rootParent.left
                    #print self.root
                    #print rootParent
                    self.root = rootParent
                    self.root.left = oldRoot
                    oldRoot.parent = self.root
                elif self.root == rootParent.right:
                    #print "rightchild"
                    #print rootParent.right
                    #print self.root
                    self.root = rootParent
                    self.root.right = oldRoot
                    oldRoot.parent = self.root
            #print "self root 2"
            #print self.root
        else:
            #print "node.left 1"
            #print node.left
            node.left = Node(interval, node)
            #print "node.left 2"
            #print node.left
            node.left.max = interval[1]
            #print "node.left 3"
            #print node.left
            self.setMaxInsert(node.left)
            #print "node.left 4"
            #print node.left
            self.splay(node.left)
            #print "node.left 5"
            #print node.left
            #print self.root.interval
            #print self.root
            #print self.root.parent
            #print self.root.parent.interval
            #print self.root.parent.parent.interval

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
                    ##print "leftchild"
                    #print rootParent.left
                    #print self.root
                    #print rootParent
                    self.root = rootParent
                    self.root.left = oldRoot
                    oldRoot.parent = self.root
                elif self.root == rootParent.right:
                    #print "rightchild"
                    #print rootParent.right
                    #print self.root
                    self.root = rootParent
                    self.root.right = oldRoot
                    oldRoot.parent = self.root

            #print self.root
            #print self.root


    # Usage:    t.setMaxInsert(n)
    # Before:   t is an object of type tree and n is an object of type node.
    # After:    The maximum value in the branch in t which n was inserted into has been updated.
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
        if node.left != None and interval[1] <= node.left.max:
            self._searchInclusive(interval, node.left)
        if node.right != None and interval[1] <= node.right.max:
            self._searchInclusive(interval, node.right)

    # Usage:    t.searchSingle(p)
    # Before:   t is an object of type tree, p is an integer (point)
    # After:    All intervals in t that include p have been added to resultToPrint
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

    # Usage:    t.searchIntersect(i)
    # Before:   t is an object of type tree, i is an interval
    # After:    All intervals in t that intersect i have been added to resultToPrint
    def _searchIntersect(self, interval, node):
        if interval[0] <= node.interval[1] and node.interval[0] <= interval[1]:
            self.resultToPrint.append(node.interval)
        if node.left != None and interval[1] <= node.left.max:
            self._searchIntersect(interval, node.left)
        if node.right != None and interval[1] <= node.right.max:
            self._searchIntersect(interval, node.right)

    # Usage:    t.printOutput()
    # Before:   t is an object of type tree
    # After:    The contents of the global variable resultToPrint have been printed
    #           onto standar output
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
        print node.interval
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
        #print "rotate left"
        #print node
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
        #print "rotate right"
        #print node
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
        #print "splay node"
        #print node
        if node.parent == None:
           # print "no parent"
            #print node
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
