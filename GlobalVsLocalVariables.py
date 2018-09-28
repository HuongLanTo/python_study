total = 0		# this is global variable

def sum(arg1, arg2):
	total = arg1 + arg2
	print("Inside the function local total: ", total)
	print(total)

sum(10, 20)
print("Outside the function global total: ", total)