"""
rock ,paper, scissors game
"""

from random import randint
from time import sleep

options = ["ROCK","PAPER","SCISSORS"]
message = {
  "key" : "Yawn it's  a tie",
  "won" : "Yay you have won",
  "lost" : "Aww you lost !"
}

#this functions decides the winner
def decide_winner(user_choice, computer_choice):
  print "Your choice is %s :" %(user_choice)
  sleep(3)
  print "The computer choice is %s :" %(computer_choice)
  sleep(3)
  
  if user_choice == computer_choice:
    print message['tie']
  elif user_choice == options[0] and computer_choice == options[2]:
    print message["won"]
  elif user_choice == options[1] and computer_choice == options[0]:
    print message["won"]
  elif user_choice == options[2] and computer_choice == options[1]:
    print message["won"]
  else:
    print message["lost"]

