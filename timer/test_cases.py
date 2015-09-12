import unittest
import timing

# All constants were calculated from http://www.easysurf.cc/utime.htm
class TestStringMethods(unittest.TestCase):
	def test_print(self):
		t = timing.Time(67210)
		self.assertEqual(t.printTime(1), "18:40:10")
		self.assertEqual(t.printTime(2), "06:40:10pm")

	def test_calculateSeconds(self):
		seconds = timing.calculateSeconds(3, 26, 32)
		KNOWN_SEC = 12392

		self.assertEqual(seconds, KNOWN_SEC)

	def test_add(self):
		t = timing.Time(0)
		t.changeSeconds(12908)
		self.assertEqual(t.printTime(1), "03:35:08")

	def test_sub(self):
		t = timing.Time(0)
		t.changeSeconds(3600)
		t.changeSeconds(-600)
		self.assertEqual(t.printTime(1), "00:50:00")

if __name__ == '__main__':
	unittest.main(verbosity=2)
