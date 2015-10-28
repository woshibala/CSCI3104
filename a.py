
import sys
X = None
Y = None
price = None
matrix = None
p = None
n = None
total = None
output1 = []
output2 = []
print1 = []
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
	#print n
	p = [] 
	line = file.readline().split()
	while line != [] :
		entry = (int(line[0]),int(line[1]),int(line[2]))#tuple[0]=ai;tuple[1]=bi;tuple[2]=ci
		p.append(entry)
		line = file.readline().split()
	file.close()

def dp():
	global p,n,total,output1,output2
	price = []
	for i in range(X+1):
		price.append([])
		for j in range(Y+1):
			price[i].append(0)
	for i in range(n):
		if price[p[i][0]][p[i][1]] < p[i][2]:
			price[p[i][0]][p[i][1]] = p[i][2]
	
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

			if l3.index(max(l3)) == 0 :
				matrix[i][j] = [[a,j],[i-a,j],1,a]
			elif l3.index(max(l3)) == 1:
				matrix[i][j] = [[i,j-b],[i,b],0,b]

 	

 	def DFS(i,j):
 		global total,output1,output2,print1
		if matrix[i][j] == None:
			return 
		else:
			visited[i][j] = True
			#print i,j,matrix[i][j][2],matrix[i][j][3]
			line = [str(i)," ",str(j)," ",str(matrix[i][j][2])," ",str(matrix[i][j][3]),"\n"]
			l1 = [i,j]
			l2 = [matrix[i][j][2],matrix[i][j][3]]
			output1.append(l1)
			output2.append(l2)
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
	file = open(sys.argv[2],"w")
	total = 0
	DFS(X,Y)
	
	def cut(a,b):
		global output1,output2,total,print1

		if [a,b] in output1:
			method = output2[output1.index([a,b])]
			if method[1] == 0:
				return
			tmp = [a,b,method[0],method[1]]
			print1.append(tmp)
			total+=1
			if method[0] == 1:
				cut(a-method[1],b)
				cut(method[1],b)
			elif method[0] == 0:
				cut(a,method[1])
				cut(a,b-method[1])
		else:
			return 
	
	cut(X,Y)
	file.writelines(str(maxprice[X][Y])+" "+str(total)+"\n")
	for i in print1:
		file.writelines(str(i[0])+" "+str(i[1])+" "+str(i[2])+" "+str(i[3])+"\n")
	file.close()
	print "maximum price is: ",maxprice[X][Y]
	print "total cut",total
	

input()
dp()
print "Done!"