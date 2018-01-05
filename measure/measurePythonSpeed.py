import time, functools

import time                                                
 
def timeit(method):
 
    def timed(*args, **kw):
        ts = time.time()
        result = method(*args, **kw)
        te = time.time()
 
        print ('%r (%r, %r) %2.2f sec' % (method.__name__, args, kw, te-ts))
        return result
 
    return timed

def primes(n):
    return (x for x in range(n) if all(x%y!=0 for y in range(2, x)))

def countGenerator(generator):
    return functools.reduce(lambda x,y:x+1, generator, 0)

@timeit
def measure(n):
    countGenerator(primes(n))

measure(100000)

