#input_file = open("rosalind_revc.txt","r")

#sample = input_file.read()
#input_file.close()
sample = "AAAACCCGGT"

DNA = []
for i in range(len(sample)-1):
	if sample[i] == "A":
		DNA.append("T")
	elif sample[i] == "C":
		DNA.append("G")
	elif sample[i] == "G":
		DNA.append("C")
	elif sample[i] == "T":
		DNA.append("A")
	else:
		DNA.append("X")
		print "Position %d not recognized" % i

complement = ''.join(DNA)

print complement[::-1]	




