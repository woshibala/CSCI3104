import sys
X = None
Y = None
price = None
h = None
v = None
tot = None
def input():
	global X,Y,price,h,v,tot
	for i in range(0,len(sys.argv)):
		print i,": ",sys.argv[i]
	file = open("cloth.txt")
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
	#store price for all size of products
	for i in range(n):
		if price[p[i][0]][p[i][1]] < p[i][2]:
			price[p[i][0]][p[i][1]] = p[i][2]

	#store the max price for a i*j cloth

	maxprice = []
	for i in range(0,X):
		maxprice.append([])
		for j in range(0,Y):
			maxprice[i].append(None)
	for i in range(1,X):
		for j in range(1,Y):
			maxprice[i][j] = -1
	
	tot= 0
	h = 0
	v = 0
	maxprice[0][0] = 0	
	def maxre(i,j):
		global tot,h,v
		if maxprice[i][j] != -1:
			return maxprice[i][j]
		else:
			max1 = 0
			max2 = 0
			x = -1
			y = -1
			#cut horizontally
			if j > 1:
				l1 = []
				for x in range(1,i):
					aaa = maxre(x,j)+maxre(i-x,j)# maxprice[x][j]+maxprice[i-x][j]
					l1.append(aaa)
					
				if not len(l1) == 0:
					max1 = max(l1)
					x = l1.index(max1)
			#cut vertically
			if i > 1:
				l2 = []
				for y in range(1,j):
					bbb = maxre(i,j-y)+maxre(i,y)#maxprice[i][j-y]+maxprice[i][y]
					l2.append(bbb)
				
				if not len(l2) == 0:
					max2 = max(l2)
					y = l2.index(max2)


			l3 = [max1,max2,price[i][j]]
			maxprice[i][j] = max(l3)
			if x*y == 0:
				print "not cut"
				return maxprice[i][j]
			if l3.index(max(l3)) == 0:
				print "h",i,j,y
				h += 1
				tot += 1
			elif l3.index(max(l3)) == 1:
				print "v",i,j,x
				v += 1
				tot += 1
			else:
				print "not cut"
			return maxprice[i][j]

	print maxre(X-1,Y-1)
	print h,v,tot


def run():
	input()
run()

