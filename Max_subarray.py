import sys,math,time
date = None
pricewave = None
def input():
	global date,pricewave
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
	pricewave = []
	for i in range(0,len(price)-1):
		pricewave.append(float(price[i+1])-float(price[i]))
	#for j in range(0,len(pricewave)-1):
	#	print pricewave[j]

def Find_Maximum_Subarray(A,low,high):
	if high == low:
		result = (low,high,A[low])
		return result
	else:
		mid = int(math.floor((low + high)/2))
		left = Find_Maximum_Subarray(A,low,mid)
		left_low = left[0]
		left_high = left[1]
		left_sum = left[2]
		right = Find_Maximum_Subarray(A,mid+1,high)
		right_low = right[0]
		right_high = right[1]
		right_sum = right[2]
		cross = Find_Max_Crossing(A,low,mid,high)
		cross_low = cross[0]
		cross_high = cross[1]
		cross_sum = cross[2]
		if left_sum >= right_sum and left_sum >= cross_sum:
			result = (left_low,left_high,left_sum)
			return result
		elif right_sum >= left_sum and right_sum >= cross_sum:
			result = (right_low,right_high,right_sum)
			return result
		else:
			result = (cross_low,cross_high,cross_sum)
			return result

def Find_Max_Crossing(A,low,mid,high):
	max_left =  0
	max_right = 0
	left_sum = -100#float("-inf")
	Sum = 0
	for i in range(mid,low,-1):
		Sum += float(A[i])
		if Sum > left_sum:
			left_sum = Sum
			max_left = i
	right_sum = -100#float("-inf")
	Sum = 0
	for j in range(mid+1,high):
		Sum += float(A[j])
		if Sum > right_sum:
			right_sum = Sum 
			max_right = j
	result = (max_left,max_right,left_sum+right_sum)
	#print result
	return result

def run():
	global date,pricewave
	input()
	result = Find_Maximum_Subarray(pricewave,0,len(pricewave)-1)
	#print result
	print "Buy stock on:", date[result[1]]
	print "Sell stock on:", date[result[0]]
	print "Max outcome per share is:", result[2]

run()