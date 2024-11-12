class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
    def __str__(self):
        return str(self.data)

class BST:
    def __init__(self,root = None):
        if root is None:
            self.root = None 
        else: 
            self.root = root

    def insert(self, data):
        self.root = BST._insert(self.root,data)
        return self.root
        
    def _insert(root, data):
        # print("Hi")
        if root is None:
            return Node(data)
        else:
            if data >= root.data:
                root.right = BST._insert(root.right, data)
            else:
                root.left = BST._insert(root.left, data)
        return root
    
    def printTree(self, node, level = 0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)

    def checkpos(self, current = None, data = None):
        result_lst = []
        if current is None:
            current = self.root

        if str(self.root) == str(data):
            return ["Root"]

        else:
            if current.data == data:
                if (current.left is None and current.right is None):
                    return ["Leaf"]
                else:
                    return ["Inner"]

            if current.left is not None:
                left = self.checkpos(current = current.left, data = data)
                if left is not None:
                    result_lst.extend(left)
                
            if current.right is not None:
                right = self.checkpos(current = current.right, data = data)
                if right is not None:
                    result_lst.extend(right)

        return result_lst

T = BST()
inp = [int(i) for i in input('Enter Input : ').split()]
for i in range(1, len(inp)):
    root = T.insert(inp[i])
T.printTree(root)
print(T.checkpos(data = inp[0])[0] if T.checkpos(data = inp[0]) else "Not exist")
    
