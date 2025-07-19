print("Welcome to the tip calculator!\n")
bill=float(input("What is your total bill? $"))
tip=int((input("How much tip you would like to give? 10, 12, or 15? ")))
peoples=int(input("How many people are there?"))
share=(bill+tip)/peoples
rounds=round(share,2)
print("each person should pay:$",f"{rounds:.2f}")

