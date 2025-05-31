def alphapyrmd(n,a):
 for i in range(1,n+1):
    for k in range(n-i):
        print(" ",end="")
    for j in range(2*i-1):
         if j==0:
            print(chr(a),end="")
         else:
             print(chr(a),end="")
             a+=1
    print()

n=int(input("enter number:"))
a=int(input("enter alpha:"))
alphapyrmd(n,a)