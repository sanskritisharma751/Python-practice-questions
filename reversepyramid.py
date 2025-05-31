def revpyramid(n):
# i = 5 in range from 5 to 0
    for i in range(n,0,-1):
#j = 5 in range from 5-5=0
#i=4 then n=5 so n-i=1
      for j in range(n-i):
          print(" ",end=" ")
      for k in range(i*2-1):
          print("*",end=" ")
      print()
revpyramid(5)