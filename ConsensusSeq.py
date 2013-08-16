fasta = open("rosalind_cons.txt.fixed","r")

# Slurp sequences only into array and learn sequence length
dataset = []
for line in fasta.readlines():
	if line[0] != ">":
		line = line.strip()
		lineSize = len(line)
		dataset.append(line)
fasta.close()

# Define counters to fit size of given sequence 
aCount = [0]*(lineSize)
cCount = [0]*(lineSize)
gCount = [0]*(lineSize)
tCount = [0]*(lineSize)

for seq in dataset:
	for i in range(len(seq)):
		if seq[i] == "A":
			aCount[i] += 1
		elif seq[i] == "C":
			cCount[i] += 1
		elif seq[i] == "G":
			gCount[i] += 1
		elif seq[i] == "T":
			tCount[i] += 1
consensus = []
for i in range(len(seq)):
	posCompare = (aCount[i],cCount[i],gCount[i],tCount[i])
	if aCount[i] == max(posCompare):
		consensus.append("A")
	elif cCount[i] == max(posCompare):
		consensus.append("C")
	elif gCount[i] == max(posCompare):
		consensus.append("G")
	elif tCount[i] == max(posCompare):
		consensus.append("T")
	#I realize this will lead to a bias toward A in equivalent consensus sequences, it's what I got for now

def pickyFormat(counter):
	return " ".join(map(str,counter))

print ''.join(consensus)
print "A:", pickyFormat(aCount)	
print "C:", pickyFormat(cCount)	
print "G:", pickyFormat(gCount)	
print "T:", pickyFormat(tCount)	




