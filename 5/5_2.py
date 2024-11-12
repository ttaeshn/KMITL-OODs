class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.previous = None

class LinkedList:
    def __init__(self, head = None):
        if head == None:
            self.head = None
            self.tail = None
            self.size = 0
        else: 
            self.head = head
            t = self.head
            self.size += 1

    def __str__(self):
        if self.isEmpty():
            return "Empty"
        cur, s = self.head, str(self.head.value) + " "
        while cur.next != None:
            s += str(cur.next.value) + " "
            cur = cur.next
        return s

    def reverse(self):
        if self.isEmpty():
            return "Empty"
        cur, s = self.tail, str(self.tail.value) + " "
        while cur.previous != None:
            s += str(cur.previous.value) + " "
            cur = cur.previous
        return s

    def isEmpty(self):
        return self.head == None

    def append(self, item):
        node = Node(item)
        if self.head == None:
            self.head = node
            self.tail = node
        else:
            node.previous = self.tail
            self.tail.next = node
            self.tail = node
        self.size +=1

    def addHead(self, item):
        node = Node(item)
        if self.head == None:
            self.head = node
            self.tail = node
        else:
            h = self.head
            h.previous = node
            node.next = h
            self.head = node
        self.size += 1

    def insert(self, pos, item):
        idx = 0
        node = Node(item)
        if pos < 0: 
            pos = self.size + pos

        if self.head == None:
            self.head = node
            self.tail = node
        else:
            if pos <= 0:
                h = self.head
                h.previous = node
                node.next = h
                self.head = node
            elif pos > self.size:
                node.previous = self.tail
                self.tail.next = node
                self.tail = node
            else:
                h = self.head
                while idx < pos - 1:
                    h = h.next
                    idx += 1
                node.next = h.next
                h.next.previous = node
                h.next = node
                node.previous = h
        
        self.size +=1
        
    def search(self, item):
        node = Node(item)
        h = self.head
        state = 0
        if node.value == h.value:
            return "Found"

        while h.next is not None:
            if node.value is h.value:
                state = 1
                break
            else: h = h.next

        if node.value == h.value:
            return "Found"

        return "Found" if state == 1 else "Not Found"

    def index(self, item):
        node = Node(item)
        idx = 0
        found = False
        h = self.head
        if node.value == h.value:
            return idx

        while h.next is not None:
            if h.value == node.value:
                found = True
                break
            else:
                h = h.next
                idx += 1

        return idx if found == True else -1

    def size(self):
        return self.size

    def pop(self, pos):
        idx = 0
        success = 0
        if pos < 0: 
            pos = self.size + pos - 1

        if self.size <= 0 or pos >= self.size:
            pass
        else:
            if pos <= 0:
                h = self.head
                self.head = h.next
                h = None
            else:
                h = self.head
                while idx < pos - 1:
                    h = h.next
                    idx += 1
                h.previous.next = h.next.previous
                h.next.previous = h.previous.next
            success = 1
            self.size -=1
        return "Success" if success == 1 else "Out of Range"


L = LinkedList()
inp = input('Enter Input : ').split(',')
for i in inp:
    if i[:2] == "AP":
        L.append(i[3:])
    elif i[:2] == "AH":
        L.addHead(i[3:])
    elif i[:2] == "SE":
        print("{0} {1} in {2}".format(L.search(i[3:]), i[3:], L))
    elif i[:2] == "SI":
        print("Linked List size = {0} : {1}".format(L.size, L))
    elif i[:2] == "ID":
        print("Index ({0}) = {1} : {2}".format(i[3:], L.index(i[3:]), L))
    elif i[:2] == "PO":
        before = "{}".format(L)
        k = L.pop(int(i[3:]))
        print(("{0} | {1}-> {2}".format(k, before, L)) if k == "Success" else ("{0} | {1}".format(k, L)))
    elif i[:2] == "IS":
        data = i[3:].split()
        L.insert(int(data[0]), data[1])
print("Linked List :", L)
print("Linked List Reverse :", L.reverse())

# ถ้าติดแต่เพื่อนไม่ติดจะบอกเพื่อนยังไงว่าคุณติด แต่เพื่อนไม่ติด
# ถ้าเอาหนึ่งคนในแลปออก จะเอาใครออก เพราะอะไรเราถึงไปแทนได้