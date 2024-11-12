def bubbleSort(arr):
    for i in range(len(arr)-1):
        swapped = False
        move = [None]
        for j in range(0,len(arr)-i-1):
            if arr[j] > arr[j+1]:
                if not arr[j] in move:
                    move.pop()
                    move.append(arr[j])
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if swapped == False or i == len(arr)-2:
            print("last step : " +str(arr)+" move"+str(move))
            break
        else:
            print(str(i+1)+" step : "+str(arr)+" move"+str(move))

inp = [int(e) for e in input("Enter Input : ").split()]
bubbleSort(inp)