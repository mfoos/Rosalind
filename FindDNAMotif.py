myString = raw_input("String: ")
mySubstring = raw_input("Substring: ")

def FindMotif(string, substring):
	subsize = len(substring)
	for i in range(len(string)):
		if string[i:i+subsize] == substring:
			print i+1,

FindMotif(myString, mySubstring)
