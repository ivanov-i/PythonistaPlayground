import matplotlib.pyplot as plt
import itertools
import math
import collections
import random


def p(x):
	print(list(x))

N = 10000
D = 10000

def createRandomPoint():
	return list((random.random() for i in range(0, D)))

pairs = ((createRandomPoint(), createRandomPoint()) for i in range(0, N))


def distance(a,b):
	return math.sqrt(sum(((x1 - x2)**2 for (x1, x2) in zip(a,b))))

distances = (round(distance(first, second), 2) for (first, second) in pairs)

counts = collections.Counter(distances)

labels, values = zip(*sorted(counts.items()))

plt.plot(labels, values)
plt.show()
