class Node():
    def __init__(self,val) -> None:
        self.val = val
        self.next =None
        self.previous = []

class linklist():
    def __init__(self,head = None) -> None:
        self.head = head
        self.tail = head

    def append(self,node):
        self.tail.next = node
        self.tail = node

    def find(self,val):
        t = self.head
        while t != None:
            if t.val == val:
                return t
            t = t.next
        return None


def search(val):
    for link in head_list:
        if link.find(val):
            return link.find(val)
    return None

def removeHead(node):
    for link in head_list:
        if link.head == node:
            head_list.remove(link)


    

a = input("Enter edges: ").split(",")
head_list = []

def display():
    print("\n----------------")
    for link in head_list:
        t = link.head
        while t != None:
            print(t.val,end=" ")
            t=t.next
        print("")
    print("----------------")
for i in a:
    print(i)
    find = False
    for link in head_list:
        if link.find(i[0]):
            find = True
  
            if search(i[-1]) :
                
                newnode = search(i[-1])
                link.find(i[0]).next = newnode
                removeHead(newnode)
            else:
                link.find(i[0]).next = Node(i[-1])
    if not find:
        node = Node(i[0])
        if search(i[-1]):
            newnode = search(i[-1])
            node.next = newnode
            removeHead(newnode)
        else:    
            node.next = Node(i[-1])
        head_list.append(linklist(node))
    display()

display()