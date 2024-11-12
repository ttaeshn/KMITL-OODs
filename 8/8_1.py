class AVLNode:
        def __init__(self, data, left = None, right = None):
            self.data = data
            self.left = None if left is None else left
            self.right = None if right is None else right
            self.height = self.setHeight()

        def __str__(self):
            return str(self.data)

        def setHeight(self):
                a = self.getHeight(self.left)
                b = self.getHeight(self.right)
                self.height = 1 + max(a,b)
                return self.height

        def getHeight(self, node):
            return -1 if node == None else node.height

        def balanceValue(self):     
            return self.getHeight(self.left) - self.getHeight(self.right)

class AVLTree:
    def __init__(self, root = None):
        self.root = None if root is None else root
    
    def add(self, data):
        self.root = self._add(self.root, data)
        return self.root

    def _add(self, root, data):
        if root is None:
            return AVLNode(data)
        else:
            if int(data) >= root.data:
                root.right = self._add(root.right, data)
            else:
                root.left = self._add(root.left, data)

        # print(root.data)

        root.height = 1 + max(root.getHeight(root.left), root.getHeight(root.right))
        # print(root.height)
        balance = root.balanceValue()
        # print(f"now {data} add after {root.data}")
        # print(f"{root.data} height is {root.getHeight(root)}")

        #left-left
        if balance > 1 and root.left.balanceValue() >= 0:
           return self.rotateRightChild(root)

        #left-right
        if balance > 1 and root.left.balanceValue() < 0:
            root.left = self.rotateLeftChild(root.left)
            return self.rotateRightChild(root)

        #right-left
        if balance < -1 and root.right.balanceValue() > 0:
            root.right = self.rotateRightChild(root.right)
            return self.rotateLeftChild(root)

        #right-right
        if balance < -1 and root.right.balanceValue() <= 0:
            return self.rotateLeftChild(root)

        return root

    def rotateLeftChild(self, x) :
        y = x.right
        T = y.left
        x.right = T
        y.left = x
        x.height = x.setHeight()
        y.height = y.setHeight()
        return y

    def rotateRightChild(self, y) :
        x = y.left
        T = x.right
        y.left = T
        x.right = y
        y.height = y.setHeight()
        x.height = x.setHeight()
        return x

    def postOrder(self):
        print("AVLTree post-order : ",end = "")   
        if self.root is None:
            return 

        self._postOrder(self.root)

    def _postOrder(self, root):
        cur_node = root
        if root.left is not None:
            self._postOrder(root.left)

        if root.right is not None:
            self._postOrder(root.right)
            
        print(cur_node, end = " ")

    def printTree(self):
        AVLTree._printTree(self.root)
        print()

    def _printTree(node , level=0): 
        if not node is None:
            AVLTree._printTree(node.right, level + 1)
            print('     ' * level, node.data)
            AVLTree._printTree(node.left, level + 1)

avl1 = AVLTree()
inp = input('Enter Input : ').split(',')
for i in inp:
    if i[:2] == "AD":
        avl1.add(int(i[3:]))
    elif i[:2] == "PR":
        avl1.printTree()
    elif i[:2] == "PO":
        avl1.postOrder()
        print()