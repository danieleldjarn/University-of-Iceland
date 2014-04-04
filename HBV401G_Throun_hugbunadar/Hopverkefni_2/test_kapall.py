#!/usr/bin/python
#coding=utf-8

from Kapall_klasi import Stokkur
from Kapall_klasi import Tree
import unittest

class testDeck(unittest.TestCase): 

    deckCount = 52
    knownCards = ["<H 1>", "<S 5>", "<T 13>", "<L 4>", "<H 10>"]
    bogusCards = ["<B 1>", "<S 14>", "<H K>", "<L 0>"]

    def testCardCount(self):
        'Prófar að fjarlægja öll spil úr stokki'
        deck = Stokkur()
        deck.nyr_random_stokkur()
        tmp = []
        self.assertTrue(deck.has_next())
        while deck.has_next():
            tmp.append(deck.get_next())
        self.assertEqual(self.deckCount, len(tmp))
        self.assertFalse(deck.has_next())

    def testKnownCards(self):
        'Athugar hvort að löggild spil séu í fullum stokki'
        deck = Stokkur()
        deck.nyr_random_stokkur()
        tmp = []
        while deck.has_next():
            tmp.append(str(deck.get_next()))
        check = all(x in tmp for x in self.knownCards)
        self.failUnless(check)

    def testBogusCards(self):
        'Athugar hvort að ólögleg spil séu í fullum stokki'
        deck = Stokkur()
        deck.nyr_random_stokkur()
        tmp = []
        while deck.has_next():
            tmp.append(str(deck.get_next()))
        check = all(x not in tmp for x in self.bogusCards)
        self.failUnless(check)


class testTree(unittest.TestCase):

    def testTreeWithFullDeck(self):
        'Setur löggildan spilastokk í tré og athugar hvort ákveðnir hnútar séu ekki eins og þeir eiga að vera'
        deck = Stokkur()
        deck.nyr_random_stokkur()
        tree = Tree()
        tree.make_tree(deck)
        self.assertIsNot(tree.root_1, tree.nil)
        self.assertIsNot(tree.root_2, tree.nil)
        self.assertIsNot(tree.root_3, tree.nil)
        self.assertIsNot(tree.root_2.right.right.left, tree.nil)
        self.assertIsNot(tree.root_2.left.left.right, tree.nil)
        self.assertIsNot(tree.root_3.right.right.right, tree.nil)
        self.assertIs(tree.root_1.right.right.right, tree.root_2.left.left.left)
        self.assertIs(tree.root_2.right.right.right, tree.root_3.left.left.left)
        for i in range(3):
            if i == 0:
                root = tree.root_1
            elif i == 1:
                root = tree.root_2
            else:
                root = tree.root_3
            self.assertIs(root.left.right, root.right.left)
            self.assertIs(root.left.left.right, root.right.left.left)
            self.assertIs(root.left.left.right, root.left.right.left)
            self.assertIs(root.left.right.right, root.right.right.left)
            self.assertIs(root.left.right.right, root.right.left.right)
        self.assertEqual(len(tree.stokkur.stokkur), 28)

    def testTreeWithTooFewCards(self):
        'Athugar hvort það sé hægt að búa til tré með of fáum spilum'
        deck = Stokkur()
        deck.nyr_random_stokkur()
        for i in range(30):
            tmp = deck.get_next()
        tree = Tree()
        tree.make_tree(deck)
        self.assertIs(tree.root_1, tree.nil)
        self.assertIs(tree.root_2, tree.nil)
        self.assertIs(tree.root_3, tree.nil)
        self.assertEqual(len(tree.stokkur.stokkur), 0)

    def testTreeUpdate(self):
        'Býr til löggild tré og fjarlægir öll spil úr því og athugar hvort það sé svo örugglega tómt að lokum'
        deck = Stokkur()
        deck.nyr_random_stokkur()
        tree = Tree()
        tree.make_tree(deck)
        self.assertIsNot(tree.root_1, tree.nil)
        self.assertIsNot(tree.root_2, tree.nil)
        self.assertIsNot(tree.root_3, tree.nil)
        while tree.stokkur.spilafjoldi > 0:
            tmp = tree.get_removeables()
            for spil in tmp.stokkur:
                tree.update_tree(spil) 
        self.assertIs(tree.root_1, tree.nil)
        self.assertIs(tree.root_2, tree.nil)
        self.assertIs(tree.root_3, tree.nil)

    def testPositions(self):
        'Athugar hvort spil séu ekki með sömu staðsetningu'
        deck = Stokkur()
        deck.nyr_random_stokkur()
        tree = Tree()
        tree.make_tree(deck)
        self.assertEqual(tree.card_pos(tree.root_1.right.right.right), tree.card_pos(tree.root_2.left.left.left))
        self.assertEqual(tree.card_pos(tree.root_2.right.right.right), tree.card_pos(tree.root_3.left.left.left))
        for i in range(3):
            if i == 0:
                root = tree.root_1
            elif i == 1:
                root = tree.root_2
            else:
                root = tree.root_3
            self.assertEqual(tree.card_pos(root.left.right), tree.card_pos(root.right.left))
            self.assertEqual(tree.card_pos(root.left.left.right), tree.card_pos(root.right.left.left))
            self.assertEqual(tree.card_pos(root.left.left.right), tree.card_pos(root.left.right.left))
            self.assertEqual(tree.card_pos(root.right.right.left), tree.card_pos(root.left.right.right))
            self.assertEqual(tree.card_pos(root.right.right.left), tree.card_pos(root.right.left.right))



if __name__ == '__main__':
    unittest.main()
