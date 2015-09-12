import unittest
from palindrome import *

a = generateRand()

class TestStringMethods(unittest.TestCase):
	def test_generate(self):
		assert a is not None

	def test_palindromeRec(self):
		for i in a:
			if i == i[::-1]:
				res = True
			else:
				res = False
			assert isPalRec(i, 0, len(i)-1) == res

	def test_palindromeIter(self):
		for i in a:
			if i == i[::-1]:
				res = True
			else:
				res = False
			assert isPalIter(i) == res

if __name__ == '__main__':
	unittest.main(verbosity=2)
