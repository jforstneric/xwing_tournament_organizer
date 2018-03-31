#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#Jure Forstneric
#jforst at google's email service
#2018-03-18

from random import shuffle
from operator import itemgetter


def addParticipants():
	allParticipants = []
	participantNumber = 1
	while True:
		print('Enter participant #' + str(participantNumber) + ': (or press enter to finish adding participants...)')
		participant = str(input())
		if participant == "":
			print('Our participants are:')
			for p in allParticipants:
				print(str(p[0]))
			if len(allParticipants) % 2 != 0:		#if list of participants == odd, add a bye
				allParticipants.append(['Bye',0,0])
			break
		allParticipants.append([participant,0,0])
		participantNumber += 1
	return(allParticipants)		#a list with participant's names
	
def printMatches(sortedList):
	for p in range(0,len(sortedList),2):
		print(sortedList[p][0] + ' plays ' + sortedList[(p+1)][0])
	print()
	print('Press enter to accept or \'m\' to manually enter new pairings...')
	print()
	acceptSorting = str(input())
	if acceptSorting == 'm' or acceptSorting == 'M':
		newSort = manualMatching(sortedList)
		return(newSort)
	else:
		return(sortedList)
	
def exportMatches(currentRound, sortedList):
	tournament = open('tournament_export.txt', 'a')
	tournament.write('The matches in round ' + str(currentRound) + ':\n')
	for p in range(0,len(sortedList),2):
		tournament.write(sortedList[p][0] + ' plays ' + sortedList[p+1][0] + '\n')
	tournament.write('\n')
	tournament.close()
		
def exportStandings(currentStandings):
	tournament = open('tournament_export.txt', 'a')
	tournament.write('The current standings are:\n')
	for p in currentStandings:
		tournament.write(p[0] + ' with ' + str(p[1]) + ' points and a MOV of ' + str(p[2]) + '\n')
	tournament.write('\n')
	tournament.close()
	
def otherSorting(sortedList):
	sortedList = sorted(sortedList, key=itemgetter(1,2), reverse=True)		#double sort with itemgetter - first by sortedList[1] then by sortedList[2]
	return(sortedList)
	
def manualMatching(sortedList):
	newSort = []
	while len(sortedList) > 1:
		newSort.append(sortedList[0])
		print('Who will play against ' + sortedList[0][0] + '?')
		del sortedList[0]
		for p in range(len(sortedList)):
			print(str(p+1) + ' ' + str(sortedList[p][0]))
		opponentChoice = int(input()) - 1
		newSort.append(sortedList[opponentChoice])
		del sortedList[opponentChoice]
	return(newSort)
		
def scoreMatches(sortedList):
	for p in range(0,len(sortedList),2):
		print('Enter ' + sortedList[p][0] + '\'s score in ship points (max. 100):')
		playScore1 = int(input())
		print('Enter ' + sortedList[p+1][0] + '\'s score in ship points (max. 100):')
		playScore2 = int(input())
		if playScore1 == playScore2:			#in case of tie
			sortedList[p][1] = (sortedList[p][1] + 1)
			sortedList[p][2] = (sortedList[p][2] + 100)
			sortedList[p+1][1] = (sortedList[p+1][1] + 1)
			sortedList[p+1][2] = (sortedList[p+1][2] + 100)
		elif (1 <= abs(playScore1 - playScore2)) and (abs(playScore1 - playScore2) < 12):		#in case of modified win
			if playScore1 > playScore2:
				sortedList[p][1] = (sortedList[p][1] + 3)
				sortedList[p][2] = (sortedList[p][2] + (100 + (playScore1 - playScore2)))
				sortedList[p+1][2] = (sortedList[p+1][2] + (100 - (playScore1 - playScore2)))
			else:
				sortedList[p+1][1] = (sortedList[p+1][1] + 3)
				sortedList[p+1][2] = (sortedList[p+1][2] + (100 + (playScore2 - playScore1)))
				sortedList[p][2] = (sortedList[p][2] + (100 - (playScore2 - playScore1)))
		else:			#normal win
			if playScore1 > playScore2:
				sortedList[p][1] = (sortedList[p][1] + 5)
				sortedList[p][2] = (sortedList[p][2] + (100 + (playScore1 - playScore2)))
				sortedList[p+1][2] = (sortedList[p+1][2] + (100 - (playScore1 - playScore2)))
			else:
				sortedList[p+1][1] = (sortedList[p+1][1] + 5)
				sortedList[p+1][2] = (sortedList[p+1][2] + (100 + (playScore2 - playScore1)))
				sortedList[p][2] = (sortedList[p][2] + (100 - (playScore2 - playScore1)))
	return(sortedList)
	
def printStandings(allParticipants):
	for p in allParticipants:
		print(p[0] + ' with ' + str(p[1]) + ' points and a MOV of ' + str(p[2]))
	print()
	

if __name__ == '__main__':
	allParticipants = addParticipants()
	print('How many rounds are we playing today?')
	playRounds = int(input())
	shuffle(allParticipants)
	#this is looped for the number of rounds:
	for r in range(playRounds):
		allParticipants = printMatches(allParticipants)
		exportMatches(r, allParticipants)
		postScoring = scoreMatches(allParticipants)
		allParticipants = otherSorting(postScoring)
		exportStandings(allParticipants)
		print()
		print('The current standings are:')
		printStandings(allParticipants)
	print('Tournament finished!')
	print('Congratulations to ' + allParticipants[0][0] + ' for the win!')
	
	


