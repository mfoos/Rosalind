content = open("rosalind_grph.txt.fixed","r")
fasta = content.readlines()
content.close()

headers = []
seqSet = []
for line in fasta:
	if line[0] == ">":
		headers.append(line[1:].strip())
	else:
		line = line.strip()
		seqSet.append(line)

for i in range(len(seqSet)):
	suffix = seqSet[i][-3:]
	firstNode = seqSet[i]
	firstNodeIndex = i #eval(str(i))		
	for i in range(len(seqSet)):
		if seqSet[i][0:3] == suffix and (seqSet[i] != firstNode):
			lastNodeIndex = i # eval(str(i))
			print headers[firstNodeIndex], headers[lastNodeIndex]

