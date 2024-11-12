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

    def create(self, val):
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
                
def printTree90(node, level = 0):
    if node is not None:
        printTree90(node.right, level + 1)
        print(' ' * 5 * level, str(node))
        printTree90(node.left, level + 1)

def father(root, data, parent=None):
    result_lst = []
    if root is None:
        return

    if root.data == data:
        if parent is None:
            return f"None Because {data} is Root"
        return parent

    left_result = father(root.left, data, root.data)
    right_result = father(root.right, data, root.data)

    result_lst.append(left_result)
    result_lst.append(right_result)

    for i in result_lst:
        if i is not None and i != "Not Found Data":
            return i
            
    return "Not Found Data"

tree = BinarySearchTree()
data = input("Enter Input : ").split("/")
for e in data[0].split():
    tree.create(int(e))
printTree90(tree.root)
if data[0] != "" and data[1] != "":
    print(father(tree.root,int(data[1])))