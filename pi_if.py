def Discrimination(num):
    if num == 3.14:
        print(num, "is pi")
    elif num > 3.14:
        print(num, "is bigger than pi")
    else:
        print(num, "is smaller than pi")


input = float(input("Enter a number: "))
Discrimination(input)
