''' An implementation of splay tree in python '''

import sys
sys.setrecursionlimit(10000)

resultToPrint = []
class Node:



    def __init__(self, interval = None, parent = None):
        self.interval = interval
        self.parent = parent
        self.left = None
        self.right = None

    
    def insert(self, interval):
        
        # If the node has no interval we set it's interval to the new interval.
        if self.interval == None:
            self.interval = interval

        # To put the new interval in the correct position we start by
        # comparing the lower end of the interval and then the 
        # higher end of the interval.
        # If the exact same interval is in the tree nothing will happen.
        elif interval[0] < self.interval[0]:
            if self.left == None:
                self.left = Node(interval, self)
            else:
                self.left.insert(interval, self)
        elif interval[0] > self.interval[0]:
            if self.right == None:
                self.right = Node(interval, self)
            else:
                self.right.insert(interval)
        elif interval[0] == self.interval[0]:
            if interval[1] < self.interval[1]:
                if self.left == None:
                    self.left = Node(interval, self)
                else:
                    self.left.insert(interval)
            elif interval[1] > self.interval[1]:
                if self.right == None:
                    self.right = Node(interval, self)
                else:
                    self.right.insert(interval)

    def search(self, interval):
        if interval == self.interval:
            return self
        elif interval[0] != self.interval[0]:
            if interval[0] > self.interval[0]:
                if self.right == None:
                    return None
                else:
                    return self.right.search(interval)
            elif interval[0] < self.interval[0]:
                if self.left == None:
                    return None
                else:
                    return self.left.search(interval)
        else:
            if interval[1] > self.interval[1]:
                if self.right == None:
                    return None
                else:
                    return self.right.search(interval)
            elif interval[1] < self.interval[1]:
                if self.left == None:
                    return None
                else:
                    return self.left.search(interval)

    def searchInclusive(self, interval):
        if self.interval[0] <= interval[0] and interval[1] <= self.interval[1]:
            resultToPrint.append(self.interval)
        if self.left != None:
            self.left.searchInclusive(interval)
        if self.right != None:
            self.right.searchInclusive(interval)

    def searchSingle(self, value):
        if self.interval[0] <= value and value <= self.interval[1]:
            resultToPrint.append(self.interval)
        if self.left != None:
            self.left.searchSingle(value)
        if self.right != None:
            self.right.searchSingle(value)

    def searchIntersect(self, interval):
        if interval[0] <= self.interval[1] and self.interval[0] <= interval[1]:
            resultToPrint.append(self.interval)
        if self.left != None:
            self.left.searchIntersect(interval)
        if self.right != None:
            self.right.searchIntersect(interval)

    def printOutput(self):
        stringToPrint = ""
        if resultToPrint == []:
            return
        else:
            for interval in resultToPrint:
                stringToPrint += str(interval)

            print stringToPrint
            self.resetResultToPrint()

    def resetResultToPrint(self):
        global resultToPrint
        resultToPrint = []

    def count_children(self):
        children = 0
        if self.left != None:
            children += 1
        if self.right != None:
            children += 1
        return children

    def max(self):
        if self.interval == None:
            return None
        else:
            node = self
            while node.right != None:
                node = node.right
            return node


    # This version of delete is much simpler because it uses the Splay
    # command to bring the node to be deleted to the root. Therefore
    # There is only one case that needs to be considdered when deleting
    def delete(self, interval):
        node = self.search(interval)
        node.splay()

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
            node.splay(node.left.max())
            node.right = temp
            node.parent = None


    '''
    # This is the old binary tree delete. It does not work properly.
    # It has been replaced by the splay delete function
    def delete(self, interval):
        node = self.search(interval)

        if node != None:
            children = node.count_children()
            print children
            if children == 0:
                print node.interval
                print node.parent.interval
                print node.parent.left
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
    '''

    def in_order_tree_walk(self):
    # Walks trhough the tree and returns all the intervals in accending order
        if(self.left != None):
            self.left.in_order_tree_walk()
        return self.interval
        if(self.right != None):
            self.right.in_order_tree_walk()


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
    def rotate_left(self):
        parent = self.parent
        if parent != None:
            grand_parent = self.parent.parent
            if grand_parent != None:
                if parent == grand_parent.left:
                    grand_parent.left = self
                else:
                    grand_parent.right = self
                if self.left != None:
                    self.left.parent = parent
                parent.right = self.left
                parent.parent = self
                self.left = parent
                self.parent = grand_parent
            else:
                root_parent = parent.parent
                if self.left != None:
                    self.left.parent = parent
                parent.right = self.left
                parent.parent = self
                self.left = parent
                self.parent = root_parent

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
    def rotate_right(self):
        parent = self.parent
        if parent != None :
            grand_parent = self.parent.parent
            if grand_parent != None:
                if parent == grand_parent.left:
                    grand_parent.left = self
                else:
                    grand_parent.right = self
                if self.right != None:
                    self.right.parent = parent
                parent.left = self.right
                parent.parent = self
                self.right = parent
                self.parent = grand_parent
            else:
                root_parent = parent.parent
                if self.left != None:
                    self.left.parent = parent
                parent.left = self.right
                parent.parent = self
                self.right = parent
                self.parent = root_parent

    def splay(self):
        if self.parent == None:
            return
        elif self.parent.parent == None:
            parent = self.parent
            if self == parent.left:    # Zikk
                self.rotate_right()
                self.splay()
            else:                           # Zakk
                self.rotate_left()
                self.splay()
        else:
            parent = self.parent
            grand_parent = self.parent.parent

            if parent == grand_parent.left:
                if self == parent.left:     # Zikk Zikk
                    parent.rotate_right()
                    self.rotate_right()
                    self.splay()
                else:                       # Zikk Zakk
                    self.rotate_left()
                    self.rotate_right()
                    self.splay()
            else:
                if self == parent.left:     # Zakk Zikk
                    self.rotate_right()
                    self.rotate_left()
                    self.splay()
                else:                       # Zakk Zakk
                    parent.rotate_left()
                    self.rotate_left()
                    self.splay()