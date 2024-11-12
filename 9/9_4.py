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

inp = input("Enter Input : ").split()
my_dict = {}
for i in inp:
    for j in i:
        if j.isalpha():
            my_dict.update({i: ord(j)})

print(" ".join(i for i in sorted_dict(my_dict)))