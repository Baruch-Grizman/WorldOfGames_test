"""
This file contains variables and functions for general project use.
SCORES_FILE_NAME - A string representing “Scores.txt” file name. Used in the Score.py and MainScores.py files.
BAD_RETURN_CODE - A value that represents an error in case of a function error, Used in MainScores.py file.
screen_cleaner - Function to clear the screen when starting a new game.
input_check - Function that checks whether the inserted characters are only numbers,
and whether they are in the correct range, depending on the requirement in the various files.
"""

import os


class Utils:

    def __init__(self):
        self.SCORES_FILE_NAME = 'Scores.txt'
        self.BAD_RETURN_CODE = "-1: Score file is unreachable"

    def screen_cleaner(self):
        return os.system('cls' if os.name == 'nt' else 'clear')

    def input_check(self, high_range):
        while True:
            try:
                # game selection
                input_number = int(input())
            # check if entered numbers only
            except ValueError:
                print(f'*********************************'
                      f'\n**  Please enter numbers only  **'
                      f'\n*********************************')
                continue
            # check if entered numbers in valid range only
            if not 1 <= input_number <= high_range:
                print(f'**************************************'
                      f'\n**  Please choose from 1 to {high_range} only  **'
                      f'\n**************************************')
                continue
            else:
                return input_number


Utils = Utils()
