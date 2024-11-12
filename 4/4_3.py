class Queue:
    def __init__(self, l=None):
        if l is not None:
            self.items = list(l)
        else:
            self.items = []

    def push(self, i):
        self.items.append(i)

def encodemsg(Q1, Q2):
    for i in range(len(Q1.items)):
        j = i % len(Q2.items)
        shift = int(Q2.items[j])
        if Q1.items[i].isalpha():
            if Q1.items[i].islower():
                Q1.items[i] = chr((ord(Q1.items[i]) - ord('a') + shift) % 26 + ord('a'))
            else:
                Q1.items[i] = chr((ord(Q1.items[i]) - ord('A') + shift) % 26 + ord('A'))
    return f"Encode message is :  {Q1.items}"

def decodemsg(Q1, Q2):
    for i in range(len(Q1.items)):
        j = i % len(Q2.items)
        shift = int(Q2.items[j])
        if Q1.items[i].isalpha():
            if Q1.items[i].islower():
                Q1.items[i] = chr((ord(Q1.items[i]) - ord('a') - shift) % 26 + ord('a'))
            else:
                Q1.items[i] = chr((ord(Q1.items[i]) - ord('A') - shift) % 26 + ord('A'))
    return f"Decode message is :  {Q1.items}"

a = input("Enter String and Code : ").split(",")
q1 = Queue()
for i in a[0]:
    if i != " ":
        q1.push(i)
q2 = Queue()
for i in a[1]:
    if i != " ":
        q2.push(i)
print(encodemsg(q1, q2))
print(decodemsg(q1, q2))
