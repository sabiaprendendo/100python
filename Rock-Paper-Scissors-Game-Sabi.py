import random

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

game_images = [rock, paper, scissors]

user_choice = int(input("Hey! Let's play Rock, Paper, Scissors! What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
print(game_images[user_choice])

computer_choice = random.randint(0, 2)
print("Computer chose:")
print(game_images[computer_choice])

if user_choice >= 3 or user_choice < 0: 
  print("You typed an invalid number, you lose! Why'd do that?") 
elif user_choice == 0 and computer_choice == 2:
  print("Nice! You win!")
elif computer_choice == 0 and user_choice == 2:
  print("You lose. Better luck next time!")
elif computer_choice > user_choice:
  print("You lose. Better luck next time!")
elif user_choice > computer_choice:
  print("Nice! You win!")
elif computer_choice == user_choice:
  print("Ohhh, It's a draw. Let's try again!")

