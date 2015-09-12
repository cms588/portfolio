#!/usr/bin/env python

import sys

#Time class
#contains total number of seconds
class Time(object):
	def __init__(self, totalSeconds):
		self.totalSeconds = totalSeconds

	#printTime - prints the Time object with either the 24hour clock or the 12 hour clock
	#type of clock to use is specified by timeType parameter (1=24hour, 2=12hour)
	#return the printed time (for testing purposes)
	def printTime(self, timeType):
		totalSec = self.totalSeconds
		#formulas to calculate hours, minutes and seconds from seconds
		hours = totalSec / 3600
		minutes = (totalSec % 3600) / 60
		seconds = totalSec % 60
		if timeType == 1 and totalSec >= 0:
			hours = hours%24
			return str(hours).zfill(2) + ":" + str(minutes).zfill(2) + ":" + str(seconds).zfill(2)
		elif timeType == 2  and totalSec >= 0:
			ampm = hours/12
			hours = hours%12
			#calculate whether the time specified is am or pm for the 12hour clock
			if ampm%2 == 0:
				timeDay = "am"
			else:
				timeDay = "pm"
			return str(hours%12).zfill(2) + ":" + str(minutes).zfill(2) + ":" + str(seconds).zfill(2) + timeDay
		else:
			print 'The time type input must be either "1" (12 hour clock) or "2" (24 hour clock).'
			sys.exit()

	#addSeconds - adds time to the clock
	def changeSeconds(self, numSeconds):
		INCREMENT_ONE = 1
		#for positive input, add to time
		if(numSeconds > 0):
			i = 1
			while i <= numSeconds:
				self.totalSeconds += INCREMENT_ONE
				i += INCREMENT_ONE
		#for negative input, subtract from time
		elif(numSeconds < 0):
			i = -1
			while i >= numSeconds:
				self.totalSeconds -= INCREMENT_ONE
				i -= INCREMENT_ONE

#calculateSeconds - hours, minutes and seconds are input
#return - number of seconds that are in the input hours, minutes and seconds
def calculateSeconds(inputHour, inputMinute, inputSecond):
	HOUR = 3600
	MINUTE = 60
	SECOND = 1
	totalSecondsToAdd = HOUR*inputHour + MINUTE*inputMinute + SECOND*inputSecond

	return totalSecondsToAdd
