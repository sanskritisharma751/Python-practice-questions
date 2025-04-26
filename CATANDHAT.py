def catandhat(str):
    if str.count('cat')== str.count('hat'):
        print(str.count('cat'),str.count('hat'))
        return True
    else:
        return False

catandhat(input("enter your string"))