content = open("rosalind_lcsm.txt.fixed","r")
fasta = content.readlines()

seqSet = []
for entry in fasta:
	if entry[0] == ">":
		next
	else:
		seqSet.append(entry)

subStringGenerator = seqSet.pop(0)
#any longest common substring will exist in any sequence in the dataset

shortestString = len(min(seqSet, key=len))
start = 0
end = 5
size = 5
match = False
while start < len(subStringGenerator):
	subString = subStringGenerator[start:end]
	for seq in seqSet:
		if subString in seq:
			print subString,
			match = True #there exists a common substring at this length
		else:
			print "subString absent"
			break
	start = end
	end += size

