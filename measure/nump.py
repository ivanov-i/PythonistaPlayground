import numpy as np
import time
import math

bt = time.time()
n = 1000
for i in range(1):
    a = np.random.uniform(low=0., high=1., size=(n, n)).astype(np.float32)
    b = np.random.uniform(low=0., high=1., size=(n, n)).astype(np.float32)
    a = a.dot(b)
print ('(%d * %d),Total Time:%.3f'%(n,n,time.time()-bt))

start = time.clock()
x = [i * 0.001 for i in xrange(10000000)]
for i, t in enumerate(x):
    x[i] = math.sin(t)
print ("math.sin:%.3f"%(time.clock() - start))

start = time.clock()
y = [i * 0.001 for i in xrange(10000000)]
y = np.array(y)
print ("numpy.sin1:%.3f"%(time.clock() - start))
start = time.clock()
np.sin(y,y)
print ("numpy.sin2:%.3f"%(time.clock() - start))

