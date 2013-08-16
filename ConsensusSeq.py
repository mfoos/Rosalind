fasta = open("rosalind_cons.txt","r")


def makeProfile(seq):
	aCount = [0]*(len(seq))
	cCount = [0]*(len(seq))
	gCount = [0]*(len(seq))
	tCount = [0]*(len(seq))
	for i in range(len(seq)):
		if seq[i] == "A":
			aCount[i] += 1
		elif seq[i] == "C":
			cCount[i] += 1
		elif seq[i] == "G":
			gCount[i] += 1
		elif seq[i] == "T":
			tCount[i] += 1
	print aCount

for line in fasta.readlines():
	if line[0] != ">":
		line = line.strip()
	#	print line, len(line)
		makeProfile(line)

