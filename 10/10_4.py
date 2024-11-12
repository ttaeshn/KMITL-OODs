class Hash:
    def __init__(self, size, maxcollision, threshold):
        self.size = size
        self.maxCol = maxcollision
        self.hashTable = [None] * size
        self.threshold = threshold
    
    def insert(self, data):
        index = data % self.size
        step = 1
        collision = 1

        while self.hashTable[index] is not None:  
            print(f"collision number {step} at {index}")
            index = (data + (step**2)) % self.size
            if collision >= self.maxCol:
                print("****** Max collision - Rehash !!! ******")
                self.rehashing()
                index = data % self.size    
            collision += 1
            step += 1

        if self.hashTable[index] is None:
            #self.hashTable[index] = data
            if (((self.sizeof() + 1) / self.size) * 100) >= self.threshold:
                print("****** Data over threshold - Rehash !!! ******")
                self.rehashing()
                self.insert(data)
            else:
                self.hashTable[index] = data
            
    
    def rehashing(self):
        olddata = []
        for i in self.hashTable:
            if i != None:
                olddata.append(i)

        newSize = self.findPrimeNumber(self.size)
        self.size = newSize
        self.hashTable = [None] * newSize
       
        for i in olddata[::-1]:
            self.insert(i)

    def sizeof(self):
        n = 0
        for i in self.hashTable:
            if i is not None:
                n += 1
        return n
    
    def findPrimeNumber(self, num):
        num *= 2
        flag = True
        while flag: 
            for i in range(2,num):
                if num % i == 0:
                    num += 1
                    break
            else:
                return num

    def findThreshold(self):
        elementNum = self.findTotalElements()
        return elementNum / self.size

    def printHash(self):
        index = 1
        for i in self.hashTable:
            print(f"#{index}\t{i}")
            index += 1
        print('----------------------------------------')


print(" ***** Rehashing *****")
inp = input("Enter Input : ").split('/')
tablesize = int(inp[0].split()[0])
maxcol = int(inp[0].split()[1])
threshold = int(inp[0].split()[2])
data = inp[1].split()
h = Hash(tablesize, maxcol, threshold)
print("Initial Table :")
h.printHash()
for i in data:
    print(f'Add : {i}')
    h.insert(int(i))
    h.printHash()