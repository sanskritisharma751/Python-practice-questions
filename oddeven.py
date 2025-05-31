def evenodd(x):
    if x%2==0:
        print(x,"is even.")
    elif x%2==1:
        print(x,"is odd.")
    else:
        print(x,"neither odd nor even")


evenodd(int(input("enter num")))