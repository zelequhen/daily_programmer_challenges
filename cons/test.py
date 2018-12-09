from cons import cons, car, cdr

import unittest

class ConsTest(unittest.TestCase):
	def test_car(self):
		expected = 3

		actual = car(cons(3, 4))

		self.assertEquals(actual, expected, 'Got {}, but expected {}'.format(actual, expected))

	def test_cdr(self):
		expected = 4

		actual = cdr(cons(3, 4))

		self.assertEquals(actual, expected, 'Got {}, but expected {}'.format(actual, expected))
		
