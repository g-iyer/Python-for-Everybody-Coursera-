largest = None
smallest = None
while True:
	num = raw_input("Enter a number: ")
	if num == "done" :
		break
	else:
		try:
			num_i=int(num)
		except:
			print "Invalid input"
			continue
	if num_i > largest:
		largest = num_i
	if smallest is None:
		smallest = num_i
	if num_i < smallest:
		smallest = num_i
    
		print num

print "Maximum is", largest
print "Minimum is", smallest