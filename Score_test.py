"""
A package that is in charge of managing the scores file.
The scores file at this point will consist of only a number. That number is the accumulation of the
winnings of the user. Amount of points for winning a game is as follows:
POINTS_OF_WINNING = (DIFFICULTY X 3) + 5
Each time the user is winning a game, the points he won will be added to his current amount of
point saved in a file.
Methods
    1.  add_score - The function’s input is a variable called difficulty. The function will try to read
        the current score in the scores file, if it fails it will create a new one and will use it to save
        the current score.
"""


from Live_test import *
from Utils_test import Utils


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
