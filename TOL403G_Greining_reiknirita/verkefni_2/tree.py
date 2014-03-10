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
    # Fyrir:    t er hlutur af gerð tree og i er heiltölubil.
    # Eftir:    Búið er að bæta bilinu i inn í tréið t á réttan stað
    def insert(self, interval):
        self._insert(interval, self.root)

    # Notkun:   t._insert(i, n)
    # Fyrir: t er hlutur af gerð tree, i er heiltölubil og n er nóða í trénu t
    # Eftir: Búið er að bæta bilinu i inn í tréð á réttan stað
    def _insert(self, interval, node):
        leftInsert = False
        rightInsert = True
        if node.interval == None:
            node.interval = interval

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

    # Notkun:   t.placeNewNode(i, n, insertionType)
    # Fyrir:    t er tré, i er heiltölubil, n er foreldri nóðu sem á að bæta við í tréð
    #           insertionType er boolean breyta sem segir hvort nýja nóðan eigi
    #           að vera vinstra eða hægra barn n. 
    #           False = left child. True = right child
    # Eftir:    Búið er að búa til nýja nóðu á réttum stað í trénu.
    def placeNewNode(self, interval, node, rightInsert):
        if rightInsert:
            node.right = Node(interval, node)
            self.splay(node.right)
            self.setRoot()
        else:
            node.left = Node(interval, node)
            self.splay(node.left)
            self.setRoot()

    # Notkun:   t.setRoot()
    # Fyrir:    t er tré sem ný búið er að framkvæma splay aðgerð á. 
    #           t.root er barn eða barnabarn rótar.
    # Eftir:    t.root er orðin rót trésins
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

    # Notkun:    n = t.search(i)
    # Fyrir:   t er tré og i er heiltölubil
    # Eftir:    Ef i var í trénu þá er n nóðan sem inniheldur i.
    #           Annars er n None
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

    # Notkun: t.searchInclusive(i)
    # Fyrir: t er tré. i er heiltölubil
    # Eftir: Búið er að finna allar nóður í t sem innihalda bilið i.
    def searchInclusive(self, interval):
        self._searchInclusive(interval, self.root)

    # Notkun: t._searchInclusive(i, n)
    # Fyrir: t er tré. i er heiltölubil, n er nóða í t.
    # Eftir: Búið er að finna allar nóður í t sem innihalda bilið i
    def _searchInclusive(self, interval, node):
        if node.interval[0] <= interval[0] and interval[1] <= node.interval[1]:
            self.resultToPrint.append(node.interval)
        if node.left != None:
            self._searchInclusive(interval, node.left)
        if node.right != None:
            self._searchInclusive(interval, node.right)

    # Notkun: t.searchSingle(p)
    # Fyrir: t er tré, p er heiltala
    # Eftir: Búið er að finna allar nóður í t sem innihalda gildið p
    def searchSingle(self, value):
        self._searchSingle(value, self.root)

    # Notkun: t._searchSingle(p, n)
    # Fyrir: t er tré, p er heiltala, n er nóða í t
    # Eftir: Búið er að finna allar nóður í t sem innihalda gildið p.
    def _searchSingle(self, value, node):
        if node.interval[0] <= value and value <= node.interval[1]:
            self.resultToPrint.append(node.interval)
        if node.left != None:
            self._searchSingle(value, node.left)
        if node.right != None:
            self._searchSingle(value, node.right)

    # Notkun: t.searchIntersect(i)
    # Fyrir: t er tré. i er heiltölubil
    # Eftir: Búið er að finna allar nóður í t sem skerast á við bilið i
    def searchIntersect(self, interval):
        self._searchIntersect(interval, self.root)

    # Notkun: t._searchIntersect(i, n)
    # Fyrir: t er tré. i er heiltölubil, n er nóða í t
    # Eftir: Búið er að finna allar nóður í t sem skerast á við bilið i
    def _searchIntersect(self, interval, node):
        if interval[0] <= node.interval[1] and node.interval[0] <= interval[1]:
            self.resultToPrint.append(node.interval)
        if node.left != None:
            self._searchIntersect(interval, node.left)
        if node.right != None:
            self._searchIntersect(interval, node.right)

    # Notkun: t.printOutput()
    # Fyrir: t er tré
    # Eftir: Innihald t.resultToPrint hafa verið prentuð út á staðalúttak.
    #        Innihaldi t.resultToPrint hefur verið eytt.
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

    # Notkun: t.countChildren(n)
    # Fyrir: t er tré. n er nóða í t
    # Eftir: Búið er að finna fjölda barna n.
    def countChildren(self, node):
        children = 0
        if node.left != None:
            children += 1
        if node.right != None:
            children += 1
        return children

    # Notkun: t.delete(i)
    # Fyrir: t er tré. i er heiltölubil
    # Eftir: Ef i var í t þá er búið að eyða nóðunni sem innihélt i.
    def delete(self, interval):
        self._delete(interval, self.root)

    # Notkun: t._delete(i, r)
    # Fyrir: t er tré. i er heiltölubil. r er rót t
    # Eftir: Ef i var í t þá er búið að eyða nóðunni sem innihélt i.
    def _delete(self, interval, root):
        if root == None:
            return False
        else:
            node = self.search(interval, root)
            if node != None and node.interval == interval:
                children = self.countChildren(node)
                if children == 0:
                    self.zeroLeafs(node)
                elif children == 1:
                    self.oneLeaf(node)
                elif children == 2:
                    self.twoLeafs(node)

    # Notkun: t.zeroLeafs(n)
    # Fyrir: t er tré. n er nóða í t sem á engin börn
    # Eftir: Búið er að eyða n úr trénu.
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

    # Notkun: t.oneLeaf(n)
    # Fyrir: t er tré. n er nóða í t sem á eitt barn
    # Eftir: Búið er að eyða n úr trénu.
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

    # Notkun: t.twoLeafs(n)
    # Fyrir: t er tré. n er nóða í t sem á eitt barn
    # Eftir: búið er að eyða n úr trénu
    def twoLeafs(self, node):
        successor = self.treeMin(node.right)
        node.interval = successor.interval

        if successor.right != None:
            self.oneLeaf(successor)
        else:
            self.zeroLeafs(successor)

    # Notkun: t.treeMin(n)
    # Fyrir: t er tré. n er nóða í t.
    # Eftir: Búið er að finna minnsta gildið í undirtré þar sem n er rót undirtrés.
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

    # Notkun: t.splay(n)
    # Fyrir: t er tré. n er nóða í t
    # Eftir: n er orðin rót t. (ath. að það þýðir ekki að n sé orðið t.root)
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
