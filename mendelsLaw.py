dom = float(raw_input("K: "))
het = float(raw_input("M: "))
rec = float(raw_input("N: "))

total = dom + het + rec

domPhen = (dom/total * het/(total-1)) + \
	(het/total * dom/(total-1)) + \
	(het/total * (het-1)/(total-1))*.75 + \
	(rec/total * het/(total-1))*.5 + \
	(het/total * rec/(total-1))*.5 + \
	(dom/total * (dom-1)/(total-1)) + \
	(dom/total * rec/(total-1)) + \
	(rec/total * dom/(total-1))

print domPhen
