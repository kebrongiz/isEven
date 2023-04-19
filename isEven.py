def isEven(num):
    return num % 2 == 0


x = int(input("Enter an integer: "))
result = isEven(x)
print(f"{x} is{'' if isEven(x) else ' not'} even")
