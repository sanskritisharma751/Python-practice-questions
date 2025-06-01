# Rock Paper Scissors ASCII Art
import random
# Rock
print("Welcome to Rock,paper and scissors game!")
Rock1=("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")

# Paper
Paper1=("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")

# Scissors
Scissors1=("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")
Photos=[Rock1,Paper1,Scissors1]
Player1=["Rock","Paper","Scissors"]
Player1=random.choice(Player1)
#print(Player1)
Player2=input("Rock,Paper,Scissors?")
if Player1==Player2:
    print(f"DRAW,try again! Player1:{Player1}, Player2:{Player2}")
elif Player1=="Rock" and Player2=="Paper":
    print(f"Player2 wins! Player1:{Player1}",Photos[0],f"Player2:{Player2}",Photos[1])
elif Player2=="Rock" and Player1=="Paper":
    print(f"Player1 wins! Player1:{Player1}",Photos[0], f"Player2:{Player2}",Photos[1])
elif Player1=="Rock" and Player2=="Scissors":
    print(f"Player2 wins! Player1:{Player1}",Photos[0], f"Player2:{Player2}",Photos[2])
elif Player2=="Paper" and Player1=="Scissors":
    print(f"Player1 wins! Player2:{Player2}",Photos[1], f"Player1:{Player1}",Photos[2])
elif Player1=="Scissors" and Player2=="Rock":
    print(f"Player2 wins! Player1:{Player1}",Photos[2], f"Player2:{Player2}",Photos[0])
elif Player1=="Rock" and Player2=="Scissors":
    print(f"Player1 wins! Player2:{Player2}",Photos[0], f"Player1:{Player1}",Photos[2])



