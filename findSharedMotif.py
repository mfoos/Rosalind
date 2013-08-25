content = open("rosalind_lcsm.txt.fixed","r")
fasta = content.readlines()

seqSet = []
for entry in fasta:
	if entry[0] == ">":
		next
	else:
		seqSet.append(entry.strip())

subStringGenerator = seqSet.pop(0)
#any longest common substring will exist in any sequence in the dataset

end = size = len(min(seqSet, key=len))
start = 0
newMin = None
while start < len(subStringGenerator):
	subString = subStringGenerator[start:end]
	mismatch = False	
	for seq in seqSet:
		if subString in seq:
			print subString
		else:
			print "String %s absent from this record" % subString
			mismatch = True
			break

	if mismatch == False:
		newMin = len(subString)		

	start = end
	end += size
	end -= 1

print newMin
