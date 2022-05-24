"""
This game uses the free CurrencyConverter api, to get the conversion rate between USD and ILS.
The object of the game is to show the user a random number in the range 1 to 100,
and ask him to write down how much he thinks the value displayed from USD to ILS.
Depending on the difficulty level selected, the correct value will be within an interval range around the correct result.
If the user correctly guessed the value of USD to ILS,
it will be printed that he succeeded and in addition the score will be added to the score file.
If the user does not guess the value of USD to ILS correctly,
it will be printed that he failed and better luck next time.
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


