l=[]
a = input("Enter Input : ").split(",")
for i in range(len(a)):
    if a[i].split()[0] == "E": l.append(a[i].split()[1]);print(f"Add {a[i].split()[1]} index is {len(l)-1}")
    elif a[i] == "D": 
        if len(l) > 0:t = l.pop(0);print(f"Pop {t} size in queue is {len(l)}")
        else:print("-1")
print(f"Number in Queue is :  {l}" if len(l) > 0 else "Empty")