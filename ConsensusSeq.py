fasta = open("rosalind_cons.txt","r")

dataset = []
for line in fasta.readlines():
	if line[0] != ">":
		dataset.append(line)

print dataset[1]
