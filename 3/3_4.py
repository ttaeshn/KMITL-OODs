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

output = Stack()
print("* Stack Calculator *")
stage = 0
a = input("Enter arguments : ").split()
for i in a:
    if i.isdigit():
        output.push(i)
    elif i in "+-*/":
        num1,num2 = output.pop(),output.pop()
        if i == "+": output.push(int(num1) + int(num2))
        elif i == "-": output.push(int(num1) - int(num2))
        elif i == "*": output.push(int(num1) * int(num2))
        elif i == "/": output.push(int(int(num1) / int(num2)))
    elif i.isalpha() and (i != "DUP" and i != "POP"):
        stage = 1;break
    elif i == "DUP":
        output.push(output.peek())
    elif i == "POP":
        output.pop()

if output.isEmpty():output.push(0)

if stage == 0: print(output.peek())
else: print(f"Invalid instruction: {i}")