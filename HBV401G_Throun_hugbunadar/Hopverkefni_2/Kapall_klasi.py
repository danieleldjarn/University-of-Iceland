#!/usr/bin/python
#coding=utf-8

################################################################################
class Spil_node(object):
    'Klasinn Spil_node býr til spil og heldur utan um gildi þess og sort'
    """
    Þar sem að Spil_node er hnútur í Tree tréinu að þá hefur það hægra og vinstra
    barn (left og right).
    """
    def __init__(self,sort,gildi,left=None,right=None):
        self.sort      = sort
        self.gildi     = gildi
        self.left      = left
        self.right     = right      

    def __eq__(self,other):
    	'Samanburðaraðgerð fyrir spil, skila True þþaa self og other séu sama spilið'
    	return self.gildi == other.gildi and self.sort == other.sort
    def __repr__(self):
        'Strengjaframmsetning spils'
        return "%s%s" % (self.sort, self.gildi)
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
    	self.spilafjoldi -= 1

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

           root_1            root_2            root_3           
           /   \             /   \             /   \  
          x     x           x     x           x     x           
        /   \ /   \       /   \ /   \       /   \ /   \ 
       x     x     x     x     x     x     x     x     x        
     /   \ /   \ /   \ /   \ /   \ /   \ /   \ /   \ /   \ 
    x     x     x     x     x     x     x     x     x     x      

	"""
	def __init__(T, make_node=Spil_node):
		T.nil       = make_node(sort=None,gildi=None)
		T.root_1    = T.nil
		T.root_2    = T.nil
		T.root_3    = T.nil
		T.stokkur   = Stokkur()

	def make_tree(T,stokkur=Stokkur()):
		'make_tree kallar á fall sem býr til tréið þþaa stokkurinn sé löglegur'
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

			T.root_2 = stokkur.get_next()

			T.root_3 = stokkur.get_next()

		for i in range(0,3):
			if i == 0:
				root = T.root_1
			elif i == 1:
				root = T.root_2
			else:
				root = T.root_3

			root.left, root.right = stokkur.get_next(), stokkur.get_next()
			root.left.left, root.right.right = stokkur.get_next(), stokkur.get_next()
			root.left.right = root.right.left = stokkur.get_next()
			root.right.right.right = stokkur.get_next()

			root.right.right.left = root.right.left.right = root.left.right.right = stokkur.get_next()
			root.right.left.left  = root.left.right.left  = root.left.left.right  = stokkur.get_next()

			if i == 0:
				root.left.left.left = stokkur.get_next()
			
			elif i == 1:
				root.left.left.left = T.root_1.right.right.right 

			else:
				root.left.left.left = T.root_2.right.right.right

			T.stokkur.add(root)
			T.stokkur.add(root.left)
			T.stokkur.add(root.right)
			T.stokkur.add(root.left.left)
			T.stokkur.add(root.right.right)
			T.stokkur.add(root.right.left)
			T.stokkur.add(root.left.left.right)
			T.stokkur.add(root.right.right.left)
			T.stokkur.add(root.left.left.left)

			if i == 0:
				T.root_1 = root
			elif i == 1:
				T.root_2 = root
			else:
				T.stokkur.add(root.right.right.right)
				T.root_3 = root

	def update_tree(T, spil):
		'update_tree fallið leitar að tilteknu spili í heildartréi og eyðir því ef það er hægt'
		if spil is not T.nil:
			for i in range(0,3):
				if i == 0:
					if T.search_and_remove(T.root_1, spil):
						T.stokkur.remove_pos(T.stokkur.stokkur.index(spil))
						return True
				elif i == 1:
					if T.search_and_remove(T.root_2, spil):
						T.stokkur.remove_pos(T.stokkur.stokkur.index(spil))
						return True
				else:
					if T.search_and_remove(T.root_3, spil):
						T.stokkur.remove_pos(T.stokkur.stokkur.index(spil))
						return True
			return False
		else:
			return False

	def search_and_remove(T, node, spil):
		'leitar í hluttrjám að spili og eyðir því og skilar True eff það er fjarlægjanlegt'

		if node == spil:
			if T.is_removeable(node):
				if node is T.root_1:
					node = T.root_1 = T.nil
				elif node is T.root_2:
					node = T.root_2 = T.nil
				elif node is T.root_3:
					node = T.root_3 = node = T.nil
				return True

		if node is not T.nil:
			if node.left == spil:
				if T.is_removeable(node.left):
					node.left = T.nil
					return True

			elif node.right == spil:
				if T.is_removeable(node.right):
					node.right = T.nil
					return True

			if node.left is not T.nil:
				if node.left.left == spil:
					if T.is_removeable(node.left.left):
						node.left.left = T.nil
						return True
				elif node.left.right == spil:
					if T.is_removeable(node.left.right):
						node.left.right = T.nil
						if node.right is not T.nil:
							node.right.left = T.nil
						return True

			if node.right is not T.nil:
				if node.right.right == spil: 
					if T.is_removeable(node.right.right):
						node.right.right = T.nil
						return True	
				elif node.right.left == spil:
					if T.is_removeable(node.right.left):
						node.right.left = T.nil
						if node.left is not T.nil:
							node.left.right = T.nil
						return True			

			if node.left is not T.nil and node.left.left is not T.nil:
				if node is T.root_1:
					if node.left.left.left == spil:
						node.left.left.left = T.nil
						return True
				if node.left.left.right == spil:
					node.left.left.right = T.nil
					if node.left.right is not T.nil:
						node.left.right.left = T.nil
					if node.right.left is not T.nil:
						node.right.left.left = T.nil
					return True

			if node.right is not T.nil and node.right.right is not T.nil:
				if node.right.right.left == spil:
					node.right.right.left = T.nil
					if node.right.left is not T.nil:
						node.right.left.right = T.nil
					if node.left.right is not T.nil:
						node.left.right.right = T.nil
					return True

				elif node.right.right.right == spil:
					node.right.right.right = T.nil
					if node is T.root_1 and T.root_2.left.left is not T.nil:
						T.root_2.left.left.left = T.nil
					elif node is T.root_2 and T.root_3.left.left is not T.nil:
						T.root_3.left.left.left = T.nil
					return True

		else:
			return False

	def get_removeables(T):
		'Skilar öllum spilunum sem eru fjarlægjanleg í heildartréi sem stokki'
		xss = []
		for i in range(0,3):
			if i == 0:
				xss += T.get_removeables_sub(T.root_1)
			elif i == 1:
				xss += T.get_removeables_sub(T.root_2)
			elif i == 2:
				xss += T.get_removeables_sub(T.root_3)
		skilastokkur = Stokkur()
		skilastokkur.stokkur = xss
		skilastokkur.spilafjoldi += len(xss)
		return skilastokkur

	def get_removeables_sub(T, root):
		'Skilar öllum þeim spilum sem lista sem eru fjarlægjanleg úr hluttréi sem hefur root sem rót'
		xss = []

		if root is not T.nil:
			if T.is_removeable(root):
				xss += [root]

			if T.is_removeable(root.left):
				xss += [root.left]
			if T.is_removeable(root.right):
				xss += [root.right]

			if root.right is not T.nil:
				if T.is_removeable(root.right.right):
					xss += [root.right.right]
				if T.is_removeable(root.right.left):
					xss += [root.right.left]

			if root.left is not T.nil:
				if T.is_removeable(root.left.left):
					xss += [root.left.left]
				if root.right is not T.nil:
					if T.is_removeable(root.left.right) and root.left.right is not root.right.left:
						xss += [root.left.right]

			if root.right is not T.nil and root.right.right is not T.nil:
				if root.right.right.right is not T.nil:
					xss += [root.right.right.right]
				if root.right.right.left is not T.nil:
					xss += [root.right.right.left]

			if root.left is not T.nil and root.right is not T.nil and root.left.right is not T.nil:
				if root.right.right is not T.nil:
					if root.left.right.right is not T.nil and root.left.right.right is not root.right.right.left:
						xss += [root.left.right.right]
			if root.right is not T.nil and root.left is not T.nil and root.right.left is not T.nil:
				if root.left.right is not T.nil and root.right.right is not T.nil:
					if root.right.left.right is not T.nil and root.right.left.right is not root.left.right.right and root.right.left.right is not root.right.right.left:
						xss += [root.right.left.right]

			if root.left is not T.nil and root.left.left is not T.nil:
				if root.left.left.right is not T.nil:
					xss += [root.left.left.right]
			if root.left is not T.nil and root.left.right is not T.nil:
				if root.left.left is not T.nil:
					if root.left.right.left is not T.nil and root.left.right.left is not root.left.left.right:
						xss += [root.left.right.left]
			if root.right is not T.nil and root.left is not T.nil and root.right.left is not T.nil:
				if root.left.left is not T.nil and root.left.right is not T.nil:
					if root.right.left.left is not T.nil and root.right.left.left is not root.left.right.left and root.right.left.left is not root.left.left.right:
						xss += [root.right.left.left]

			if root is T.root_1 and root.left is not T.nil and root.left.left is not T.nil:
				if root.left.left.left is not T.nil:
					xss += [root.left.left.left]

		return xss

	def is_removeable(T,node):
		'Skila True eff hægt sé að fjarlægja spil úr tréi'
		if type(node) is type(T.nil):
			return node.left is T.nil and node.right is T.nil and node is not T.nil
		return False
		
		def card_pos(T, card):
		'Sækir staðsetningu spils í tréi'
		"""
                   10                20                30          
           	  /   \             /  \              /  \   
           	 11    12          21   22          31    32           
           	/   \ /   \       /   \ /  \        /  \  /  \ 
       	       13    14    15    23   24   25     33    34   35        
    	      /   \ /  \ /  \   /  \ /  \ /  \   /  \  /  \  /  \ 
    	     16    17   18    26    27   28    36    37    38    39 
		"""
		if type(card) is not type(T.nil) or card is T.nil:
			print card," ekki löglegt spil"
			return None
		for i in range(3):
			if i == 0:
				if T.subtree_card_pos(T.root_1, card):
					return str(1)+T.subtree_card_pos(T.root_1, card)
			elif i == 1:
				if T.subtree_card_pos(T.root_2, card):
					return str(2)+T.subtree_card_pos(T.root_2, card)
			else:
				if T.subtree_card_pos(T.root_3, card):
					return str(3)+T.subtree_card_pos(T.root_3, card)

	def subtree_card_pos(T, root, card):
		'Sækir staðsetningu spils í undirtréi ef hún er til'
		if root is not T.nil:
			if card is root: return "0"
			if root.left is not T.nil:
				if card is root.left: return "1"
				if root.left.right is not T.nil:
					if card is root.left.right:	return "4"
					if card is root.left.right.right: return "8"
					if card is root.left.right.left: return "7"
				if root.left.left is not T.nil:
					if card is root.left.left: return "3"
					if card is root.left.left.left:	return "6"
					if card is root.left.left.right: return "7"

			if root.right is not T.nil:
				if card is root.right: return "2"
				if root.right.left is not T.nil:
					if card is root.right.left: return "4"
					if card is root.right.left.left: return "7"
					if card is root.right.left.right: return "8"
				if root.right.right is not T.nil:
					if card is root.right.right: return "5"
					if card is root.right.right.left: return "8"
					if card is root.right.right.right and root is T.root_3: return "9"
		return ""
#-------------------------------------------------------------------------------
