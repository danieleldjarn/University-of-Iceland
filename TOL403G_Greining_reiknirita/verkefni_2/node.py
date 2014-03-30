#!/usr/bin/env python
# -*- coding: utf-8 -*-

#Smiður fyrir nóður
# Notkun: Node(i, p)
# Fyrir: i er heiltölubil, p er foreldri nóðunnar
# Eftir: Búið er að búa til nýa nóðu með interval i og parent p
class Node:

    def __init__(self, interval = None, parent = None):
        self.interval = interval
        self.parent = parent
        self.left = None
        self.right = None
