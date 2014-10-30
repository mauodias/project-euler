def sumsqrange(x, y):
	sum = 0
	for i in range(x, y):
		sum += pow(i, 2)
	return sum

def sqsumrange(x, y):
	sum = 0
	for i in range(x,y):
		sum += i
	return pow(sum, 2)

sumsq = sumsqrange(1, 101)

sqsum = sqsumrange(1, 101)
diff = sqsum-sumsq
print(sqsum)
print(sumsq)
print(diff)