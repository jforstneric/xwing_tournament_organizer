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
		print('Enter participant #' + str(participantNumber) + ': (or press enter to continue...)')
		participant = str(input())
		if participant == "":
			print('Our participants are:')
			for p in allParticipants:
				print(str(p[0]))
			if len(allParticipants) % 2 != 0:		#if list of participants == odd, add a bye
				allParticipants.append(['Bye',0,0])
			break
		allParticipants.append([participant,0,0])
		print('Our participants are:')
		for p in allParticipants:
			print(str(p[0]))
		participantNumber += 1
	return(allParticipants)		#a list with participant's names
	
def firstSort(allParticipants):
	shuffle(allParticipants)
	print('List after random shuffle:')
	print(allParticipants)
	return allParticipants
	
def printMatches(sortedList):
	for p in range(0,len(sortedList),2):
		print(sortedList[p][0] + ' plays ' + sortedList[(p+1)][0])
		
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
		if 1 <= abs(playScore1 - playScore2) < 12:		#in case of modified win (difference in MOV < 12
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
	print(sortedList)
	return(sortedList)
	
def otherSorting(sortedList):
	sortedList = sorted(sortedList, key=itemgetter(1,2), reverse=True)		#double sort with itemgetter - first by sortedList[1] then by sortedList[2]
	return(sortedList)
	

if __name__ == '__main__':
	allParticipants = addParticipants()
	print('How many rounds are we playing today?')
	playRounds = int(input())
	sortedList = firstSort(allParticipants)
	printMatches(sortedList)
	#this should be looped for the number of rounds:
	for r in range(playRounds):
		postScoring = scoreMatches(sortedList)
		sortedList = otherSorting(postScoring)		#here we should show the list to the user and ask if they want to manually assign pairs!
		printMatches(sortedList)
	
	


