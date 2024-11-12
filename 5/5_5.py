class Node:
    def __init__(self, data, next = None):
        self.data = data
        self.next = next if next != None else None
    
class LinkList:
    def __init__(self, head = None):
        self.head = head if head != None else None
        self.size = 0
    
    def add_head(self, new_head):
        self.head = Node(new_head, self.head) if self.head != None else Node(new_head)
        self.size += 1

    def append(self, data):
        if not self.is_empty():
            new_node = Node(data)
            current_node = self.head
            while current_node.next != None:
                current_node = current_node.next
            current_node.next = new_node
            self.size += 1
        else:
            self.add_head(data)

    def remove(self, data):
        if not self.is_empty():
            if self.head.data == data:
                self.remove_head()
            else:
                current_node = self.head
                while current_node.next.data != data:
                    current_node = current_node.next
                remove_node = current_node.next 
                current_node.next = remove_node.next
                self.size -= 1
                return remove_node
        else:
            return -1

    def remove_tail(self):
        if not self.is_empty():
            if self.head.next == None:
                return self.remove_head()
            else:
                current_node = self.head
                while current_node.next.next != None:
                    current_node = current_node.next
                remove_node = current_node.next 
                current_node.next = remove_node.next
                self.size -= 1
                return remove_node
        else:
            return -1

    def remove_head(self):
        if not self.is_empty():
            remove_node = self.head
            self.head = self.head.next
            self.size -= 1
            return remove_node
        else:
            return None

    def search(self, data):
        current_node = self.head
        while current_node != None:
            if current_node.data == data:
                return True
            current_node = current_node.next
        return False

    def is_empty(self):
        return True if self.head == None else False

    def list_size(self):
        return self.size
    
    def largest_element(self):
        if self.is_empty():
            return None
        largest = int(self.head.data)
        current_node = self.head
        while current_node.next != None:
            if int(current_node.data) > largest:
                largest = int(current_node.data)
            current_node = current_node.next
        return largest

    def __str__(self):
        current_node = self.head
        rep = []
        while current_node != None:
            rep.append(str(current_node.data))
            current_node = current_node.next
        return " -> ".join(rep)

def convert_to_linklist(ls):
    linklist = LinkList()
    for data in ls:
        linklist.append(data)
    return linklist

def calculate_number_of_iteration(ls):
    largest_element = ls.largest_element()
    counter = 0
    while largest_element > 0:
        counter += 1
        largest_element //= 10
    return counter

def get_data_at_index(data, index):
    for _ in range(index):
        data //= 10
    return data % 10

def radix_sort(ls):
    before = convert_to_linklist(ls)
    linklist = convert_to_linklist(ls)
    number_of_iteration = calculate_number_of_iteration(linklist)
    queue_digits = [LinkList(), LinkList(), LinkList(), LinkList(), LinkList(), LinkList(), LinkList(), LinkList(), LinkList(), LinkList()]
    for index in range(number_of_iteration):
        print(f"Round : {index + 1}")
        flag = []
        current_node = linklist.head
        while current_node != None:
            if int(current_node.data) >= 0:
                data = int(current_node.data)
                data_at_index = get_data_at_index(data, index)
                queue_digits[data_at_index].append(data)
                flag.append(current_node.data)
            current_node = current_node.next
        for i in range(len(flag)):
            linklist.remove(flag[i])
        while not linklist.is_empty():
            data = int(linklist.remove_head().data)
            data_at_index = get_data_at_index(abs(data), index)
            queue_digits[data_at_index].append(data)


        for i in range(10):
            tmp = []
            current_queue = queue_digits[i]
            current_node = current_queue.head
            while current_node != None:
                tmp.append(str(current_node.data))
                current_node = current_node.next
            print(f"{i} : {' '.join(tmp)}")

        flag = []
        for i in range(9,-1,-1):
            current_queue = queue_digits[i]
            current_node = current_queue.head
            while current_node != None:
                if current_node.data >= 0:
                    linklist.append(str(current_node.data))
                    flag.append((i, current_node.data))
                current_node = current_node.next
        for i in range(len(flag)):
            queue_digits[flag[i][0]].remove(flag[i][1])
        for i in range(10):
            current_queue = queue_digits[i]
            while not current_queue.is_empty():
                linklist.append(str(current_queue.remove_head().data))

        print("------------------------------------------------------------")
    return number_of_iteration, before, linklist

ls = input("Enter Input : ").split(" ")
print("------------------------------------------------------------")
number_of_iteration, before, sorted_ls = radix_sort(ls)
print(f"{number_of_iteration} Time(s)")
print(f"Before Radix Sort : {before}")
print(f"After  Radix Sort : {sorted_ls}")