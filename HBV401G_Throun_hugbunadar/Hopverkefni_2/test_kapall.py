from Kapall_klasi import Stokkur
from Kapall_klasi import Tree
import unittest

class testDeck(unittest.TestCase): 


    deckCount = 52
    knownCards = ["<H 1>", "<S 5>", "<T 13>", "<L 4>", "<H 10>"]
    bogusCards = ["<B 1>", "<S 14>", "<H K>", "<L 0>"]

    def testCardCount(self):
        deck = Stokkur()
        deck.nyr_random_stokkur()
        tmp = []
        while deck.has_next():
            tmp.append(deck.get_next())
        self.assertEqual(self.deckCount, len(tmp))

    def testKnownCards(self):
        deck = Stokkur()
        deck.nyr_random_stokkur()
        tmp = []
        while deck.has_next():
            tmp.append(str(deck.get_next()))
        check = all(x in tmp for x in self.knownCards)
        self.failUnless(check)

    def testBogusCards(self):
        deck = Stokkur()
        deck.nyr_random_stokkur()
        tmp = []
        while deck.has_next():
            tmp.append(str(deck.get_next()))
        check = all(x not in tmp for x in self.bogusCards)
        self.failUnless(check)


class testTree(unittest.TestCase):


    def testTreeWithFullDeck(self):
        deck = Stokkur()
        deck.nyr_random_stokkur()
        tree = Tree()
        tree.make_tree(deck)
        self.assertNotEqual(tree.root_1, tree.nil)
        self.assertNotEqual(tree.root_2, tree.nil)
        self.assertNotEqual(tree.root_3, tree.nil)
        self.assertNotEqual(tree.root_2.right.right.left, tree.nil)
        self.assertNotEqual(tree.root_2.left.left.right, tree.nil)
        self.assertNotEqual(tree.root_3.right.right.right, tree.nil)

    def testTreeWithTooFewCards(self):
        deck = Stokkur()
        deck.nyr_random_stokkur()
        for i in xrange(30):
            tmp = deck.get_next()
        tree = Tree()
        tree.make_tree(deck)
        self.assertEqual(tree.root_1, tree.nil)
        self.assertEqual(tree.root_2, tree.nil)
        self.assertEqual(tree.root_3, tree.nil)

    def testNodeDepth(self):
        deck = Stokkur()
        deck.nyr_random_stokkur()
        tree = Tree()
        tree.make_tree(deck)
        self.assertEqual(tree.node_depth(tree.root_1), 0)
        self.assertNotEqual(tree.node_depth(tree.root_3),1)
        self.assertEqual(tree.node_depth(tree.root_2.left), 1)
        self.assertEqual(tree.node_depth(tree.root_3.left.right), 2)
        self.assertEqual(tree.node_depth(tree.root_3.left.right.left), 3)
        self.assertNotEqual(tree.node_depth(tree.root_3.right.left.right), 4)


if __name__ == '__main__':
    unittest.main()
