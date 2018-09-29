# Open a file
fo = open("foo.txt", "wb")
print("Name of the file: ", fo.name)		# Return name of the file
print("Closed or not: ", fo.closed)			# Return true if file is closed, false otherwise
print("Opening mode: ", fo.mode)			# Return access mode with which file was opened
print("Softspace flag: ", fo.softspace)		# Return false if space explicitly required with print, true otherwise