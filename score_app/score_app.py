"""DOCSTRING"""
from flask import Flask, render_template, request
from tscores import Scores

APP = Flask(__name__)
SCORE = Scores()

@APP.route('/')
def hello_world():
    """Takes the information from the score form in index.html"""
    team = request.args.get('team')
    dscore = request.args.get('dscore')
    SCORE.add_initial_score()
    score1 = SCORE.get_score('team1')
    score2 = SCORE.get_score('team2')
    return render_template('index.html', score1=score1, score2=score2)

if __name__ == '__main__':
    APP.run(debug=True)
