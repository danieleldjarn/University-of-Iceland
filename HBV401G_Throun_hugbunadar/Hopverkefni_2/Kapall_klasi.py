#!/usr/bin/python
#coding=utf-8

################################################################################
class Spil_node(object):
    'Klasinn Spil_node býr til spil og heldur utan um gildi þess og sort'
    """
    Þar sem að Spil_node er hnútur í Tree tréinu að þá hefur það hægra og vinstra
    barn (left og right) og hægra og vinstra foreldri (left_p og right_p).
    """
    def __init__(self,sort,gildi,left=None,right=None,left_p=None,right_p=None):
        self.sort      = sort
        self.gildi     = gildi
        self.left      = left
        self.right     = right
        self.left_p    = left_p
        self.right_p   = right_p        

    def __repr__(self):
        'Strengjaframmsetning spils'
        #letters = {1:'Ás', 11:'Gosi', 12:'Drolla', 13:'Kóngur'}
        #letter = letters.get(self.gildi, str(self.gildi))
        #return "<%s %s>" % (self.sort, letter)
        return "<%s %s>" % (self.sort, self.gildi)
#-------------------------------------------------------------------------------

################################################################################
class Stokkur(object):
    'Klasinn Stokkur býr til stokk og heldur utan um spilin sem eru í honum'
    def __init__(self, make_card=Spil_node):
        self.stokkur = []
        self.spilafjoldi = 0
        self.make_card = make_card

    def nyr_random_stokkur(self):
        'Tæmir stokk og setur 52 ný spil í hann í random röð'
        sort = ["H","S","T","L"]
        gildi = [1,2,3,4,5,6,7,8,9,10,11,12,13]
        self.stokkur = []
        self.spilafjoldi = 0
        for i in range(len(sort)):
            for j in range(len(gildi)):
                self.add(self.make_card(sort=sort[i], gildi=gildi[j]))
        return self.stokka()

    def stokka(self):
        'Stokkar stokkinn'
        from random import shuffle
        return shuffle(self.stokkur)

    def add(self,*spilin):
        'Bætir ótakmörkuðum fjölda spila í stokk'
        for spil in spilin:
            self.stokkur += [spil]
            self.spilafjoldi += 1

    def get_next(self, pos=-1):
        'Sækir spil í staðsetningu pos í stokkinn, skilar því og eyðir því'
        if self.spilafjoldi == 0 or pos >= self.spilafjoldi:
            return None
    	else:
    		self.spilafjoldi -= 1
    		x = self.stokkur.pop(pos)
    		return x
    def remove_pos(self,pos=-1):
    	'Eyðir spili úr staðsetningu pos úr stokkinum'
    	self.stokkur.pop(pos)

    def has_next(self):
        'Skilar True þþaa stokkurinn sé ekki tómur'
        return (self.spilafjoldi > 0)

    def __repr__(self):
        'Strengjaframmsetning stokks'
        s = ""
        for i in range(len(self.stokkur)):
            s = s + " " + str(self.stokkur[i])+", "
        return s[0:-2]+"\n"
#-------------------------------------------------------------------------------

################################################################################
class Tree(object):
	'Klasinn Tree er klasi sem býr til tré sem heldur utan um spilin'
	"""
	Ath. að tréið hefur 3 rætur og hver hnútur (sem er spil) getur átt tvö foreldri
	Uppsetning trés:
                                                               Dýpt
           root_1            root_2            root_3           0
           /   \             /   \             /   \  
          x     x           x     x           x     x           1
        /   \ /   \       /   \ /   \       /   \ /   \ 
       x     x     x     x     x     x     x     x     x        2
     /   \ /   \ /   \ /   \ /   \ /   \ /   \ /   \ /   \ 
    x     x     x     x     x     x     x     x     x     x     3 

	"""
	def __init__(T, make_node=Spil_node):
		T.nil       = make_node(sort=None,gildi=None)
		T.root_1    = T.nil
		T.root_2    = T.nil
		T.root_3    = T.nil
		T.stokkur   = Stokkur()

	def make_tree(T,stokkur=Stokkur()):
		'make_tree athugar kallar fall sem býr til tréið þþaa stokkurinn sé löglegur'
		if stokkur.spilafjoldi <= 28:
			print 'Stokkur of lítill'
			return
		T.add_to_tree(stokkur)

	def add_to_tree(T, stokkur):
		'add_to_tree fallið býr til tréið sem heldur utan um spilin'
		'''
		Þar sem að tréið er ekki hefðbundið tré er hver einasti hnútur settur manually
		inn í tréið.
		'''
		if T.root_1 == T.nil:
			T.root_1 = stokkur.get_next()
			T.root_1.left_p  = T.nil
			T.root_1.right_p = T.nil

			T.root_2 = stokkur.get_next()
			T.root_2.left_p  = T.nil
			T.root_2.right_p = T.nil

			T.root_3 = stokkur.get_next()
			T.root_3.left_p  = T.nil
			T.root_3.right_p = T.nil

		for i in range(0,3):
			#Búum til hluttréið sem hefur root_1 sem rót
			if i == 0:
				root = T.root_1
				root.left,  root.left.right_p  = stokkur.get_next(), root
				root.right, root.right.left_p  = stokkur.get_next(), root
				root.left.left_p   = T.nil
				root.right.right_p = T.nil

				root.left.right , root.left.right.left_p  = stokkur.get_next(), root.left
				root.right.left , root.right.left.right_p = root.left.right   , root.right
				root.left.left  , root.left.left.right_p  = stokkur.get_next(), root.left
				root.right.right, root.right.right.left_p = stokkur.get_next(), root.right
				root.left.left.left_p    = T.nil
				root.right.right.right_p = T.nil

				root.left.left.right , root.left.left.right.left_p   = stokkur.get_next()   , root.left.left
				root.left.right.left , root.left.right.left.right_p  = root.left.left.right , root.left.right
				root.left.right.right, root.left.right.right.left_p  = stokkur.get_next()   , root.left.right
				root.right.right.left, root.right.right.left.right_p = root.left.right.right, root.right.right

				root.right.right.right, root.right.right.right.left_p  = stokkur.get_next(), root.right.right
				root.left.left.left   , root.left.left.left.right_p    = stokkur.get_next(), root.left.left
				root.left.left.left.left_p = T.nil

				T.stokkur.add(root.left)
				T.stokkur.add(root.right)
				T.stokkur.add(root.left.right)
				T.stokkur.add(root.left.left)
				T.stokkur.add(root.right.right)
				T.stokkur.add(root.left.left.right)
				T.stokkur.add(root.left.right.right)
				T.stokkur.add(root.right.right.right)
				T.stokkur.add(root.left.left.left)
				T.root_1 = root
			
			#Búum til hluttréið sem hefur root_2 sem rót
			elif i == 1:
				root = T.root_2
				root.left,  root.left.right_p  = stokkur.get_next(), root
				root.right, root.right.left_p  = stokkur.get_next(), root
				root.left.left_p   = T.nil
				root.right.right_p = T.nil

				root.left.right , root.left.right.left_p  = stokkur.get_next(), root.left
				root.right.left , root.right.left.right_p = root.left.right   , root.right
				root.left.left  , root.left.left.right_p  = stokkur.get_next(), root.left
				root.right.right, root.right.right.left_p = stokkur.get_next(), root.right
				root.left.left.left_p    = T.nil
				root.right.right.right_p = T.nil

				root.left.left.right , root.left.left.right.left_p   = stokkur.get_next()   , root.left.left
				root.left.right.left , root.left.right.left.right_p  = root.left.left.right , root.left.right
				root.left.right.right, root.left.right.right.left_p  = stokkur.get_next()   , root.left.right
				root.right.right.left, root.right.right.left.right_p = root.left.right.right, root.right.right

				root.right.right.right, root.right.right.right.left_p  = stokkur.get_next()        , root.right.right
				root.left.left.left   , root.left.left.left.right_p    = T.root_1.right.right.right, root.left.left

				T.stokkur.add(root.left)
				T.stokkur.add(root.right)
				T.stokkur.add(root.left.right)
				T.stokkur.add(root.left.left)
				T.stokkur.add(root.right.right)
				T.stokkur.add(root.left.left.right)
				T.stokkur.add(root.left.right.right)
				T.stokkur.add(root.right.right.right)
				T.root_2 = root

			#Búum til hluttréið sem hefur root_3 sem rót
			else:
				root = T.root_3
				root.left,  root.left.right_p  = stokkur.get_next(), root
				root.right, root.right.left_p  = stokkur.get_next(), root
				root.left.left_p   = T.nil
				root.right.right_p = T.nil

				root.left.right , root.left.right.left_p  = stokkur.get_next(), root.left
				root.right.left , root.right.left.right_p = root.left.right   , root.right
				root.left.left  , root.left.left.right_p  = stokkur.get_next(), root.left
				root.right.right, root.right.right.left_p = stokkur.get_next(), root.right
				root.left.left.left_p    = T.nil
				root.right.right.right_p = T.nil

				root.left.left.right , root.left.left.right.left_p   = stokkur.get_next()   , root.left.left
				root.left.right.left , root.left.right.left.right_p  = root.left.left.right , root.left.right
				root.left.right.right, root.left.right.right.left_p  = stokkur.get_next()   , root.left.right
				root.right.right.left, root.right.right.left.right_p = root.left.right.right, root.right.right

				root.right.right.right, root.right.right.right.left_p  = stokkur.get_next()        , root.right.right
				root.left.left.left   , root.left.left.left.right_p    = T.root_2.right.right.right, root.left.left
				root.right.right.right.right_p = T.nil

				T.stokkur.add(root.left)
				T.stokkur.add(root.right)
				T.stokkur.add(root.left.right)
				T.stokkur.add(root.left.left)
				T.stokkur.add(root.right.right)
				T.stokkur.add(root.left.left.right)
				T.stokkur.add(root.left.right.right)
				T.stokkur.add(root.right.right.right)
				T.root_3 = root
		
	def node_depth(T,node):
		'node_depth fallið skilar í hvaða hæð hnútur er'
		try:
			cnt = 0
			while node is not T.nil:
				if node.left_p != T.nil:
					node = node.left_p
				elif node.right_p != T.nil:
					node = node.right_p
				else:
					break
				cnt += 1
			return cnt
		except:
			print "Ekki löglegur hnútur"
			return -1

	def is_removeable(T,node):
		'Skila True eff hægt sé að fjarlægja hann úr tréi'
		try:
			return node.left is None and node.right is None
		except:
			print "Ekki löglegur hnútur"
			return False
#-------------------------------------------------------------------------------
