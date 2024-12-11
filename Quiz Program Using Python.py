import random
def get_computer_choice():
  choices = ['rock', 'paper', 'scissors']
  return random.choice(choices)
def get_player_choice():
    pchoice = input("Enter your choice (rock/paper/scissors): ")
    while pchoice not in ['rock', 'paper', 'scissors']:
          pchoice = input("Invalid choice. Enter your choice (rock/paper/scissors):")
    return pchoice
def determine_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
      return "It's a tie !"
    elif (player_choice == 'rock' and computer_choice == 'scissors') or \
         (player_choice == 'scissors' and computer_choice == 'paper') or \
         (player_choice == 'paper' and computer_choice == 'rock'):
         return "Player wins"
    else:
         return "Computer wins"
def play_game():
    player_choice = get_player_choice()
    computer_choice = get_computer_choice()
    print("Player choose " + player_choice)
    print("Computer choose " + computer_choice)
    print(determine_winner(player_choice, computer_choice))
play_game()