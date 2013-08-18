import re

content = open("rosalind_lcsm.txt.fixed","r")
fasta = content.readlines()

entryCount = 0
for entry in fasta:
	if entry[0] == ">":
		entryCount += 1

start = 3
for i in range(1,len(fasta), 2):
	substring = fasta[i][:start]
	for j in range(1,len(fasta),2):
		while j < len(fasta):
			if re.search(substring, fasta[j],flags=0):
				print substring
			else:
				print "Not found in sequence %d" % (j/2)
				continue	
			j += 1
		else:
			start += 1
