#!/bin/python

import sys

for i in xrange(1, len(sys.argv)):
	hashResult = (3 * int(sys.argv[i]) + 7) % 11
	print hashResult,"\t",bin(hashResult)
