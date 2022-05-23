"""
This game will use the free currency api to get the current exchange rate from USD to ILS, will
generate a new random number between 1-100 and will ask the user what he thinks is the value of
the generated number from USD to ILS, depending on the user’s difficulty his answer will be
correct if the guessed value is between the interval surrounding the correct answer
"""
from time import sleep
import random
from currency_converter import CurrencyConverter
from Live_test import *
from data.Score_test import Score


class CurrencyRouletteGame:

    def __init__(self):
        # define the interval range for correct answer
        self.LOW = 0
        self.HIGH = 0
        # current exchange rate from USD to ILS
        self.CURRENCY = 0
        # generate a new random number between 1-100
        self.RANDOM = random.randint(1, 100)
        # get input guess number from user
        self.GUESS_VALUE = 0

    # current exchange rate from USD to ILS
    def current_exchange(self):
        return CurrencyConverter().convert(self.RANDOM, 'USD', 'ILS')

    # game play method
    def play(self):
        self.CURRENCY = self.current_exchange()
        print(f'{Live.NAME} Welcome to Currency Roulette - try and guess the value of a random amount of USD in ILS')
        sleep(3)
        print('Get ready to play')
        sleep(2)

        # get input guess number from user
        print(f'\rplease guess the value of {self.RANDOM} USD in ILS: ')
        self.GUESS_VALUE = Utils.input_check(1000)
        self.LOW = (self.CURRENCY - (18 - Live.GAME_DIFF))
        self.HIGH = (self.CURRENCY + (18 - Live.GAME_DIFF))

        # check if guess value is in range
        if self.LOW <= self.GUESS_VALUE <= self.HIGH:
            print(f'The actual value of {self.RANDOM} USD in ILS is {self.CURRENCY}', end='')
            print("\nVery good, you are correct.\n")
            Score.add_score()
        else:
            print(f'The actual value of {self.RANDOM} USD in ILS is {self.CURRENCY}', end='')
            print("\nSorry, better luck next time.\n")


