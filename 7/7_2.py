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

T = BST()
num_lst = []
inp = input('Enter Input : ').split("|")
num = [int(i) for i in inp[0].split()]
for i in num:
    root = T.insert(i)
    if i < int(inp[1]):
        num_lst.append(i)
T.printTree(root)
print("--------------------------------------------------")
# print(num_lst)
print(f"Below {inp[1]} : ",end="")
if len(num_lst) > 0:
    for i in range(len(num_lst)-1,-1,-1):
        for j in range(0,i):
            # print(num_lst[i-1], num_lst[i])
            if num_lst[j] > num_lst[j+1]:
                # print("Hi")
                temp = num_lst[j+1]
                num_lst[j+1] = num_lst[j]
                num_lst[j] = temp

    ans_str = " ".join(str(i) for i in num_lst)
    print(f"{ans_str}")
else:
    print("Not have")