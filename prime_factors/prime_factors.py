#from memoizer import memoize
import functools

class Number:
  def __init__(self, n):
    self.n = n
  
#  @memoize
  @functools.lru_cache(maxsize=None)
  def factors(self):
    if self.n < 2:
      return []
    else:
      return self.factors_unchecked()
  
  def factors_unchecked(self):
    factor = 2
    while self.n % factor != 0 and factor <= self.n:
      factor += 1
    if(factor > self.n):
      return []
    else:
      return [factor] + Number(int(self.n / factor)).factors()
    
  
  
if __name__ == '__main__':
  n = 0
  while True:
    print(n, '=', '*'.join(map(str,Number(n).factors())))
    digit = input('next digit or non-digit to del:')
    try:
      digit = int(digit)
      if not 0 <= digit <= 9:
        raise
      else:
        n = n*10 + digit
    except:
      n = int(n/10)
    print(n)
        
