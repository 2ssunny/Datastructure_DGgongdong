def number(num):
    if num < 10:
        return "one digit number"
    elif num < 100 and num >= 10:
        return "two digit number"
    else:
        return "three digit number or bigger than three digit"


x = int(input("Input Number: "))
y = number(x)
print(y)
