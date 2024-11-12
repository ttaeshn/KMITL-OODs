class Stack():
    def __init__(self, lst=None):
        if lst is not None:
            self.lst = lst
        else:
            self.lst = []
    
    def push(self, item):
        self.lst.append(item)

    def pop(self):
        return self.lst.pop()

    def peek(self):
        return self.lst[-1]

    def isEmpty(self):
        return len(self.lst) == 0

    def items(self):
        return self.lst

    def __str__(self):
        return str(self.lst)

a = input("Enter Infix : ")
priority = {
    "(": 0, 
    "+": 1,
    "-": 1,
    "*": 2,
    "/": 2,
    "^": 3,
    ")": 0
}

output = Stack()
operands = Stack()

for i in a:
    if i.isalpha():
        output.push(i)
    elif i in "+-*/^":
        while not operands.isEmpty() and priority[operands.peek()] >= priority[i]:
            output.push(operands.pop())
        operands.push(i)
    elif i == "(":
        operands.push(i)
    elif i == ")":
        while operands.peek() != "(":
            output.push(operands.pop())
        operands.pop()

while not operands.isEmpty():
    output.push(operands.pop())

print("Postfix : ", end="")
for i in output.lst:
    print(i, end="")