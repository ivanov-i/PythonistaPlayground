import itertools
import math

def p(x):
	print(list(x))

N = 10
D = 3

x = [x/N for x in range(0, N+1)]

points = list(itertools.combinations_with_replacement(x, D))
pairs = itertools.combinations_with_replacement(points,2)

def distance(a,b):
	return math.sqrt(sum([(x1 - x2)**2 for (x1, x2) in zip(a,b)]))
	
distances = itertools.chain([distance(first, second) for (first, second) in pairs if(first != second)])

print(list(distances))