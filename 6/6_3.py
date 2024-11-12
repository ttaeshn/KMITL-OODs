def binary(start = 0,till = 0, num = 0):
    if till < 0:
        print("Only Positive & Zero Number ! ! !")
    elif till == 0:
        print("0".zfill(num))
    else:
        if start <= till:
            now_str = str(bin(start)[2:]).zfill(num)
            start += 1
            print(now_str)
            binary(start, till ,num)

inp = int(input("Enter Number : "))
binary(0,2**inp - 1, inp)