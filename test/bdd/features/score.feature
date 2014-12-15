Feature: An application that is able to the record the scores of two playing teams in basketball

	As a user I want to know the scores of the teams after each shoot of a player

	Scenario Outline: Record the scores of the team
	Given I visit the application 
	When I enter the team "team1" of score "2"
	And when I enter the team "team2" of score "2"
	Then there score will be updated to "2" and "2"