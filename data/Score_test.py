"""
This file is responsible for keeping the user's score in case of a text file win.
The score is determined by a formula
POINTS_OF_WINNING = (DIFFICULTY X 3) + 5
If there is already a file with a score, the new score will be added to the existing one.
If no score file exists, a new file will be created.
"""


from Live_test import *
from data.Utils_test import Utils


class Score:

    def __init__(self):
        self.SCORE_DIFFICULTY = 0
        # self.SCORE_DIFFICULTY = 2   # hardcoded for self testing

    def add_score(self):
        self.SCORE_DIFFICULTY = Live.DIFFICULTY
        points_of_winning = self.SCORE_DIFFICULTY*3+5

        try:
            # try to open file, if not exist it will create a new one
            with open(Utils.SCORES_FILE_NAME, encoding='utf-8') as score_file:
                for line in score_file.readlines():     # reading current score from file
                    points_of_winning += int(line)      # adding new points of winning to current score
            with open(Utils.SCORES_FILE_NAME, 'w+', encoding='utf-8') as score_file:
                score_file.write(f'{points_of_winning}')    # writing the new sum score to file

        except:
            # if no score.txt file exist, creating new one
            with open('Scores.txt', 'w+', encoding='utf-8') as score_file:
                score_file.write(f'{points_of_winning}')    # writing the new score to file


Score = Score()
