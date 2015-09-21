import sys,math
for i in range(0,len(sys.argv)):
		print i,": ",sys.argv[i]
file_object = open(sys.argv[1])
try:
     all_the_text = file_object.read( )
finally:
     file_object.close( )
a = ""
for i in all_the_text:
	if not i.isspace():
		a += i
	else:
		break
print a 