"""
The purpose of memory game is to display an amount of random numbers to the users for 0.7
seconds and then prompt them from the user for the numbers that he remember. If he was right
with all the numbers the user will win otherwise he will lose.
"""

from Live import dif_sel
from time import sleep
import random

# listlen = 0
difficulty = 1
generate_sequence = []      # Will generate a list of random numbers between 1 to 101. The list length will be difficulty
get_list_from_user = []     # Will return a list of numbers prompted from the user. The list length will be in the size of difficulty


if difficulty == 1:
    listlen = 3
elif difficulty == 2:
    listlen = 6
elif difficulty == 3:
    listlen = 9
elif difficulty == 4:
    listlen = 12
elif difficulty == 5:
    listlen = 15

def rand_num():
   gen_list = random.sample(range(1, 101), listlen)    # create a list of random numbers without duplicates
   generate_sequence.extend(gen_list)
   for num in generate_sequence:
       print('\r', num, sep='', end='')
       sleep(1)    # changed to 1 sec instead of 0.7

rand_num()
print(generate_sequence)
# while True:
#     try:
#         for i in range(listlen):
#             get_num = int(input(f'\rplease enter {listlen} numbers from memory, as appeared before: '))
#             get_list_from_user.append(get_num)
#     except ValueError:
#         print("\nSorry, please enter numbers only.\n")
#         continue
#     else:
#         break
#
# print(f'Game Numbers: {generate_sequence}')
# print(f'Your Numbers: {get_list_from_user}')
#
#
# def is_list_equal(generate_sequence, get_list_from_user):        # function to compare two lists if they are equal. The function will return True / False
#     generate_sequence.sort()
#     get_list_from_user.sort()
#     if generate_sequence == get_list_from_user:
#         return 'Your numbers are Equal, good memory'
#     else:
#         return 'Sorry, your numbers are Not Equal, better luck next time'
#
#
# print(is_list_equal(generate_sequence, get_list_from_user))

# def play():                 # Will call the functions above and play the game. Will return True / False if the user lost or won


