from node import Node

root = Node([2, 5])
root.insert([2, 6])
root.insert([3, 4])
root.insert([2, 7])
root.insert([6, 7])
root.insert([4, 8])
root.insert([1, 10])

root.in_order_tree_walk()


'''
print root.search([2, 5])
print root.search([2, 6])
print root.search([3, 4])
print root.search([4, 8])
print root.search([1, 10])
print root.search([5, 8])
print root.search([2, 7])
print root.search([6, 7])
'''