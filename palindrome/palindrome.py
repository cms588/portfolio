#!/usr/bin/env python

import random

#Generates random amount of "words", each with their own number of chars
#A random number of words to return is also random
#Any odd number for the return words is a palindrome, the other half are not
def generateRand():
	NUMARRWORDSLOW = 1
	NUMARRWORDSHIGH = 5
	WORDLENLOW = 1
	WORDLENHIGH = 20
	ZERO = '0'
	NINE = '9'
	CAPA = 'A'
	CAPZ = 'Z'
	A = 'a'
	Z = 'z'

	#input all possible usable characters into one list
	posibilitiesArr = []
	for i in range(0, ord(NINE)-ord(ZERO)+1):
		posibilitiesArr.append(chr(ord(ZERO)+i))
	for i in range(0, ord(CAPZ)-ord(CAPA)+1):
		posibilitiesArr.append(chr(ord(CAPA)+i))
	for i in range(0, ord(Z)-ord(A)+1):
		posibilitiesArr.append(chr(ord(A)+i))

	#the words that are 
	words = []
	#random number of words in each array
	wordsInArray = random.randint(NUMARRWORDSLOW,NUMARRWORDSHIGH)
	for k in range(0, wordsInArray):
		#randomly choose the word length (length of half of the end word) the other half 
		#of the word will be a duplication and reversal of the first half of the word
		randLen = random.randint(WORDLENLOW,WORDLENHIGH)
		word = ""
		#when the number of words in each array is odd,
		#make the word a palindrome (otherwise the word would not be a palindrome)
		if k%2 == 1:
			for i in range(0, randLen/2):
				word += random.choice(posibilitiesArr)
			#when the number of chars in a string is off then add a single random
			#char to the end of the current string (will act as middle char in odd strings)
			if randLen%2 == 1:
				word += random.choice(posibilitiesArr)
			#append the reversed substring of the beginning of the string to the end of the string
			word += ''.join(reversed(word[0:randLen/2]))
			words.append(word)
		else:
			for i in range(0, randLen):
				word += random.choice(posibilitiesArr)
			words.append(word)

	return words

# Recursive implementation of checking for a palindrome
def isPalRec(word, left = None, right = None):
	if left == None:
		left = 0
	if right == None:
		right = len(word)-1
	# if during the iteration the two position trackers
	# overlap or cross end the program with success
	if left >= right:
		return True
	else:
		if word[left] == word[right]:
			return isPalRec(word, left+1, right-1)
		else:
			return False

# iterative implementation of checking for a palindrome
def isPalIter(word):
	left = 0;
	right = len(word)-1
	# make sure that the two position trackers do not overlap
	while left < right:
		if word[left] == word[right]:
			left+=1
			right-=1
			continue
		else:
			return False
	return True
