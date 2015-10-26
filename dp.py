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
		entry = (int(line[0]),int(line[1]),int(line[2]))#tuple[0]=ai;tuple[1]=bi;tuple[2]=ci
		p.append(entry)
		line = file.readline().split()
	for i in p:
		print i
	price = []
	for i in range(X):
		price.append([])
		for j in range(Y):
			price[i].append(-1)
	#store price for all sizes of cloth
	for i in range(n):
		if price[p[i][0]][p[i][1]] < p[i][2]:
			price[p[i][0]][p[i][1]] = p[i][2]
	for i in price:
		print i
	#store the max price for a i*j cloth
	maxprice = []
	for i in range(X):
		maxprice.append([])
		for j in range(Y):
			maxprice[i].append(-1)
	maxprice[0][0] = 0

	for obj in range(n):
		for i in range(X):
			for j in range(Y):
				









def run():
	input()

run()

