import unittest
import Checkmate
import itertools
import textwrap


class TestFigureThatAttacksItself(Checkmate.Figure):
  def attacks(self, x, y):
    result = (x,y) == (self.x, self.y)
    return result


class TestFigureThatAttacksNothing(Checkmate.Figure):
  def attacks(self, x, y):
    return False


class Test_King(unittest.TestCase):
  def test_checkmate_when_all(self):
    field = [TestFigureThatAttacksItself(x,y) for x in range(99,102) for y in range(99,102)]
    field.append([TestFigureThatAttacksNothing(x,y) for x in range(0,5) for y in range(10,20)])
    king = Checkmate.King(100,100)
    self.assertTrue(king.is_checkmate(field))

  def test_checkmate_checks_all_fields(selfs):
    king = Checkmate.King(100, 100)
    field = [TestFigureThatAttacksItself(x,y) for x in range(99,102) for y in range(99,102)]
    while len(field) > 0:
      field.pop()
      selfs.assertFalse(king.is_checkmate(field))


class Test_Bishop(unittest.TestCase):
  def test_all(self):
    ox, oy = 94, 48   
    to_test = ((x, y, ((x,y) != (ox, oy)) and (abs(x - ox) == abs(y - oy))) for x in range(-100, 100) for y in range(-100, 100))
    for (x, y, value) in to_test:
      self.assertEqual(Checkmate.Bishop(ox, oy).attacks(x, y), value, (x, y, value))
     
class Test_Knight(unittest.TestCase):
  def test_does_not_attack_far(self):
    ox,oy = 84, 42
    k = Checkmate.Knight(ox, oy)
    to_test = ((x + ox, y + oy) for x in range(-100, 100) for y in range(-100,100) if abs(x) > 2 and abs(y) > 2)
    for x,y in to_test:
      self.assertFalse(k.attacks(x, y), (x, y))
      
  def test_attacks_L(self):
    ox,oy = 2000, 129
    k = Checkmate.Knight(ox, oy)
    
    all_possibilities = [(x,y) for x in range(-2, 3) for y in range(-2, 3)]
    
    def is_L(x,y):
      return (abs(x) == 2 and abs(y) == 1) or (abs(x) == 1 and abs(y) == 2)
      
    expected = ((x + ox, y + oy, is_L(x, y)) for (x,y) in all_possibilities)
    
    for (x, y, value) in expected:
      self.assertEqual(k.attacks(x, y), value, (x, y, value))
      
class Test_King(unittest.TestCase):
  def test_does_not_attack_self(self):
    ox,oy = 102, 93
    king = Checkmate.King(ox,oy)
    self.assertFalse(king.attacks(ox,oy))
    
  def test_attacks_around(self):
    ox,oy = 102, 93
    king = Checkmate.King(ox,oy)
    to_check = ((ox+x,oy+y) for x in range(-1, 2) for y in range(-1, 2) if ((x,y) != (0,0)))
    for x,y in to_check:
      self.assertTrue(king.attacks(x,y), (x,y))

  def test_does_not_go_far(self):
    ox,oy = 102, 93
    king = Checkmate.King(ox,oy)
    to_check = ((ox+x,oy+y) for x in range(-100, 100) for y in range(-100, 100) if (abs(x) > 1 and abs(y) > 1))
    for x,y in to_check:
      self.assertFalse(king.attacks(x,y), (x,y))
  

class Test_Board(unittest.TestCase):
  def test_draws_empty(self):
    board = Checkmate.Board([])
    expected = u"""\
    ⬜️⬛️⬜️⬛️⬜️⬛️⬜️⬛️
    ⬛️⬜️⬛️⬜️⬛️⬜️⬛️⬜️
    ⬜️⬛️⬜️⬛️⬜️⬛️⬜️⬛️
    ⬛️⬜️⬛️⬜️⬛️⬜️⬛️⬜️
    ⬜️⬛️⬜️⬛️⬜️⬛️⬜️⬛️
    ⬛️⬜️⬛️⬜️⬛️⬜️⬛️⬜️
    ⬜️⬛️⬜️⬛️⬜️⬛️⬜️⬛️
    ⬛️⬜️⬛️⬜️⬛️⬜️⬛️⬜️
    """
    expected = textwrap.dedent(expected)
    
    self.assertEqual(expected, board.draw())
    
  def test_draws_pieces(self):
    king = Checkmate.King(4, 5)
    bishop = Checkmate.Bishop(8, 8)
    pieces = [king, bishop]
    board = Checkmate.Board(pieces)
    expected = u"""\
    ⬜️⬛️⬜️⬛️⬜️⬛️⬜️⛪️
    ⬛️⬜️⬛️⬜️⬛️⬜️⬛️⬜️
    ⬜️⬛️⬜️⬛️⬜️⬛️⬜️⬛️
    ⬛️⬜️⬛️🃏⬛️⬜️⬛️⬜️
    ⬜️⬛️⬜️⬛️⬜️⬛️⬜️⬛️
    ⬛️⬜️⬛️⬜️⬛️⬜️⬛️⬜️
    ⬜️⬛️⬜️⬛️⬜️⬛️⬜️⬛️
    ⬛️⬜️⬛️⬜️⬛️⬜️⬛️⬜️
    """
    expected = textwrap.dedent(expected)
    
    self.assertEqual(expected, board.draw())
    
def do_tests():
  unittest.main()

if __name__ == '__main__':
  do_tests()

