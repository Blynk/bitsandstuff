#!/bin/python
import math

## Normalizing data input 


def avg(l): return sum(l) * 1.0 / len(l)

print "Enter numbers separated by spaces"
n = sorted(map(int, raw_input().split(" ")))

while True:
	print "Enter 1 for min-max, 2 for Z-score,", 
	print "3 for Z-score w/ mean abs deviation,",
	print "4 for decimal scaling"
	choice = int(raw_input())
	if choice == 1:
		print "min-max normalization:"
		print "Enter new min"
		minVal = int(raw_input())
		print "Enter new max"
		maxVal = int(raw_input())
		for i in xrange(len(n)):
			print (n[i] - n[0] + 0.0)/(n[len(n)-1] - n[0]) * (maxVal - minVal) + minVal,
		print ""
	elif choice == 2:
		mean = avg(n)
		stdDev = math.sqrt(avg(map(lambda x:(x - mean)**2, n)))
		for i in xrange(len(n)):
			print (n[i] - mean) / stdDev,
		print ""
	elif choice == 3:
		mean = avg(n)
		stdDev = avg(map(lambda x:abs(x - mean), n))
		for i in xrange(len(n)):
			print (n[i] - mean) / stdDev,
		print ""
	elif choice == 4:
		maxVal = max(map(abs, n))
		print maxVal
		maxVal = maxVal / 10.0
		count = 1
		while maxVal > 1:
			maxVal = maxVal / 10.0
			count = count + 1
		print count
		print map(lambda x: (x + 0.0) / 10.0**count, n),
		print ""
	else:
		break
