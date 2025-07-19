import random

print("welcome to black jack game".upper())

cards=[11,0,2,3,4,5,6,7,8,9,10,10,10,10]

def deal_cards():
    card= random.choice(cards)
    return card

def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) >21:
        cards.remove(11)
        cards.append(1)
    cards_score=sum(cards)
    return cards_score

computer_cards=[]
player_cards=[]
computer_score=0
player_score=0

def compare(computer_score,player_score):
    if computer_score==player_score:
        print("It's a draw:|")
    if 0 in computer_cards:
        print("computer has black jack.User wins:)")
    if 0 in player_cards:
        print("player has black jack.User wins:)")
    if player_score > 21:
        print("You bust.Computer wins!")
    if computer_score > 21:
        print("You wins!.Computer bust!")
    if 21>player_score > computer_score:
        print(f"Player wins!.:)")
    if 21>computer_score > player_score:
        print(f"Computer wins!:(")
    print(f"computer cards: {computer_cards},computer score: {computer_score}. "
          f"Player cards: {player_cards},player score: {player_score}")
def play_game():
 game_over=False
 while not game_over:
  for i in range(2):
     computer_cards.append(deal_cards())
     player_cards.append(deal_cards())
  print(f"computer first card {computer_cards[0]}")
  print(f"Player cards {player_cards}")
  computer_score=calculate_score(computer_cards)
  player_score=calculate_score(player_cards)
  if computer_score==0 or player_score==0 or player_score >21:
     game_over=True
  else:
     player_turn = input("you want another card? Hit/stand")
     if player_turn == "hit":
        player_cards.append(deal_cards())
        player_score=calculate_score(player_cards)
        print(player_cards)
     else:
         game_over=True
  while computer_score!=0 and computer_score<17:
        computer_cards.append(deal_cards())
        computer_score=calculate_score(computer_cards)
  compare(computer_score,player_score)
  game_over=True

user=input("You want to play game of blackjack type y/n").lower()
if user == "y":
    play_game()




