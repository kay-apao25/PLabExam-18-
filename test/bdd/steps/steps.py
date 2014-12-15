from lettuce import *
from nose.tools import assert_equal, assert_in
from webtest import TestApp
from score_app.tscores import Scores
from score_app.score_app import APP, SCORE

@step(u'Given I visit the application')
def given_i_visit_the_application(step):
    world.browser = TestApp(APP)
    world.response = world.browser.get('http://localhost:5000/')
    assert_equal(world.response.status_code, 200)
    SCORE.add_initial_score()

@step(u'When I enter the team "([^"]*)" of score "([^"]*)"')
def when_i_enter_the_team_group1_of_score_group2(step, team, score):
    form = world.response.forms['score-form']
    form['team'] = team
    form['dscore'] = score
    world.form_response = form.submit()
    SCORE.add_score(team, score)
    assert_equal(world.form_response.status_code, 200)

@step(u'And when I enter the team "([^"]*)" of score "([^"]*)"')
def when_i_enter_the_team_group1_of_score_group2(step, team, score):
    form = world.response.forms['score-form']
    form['team'] = team
    form['dscore'] = score
    world.form_response = form.submit()
    SCORE.add_score(team, score)
    assert_equal(world.form_response.status_code, 200)

@step(u'Then there score will be updated to "([^"]*)" and "([^"]*)"')
def then_there_score_will_be_updated_to_group1_and_group2(step, s1, s2):
    assert_equal(SCORE.get_score('team1'), int(s1))
    assert_equal(SCORE.get_score('team2'), int(s2))
    