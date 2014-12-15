import unittest
from score_app.tscores import Scores

class TestAccount(unittest.TestCase):

    def test_if_score_of_teams_are_recorded(self):
        scores = Scores(2, 2)
        self.assertEqual(scores.scoret1, 2)
        self.assertEqual(scores.scoret2, 2)
        #self.assertEqual(account.balance, 50)

if __name__ == '__main__':
    unittest.main()