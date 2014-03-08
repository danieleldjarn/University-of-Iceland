public class SplayTree<Key extends Comparable<Key>> 
{
	/*
		FASTAYRÐING GAGNA:
		Node er hlekkur í Splay tré
		Node inniheldur heiltölu gildi
		Node inniheldur tilvísun í vinstra og hægra barn sitt (má vera null) og foreldri sitt(má vera null)
		Börn og foreldrar eru aðrir hlekkir (Nodes), ef þau eru til.
		Splay tré hlutur inniheldur hlekki af taginu Node. 
		Efsti hlekkurinn (root) á ekkert foreldri.
		Lauf eiga engin börn.
		root er hlekkur sem er rót Splay trés (má vera null).
		
		Að auki uppfyllir tréð tvíleitartrjáaskilyrði:
			Öll gildi í vinstra undirtré eru alltaf (fyrir öll undirtré)
			< rótargildi og öll gildi í hægra undirtré (fyrir öll undirtré)
			eru > rótargildi.
		Tvö (eða fleiri) eins gildi eru ekki leyfð.
		
	*/
        private class Node 
        {
                private Key key;
                private Node left, right, parent;

                /*
			Notkun: Node node = new Node(key);
			Eftir : node er nýr hlekkur í tré, sem inniheldur gildið key
                */
                public Node(Key key) 
                {
                        this.key = key;
                }
                
                /*
			Notkun: int i = node.leafCount();
			Fyrir : Node hlutur er til
			Eftir : i inniheldur fjölda laufa í node
                */
                public int leafCount()
                {
			int counter = 0;
			if(left != null)
				counter++;
			if(right != null)
				counter++;
			return counter;
                }
        }
        private Node root; 

        /*
		Notkun: st = new SplayTree<Integer>();
		Eftir: st er nýtt tómt Splay tré
        */
        public SplayTree()
        {
		root = null;
        }
        

	/*
		Notkun: st.printTree();
		Fyrir : st er Splay tré
		Eftir : Búið er að prenta út gildin í st
	*/
        public void printTree()
        {
		InOrderTreeWalk(root);
        }
        
        /*
		Notkun: InOrderTreeWalk(n);
		Fyrir: n er hlekkur af tagi Node í Splay tré
		Eftir: Búið er að ganga í gegnum Splay tré í in-order röð 
			og prenta út gildin í Splay trénu
        */
        private void InOrderTreeWalk(Node n)
        {
		if(n != null){
			InOrderTreeWalk(n.left);
			System.out.println(n.key);
			InOrderTreeWalk(n.right);
		}
        }
        
        /*
		Notkun: st.put(key);
		Fyrir : st er Splay tré (má vera tómt), key er heiltala
		Eftir : Búið er að bæta gildi key á réttan stað í Splay trénu
        */
        public void put(Key key) 
        {
		Node node = new Node(key);
		if(root == null)
			root = node;
                else{
			putRecursive(root,node);
		}
        }

        /*
		Notkun: putRecursive(oldNode,newNode);
		Fyrir : oldNode & newNode eru hlekkir af tagi Node.
			oldNode er hlekkur í Splay tré
		Eftir: Búið er að bæta newNode við Splay tréð á réttum stað 
			ef newNode er ekki til í Splay trénu, newNode er nýja rót Splay trésins. 
			Ef newNode var til í trénu þá er sá hlekkur sem var eins og newNode
			orðin að rót trésins.
        */
        private void putRecursive(Node oldNode, Node newNode)
        {
		
		switch(oldNode.key.compareTo(newNode.key))
		{
			case 1:
				if(oldNode.left == null){
					oldNode.left = newNode;
					newNode.parent = oldNode;
					Splay(newNode);
					root = newNode;
					return;
				}
				else {
					putRecursive(oldNode.left,newNode);
				}
			case 0: 
				get(newNode.key);
				return;
			case -1:
				if(oldNode.right == null){
					oldNode.right = newNode;
					newNode.parent = oldNode;
					Splay(newNode);
					root = newNode;
					return;
				}
				else {
					putRecursive(oldNode.right,newNode);
				}
		}
        }
        
        /*
		Notkun: s = st.get(key);
		Fyrir: st er Splay tré, key er heiltala
		Eftir: Búið er að sækja hlekkinn sem inniheldur gildið key.
			Ef sá hlekkur er til þá er hann orðinn rót Splay trésins 
			og strengnum T er skilað. Annars er strengnum F skilað.
        */
        public String get(Key key) 
        {
		if(root == null)
			return "F";
                else{
			Node nodeToGet = findNode(key,root);
			if(key.equals(nodeToGet.key)){
				Splay(nodeToGet);
				root = nodeToGet;
				return "T";
			}
			else
				Splay(nodeToGet);
				root = nodeToGet;
				return "F";
	        }
	              
        }

        /*
		Notkun: n = findNode(key,node);
		Fyrir: key er heiltala, node er hlekkur í Splay tré
		Eftir: n er hlekkur í Splay tré sem inniheldur gildið key, annars er
			n null ef engin hlekkur í Splay tré inniheldur gildið key.
		
        */
	private Node findNode(Key key, Node node)
	{
		if(node != null) {
			switch(node.key.compareTo(key)){
				case 1:
					if(node.left != null){
						return findNode(key, node.left);
					}
					else
						return node;
				case 0:
					return node;
				case -1:
					if(node.right != null){
						return findNode(key, node.right);
					}
					else
						return node;
				default:
					return null;
			}
		}
		else
			return null;
	}
	
	/*
		Notkun: b = st.delete(key);
		Fyrir: key er heiltala
		Eftir: b er bólkst gildi
			b er True ef tókst að eyða hlekknum sem inniheldur key 
			b er False ef hlekkur er ekki til
	*/
	public boolean delete(Key key) 
        {
		if(root == null)
			return false;
		
    else{
			Node nodeToDelete = findNode(key,root);
			if(nodeToDelete != null && key.equals(nodeToDelete.key)) {
				switch(nodeToDelete.leafCount()) {
					case 0:
						zeroLeafs(nodeToDelete);
						return true;
					case 1:
						oneLeafs(nodeToDelete);
						return true;
					case 2:
						twoLeafs(nodeToDelete);
						return true;
					default:
						return false;
				}
			}
			else 
				return false;
		}
        }
        
        /*
		Notkun: zeroLeafs(node);
		Fyrir: node er hlekkur sem á að eyða úr Splay trénu
			hlekkurinn node hefur engin lauf
		Eftir: Búið er að eyða hlekknum node úr Splay trénu 
        */
	private void zeroLeafs(Node nodeToDelete)
	{
		Node parentOfNodeToDelete = nodeToDelete.parent;

		if(nodeToDelete.parent != null) {
			
			if(nodeToDelete == parentOfNodeToDelete.left){
				parentOfNodeToDelete.left = null;
				//nodeToDelete = null;
			}
			else {
				parentOfNodeToDelete.right = null;
				//nodeToDelete = null;
			}
		}
		else{
			// eyða rótinni
			root = null;
			nodeToDelete = null;
		}
	}
	
	/*
		Notkun: oneLeafs(node);
		Fyrir: node er hlekkur sem á að eyða úr Splay trénu
			hlekkurinn node hefur nákvæmlega eitt lauf
		Eftir: Búið er að eyða hlekknum node úr Splay trénu 
        */
	private void oneLeafs(Node nodeToDelete)
	{
		if(nodeToDelete.parent != null){
			if(nodeToDelete.left != null){
				if(nodeToDelete == nodeToDelete.parent.left){
					nodeToDelete.left.parent = nodeToDelete.parent;
					nodeToDelete.parent.left = nodeToDelete.left;
				}
				else{
					nodeToDelete.left.parent = nodeToDelete.parent;
					nodeToDelete.parent.right = nodeToDelete.left;
				}
			}
			else{
				if(nodeToDelete == nodeToDelete.parent.right){
					nodeToDelete.right.parent = nodeToDelete.parent;
					nodeToDelete.parent.right = nodeToDelete.right;
					
				}
				else{
					nodeToDelete.right.parent = nodeToDelete.parent;
					nodeToDelete.parent.left = nodeToDelete.right;
				}
			}
		}
		else{
			//Nóðan til að eyða er rótin á trénu
			if(nodeToDelete.left != null){
				root = nodeToDelete.left;
				nodeToDelete = null;
			}
			else{
				root = nodeToDelete.right;
				nodeToDelete = null;
			}
		}
	}

	/*
		Notkun: twoLeafs(node);
		Fyrir: node er hlekkur sem á að eyða úr Splay trénu
			hlekkurinn node hefur tvö lauf
		Eftir: Búið er að eyða hlekknum node úr Splay trénu 
        */
	private void twoLeafs(Node nodeToDelete)
	{
		Node succesor = treeMin(nodeToDelete.right);
		nodeToDelete.key = succesor.key;
	
		if(succesor.right != null){
		
			oneLeafs(succesor);
			return;
		}
		else{
	
			zeroLeafs(succesor);
			return;
		}
			
	}
	
	/*
		Notkun: treeMin(node);
		Fyrir: node er hlekkur í Splay tré
		Eftir: Búið er að finna minnsta gildið í undirtré þar sem node er rót undirtrés
        */
	private Node treeMin(Node node)
	{
		while(node.left != null)
			node = node.left;
		return node;
	}
	
	/*
		Notkun: treeMax(node);
		Fyrir: node er hlekkur í Splay tré
		Eftir: Búið er að finna hæsta gildið í undirtré þar sem node er rót undirtrés
        */
	private Node treeMax(Node node)
	{
		while(node.right != null)
			node = node.right;
		return node;
	}
	
	/*
		Notkun: Splay(node);
		Fyrir: node er hlekkur í Splay tré
		Eftir: node er orðin rót Splay trésins
	*/
	private void Splay(Node node)
	{
		if(node.parent == null)
			return;
		else if(node.parent.parent == null)
		{
			Node rootParent = node.parent;
			if(node == rootParent.left)
			{
					rotateRight(node);
					Splay(node);
			}
			else
			{
				rotateLeft(node);
				Splay(node);
			}
		}
		else
		{
			Node grandParent = node.parent.parent;
			Node parent = node.parent;
			if(parent == grandParent.left)
			{
				if(node == parent.left){
					// Sikk-sikk:
					//        g        n
					//       / \      / \
					//      p   D    A   p
					//     / \          / \
					//    n   C   =>   B   g
					//   / \              / \
					//  A   B            C   D
					rotateRight(parent);
					rotateRight(node);
					Splay(node);
				}
				else {
					// Sikk-sakk:
					//       g          n
					//      / \   =>   / \
					//     p   D      /   \
					//    / \        p     g
					//   A   n      / \   / \
					//      / \    A   B C   D
					//     B   C
					rotateLeft(node);
					rotateRight(node);
					Splay(node);
				}
			}
			else {
				if(node == parent.left){
					// Sakk-sikk:
					//        g           n
					//       / \   =>    / \
					//      A   p       /   \
					//         / \     g     p
					//        n   D   / \   / \
					//       / \     A   B C   D
					//      B   C
					rotateRight(node);
					rotateLeft(node);
					Splay(node);
				}
				else {
					// Sakk-sakk:
					//     g               n
					//    / \     =>      / \
					//   A   p           p   D 
					//      / \         / \
					//     B   n       g   C
					//        / \     / \
					//       C   D   A   B
					rotateLeft(parent);
					rotateLeft(node);
					Splay(node);
				}
			}
		}
	}
	
	/*
		Notkun: rotateLeft(node);
		Fyrir : node er hlekkur í Splay tré
		Eftir : Búið er að færa node upp um eitt sæti eins og sést á eftirfarandi mynd
			(n = node)

		    p          n
		   / \   =>   / \
		  A   n      p   C
		     / \    / \
		    B   C  A   B
	*/
	private void rotateLeft(Node node)
	{
		Node parent = node.parent;
		if(parent != null){
			Node grandParent = node.parent.parent;
			if(grandParent != null){
				if(parent == grandParent.left){
					grandParent.left = node;
				}
				else{
					grandParent.right = node;
				}
				if(node.left != null){
					node.left.parent = parent;
				}
				parent.right = node.left;
				parent.parent = node;
				node.left = parent;
				node.parent = grandParent;
			}
			else{
				Node rootParent = parent.parent;
				if(node.left != null){
					node.left.parent = parent;
				}
				parent.right = node.left;
				parent.parent = node;
				node.left = parent;
				node.parent = rootParent;
			}
		}
	}

	/*
		Notkun: rotateRight(node);
		Fyrir : node er hlekkur í Splay tré
		Eftir : Búið er að færa node upp um eitt sæti eins og sést á eftirfarandi mynd
			(n = node)

		      p        n
		     / \  =>  / \
		    n   C    A   p
		   / \          / \
		  A   B        B   C
		
	*/
	private void rotateRight(Node node)
	{
		Node parent = node.parent;
		if(parent != null){
			Node grandParent = node.parent.parent;
			if(grandParent != null){
				if(parent == grandParent.left){
					grandParent.left = node;
				}
				else{
					grandParent.right = node;
				}
				if(node.right != null){
					node.right.parent = parent;
				}
				parent.left = node.right;
				parent.parent = node;
				node.right = parent;
				node.parent = grandParent;
			}
			else{
				Node rootParent = parent.parent;
				if(node.right != null){
					node.right.parent = parent;
				}
				parent.left = node.right;
				parent.parent = node;
				node.right = parent;
				node.parent = rootParent;
			}
		}
	}
}