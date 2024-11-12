def minimum(l):
    n=len(l) - 1
    if n == 0: 
        return False
    elif n == 1:
        return l[0]
    else:
        return min(l[n],minimum(l[:n]))

l = list(map(int, input("Enter Input : ").split()))
print("Min : " + str(minimum(l)))