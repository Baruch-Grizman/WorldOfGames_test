"""
This file’s sole purpose is to serve the user’s score currently in the scores.txt file over HTTP with
HTML. This will be done by using python’s flask library.
"""

from flask import Flask, render_template
from data.Utils_test import Utils

app = Flask('MainScores')


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

