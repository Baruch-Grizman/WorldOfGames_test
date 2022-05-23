"""
A general purpose python file. This file will contain general information and operations we need
for our game.
1. SCORES_FILE_NAME - A string representing a file name. By default “Scores.txt”
2. BAD_RETURN_CODE - A number representing a bad return code for a function.
3. Screen_cleaner - A function to clear the screen (useful when playing memory game or
before a new game starts).
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
