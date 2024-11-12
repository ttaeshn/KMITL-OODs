def insertionSortRecursive(arr,n): 
    if n<=1: 
        return
        
    insertion_list = [arr.pop(0)]
    print(f"{insertion_list} {arr}")
    insertionSortRecursive(arr,n-1) 
    last = arr[n-1] 
    j = n-2
      
    while (j>=0 and arr[j]>last): 
        arr[j+1] = arr[j]
        print(f"insert {arr[j]} at index {j} : {insertion_list} {arr}")
        j = j-1 
  
    arr[j+1]=last

inp = input("Enter Input : ").split()
print(insertionSortRecursive(inp,len(inp)))