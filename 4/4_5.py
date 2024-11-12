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

    def front(self):
        if not self.isEmpty(): return self.items[0]
        else: return False

normal, mirror = input("Enter Input (Normal, Mirror) : ").split()
normal_queue, mirror_queue, bomb = Queue(), Queue(), Queue()

for i in range(len(mirror) - 1, -1,-1):
    mirror_queue.enqueue(mirror[i])

for i in range(len(normal)):
    normal_queue.enqueue(normal[i])


i, k, mirror_bombed, failed, normal_bombed = 0, 0, 0, 0, 0 

while i < len(mirror_queue.items) - 2:
    if mirror_queue.items[i] is mirror_queue.items[i+1] and mirror_queue.items[i] is mirror_queue.items[i+2]:
        mirror_bombed += 1
        for j in range(3):
            if j == 0:
                a = mirror_queue.items.pop(i)
                bomb.enqueue(a)
            else:
                mirror_queue.items.pop(i)
        i = 0
    else: i+=1

check_again = 0
if mirror_queue.size() > 2 :
    if mirror_queue.items[i -1] == mirror_queue.items[i-2] and mirror_queue.items[i] == mirror_queue.items[i-3]:
        mirror_bombed += 1
        if check_again == 0:
            a = mirror_queue.dequeue()
            bomb.enqueue(a)
            check_again += 1
        else:
            mirror_queue.dequeue()

failed, normal_bombed = 0, 0
while k < len(normal_queue.items) - 2:
    if normal_queue.items[k] is normal_queue.items[k+1] and normal_queue.items[k] is normal_queue.items[k+2]:
        if bomb.size() > 0:
            bombing = bomb.dequeue()
            normal_queue.items.insert(k+2, bombing)
            if normal_queue.items[k] is normal_queue.items[k+1] and normal_queue.items[k] is normal_queue.items[k+2]:
                failed += 1
                for _ in range(3):
                    normal_queue.items.pop(k)
                k+=1
            else: k+=1
        else: 
            normal_bombed += 1
            for _ in range(3):
                normal_queue.items.pop(k)
    else: k +=1

k = 0
while k < normal_queue.size() - 2:
    if normal_queue.items[k] == normal_queue.items[k+1] and normal_queue.items[k] == normal_queue.items[k+2]:
        check_again = 0
        normal_bombed +=1
        for _ in range(3):
            normal_queue.items.pop(k)
        k = 0
    else: k += 1

print("NORMAL :" + "\n" + str(len(normal_queue.items)))

if not normal_queue.isEmpty():
    for i in range(len(normal_queue.items) -1, -1, -1):
        print(normal_queue.items[i],end="")
    print()
else: print("Empty")
print(f"{normal_bombed} Explosive(s) ! ! ! (NORMAL)" if failed < 1 else f"{normal_bombed} Explosive(s) ! ! ! (NORMAL)" + "\n" f"Failed Interrupted {failed} Bomb(s)")
print("------------MIRROR------------" + "\n" + ": RORRIM" + "\n" + str(len(mirror_queue.items)))

if len(mirror_queue.items) > 0:
    for i in range(len(mirror_queue.items) -1, -1, -1):
        print(mirror_queue.items[i],end="")
    print()
else:print("ytpmE")
print(f"(RORRIM) ! ! ! (s)evisolpxE {mirror_bombed}")