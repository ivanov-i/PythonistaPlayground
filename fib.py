N = 0

def memoized(f):
  cache = {}
  def wrap(*args):
    if args not in cache:
      cache[args] = f(*args)
    return cache[args]
  return wrap

@memoized
def fib(n):
  global N
  N = N + 1
  if n == 0:
    return 0
  elif n == 1:
    return 1
  else:
    return fib(n-1) + fib(n-2)

print(fib(100))
