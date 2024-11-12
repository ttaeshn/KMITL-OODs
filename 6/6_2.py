count = 0
def palindrome(str):
    global count
    if len(str) == 0:
        return 
    elif len(str) == 1:
        count += 1
    else:
        if str[0] == str[-1]:
            count += 1 
            return palindrome(str[1:-1])
        else:
            return

_str = input("Enter Input : ")
palindrome(_str)
if len(_str) == 0:
    print("Empty")
elif len(_str) % 2 == 0 and len(_str) != 0:
    print(f"'{_str}' is palindrome" if count == len(_str) // 2 else f"'{_str}' is not palindrome")
else:
    print(f"'{_str}' is palindrome" if count - 1 == len(_str) // 2 else f"'{_str}' is not palindrome")