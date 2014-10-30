def gcd(x, y):
	while True:
		rem = x%y
		if rem == 0:
			return y
		x = y
		y = rem


def llm(x, y):
	return x*y/gcd(x, y)

minimum = reduce(llm, range(1,21))

print(minimum)