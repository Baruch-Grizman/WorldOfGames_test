"""
This file is responsible for reading the score file and publishing it to HTTP using HTML,
this process will be done using Python FLASK library.
In the event of an error in reading the score file, the error code we defined will be displayed.
"""

from flask import Flask, render_template
from data.Utils_test import Utils
import os

template_dir = os.path.abspath('../templates')

app = Flask('MainScores', template_folder=template_dir)


@app.route('/')
def read_score():
    try:
        with open(Utils.SCORES_FILE_NAME, encoding='utf-8') as read_file:
            score = read_file.read()
            return render_template('wogmainscores.html', SCORE=score)
    except:
        return render_template('wogmainscores-error.html', ERROR=Utils.BAD_RETURN_CODE)


if __name__ == '__main__':
    app.run(debug=True)

