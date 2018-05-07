#!C:\Users\User\AppData\Local\Programs\Python\Python37\python
from random import choice

players = []

file = open('player.txt','r')
players = file.read().splitlines()
print('Choose Player from :',players)

team1 = []
team2 = []

while len(players) > 0:
  player_choice1 = input("Select Your Player FromAabove List: ")
  print("Your Choice is:", player_choice1)
  team1.append(player_choice1)
  players.remove(player_choice1)
  print('Player Left :', players)
  
  player_choice2 = choice(players)
  print("Computer Choice is:", player_choice2)
  team2.append(player_choice2)
  players.remove(player_choice2)
  print('Player Left :', players)
  
print('Your Team:', team1)
print('Computer Team:', team2)