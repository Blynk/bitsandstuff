import math


def get_prime():
	print "Enter a prime number"
	p = int(raw_input())
	for i in xrange(2, int(math.sqrt(p))):
		if p % i == 0:
			return 0
	return p

def calc_pub_key(root, priv, prime):
	return root ** priv % prime

def calc_priv_key(pub, priv, prime):
	return pub ** priv % prime

prime = 0

while(prime == 0):
	prime = get_prime()

print "Enter a number"
root = int(raw_input())

print "Enter Alice's private key"
a_priv = int(raw_input())

print "Enter Bob's private key"
b_priv = int(raw_input())

a_pub = calc_pub_key(root, a_priv, prime)
b_pub = calc_pub_key(root, b_priv, prime)

if(calc_priv_key(b_pub, a_priv, prime) == calc_priv_key(a_pub, b_priv, prime)):
	print "Success!\tKey ==", calc_priv_key(b_pub, a_priv, prime)
else:
	print calc_priv_key(b_pub, a_priv, prime), calc_priv_key(a_pub, b_priv, prime)
