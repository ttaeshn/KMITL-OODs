class Queue:
    def __init__(self, lst = None):
        if lst == None: self.items = []
        else: self.items = lst

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        return self.items.pop(0)

    def isEmpty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

a = input("Enter people and time : ").split()
main_queue, first_queue, second_queue =  Queue(),Queue(),Queue()
for i in a[0]:
    main_queue.enqueue(i)

stage = 0
for i in range(1, int(a[1])+1):
    if not second_queue.isEmpty(): 
        stage += 1

    if not main_queue.isEmpty():
        if (i-1) % 3 == 0 and i != 1:
            first_queue.dequeue()
        if stage % 2 == 0 and stage != 0:
            second_queue.dequeue()

        if first_queue.size() < 5:
            first_queue.enqueue(main_queue.dequeue())
        elif first_queue.size() >= 5 and second_queue.size() < 5:
            second_queue.enqueue(main_queue.dequeue())
        else: continue
    else: 
        if (i-1) % 3 == 0 and i != 1:
            first_queue.dequeue()
        elif stage % 2 == 0:
            second_queue.dequeue()

    print(i, main_queue.items, first_queue.items, second_queue.items)