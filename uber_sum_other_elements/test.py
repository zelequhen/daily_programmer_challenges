import sum

import unittest

class SumTest(unittest.TestCase):
    def test_easy(self):
        input = [3, 2, 1]
        expected = [2, 3, 6]

        actual = sum.generate_array(input)

        self.assertEquals(actual, expected, 'simple test failed. Got {} instead of {}'.format(actual, expected))

    def test_complex(self):
        input = [1, 2, 3, 4, 5]
        expected = [120, 60, 40, 30, 24]

        actual = sum.generate_array(input)

        self.assertEquals(actual, expected, 'simple test failed. Got {} instead of {}'.format(actual, expected))

    def test_duplicate(self):
        input = [1, 2, 3, 4, 5, 3]
        expected = [360, 180, 120, 90, 72, 120]

        actual = sum.generate_array(input)
  
        self.assertEquals(actual, expected, 'simple test failed. Got {} instead of {}'.format(actual, expected))
