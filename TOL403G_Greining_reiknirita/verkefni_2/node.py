''' An implementation of splay tree in python '''

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

def delete(self, interval):

    node, nodeParent = self.search(interval)
    if node != None:
        children = node.count_children()

        if children == 0:
            if parent.left == node:
                parent.left = None
            else:
                parent.right = None
