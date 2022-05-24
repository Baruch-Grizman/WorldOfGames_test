"""
The object of the game is to display a quantity (the quantity is based on the difficulty level,
selected in the initial stage) of random numbers in the range from 1 to 101, for 1.5 seconds.
The user will then be prompted to enter the numbers based on the memory.
At the end both the numbers displayed and the numbers guessed will be displayed.
If the user was right and remembered all the numbers,
it will be printed that he succeeded and in addition the score will be added to the score file
If the user made a mistake and did not remember all the numbers,
it will be printed that he failed and better luck next time
"""

from time import sleep
import random
from Live_test import *
from data.Score_test import Score


class MemoryGame:
    def __init__(self):
        # Will generate a list of random numbers from 1 to 101. The list length will be difficulty
        self.GENERATE_SEQUENCE = []
        # Will return a list of numbers prompted from the user. The list length will be in the size of difficulty
        self.GET_LIST_FROM_USER = []
        # input number from user
        self.GET_NUMBER = 0

    def random_numbers(self):
        # create a list of random numbers without duplicates
        return random.sample(range(1, 101), Live.GAME_DIFF)

    # game play method
    def play(self):
        gen_list = self.random_numbers()
        self.GENERATE_SEQUENCE.extend(gen_list)
        print(f'{Live.NAME} Welcome to Memory Game - a sequence of numbers will'
              f' appear for 1.5 second and you have to guess it back')
        sleep(3)
        print('Get ready to play')
        sleep(2)
        for num in self.GENERATE_SEQUENCE:
            print('\r', 'Try to remember this numbers --> ', num, sep='', end=' <--')
            sleep(1.5)    # changed to 1.5 sec instead of 0.7

        # get input number from user
        for i in range(Live.GAME_DIFF):
            print(f'\rplease enter {Live.GAME_DIFF} numbers from memory from 1 to 101'
                  f', as appeared before: ')
            self.GET_NUMBER = Utils.input_check(101)
            self.GET_LIST_FROM_USER.append(self.GET_NUMBER)

        print(f'Game Numbers: {self.GENERATE_SEQUENCE}')
        print(f'Your Numbers: {self.GET_LIST_FROM_USER}')

        # compare two lists if they are equal.
        if sorted(self.GENERATE_SEQUENCE) == sorted(self.GET_LIST_FROM_USER):
            print('Your numbers are Equal, good memory')
            Score.add_score()
        else:
            print('Sorry, your numbers are Not Equal, better luck next time')

