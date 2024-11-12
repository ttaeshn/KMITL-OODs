a=input("Enter All Bid : ").split()
l=[]
for i in a:l.append(int(i))
if len(l) > 1:l.sort();print(f"winner bid is {l[-1]} need to pay {l[-2]}" if l.count(l[-1]) == 1 else "error : have more than one highest bid")
else:print("not enough bidder")