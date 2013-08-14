#input_file = open("rosalind_revc.txt","r")

#sample = input_file.read()
#input_file.close()
sample = "AAAACCCGGT"

DNA = []
for i in range(len(sample)):
	if sample[i] == "A":
#		 DNA += "T"
		print "T",
	elif sample[i] == "C":
	#	DNA += "G"
		print "G",
	elif sample[i] == "G":
		#DNA += "C"
		print "C",
	elif sample[i] == "T":
		#DNA += "A"
		print "A",
	else:
		DNA.append("X")
		print "Position %d not recognized" % i

#complement = ''.join(DNA)

#print DNA[::-1]	




