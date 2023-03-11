import random

def get_choices():
  player_choice = input("Enter a choice (rock, paper, scissors): ")
  options = ["rock", "paper", "scissors"]
  computer_choice = random.choice(options)
  choices = {"player": player_choice, "computer": computer_choice}
  return choices

def check_win(choices):
  player_choice,computer_choice = choices["player"], choices["computer"]
  if player_choice == computer_choice: return "tie"
  return ("computer wins") if (player_choice == "rock" and computer_choice == "paper") or (player_choice == "paper" and computer_choice == "scissors") or (player_choice == "scissors" and computer_choice == "rock") else ("player_wins")
  
choice = get_choices()
print(choice)
print(check_win(choice))