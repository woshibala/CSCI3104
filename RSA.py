import random
import time
x=None
y=None
N=None
e=None

def randomPrime(n):
	flag = False
	while flag == False:
		num = random.randint(10**(n-1),10**(n)-1)
		if 2**(num-1) % num == 1:
			flag = True
	return num

def encode(plaintext,bit):
	global e,N
	#bit = len(str(plaintext))
	#bit = 3
	start = time.clock()
	flag = False
	while flag == False:
		p = randomPrime(bit)
		q = randomPrime(bit)
		N = p * q
		eulerF = (p-1)*(q-1)
		e = relativelyprime(eulerF)
		ExtendEuclid(e,eulerF)
		if x > 0:
			flag = True 
	end = time.clock()
	print ("The public keys are:"),e,N
	print ("The private keys are:"),x,N
	print ("The running time of step a is:"),end-start
	#d = x/(e*x + eulerF*y) 
	start = time.clock()
	ciphertext = plaintext**e % N
	end = time.clock()
	print ("The ciphertext is:"),ciphertext
	print ("The running time of step b is:"),end-start
	return ciphertext

def decode(ciphertext):
	global x,N
	start = time.clock()
	M = ciphertext**x % N
	end = time.clock()
	print ("The plaintext is:"),M
	print ("The running time of step c is:"),end-start
	print("**************************************************")

def ExtendEuclid(a,b):
	global x,y
	if b == 0:
		x = 1
		y = 0
		q = a
		#print q
		return
	ExtendEuclid(b,a%b)
	t = x
	x = y 
	y = t-a/b*y
	#print x,y
	return 

def relativelyprime(num):
	length = len(str(num))
	flag = False
	i = 10**(length-1)
	while flag == False:
		if 2**(i-1) % i == 1:
			return i 
		else:
			i+=1


text = encode(2015,3)
decode(text)
text = encode(119,3)
decode(text)
text = encode(110,3)
decode(text)
text = encode(1200,3)
decode(text)

#Honor Code Pledge: "On my honor, as a University of Colorado at Boulder student, I have neither given nor received unauthorized assistance."