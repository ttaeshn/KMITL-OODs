class Data:
    def __init__(self, key, value):
        self.key = key
        self.value = value

    def __str__(self):
        return "({0}, {1})".format(self.key, self.value)

class Hash:
    def __init__(self, items, size, maxCol):
        self.items = items
        self.size = size
        self.maxCol = maxCol

    def isFull(self):
        for i in self.items:
            if i == None:
                return False
        return True

    def findIndex(self, number):
        idx = number % self.size
        step = 1
        while self.items[idx] != None:
            print(f"collision number {step} at {idx}")
            if step >= self.maxCol:
                print("Max of collisionChain")
                return
            idx = (number + pow(step,2)) % self.size
            step += 1
        return idx

    def printTable(self):
        for i in range(len(self.items)):
            print('#'+str(i+1)+"	"+str(self.items[i]))
        print("---------------------------")

def sumOfASCII(string):
    sum = 0
    for char in string:
        sum += ord(char)
    return sum

print(" ***** Fun with hashing *****")
condition, data = input("Enter Input : ").split("/")
sizeOfItems, maxCollision = map(int, condition.split())
items = [None] * sizeOfItems
h = Hash(items, sizeOfItems, maxCollision)
for i in data.split(","):
    if h.isFull():
        print("This table is full !!!!!!")
        break
    key, value = i.split()
    idx = h.findIndex(sumOfASCII(key))
    if idx != None:
        items[idx] = Data(key, value)
    h.printTable()