from art import logo, vs
from game_data import data
import random

celebrity_A = random.choice(data)
celebrity_B = random.choice(data)

play_game = True

def game():
  while play_game:
    print(logo)
    
    print(f"Compare A: {celebrity_A['name']}, a {celebrity_A['description']} from {celebrity_A['country']}")
    
    print(vs)
    
    print(f"Against B: {celebrity_B['name']}, a {celebrity_B['description']} from {celebrity_B['country']}")
    
    choice = input("Who has more followers? Type 'A' or 'B': ").lower() 

game()

