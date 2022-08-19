#!/usr/bin/python3

import random
from ascii_art import logo , logo2 ,logo3


print(logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100 ")
random_number = random.randint(1,100)

easy_level = 10
hard_level = 5

def difficulty_set():
  diff_level = input("Choose a difficulty . Type 'easy ' or 'hard' ").lower()
  if diff_level == "easy":
    return easy_level
  elif diff_level == "hard":
    return hard_level

def game():
  def answer_checker(user_choice, random_number,turns):
    if user_choice > random_number:
      print("Too high")
      print("Guess again")
      return turns - 1
    elif user_choice < random_number:
      print("Too low")
      print("Guess again")
      return turns - 1
    elif user_choice == random_number:
      print(f"You got it. The answer is {random_number}")
      print(logo3)

  turns = difficulty_set()

  user_choice = 0
  while user_choice != random_number:
    print(f"You have {turns} no of attempt to guess the correct number.")
    user_choice = int(input("Make a guess \n"))
    turns = answer_checker(user_choice , random_number, turns)
    if turns == 0:
      print("You've run out of guesses , You lose.")
      print(logo2)
      print(f"The correct answer is -> {random_number}")
      return
game()
