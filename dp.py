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

	for obj in p:
		for i in range(X):
			for j in range(Y):
				if obj[0] > i or obj[1] > j:
					maxprice[i][j] = maxprice[i][j-1]
				else:
					l1 = []
					for x in range(i):
						aaa = maxprice[x][j]+maxprice[i-x][j]
						l1.append(aaa)
					max1 = max(l1)
					l2 = []
					for y in range(j):
						bbb = maxprice[i][j-y]+maxprice[i][y]
						l2.append(bbb)
					max2 = max(l2)
					l3 = [max1,max2,price[i][j]]
					maxprice[i][j] = max(l3)

	print maxprice[X-1][Y-1]











def run():
	input()

run()

