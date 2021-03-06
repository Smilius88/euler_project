# actually this returns the highest prime that is a sum of multiple primes. Oops.  
import isprime as ip

def euler50():
	primes = list(ip.primes_sieve2(500010))
	primeset = set(primes)
	compset = set()
	ans, counter = 0, 0
	test = [0] * (len(primes)+1)
	test[0] = primes[0]
	for i in range(1, len(test)-1):
		test[i] = primes[i] + test[i-1]
		for j in range(i):
			concurrent = test[i] - test[j]
			if concurrent > 1000000:
				break
			elif concurrent > ans:
				if testprime(concurrent, primeset, compset):
					ans = concurrent
					print ans
	print ans


def testprime(n, primeset, compset):
	if n in primeset:
		return True
	elif n in compset:
		return False
	elif ip.isprime(n):
		primeset.add(n)
		return True
	else:
		compset.add(n)
		return False

if __name__ == "__main__":
	euler50()
