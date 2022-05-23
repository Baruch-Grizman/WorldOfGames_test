"""
The purpose of guess game is to start a new game, cast a random number between 1 to a
variable called difficulty . The game will get a number input from the
"""

from time import sleep
import random
from Live_test import *
from data.Utils_test import Utils
from data.Score_test import Score


class GuessGame:

    def __init__(self):
        # define the range
        self.LOW = 1
        self.HIGH = Live.GAME_DIFF
        self.SECRET_NUMBER = 0
        self.USER_NUMBER = 0

    # Will generate number between 1 to difficulty and save it to self.SECRET_NUMBER.
    def generate_number(self):
        return random.randint(self.LOW, self.HIGH)

    # game play method
    def play(self):
        # generating the random number
        self.SECRET_NUMBER = self.generate_number()
        print(f'{Live.NAME} Welcome to Guess Game - guess a number and see if you choose like the computer')
        sleep(3)
        print('Get ready to play')
        sleep(2)
        print(f'Guess a number between {self.LOW} and {self.HIGH}')

        # get input guess number from user
        print('Enter the guessed number: ')
        self.USER_NUMBER = Utils.input_check(self.HIGH)

        # compare random (secret) number to user input number
        if self.SECRET_NUMBER == self.USER_NUMBER:
            print(f'The computer number was: {self.SECRET_NUMBER}')
            print(f'You Guessed correctly, Very Good!')
            Score.add_score()
        else:
            print(f'The computer number was: {self.SECRET_NUMBER}')
            print(f'Sorry, you Guessed incorrect, better luck next time')

