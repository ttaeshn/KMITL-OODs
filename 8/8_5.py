class BST:
    class BSTNode:
        def __init__(self, val, left=None, right=None) -> None:
            self.val = val
            self.left = left
            self.right = right

        def __str__(self):
            return str(self.val)

    def __init__(self, root=None) -> None:
        if root is None:
            self.root = None 
        else: 
            self.root = root

    def search_subtree(self, root, key):
        if root is None:
            return None

        if root.val == key:
            return root  

        elif key < root.val:
            return self.search_subtree(root.left, key)
        else:
            return self.search_subtree(root.right, key)

    def insert(self, data):
        self.root = self._insert(self.root, data)
        return self.root

    def _insert(self, root, data):
        if root is None:
            return self.BSTNode(data)
        else:
            if int(data) >= root.val:
                root.right = self._insert(root.right, data)
            else:
                root.left = self._insert(root.left, data)
        return root

    def delete_subtree(self, root, key):
        if root is None:
            return

        if key == self.root.val:
            self.root = None
            return 

        if root.left is not None:
            if root.left.val == key:
                root.left = None

        if root.right is not None:
            if root.right.val == key:
                root.right = None

        if root.left is not None:
            self.delete_subtree(root.left, key)
        if root.right is not None:
            self.delete_subtree(root.right, key)

        return root

    def printTree90(self, root, indent=0):
        if root is not None:
            self.printTree90(root.right, indent + 1)
            print("    " * indent + str(root.val))
            self.printTree90(root.left, indent + 1)

class AVLTree:
    class AVLNode:
        def __init__(self, val, left=None, right=None) -> None:
            self.val = val
            self.left = left
            self.right = right
            self.height = self.setHeight()

        def __str__(self):
            return str(self.val)

        def setHeight(self):
            a = self.getHeight(self.left)
            b = self.getHeight(self.right)
            self.height = 1 + max(a,b)
            return self.height

        def getHeight(self, node):
            return -1 if node == None else node.height

        def balanceValue(self):     
            return self.getHeight(self.left) - self.getHeight(self.right)

    def __init__(self, root=None) -> None:
        self.root = root

    def insert(self, root, key):
        if root is None:
            return self.AVLNode(key)
        else:
            if int(key) >= root.val:
                root.right = self.insert(root.right, key)
            else:
                root.left = self.insert(root.left, key)

        root.height = 1 + max(root.getHeight(root.left), root.getHeight(root.right))
        balance = root.balanceValue()
        
        #left-left
        if balance > 1 and root.left.balanceValue() >= 0:
           return self.right_rotate(root)

        #left-right
        if balance > 1 and root.left.balanceValue() < 0:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)

        #right-left
        if balance < -1 and root.right.balanceValue() > 0:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)

        #right-right
        if balance < -1 and root.right.balanceValue() <= 0:
            return self.left_rotate(root)

        return root

    def left_rotate(self, x):
        y = x.right
        T = y.left
        x.right = T
        y.left = x
        x.height = x.setHeight()
        y.height = y.setHeight()
        return y

    def right_rotate(self, y):
        x = y.left
        T = x.right
        y.left = T
        x.right = y
        y.height = y.setHeight()
        x.height = x.setHeight()
        return x

    def bst_to_avl(self, bst_root):
        sorted_values = self.inorder_traversal(bst_root)

        for val in sorted_values:
            self.root = self.insert(self.root, val)

    def inorder_traversal(self, root):
        if root is None:
            return []
        return (
            self.inorder_traversal(root.left)
            + [root.val]
            + self.inorder_traversal(root.right)
        )

    def printTree90(self, root, indent=0):
        if root is not None:
            self.printTree90(root.right, indent + 1)
            print("    " * indent + str(root.val))
            self.printTree90(root.left, indent + 1)

inp1, inp2 = input(
    "Enter the val of tree and node to cut: "
).split("/")
bst = BST()
for i in inp1.split():
    bst.insert(int(i))
print("Before cut:")
bst.printTree90(bst.root)

avl1, avl2 = AVLTree(), AVLTree()

print("Cutted Tree:")
subtree_root = bst.search_subtree(bst.root, int(inp2))
avl1.bst_to_avl(subtree_root)
avl1.printTree90(avl1.root)

print("Left Tree:")
bst.root = bst.delete_subtree(bst.root, int(inp2))
avl2.bst_to_avl(bst.root)
avl2.printTree90(avl2.root)