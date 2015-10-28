import sys
X = None
Y = None
price = None
matrix = None
def input():
	global X,Y,price,matrix
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
	price = []
	print p
	for i in range(X+1):
		price.append([])
		for j in range(Y+1):
			price[i].append(None)
	for i in range(X+1):
		for j in range(Y+1):
			price[i][j] = -1
	#store price for all size of products
	for i in range(n):
		if price[p[i][0]][p[i][1]] < p[i][2]:
			price[p[i][0]][p[i][1]] = p[i][2]

	#store the max price for a i*j cloth
	maxprice = []
	for i in range(X+1):
		maxprice.append([])
		for j in range(Y+1):
			maxprice[i].append(None)
	for i in range(1,X+1):
		for j in range(1,Y+1):
			maxprice[i][j] = -1
	maxprice[0][0] = 0
	#maxprice[0][0] = 0																																																																																																																																																																																																																																																																																																																			z
	sum = 0
	h = 0
	v = 0
	matrix = []
	for i in range(X+1):
		matrix.append([])
		for j in range(Y+1):
			matrix[i].append(None)		
	
	def maxre(i,j):
		if maxprice[i][j] != -1:
			return maxprice[i][j]
		else:
			max1 = 0
			max2 = 0
			a = 0
			b = 0
			#cut horizontally
			if j > 1:
				l1 = []
				for x in range(1,i-1):
					if maxprice[x][j] == -1 and maxprice[i-x][j] == -1:
						aaa = maxre(x,j)+maxre(i-x,j)# maxprice[x][j]+maxprice[i-x][j]
					elif maxprice[x][j] != -1 and maxprice[i-x][j] == -1:
						aaa = maxprice[x][j]+maxre(i-x,j)
					elif maxprice[x][j] != -1 and maxprice[i-x][j] != -1:
						aaa = maxprice[x][j] + maxprice[i-x][j]
					else:
						aaa = maxre(x,j)+maxprice[i-x][j]
					l1.append(aaa)
				
				if not len(l1) == 0:
					max1 = max(l1)
					a = l1.index(max1)
			#cut vertically
			if i > 1:
				l2 = []
				for y in range(1,j-1):
					if maxprice[i][j-y] == -1 and maxprice[i][y] == -1:
						bbb = maxre(i,j-y)+maxre(i,y)#maxprice[i][j-y]+maxprice[i][y]
					elif maxprice[i][j-y] != -1 and maxprice[i][y] == -1:
						bbb = maxprice[i][j-y]+maxre(i,y)
					elif maxprice[i][j-y] != -1 and maxprice[i][y] != -1:
						bbb = maxprice[i][j-y]+maxprice[i][y]
					else:
						bbb = maxre(i,j-y)+maxprice[i][y]
					l2.append(bbb)
				
				if not len(l2) == 0:
					max2 = max(l2)
					b = l2.index(max2)
		
 

			l3 = [max1,max2,price[i][j]]
			if max1 == price[i][j] or max2 == price[i][j]:
				l3.pop()
			maxprice[i][j] = max(l3)
			print i,j,l3.index(max(l3))
			if l3.index(max(l3)) == 0 :
				if  a != 0:
					matrix[i][j] = [[a,j],[i-a,j],"v",a]
					print matrix[i][j]
			elif l3.index(max(l3)) == 1:
				if b != 0:
					matrix[i][j] = [[i,j-b],[i,b],"h",b]
					print matrix[i][j]
			return maxprice[i][j]
		return maxprice[X][Y]
	def DFS(i,j):
		global matrix
		if matrix[i][j] == None or matrix[i][j] == -1:
			return 
		else:
			visited[i][j] = True
			print i,j,matrix[i][j][2],matrix[i][j][3]
			line = [str(i),str(j),matrix[i][j][2],str(matrix[i][j][3]),"\n"]
			file.writelines(line)
			k = matrix[i][j][0]#child 1
			x = k[0]
			y = k[1]
			if not visited[x][y]:
				DFS(x,y)
			k = matrix[i][j][1]#child 2
			x = k[0]
			y = k[1]
			if not visited[x][y]:
				DFS(x,y)
	print maxre(X,Y)
	


	visited = []
	for i in range(X+1):
		visited.append([])
		for j in range(Y+1):
			visited[i].append(False)
	file = open("output.txt","w")
	DFS(X,Y)
	file.close()
	


	for i in maxprice:
		print i
	for i in price:
		print i
	for i in matrix:
		print i

	
	
	
def run():
	input()
	print("Done")
run()

