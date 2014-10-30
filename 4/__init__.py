largest = -1

for i in range(1, 999):
	for j in range(i, 999):
		strnum = str(i*j)
		pal = False
		for k in range((len(strnum)/2)+(len(strnum))%2):
			if strnum[k]==strnum[len(strnum)-k-1]:
				pal = True
			else:
				pal = False
				break
		if pal:
			print(str(i) + '*' + str(j) + '=' + str(strnum))
			largest = strnum if int(strnum) > int(largest) else largest
print('Largest: ' + str(largest))