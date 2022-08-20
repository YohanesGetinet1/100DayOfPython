#!/usr/bin/python3

import random
from game_data import data
from art import logo , vs
from replit import clear
print(logo)
score = 0
Account_B = random.choice(data)

game_continue =True
while game_continue:
  Account_A = Account_B
  Account_B = random.choice(data)
  
  while Account_A == Account_B:
    B = random.choice(data)
  
  def account_detail(Account):
    account_name = Account["name"]
    account_description = Account["description"]
    account_country = Account["country"]
    return f"{account_name}, a {account_description}, from {account_country}"


  def answer_checker(guess,follower_count_A,follower_count_B):
    if follower_count_A > follower_count_B :
      return guess == "a"
    else:
      return guess == "b"

  print(f"compare A : {account_detail(Account_A)}")
  print(vs)
  print(f"Against B : {account_detail(Account_B)}")

  guess = input("Who has more followers? Type 'A' or 'B':").lower()
  follower_count_A = Account_A["follower_count"]
  follower_count_B = Account_B["follower_count"]

  is_answer_correct = answer_checker(guess,follower_count_A,follower_count_B)
  clear()
  print(logo)
  if is_answer_correct:
    score += 1
    print(f"You're right! current score {score}")
  else:
    game_continue = False
    print(f"That's wrong. final score is {score}.")


