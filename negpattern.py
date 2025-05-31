n= int(input("enter number:"))

for i in range(n,0,-1):
 a=[]
 for j in range(i,0,-1):
     print(j,sep=" ",end=" ")
     a.append(i)
     if i>=j and j>1:
         print('+',sep=" ",end=" ")
 print('=',sum(a))