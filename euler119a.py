# a = [614656, 1679616, 17210368, 52521875, 60466176, 612220032, 8303765625, 10460353203, 24794911296, 27512614111, 52523350144, 68719476736, 271818611107, 2207984167552, 20047612231936, 72301961339136, 248155780267521]
# A30 is probably < 20 digits.
# probably in i**j, i < 100, j < 10000000000 

import math as m
def euler119():
	bound = 81920000000000000
	powers = [i**j for i in range(2,100) for j in range(2, 100)]
	ans = sorted(list(set([p for p in powers if isdigsumpower(p)])))
	print ans[28]	# prints A[30] but I don't know why!!! What am I missing!!!

def isdigsumpower(num):
	digsum = sum(int(i) for i in str(num))
	try:
		return num == digsum**int(m.log(num, digsum))
	except:
		return False

if __name__ == "__main__":
	euler119()
