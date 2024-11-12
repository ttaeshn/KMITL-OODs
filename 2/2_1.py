class Calculator :
    def __init__(self,n1,n2):
        self.__num1 = int(n1)
        self.__num2 = int(n2)

    def __add__(self):
        return self.__num1 + self.__num2

    def __sub__(self):

        return self.__num1 - self.__num2

    def __mul__(self):

        return self.__num1 * self.__num2

    def __truediv__(self):

        return self.__num1 / self.__num2

x,y = input("Enter num1 num2 : ").split(",")
print(Calculator(x,y).__add__())
print(Calculator(x,y).__sub__())
print(Calculator(x,y).__mul__())
print(Calculator(x,y).__truediv__())