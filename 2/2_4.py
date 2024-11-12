def count_decimal_places(number):
    s = str(number)
    if '.' in s:
        return len(s.split('.')[1])
    return 0

def max_decimal_places(*args):
    return max(count_decimal_places(arg) for arg in args)

def range(a, b=0.0, c=0.0):
    decimal_places = max_decimal_places(a, b, c)
    format_str = f"{{:.{decimal_places}f}}"  # Format string to match the max decimal places
    range_list = []

    if b == 0.0 and c == 0.0:
        start = 0.0
        while start < a:
            range_list.append(float(format_str.format(start)))
            start += 1.0
    elif b != 0.0 and c == 0.0:
        while a < b:
            range_list.append(float(format_str.format(a)))
            a += 1.0
    elif b != 0.0 and c != 0.0:
        while a < b:
            range_list.append(float(format_str.format(a)))
            a += float(format_str.format(c))

    return f"({', '.join([str(x) for x in range_list])})"

print("*** New Range ***")
inputs = input("Enter Input : ").split()
numbers = [float(num) for num in inputs]
if len(numbers) == 1:
    print(range(numbers[0]))
elif len(numbers) == 2:
    print(range(numbers[0], numbers[1]))
elif len(numbers) == 3:
    print(range(numbers[0], numbers[1], numbers[2]))
