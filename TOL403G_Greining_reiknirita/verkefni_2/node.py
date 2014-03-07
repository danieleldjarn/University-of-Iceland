''' An implementation of splay tree in python '''

resultToPrint = []
class Node:



    def __init__(self, interval = None):
        self.interval = interval
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
                self.left = Node(interval)
            else:
                self.left.insert(interval)
        elif interval[0] > self.interval[0]:
            if self.right == None:
                self.right = Node(interval)
            else:
                self.right.insert(interval)
        elif interval[0] == self.interval[0]:
            if interval[1] < self.interval[1]:
                if self.left == None:
                    self.left = Node(interval)
                else:
                    self.left.insert(interval)
            elif interval[1] > self.interval[1]:
                if self.right == None:
                    self.right = Node(interval)
                else:
                    self.right.insert(interval)

    def search(self, interval, parent = None):
        if interval == self.interval:
            return self, parent
        elif interval[0] != self.interval[0]:
            if interval[0] > self.interval[0]:
                if self.right == None:
                    return None, None
                else:
                    return self.right.search(interval, self)
            elif interval[0] < self.interval[0]:
                if self.left == None:
                    return None, None
                else:
                    return self.left.search(interval, self)
        else:
            if interval[1] > self.interval[1]:
                if self.right == None:
                    return None, None
                else:
                    return self.right.search(interval, self)
            elif interval[1] < self.interval[1]:
                if self.left == None:
                    return None, None
                else:
                    return self.left.search(interval, self)

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
        if self.interval[0] <= interval[0] and interval[0] <= self.interval[1]:
            resultToPrint.append(self.interval)
        if self.interval[0] <= interval[1] and interval[1] <= self.interval[1] and self.interval not in resultToPrint:
            resultToPrint.append(node)
        if self.left != None:
            self.left.searchIntersect(interval)
        if self.right != None:
            self.right.searchIntersect(interval)

    def printOutput(self):
        stringToPrint = ""
        if resultToPrint == []:
            print '[]'
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

    def delete(self, interval):
        node, node_parent = self.search(interval)

        if node != None:
            children = node.count_children()

            if children == 0:
                if node_parent.left == node:
                    node_parent.left = None
                else:
                    node_parent.right = None

            elif children == 1:
                if node_parent.left == node:
                    if node.left != None:
                        node_parent.left = node.left
                    elif node.right != None:
                        node_arent.left = node.right
                elif node_parent.right == node:
                    if node.left != None:
                        node_parent.right = node.left
                    elif node.right != None:
                        node_parent.right = node.right

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
