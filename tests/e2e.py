"""
this file is "end2end" test that will check if the scores.txt file is in range 1-1000
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
import os


def test_scores_service(url):
    webdriver_dir = os.path.abspath('../tests/chromedriver.exe')    # ver 103
    chrome_driver = webdriver.Chrome(executable_path=webdriver_dir)
    chrome_driver.get(url)
    score_read = chrome_driver.find_element(By.ID, 'score').text

    if 1 <= int(score_read) <= 1000:
        True
    else:
        False


def main_function():
    test_scores_service('http://127.0.0.1:5000/')
    if True:
        return exit(0)
    else:
        return exit(-1)


main_function()
