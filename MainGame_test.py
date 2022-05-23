"""
The purpose of this file is to call the functions from Live.py
"""

from Live_test import *
from games.GuessGame_test import GuessGame
from games.MemoryGame_test import MemoryGame
from games.CurrencyRouletteGame_test import CurrencyRouletteGame
from data.Utils_test import Utils

# call the functions from Live.py
print(Live.welcome())
Live.load_game()

# Launch game based on user selection
if Live.GAME == 1:
    Utils.screen_cleaner()
    MemoryGame = MemoryGame()
    MemoryGame.play()
elif Live.GAME == 2:
    Utils.screen_cleaner()
    GuessGame = GuessGame()
    GuessGame.play()
elif Live.GAME == 3:
    Utils.screen_cleaner()
    CurrencyRouletteGame = CurrencyRouletteGame()
    CurrencyRouletteGame.play()

