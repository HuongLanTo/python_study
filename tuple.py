tuple = ('abcd', 786, 2.23, 'John', 70.2)
tinyTuple = (123, 'John')

print(tuple)		# Print complete list
print(tuple[0])		# Print first element of the list
print(tuple[1:3])	# Print elements starting from 2nd till 3rd
print(tuple[2:])	# Print elements starting from 3rd element
print(tinyTuple * 2)	# Print list two times
print(tuple + tinyTuple)    # Print concatenated lists

# tuple[0] = 'a'  => Invalid syntax with tuple
# => Tuples can be thought of as read-only lists.
