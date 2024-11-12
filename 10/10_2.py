inp = input("Enter Input : ").split("/")
data_lst,find_lst = inp[0].split(), inp[1].split()

for j in find_lst:
    val,find = 9999,0
    for i in data_lst:
        if int(i) > int(j) and int(i) <= int(val):
            val = i
            find = 1
    print(val if find else "No First Greater Value")