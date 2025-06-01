import random
import string
n=int(input("enter how many letters you want in your password?\n"))
k=int(input("enter how many numbers you want in your password?\n"))
l=int(input("enter how many special characters you want in your password?\n"))
Password=[]
a=[]
for i in range(n):
    random_letter = random.choice(string.ascii_letters)  # Includes both uppercase and lowercase
    a.append(random_letter)
Password="".join(a)

for j in range(k):
    random_number = random.randint(0,n)
    a.append(str(random_number))
Password="".join(a)

for s in range(l):
    # Define a string of special characters
    special_characters = "!@#$%^&*()_+-=[]{}|;:',.<>?/"

    # Generate a random special character
    random_character = random.choice(special_characters)
    a.append(random_character)
random.shuffle(a)
Password="".join(a)

print(f"Your password is: {Password}")



