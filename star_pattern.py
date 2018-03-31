# -*- coding: utf-8 -*-
"""
Created on Sat Mar 31 14:47:50 2018

@author: User
"""
#pattern 1
num = 1
for i in range(1,5):
    for j in range(i):
        print(num," ",end="")
        num = num + 1
    print('\r')

#pattern 2
for i in range(1,6):
    for j in range(i):
        print(i," ",end="")
      
    print('\r')

#pattern 3
for i in range(1,6):
    for j in range(1,i+1):
        print(j," ",end="")
      
    print('\r')
