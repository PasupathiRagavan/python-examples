#!C:\Users\User\AppData\Local\Programs\Python\Python37\python
from random import randint

player = input('rock (r), paper (p) or scissors (s) ? ')

print(player, 'vs', end = ' ')

random_choose = randint(1,3)

if random_choose == 1:
  computer = 'r'
elif random_choose == 2:
  computer = 'p'
elif random_choose == 3:
  computer = 's'

print(computer)

if(player == computer):
  print('Draw')
elif(player == 'r' and computer == 's'):
  print('Player Win!!!')
elif(player == 'r' and computer == 'p'):
  print('Computer Win!!!')
elif(player == 'p' and computer == 'r'):
  print('Player Win!!!')
elif(player == 'p' and computer == 's'):
  print('Computer Win!!!')
elif(player == 's' and computer == 'r'):
  print('Player Win!!!')
elif(player == 's' and computer == 'p'):
  print('Player Win!!!')