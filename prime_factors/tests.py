import prime_factors as pf
import unittest

class NumberTest(unittest.TestCase):
  def test(self):
    tests = [
      [0, []],
      [1, []],
      (2, [2]),
      (3, [3]),
      (4, [2,2]),
      (5, [5]),
      (6, [2,3]),
      (7, [7]),
      (8, [2,2,2]),
      (9, [3,3]),
      (25, [5,5]),
      (568, [2,2,2,71])
    ]
    for [n, expected] in tests:
      self.assertSequenceEqual(pf.Number(n).factors(), expected, 'was testing ' + str(n))
    

if __name__ == '__main__':
  unittest.main()
