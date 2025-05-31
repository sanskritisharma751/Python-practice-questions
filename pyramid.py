def pyramid(n):
# i=1 for 1 to 5
    for i in range(1,n+1):
#for j=1 , 5-1 = 4
     for j in range(n-i):
         print(" ",end="")
# k=1 for 1 to 2
     for k in range(1,i*2):
         print("*",end="")
     print()

pyramid(5)
