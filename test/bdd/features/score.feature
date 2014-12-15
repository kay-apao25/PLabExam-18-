Feature: An application that is able to the record the scores of two playing teams in basketball

	As a user I want to know the scores of the teams after each shoot of a player

	Scenario Outline: Record the score of the first team
	Given team 1 is playing against team 2
	When a player of team 1 got a shot point
	Then there score will be updated