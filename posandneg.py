# {
# Driver Code Starts
# Initial Template for Python 3

# } Driver Code Ends

# User function Template for python3

def pos(n):
    ## Write the code
    if n == 0:
        print(n)
    ##while(n>0):
    ##    print(i,)
    if n > 0:
        for i in range(n - 1, -1, -1):
            print(i, end=' ')


def neg(n):
    ##Write the code
    if n < 0:
        for i in range(n, 1, 1):
            print(i, end=' ')


# {
# Driver Code Starts.


def main():
    testcases = int(input())  # testcases
    while (testcases > 0):
        n = int(input())
        if (n > 0):
            pos(n)
        elif (n < 0):
            neg(n)
        else:
            print("already Zero", end="")
        print()
        testcases -= 1

        print("~")


if __name__ == '__main__':
    main()
# } Driver Code Ends