def max_dict_key(Dict):
    max_val = -9999
    for i in Dict.key:
        if i > max_val:
            max_val = i

    return max_val

def sorted_dict(original_dict):
    sorted_Dict = {}
    while original_dict:
        sorted_val = max(original_dict)
        sorted_Dict[sorted_val] = original_dict.pop(sorted_val)

    return sorted_Dict

inp = [int(e) for e in input("Enter list  of numbers: ").split()]
index_list = []
for i in inp:
    if i not in index_list:
        index_list.append(i)

info = {}
for i in inp:
    if i in info.keys():
        info[i] += 1
    else:
        info[i] = 1

ans = sorted_dict(info)
for i in ans:
    print(f"number {i}, total: {ans[i]}")