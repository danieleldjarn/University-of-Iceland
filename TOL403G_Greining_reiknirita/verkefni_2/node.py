#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Node:



    def __init__(self, interval = None, parent = None):
        self.interval = interval
        self.parent = parent
        self.left = None
        self.right = None
