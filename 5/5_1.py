class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

    def __str__(self):
        return str(self.data)


class List:
    def __init__(self):
        self.head = None
        self.size = 0

    def isEmpty(self):
        return self.size == 0

    def __str__(self):
        head = self.head
        if not self.isEmpty():
            result = ""
            while head is not None:
                result += str(head.data) + "->"
                head = head.next
            return "link list : " + result[:-2]
        else:
            return "List is empty"

    def append(self, data):
        current = Node(data)
        if self.head is None:
            self.head = current
        else:
            head = self.head
            while head.next is not None:
                head = head.next
            head.next = current
        self.size += 1

    def insert(self, index, data):
        if 0 <= index <= self.size:
            print(f"index = {index} and data = {data}")
            current = Node(data)
            if index == 0:
                current.next = self.head
                self.head = current
            else:
                head = self.head
                count = 0
                while count < index - 1:
                    head = head.next
                    count += 1
                current.next = head.next
                head.next = current
            self.size += 1
        else:
            print("Data cannot be added")

    def sizeof(self):
        return self.size


inp = input("Enter Input : ").split(",")
linked_list = List()
if len(inp[0]) > 0:
    for i in inp[0].split():
        linked_list.append(i)
    print(linked_list)
else:
    print(linked_list)

if len(inp) > 1:
    for j in range(1, len(inp)):
        now = inp[j].split(":")
        index, data = int(now[0]), now[1]
        linked_list.insert(index, data)
        print(linked_list)