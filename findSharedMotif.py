import sys

DEBUG = False
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

newMin = 0
for seqPos in reversed(range(len(subStringGenerator))):
	start = 0
	end = start
	#window = len(subStringGenerator)
	print "sequence position: %d" % seqPos
	while start < len(subStringGenerator) and end <= len(subStringGenerator):
		end = start + seqPos + 1 #window
		subString = subStringGenerator[start:end]
		if DEBUG:
			print "start: %d" % start
			print "end: %d" % end
			print "substring: %s" % subString
		mismatch = False	
		for seq in seqSet:
			if subString not in seq:
				#print "String %s absent from this record" % subString
				mismatch = True
				break
		
		if mismatch == False and len(subString) > newMin:
			newMin = len(subString)		
			print newMin
			print "Match Found! - %s" % subString
			sys.exit(0)

		start += 1
