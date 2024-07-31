rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

import random
import os

clear = lambda: os.system('clear')

option = [rock, paper, scissors]
str_option = ["rock", "paper", "scissors"]
new_game = 'y'
while new_game == 'y':
    clear()
    choose = int(
        input(
            "What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors) "
        ))
    computer_choose = random.randint(0, 2)
    if choose == computer_choose:
        print(f"You choose {str_option[choose]} {option[choose]}")
        print(
            f"Computer choose {str_option[computer_choose]} {option[computer_choose]}"
        )
        print("You have a draw")
    elif choose == 0 and computer_choose == 1 or choose == 1 and computer_choose == 2 or choose == 2 and computer_choose == 0:
        print(f"You choose {str_option[choose]} {option[choose]}")
        print(
            f"Computer choose {str_option[computer_choose]} {option[computer_choose]}"
        )
        print("You lose")
    elif choose == 1 and computer_choose == 0 or choose == 2 and computer_choose == 1 or choose == 0 and computer_choose == 2:
        print(f"You choose {str_option[choose]} {option[choose]}")
        print(
            f"Computer choose {str_option[computer_choose]} {option[computer_choose]}"
        )
        print("You win")
    new_game = input("Do you want to play again? (Y/N) ").lower()


