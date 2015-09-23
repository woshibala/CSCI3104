for i in range(0,len(sys.argv)):
			print i,": ",sys.argv[i]
	file_object = open(sys.argv[1])
	try:
	     all_the_text = file_object.read( )
	finally:
	     file_object.close( )
	a = ""
	b = ""
	date = []
	price = []
	flag = True
	for i in all_the_text:
		if i == "\t":
			flag = False
			date.append(a)
			a = ""
		elif i == "\n":
			flag = True
			price.append(b)
			b = ""
		else:
			if flag == True:
				a += i
			else:
				b += i 
	price.append(b)