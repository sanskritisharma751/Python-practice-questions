import time
timestamp=time.strftime('%H:%M:%S')
#timestamp=int(input("enter time:"))
print(timestamp)

if timestamp<='11:59:59':
    print("Good morning")
elif timestamp>='11:59:59':
    print("Good afternoon")
elif timestamp>='16:30:59':
    print("Good evening")
elif timestamp>='21:00:00':
    print("Good night")
