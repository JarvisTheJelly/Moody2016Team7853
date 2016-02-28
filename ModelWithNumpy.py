import numpy as np

duration_array = np.array([15.49 for x in xrange(97)] + [2.75 for x in xrange(99406)] + [5.96 for x in xrange(248996)] + [12.81 for x in xrange(437851)] + [21.92 for x in xrange(161431)] + [30.81 for x in xrange(108786)] + [42.37 for x in xrange(43250)] + [92.96 for x in xrange(64641)])

duration_array2 = np.array([0.85 for x in xrange(100372)] + [1.87 for x in xrange(249838)] + [4.47 for x in xrange(422060)] +[9.33 for x in xrange(159417)] + [14.13 for x in xrange(103138)] + [21.42 for x in xrange(41379)] + [69.25 for x in xrange(59390)])

print np.mean(duration_array)
print np.std(duration_array)
