#!/usr/bin/python3
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

#Write your code below this line 👇

images = [rock, paper, scissors]

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors"))

print(images[user_choice])
computer_choice = random.randint(0,2)
print(images[computer_choice])

if user_choice < 0 or user_choice >= 3:
  print("You have entered invalid number")
elif user_choice == 0 and computer_choice == 2:
  print("You win")
elif user_choice == 1 and computer_choice == 0:
  print("You win")
elif user_choice == 2 and computer_choice == 1:
  print("You win")
elif computer_choice == 0 and user_choice == 2:
  print("You lose")
elif computer_choice == 1 and user_choice == 0:
  print("You lose")
elif computer_choice == 2 and user_choice == 1:
  print("You lose")
elif computer_choice == user_choice:
  print("You draw")
