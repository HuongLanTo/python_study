list = ['abcd', 786, 2.23, 'John', 70.2]
tinyList = [123, 'John']

print(list)			# Print complte list
print(list[0])		# Print first element of the list
print(list[1:3]) 	# Print elements starting from 2nd till 3rd
print(list[2:])		# Print elements starting from 3rd element
print(tinyList * 2)	# Print list two times
print(list + tinyList)  # Print concatenated lists

list[0] = 'a'
print(list)