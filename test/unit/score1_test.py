import unittest
from score_app.tscores import Scores

class TestAccount(unittest.TestCase):

    def test_if_initial_score_is_zero(self):
        scores = Scores()
        scores.add_initial_score()

        self.assertEqual(scores.get_score('team1'), 0)
        self.assertEqual(scores.get_score('team2'), 0)

    def test_if_score_of_teams_are_recorded(self):
        scores = Scores()
        scores.add_initial_score()

        scores.add_score('team1', 2)
        scores.add_score('team2', 2)

        self.assertEqual(scores.get_score('team1'), 2)
        self.assertEqual(scores.get_score('team2'), 2)

    def test_if_i_added_score_is_update(self):
        scores = Scores()

        scores.add_initial_score()

        scores.add_score('team1', 2)
        scores.add_score('team2', 2)

        scores.add_score('team1', 3)
        scores.add_score('team2', 0)

        self.assertEqual(scores.get_score('team1'), 5)
        self.assertEqual(scores.get_score('team2'), 2)


if __name__ == '__main__':
    unittest.main()