import sys,math,time,csv

date = None
pricewave = None
def input():
	global date,pricewave
	d = []
	p = []
	date = []
	price = []
	pricewave = []
	with open(sys.argv[1],'r') as file:
		for i in file:
			d.append(i.split(",")[0])
			p.append(i.split(",")[1])
	while len(d) != 0:
		date.append(d.pop())
	while len(p) != 0:
		price.append(p.pop())
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
	left_sum = float("-inf")
	Sum = 0
	for i in range(mid,low,-1):
		Sum += float(A[i])
		if Sum > left_sum:
			left_sum = Sum
			max_left = i
	right_sum = float("-inf")
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
	print "Start date:",date[0]
	print "End date:",date[len(date)-1]
	print "Buy date:", date[result[0]]
	print "Sell date:", date[result[1]]
	print "Max reward per share is:", result[2]

run()

# the first argv is the name of the .csv file
# you can run the algorithm by enter this:
# pyhton Song_Yang_HW3.py KO.csv
# KO.csv for coca-cola company
# BABA.csv for Alibaba Group Holding
# MSFT.csv for Microsoft Corporation 