while True:
    a=int(input("Enter the value of a="))
    b=int(input("Enter the value of b="))
    print("Choices:\n1.Add\n2.Subtract\n3.Multiply\n4.Divide\n5.Modular Division")
    x=int(input("Enter your choice:"))
    if x == 1:
        print(a+b)
    elif x == 2:
        print(a-b) 
    elif x == 3:
        print(a*b)
    elif x == 4:
        try:
            c=a/b
            print(c)
        except:
            print("Can't divide by zero")
    elif x == 5:
        try:
            c=a%b
            print(c)
        except:
            print("Can't divide by zero")
    else:
        print("Enter a valid choice")
        