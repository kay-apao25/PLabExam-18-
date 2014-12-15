class Scores(object):
    def __init__(self):
        self.scores = {}
    
    def add_initial_score(self):
        self.scores['team1'] = 0
        self.scores['team2'] = 0

    def add_score(self, team, score):
        self.scores[team] = int(self.scores.get(team)) + int(score)

    def get_score(self, team):
    	return self.scores.get(team)



