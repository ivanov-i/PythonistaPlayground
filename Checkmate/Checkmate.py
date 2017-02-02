import unittest
import draw_board


class Figure:
  def __init__(self, x, y):
    self.x = x
    self.y = y


class King(Figure):
  def is_checkmate(self, figures):
    must_be_attacked = ((x,y) for x in range(self.x - 1, self.x + 2) for y in range(self.y - 1, self.y + 2))
    actually_attacked = (any(figure.attacks(x,y) for figure in figures) for x,y in must_be_attacked)
    result = all(actually_attacked)
    return result
    
  def attacks(self, x,y):
    dx,dy = (abs(self.x - x), abs(self.y - y))
    if((dx,dy) == (0,0)):
      return False
    elif dx > 1 or dy > 1:
      return False
    else:
      return True

  def draw(self):
    return 6


class BlackKing(King):
  def draw(self):
    return -6
    
    
class Bishop(Figure):
  def attacks(self, x, y):
    (dx, dy) = (abs(x - self.x), abs(y - self.y))

    return dx == dy and (self.x, self.y) != (x, y)

  def draw(self):
    return 3

class Knight(Figure):
  def attacks(self, x, y):
    (dx, dy) = (abs(x - self.x), abs(y - self.y))
    if dx == 2 and dy == 1:
      return True
    elif dx == 1 and dy == 2:
      return True
    else:
      return False

  def draw(self):
    return 2


class Board:
  def __init__(self, pieces):
    self.pieces = pieces

  def draw(self):
    def square(x, y):
      chars = [p.draw() for p in self.pieces if (p.x, p.y) == (x, y)]
      if(chars):
        return chars[0]
      else:
        return 0

    raw_board = [square(x, y) for y in range(1, 9) for x in range(1, 9)]
    lines = [raw_board[i: i + 8] for i in range(0, len(raw_board), 8)]
    lines.reverse()
    board = draw_board.game(lines)
    return board

def different(a, b, c, d):
  return a != b and a != c and a != d and b != c and b != d and c != d

if __name__ == '__main__':
  all_combinations = ([BlackKing(xbk,ybk), King(xk,yk), Bishop(xb,yb), Knight(xkn,ykn)]\
    for xbk in range(1,9) for ybk in range(1,9)\
    for xkn in range(1,9) for ykn in range(1,9)\
    for xb in range(1,9) for yb in range(1,9)\
    for xk in range(1,9) for yk in range(1,9)\
    if(different((xbk, ybk), (xk,yk), (xb,yb), (xkn,ykn))))
    
  checkmates = ([black_king, king, bishop, knight] for [black_king, king, bishop, knight] in all_combinations\
     if(black_king.is_checkmate([king, bishop, knight])))
    
  boards = (Board(combination) for combination in checkmates)
  
  #print(sum(1 for x in boards))
  
  for i,board in enumerate(boards):
    print(i)
    print(board.draw())
    print('>')
    
  print('done')
