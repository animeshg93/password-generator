import numpy as np

numbers = np.arange(0,100,2)

user = int(input("Enter number you want to search: "))

l = 0;
r = numbers.size-1
found = False

while l <= r:
	mid = l + (r-l)//2
	if numbers[mid] == user:
		print("Found your number %s" %numbers[mid])
		found = True
		break
	elif numbers[mid] > user:
		r = mid-1
	else :
		l = mid+1

if found == False:
	print("Your number does not exist")