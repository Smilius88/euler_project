def euler1():
	print sum([i for i in xrange(1000) if (i % 3 == 0 or i % 5 == 0)])

if __name__ == "__main__":
	euler1()
