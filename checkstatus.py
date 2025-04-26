class checkstatus:
    def checkstatus(self,a,b,flag):
        if (a>=0 and b<0 and flag==False) or (a<0 and b<=0 and flag==True) or (a>0 and b>0 and flag==False):
            return True
        else:
            return False

a=int(input("enter your number"))
b=int(input("enter your number"))
flag=bool(input("enter your flag"))
checkstatus(a,b,flag)