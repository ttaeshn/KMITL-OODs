class Stack:
    def __init__(self, l=None):
        if l is not None:
            self.items = l
        else:
            self.items = []
    
    def push(self, i):
        self.items.append(i)
    
    def pop(self):
        return self.items.pop()
    
    def isEmpty(self):
        return len(self.items) == 0
    
    def size(self):
        return len(self.items)

def parenMatching(str):
    s = Stack()
    i = 0
    error = 0
    while i < len(str) and error == 0:
        c = str[i]
        if c in "({[":
            s.push(c)
        elif c in ")}]":
            if s.size() > 0:
                if not match(s.pop(), c):
                    error = 1
            else:
                error = 2  # No matching opening parenthesis
        i += 1
    
    if s.size() > 0 and error == 0:
        error = 3  # Extra opening parentheses
    
    return error, c, i, s

def match(op, cl):
    open_chars = "{(["
    close_chars = "})]"
    return open_chars.index(op) == close_chars.index(cl)

a = input("Enter expresion : ")
error, c, i, s = parenMatching(a)

if error == 1:
    print(a + " Unmatch open-close")
elif error == 2:
    print(a + " close paren excess")
elif error == 3:
    print(a + " open paren excess   " +str(s.size()) + " :", end=" ")
    for ele in s.items:
        print(ele, end="")
    print()
else:
    print(a + " MATCH")