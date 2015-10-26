import sys
X = None
Y = None
price = None
def input():
	global X,Y,price
	for i in range(0,len(sys.argv)):
		print i,": ",sys.argv[i]
	file = open(sys.argv[1])
	line = file.readline().split()
	X = int(line[0])
	Y = int(line[1])
	print X,Y
	line = file.readline().split()
	n = int(line[0])
	print n
	p = []
	line = file.readline().split()
	while line != [] :
		entry = (int(line[0]),int(line[1]),int(line[2]))
		p.append(entry)
		line = file.readline().split()
	for i in p:
		print i
	price = []
	for i in range(X):
		price.append([])
		for j in range(Y):
			price[i].append(-1)
	for i in range(n):
		if price[p[i][0]][p[i][1]] < p[i][2]:
			price[p[i][0]][p[i][1]] = p[i][2]
	for i in price:
		print i









def run():
	input()

run()

