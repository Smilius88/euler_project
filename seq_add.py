# num and denom are generators that give the numerator and denominator of the next number in the sequence
def seq_add(num, denom):
	from isprime import divreduce
	curr = (0,1)
	while True:
		next_num, next_denom = num.next(), denom.next()
		curr = divreduce(curr[0]*next_denom + curr[1]*next_num, next_denom * curr[1])
		yield curr

def num():
	count = 1
	while True:
		yield ((-1)**(count+1)) * (2* count + 1)
		count += 1

def denom():
	count = 1
	while True:
		yield count**2 + count
		count += 1
