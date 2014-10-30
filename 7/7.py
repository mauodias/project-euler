primes = [2]
i = 3
while True:
	flag = False
	for j in primes:
		if i%j == 0:
			i+=1
			flag = False
			break
		else:
			flag = True
	if flag:
		primes += [i]
		print(len(primes))
	if len(primes) >= 10001:
		print(primes[-1])
		break
print(primes[-1])