import sys
X = None
Y = None
price = None
matrix = None
visited = None

def input():
	global X,Y,price,matrix,visited
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
			price[i].append(0)
	#store price for all size of products
	for i in range(n):
		if price[p[i][0]][p[i][1]] < p[i][2]:
			price[p[i][0]][p[i][1]] = p[i][2]

	#store the max price for a i*j cloth
	maxprice = []
	for i in range(X):
		maxprice.append([])
		for j in range(Y):
			maxprice[i].append(0)
	matrix = []
	for i in range(X):
		matrix.append([])
		for j in range(Y):
			matrix[i].append(None)

	sum = 0
	h = 0
	v = 0
	#when the size of the cloth grows
	previous = [None,None,None]
	for i in range(X):
		for j in range(Y):
			max1 = 0
			max2 = 0
			a = 0
			b = 0
			#cut horizontally
			if j > 0:
				l1 = []
				for x in range(1,i):
					aaa = maxprice[x][j]+maxprice[i-x][j]
					#if maxprice[x][j]*maxprice[i-x][j] != 0:
					l1.append(aaa)
				
				if not len(l1) == 0:
					max1 = max(l1)
					a = l1.index(max1)+1
			#cut vertically
			if i > 0:
				l2 = []
				for y in range(1,j):
					bbb = maxprice[i][j-y]+maxprice[i][y]
					#if maxprice[i][j-y]*maxprice[i][y] != 0:
					l2.append(bbb)
				
				if not len(l2) == 0:
					max2 = max(l2)
					b = l2.index(max2)+1

			if max1==0 and max2 == 0 and price[i][j] == 0:
				pass
			else:
				l3 = [max1,max2,price[i][j]]
				maxprice[i][j] = max(l3)
				if l3.index(max(l3)) == 0 :
					#print "h"
					sum += 1
					h +=1
					matrix[i][j] = [[a,j],[i-a,j],"v",a]
	
				elif l3.index(max(l3)) == 1:
					#print "v"
					sum += 1
					v += 1
					matrix[i][j] = [[i,j-b],[i,b],"h",b]
				
					#print "not cut"
	

	visited = []
	for i in range(X):
		visited.append([])
		for j in range(Y):
			visited[i].append(False)
	#for i in visited:
	#	print i

	def DFS(i,j):
		if matrix[i][j] == None:
			return
		else:
			visited[i][j] = True
			print i+1,j+1,matrix[i][j][2],matrix[i][j][3]
			k = matrix[i][j][0]
			x = k[0]
			y = k[1]
			if not visited[x][y]:
				DFS(x,y)
			k = matrix[i][j][1]
			x = k[0]
			y = k[1]
			if not visited[x][y]:
				DFS(x,y)


	print "maximum price is:",maxprice[X-1][Y-1]
	
	
	DFS(X-1,Y-1)




def run():
	input()

run()

