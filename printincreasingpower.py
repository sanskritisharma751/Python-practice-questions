def increasingpower(n):
    i=1
    while(i*i<n+1):
        print(i*i,end=' ')
        i=i+1

increasingpower(int(input("enter num")))