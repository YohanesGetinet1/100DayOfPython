#!/usr/bin/python3

from replit import clear
from art import logo
print(logo)

auction = {}
add_user = False

def highest_bid(record):
  highest_price = 0
  for bidder in record:
    bid_amount = record[bidder]
    if bid_amount > highest_price:
      highest_price = bid_amount
      winner = bidder
  print(f"The winner is {winner} with bid of ${highest_price}")

while not add_user:
  name=input("What is your name?:")
  bid=int(input("What is your bid?: $"))
  auction[name] = bid
  to_continue = input("Are there any other bidders? Type 'yes' or 'no'.\n")
  if to_continue == "no":
    add_user = True
    highest_bid(auction)
  elif to_continue == "yes":
    clear()
