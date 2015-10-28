
import sys
X = None
Y = None
price = None
matrix = None
p = None
n = None
def input():
	global X,Y,p,n
	for i in range(0,len(sys.argv)):
		print i,": ",sys.argv[i]
	file = open(sys.argv[1])
	line = file.readline().split()
	X = int(line[0])
	Y = int(line[1])
	line = file.readline().split()
	n = int(line[0])
	print n
	p = [] 
	line = file.readline().split()
	while line != [] :
		entry = (int(line[0]),int(line[1]),int(line[2]))#tuple[0]=ai;tuple[1]=bi;tuple[2]=ci
		p.append(entry)
		line = file.readline().split()
	file.close()

def dp():
	global p,n
	price = []
	for i in range(X+1):
		price.append([])
		for j in range(Y+1):
			price[i].append(0)
	for i in range(n):
		if price[p[i][0]][p[i][1]] < p[i][2]:
			price[p[i][0]][p[i][1]] = p[i][2]
	for i in price:
		print i

	maxprice = []
	for i in range(X+1):
		maxprice.append([])
		for j in range(Y+1):
			maxprice[i].append(0)
	
	matrix = []
	for i in range(X+1):
		matrix.append([])
		for j in range(Y+1):
			matrix[i].append(None)

	for i in range(1,X+1):
		for j in range(1,Y+1):
			max1 = 0
			max2 = 0
			a = 0
			b = 0
			#cut horizontally
			l1 = []
			for x in range(1,i):
				aaa = maxprice[x][j]+maxprice[i-x][j]
				l1.append(aaa)
			if not len(l1) == 0:
				max1 = max(l1)
				a = l1.index(max1)+1
			
			#cut vertically
			l2 = []
			for y in range(1,j):
				bbb = maxprice[i][j-y]+maxprice[i][y]
				l2.append(bbb)				
			if not len(l2) == 0:
				max2 = max(l2)
				b = l2.index(max2)+1

			l3 = [max1,max2,price[i][j]]
			maxprice[i][j] = max(l3)
			print i,j,maxprice[i][j]
			#store maxprice

			if l3.index(max(l3)) == 0 :
				matrix[i][j] = [[a,j],[i-a,j],"v",a]
			elif l3.index(max(l3)) == 1:
				matrix[i][j] = [[i,j-b],[i,b],"h",b]

 	print maxprice[X][Y]

 	def DFS(i,j):
		if matrix[i][j] == None:
			return 0
		else:
			visited[i][j] = True
			print i,j,matrix[i][j][2],matrix[i][j][3]
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

 	visited = []
	for i in range(X+1):
		visited.append([])
		for j in range(Y+1):
			visited[i].append(False)
	DFS(X,Y)
	

input()
dp()