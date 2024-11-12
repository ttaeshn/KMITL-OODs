class Node:
    def __init__(self, data): 
        self.data = data  
        self.left = None  
        self.right = None 
        self.level = None 

    def __str__(self):
        return str(self.data) 

class BinarySearchTree:
    def __init__(self): 
        self.root = None

    def insert(self, val):  
        if self.root is None:
            self.root = Node(val)
        else:
            current = self.root

            while True:
                if val < int(current.data):
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
                elif val > int(current.data):  
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break

    def delete(self, root, data):
        if root is None:
            print("Error! Not Found DATA")
            return

        if self.root.left is None and self.root.right is None and self.root.data == data:
            self.root = None
        elif self.root.left is None and self.root.data == data:
            self.root = self.root.right
        elif self.root.right is None and self.root.data == data:
            self.root = self.root.left
        
        if root.data != data:
            if root.data > data:
                root.left = self.delete(root.left, data)
            else:
                root.right = self.delete(root.right, data)

        else:
            if root.left is None:
                root = root.right
                return root

            elif root.right is None:
                root = root.left
                return root

            else:  
                cur = root.right #inorder successor
                while cur.left is not None: 
                    cur = cur.left 
                root.data = cur.data
                root.right = self.delete(root.right, cur.data)

        return root
                
def printTree90(node, level = 0):
    if node != None:
        printTree90(node.right, level + 1)
        print('     ' * level, node)
        printTree90(node.left, level + 1)


tree = BinarySearchTree()
data = input("Enter Input : ").split(",")
for i in data:
    if i.split()[0] == "i":
        print(f"insert {i.split()[1]}")
        tree.insert(int(i.split()[1]))
        printTree90(tree.root)
    elif i.split()[0] == "d":
        print(f"delete {i.split()[1]}")
        tree.delete(tree.root, int(i.split()[1]))
        printTree90(tree.root)