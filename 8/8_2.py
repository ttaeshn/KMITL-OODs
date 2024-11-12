class TreeNode(object): 
    def __init__(self, val): 
        self.val = val 
        self.left = None
        self.right = None
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
  
class AVL_Tree(object): 
    def __init__(self, root = None):
        self.root = None if root is None else root
    
    def add(self, root, data):
        if root is None:
            return TreeNode(data)
        else:
            if int(data) >= root.val:
                root.right = self.add(root.right, data)
            else:
                root.left = self.add(root.left, data)

        # print(root.data)

        root.height = 1 + max(root.getHeight(root.left), root.getHeight(root.right))
        # print(root.height)
        # print(f"now {data} add after {root.val}")
        # print(f"{root.data} height is {root.getHeight(root)}")
        balance = root.balanceValue()
        
        # print(f"{root} = {balance}")

        if balance > 1 or balance < -1:
            print("Not Balance, Rebalance!")
            
        #left-left
        if balance > 1 and root.left.balanceValue() >= 0:
        #    print("ll")
           return self.rotateRightChild(root)

        #left-right
        if balance > 1 and root.left.balanceValue() < 0:
            # print("lr")
            root.left = self.rotateLeftChild(root.left)
            return self.rotateRightChild(root)

        #right-left
        if balance < -1 and root.right.balanceValue() > 0:
            # print("rl")
            root.right = self.rotateRightChild(root.right)
            return self.rotateLeftChild(root)

        #right-right
        if balance < -1 and root.right.balanceValue() <= 0:
            # print("rr")
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

def printTree90(node, level = 0):
    if node != None:
        printTree90(node.right, level + 1)
        print('     ' * level, node)
        printTree90(node.left, level + 1)
  
myTree = AVL_Tree() 
root = None

data = input("Enter Input : ").split()
for e in data:
    print("insert :",e)
    root = myTree.add(root, int(e))
    printTree90(root)
    print("===============")
