n = int(raw_input())

intlist = []
strlist = []
freq = [0 for x in xrange(100)]

for x in xrange(n):
	s = raw_input().strip().partition(" ")
	num = int(s[0])
	intlist.append(num)
	if x < n/2:
		strlist.append("-")
	else:
		strlist.append(s[2])
	freq[num] += 1;
    
total = 0
for x in xrange(100):
	oldcount = freq[x]
	freq[x] = total
	total += oldcount
    
output = ["" for x in xrange(n)]
for x in xrange(n):
	output[freq[intlist[x]]] = strlist[x]
	freq[intlist[x]] += 1;
           
print " ".join(output)
    
