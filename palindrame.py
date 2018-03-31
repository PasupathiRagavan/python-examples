# Program to check if a string
#  is palindrome or not

# change this value for a different output
my_str = input('Enter the String:')

# make it suitable for caseless comparison
my_str = my_str.casefold()

#check user input is string or integer
if my_str.isalpha():
   # reverse the stritestteatng
   rev_str = reversed(my_str)
   # check if the string is equal to its reverse
   if list(my_str) == list(rev_str):
       print("It is PALINDROME")
   else:
       print("It is NOT palindrome")   
elif my_str.isdigit():
   if my_str == str(my_str)[::-1]:
       print('The number is PALINDROME')
   else:
       print('The number is NOT a palindrome')

