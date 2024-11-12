class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def __repr__(self) -> str:
        return f"Node({self.data})"

    def height(self):
        return (max(Node.height(self.left), Node.height(self.right)) + 1) if self else -1
    
    def balance(self):
        return Node.height(self.left) - Node.height(self.right) if self else 0
    def leftRotate(self):
        y = self.right
        T = y.left
        y.left = self
        self.right = T
        return y

    def rightRotate(self):
        x = self.left
        T = x.right
        x.right = self
        self.left = T
        return x

    def insert(root, data):
        if root is None:
            return Node(data)
        branch = "left" if data < root.data else "right"
        root.__dict__[branch] = Node.insert(root.__dict__[branch], data)

        balance = root.balance()

        # Left Left
        if balance > 1 and root.left.balance() >= 0:            
            return Node.rightRotate(root)

        # Left Right
        if balance > 1 and root.left.balance() < 0:       
            root.left = Node.leftRotate(root.left)
            return Node.rightRotate(root)

        # Right Right
        if balance < -1 and root.right.balance() <= 0:
            return Node.leftRotate(root)

        # Right Left
        if balance < -1 and root.right.balance() > 0:
            root.right = Node.rightRotate(root.right)
            return Node.leftRotate(root)
        
        return root

    def _gen_display(self) -> 'tuple[list, int, int, int]':
        '''
        return
        - tree image: list[str]
        - left spacing: int
        - value width: int
        - right spacing: int
        '''
        if self is None:
            return [], 0, 0, 0
        lt, lf, lv, lb = Node._gen_display(self.left)
        rt, rf, rv, rb = Node._gen_display(self.right)
        data = str(self.data)
        if not lt and not rt:
            return [data], 0, len(data), 0
        add_left, add_right = int(bool(lt)), int(bool(rt))
        line = ((' '*(lf+lv) + '/' + ' '*(lb)) * add_left +
                ' ' * len(data) +
                (' '*rf + '\\' + ' '*(rv+rb)) * add_right)
        out = [' '*(lf+lv+add_left) + '_'*lb + data +
               '_'*rf + ' '*(rv+rb+add_right), line]
        if len(lt) > len(rt):
            rt.extend([' ' * (rf+rv+rb)] * (len(lt) - len(rt)))
        elif len(lt) < len(rt):
            lt.extend([' ' * (lf+lv+lb)] * (len(rt) - len(lt)))
        for l, r in zip(lt, rt):
            out.append(l + ' '*(len(data)+add_left+add_right) + r)
        return out, (lf+lv+lb+add_left), len(data), (rf+rv+rb+add_right)
    
    def find_me(root,lst):
        if root == None:
            return
        Node.find_me(root.left,lst)
        Node.find_me(root.right,lst)
        lst.append(root.data)

    def rebalance(root,val,dir):
        temp = root
        while temp != None and temp.data != val :
            if val < temp.data:
                temp = temp.left
            elif val > temp.data:
                temp = temp.right

        lst =[]
        Node.find_me(temp,lst)       
        if int(val) not in lst:
            print(f"No {val} in this tree") 
            return 1
        if dir == "left":
            lst = sorted(lst,reverse=True)            
            newTree  =  Node(lst[0])
            temp_new = newTree
            for i in lst[1:]:
                temp_new.left = Node(i)
                temp_new = temp_new.left
            temp.data = newTree.data
            temp.left = newTree.left
            temp.right =None

        elif dir == "right":
            lst = sorted(lst,reverse=False)            
            newTree  =  Node(lst[0])
            temp_new = newTree
            for i in lst[1:]:
                temp_new.right = Node(i)
                temp_new = temp_new.right
            temp.data = newTree.data
            temp.right = newTree.right
            temp.left = None
        return None  

# rotate = node to be rotate
rotate, direction, inp = input('Enter input: ').split(',')
rotate = int(rotate)
root = None
for i in map(int, inp.split()):
    root = Node.insert(root, int(i))
tree_image = root._gen_display()
print("Before")
print(*tree_image[0], sep='\n')
print("-" * sum(tree_image[1:]))

# Straighten a specified node with specified direction
# Generate new display: tree_image = Node._gen_display(<Node object at 0x80085>)
if not Node.rebalance(root,rotate, direction):
    print("After")
    tree_image = root._gen_display()
    print(*tree_image[0], sep='\n')