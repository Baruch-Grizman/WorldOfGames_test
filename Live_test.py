"""
this program is for getting inputs for WorldOfGames, includes name, game, difficulty
"""

from Utils_test import Utils


class Live:

    def __init__(self):
        self.NAME = input('Please enter your name: ')
        self.GAME = 0           # game selection
        self.DIFFICULTY = 0     # difficulty selection
        self.GAME_DIFF = 0      # in game difficulty for all games

    def welcome(self):
        return f'Hello {Live.NAME} and welcome to the World of Games (WoG).' \
               f'\nHere you can find many cool games to play.\n'

    # getting inputs for WorldOfGames
    def load_game(self):
        # game selection
        print("""Our Games:
    1. Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back
    2. Guess Game - guess a number and see if you choose like the computer
    3. Currency Roulette - try and guess the value of a random amount of USD in ILS

    Please choose a game number to play: """)
        self.GAME = Utils.input_check(3)

        # difficulty selection
        print('Please choose game difficulty from 1 to 5: ')
        # check if entered numbers only
        self.DIFFICULTY = Utils.input_check(5)

        # settings in game difficulty for all games
        if self.DIFFICULTY == 1:
            self.GAME_DIFF = self.DIFFICULTY*3
        elif self.DIFFICULTY == 2:
            self.GAME_DIFF = self.DIFFICULTY*3
        elif self.DIFFICULTY == 3:
            self.GAME_DIFF = self.DIFFICULTY*3
        elif self.DIFFICULTY == 4:
            self.GAME_DIFF = self.DIFFICULTY*3
        elif self.DIFFICULTY == 5:
            self.GAME_DIFF = self.DIFFICULTY*3


Live = Live()
