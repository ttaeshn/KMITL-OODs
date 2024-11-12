def bi_search(l, r, arr, x):
    mid = (l + r) // 2
    print(l,r,mid)

    if l > r:
        return False
    
    elif x == arr[mid]:
        return True

    else:
        if arr[mid] < k:
            return bi_search(mid+1, len(arr) - 1, sorted(arr), k)
        else:
            return bi_search(l, mid - 1, sorted(arr), k)

inp = input('Enter Input : ').split('/')
arr, k = list(map(int, inp[0].split())), int(inp[1])
print(bi_search(0, len(arr) - 1, sorted(arr), k))