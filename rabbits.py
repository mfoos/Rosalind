months = int(raw_input("n = ? "))
litter = int(raw_input("k = ? "))

mature = 0
born = 1
next_mature = 0
next_born = 0

for i in range(months):
	bunnies = mature + born

	next_born = mature*litter
	next_mature = mature + born

	mature = next_mature
	born = next_born

	print "index %d, bunnies %d" % (i, bunnies)

print bunnies
