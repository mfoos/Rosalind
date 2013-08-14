input = open("DNAstring.txt")

myBases = input.read()

(acount,ccount,gcount,tcount) = (0,0,0,0)
for i in myBases[:]:
	if i == "T":
		tcount = tcount + 1
	elif i == "C":
		ccount = ccount + 1
	elif i == "G":
		gcount = gcount + 1
	elif i == "A":
		acount = acount + 1
	else: 
		print "%s is not a recognized base" % i

print "T: %s, C: %s, G: %s, A: %s" % (tcount, ccount, gcount, acount) 
			
