from random import *
import time
lSize = 1000
l=range(lSize)
shuffle(l)

start = time.time()
for i in range(lSize):
    # print i
    for j in xrange(1, len(l) - i):
        # print l
        # print "Comparing %d to %d (%d,%d)" % (l[i],l[j],i,j)
        if l[j - 1] > l[j]:
            l[j - 1], l[j] = l[j], l[j - 1]
end = time.time()

print end - start
