#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#Jure Forstneric
#jforst at google's email service
#2018-03-18

import random

def addParticipants():
	allParticipants = {}
	participantNumber = 1
	while True:
		print('Enter participant #' + str(participantNumber) + ': (or press enter to continue...)')
		participant = str(input())
		if participant == "":
			print('Our participants are:')
			for p in allParticipants:
				print(str(p))
			if len(allParticipants) % 2 != 0:
				allParticipants['Bye'] = [0,0]
			break
		allParticipants[participant] = [0,0]
		print('Our participants are:')
		for p in allParticipants:
			print(str(p))
		participantNumber += 1
	return(allParticipants)		#at the moment, this is a dictionary with the participant names as the keys and 0,0 as the values
	
def firstSort(allParticipants):
	sortingList = list(allParticipants)		#this changes the dictionary into a list with [name, 0, 0] as each value in the list
	

if __name__ == '__main__':
	allParticipants = addParticipants()
	print('Done with adding participants, they are:')
#	print(allParticipants)
	for p in allParticipants:
		print(str(p))
	firstSort(allParticipants)


