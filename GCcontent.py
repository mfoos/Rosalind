def GCcount(myBases):
	(count,acount,ccount,gcount,tcount) = (0,0,0,0,0)
	for i in myBases:
		count = len(myBases)#+= 1.0
		if i.upper() == "C":
			ccount += 1.0
		elif i.upper() == "G":
			gcount += 1.0
		elif not i.strip():
			count -= 1.0
	GCpercent = ((gcount + ccount) / (count))*100	
	return GCpercent, count

#filename = raw_input("input file name: ")
content = open('gc.txt.fixed','r')
infile = content.readlines()
content.close()

countlist = []
idlist = []
for line in infile:
	if not line.strip():
		continue
	elif line[0] == ">":
		print line, 
		idlist.append(line)
	else: 
		print GCcount(line)
		countlist.append(GCcount(line))

print idlist[countlist.index(max(countlist))],
print countlist[countlist.index(max(countlist))]		

