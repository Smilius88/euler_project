from isprime import *
primes = [i for i in range(1,1000) if isprime(i)]
primes.extend([-i for i in primes])
pairs = []
answer = dict()
for i in primes:
	for j in primes:
		if isprime(i+j+1):
			pairs.append((i,j))
for pair in pairs:
	a, b = pair
	i = 1
	while (isprime(i**2 + a*i + b)):
		i+=1
	answer[i] = pair

print answer[max(answer.keys())]
a,b = answer[max(answer.keys())]
print a*b
