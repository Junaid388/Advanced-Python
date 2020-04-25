items = [2, 35, 25, 9]
divisor = 12

for item in items:
	if item % divisor == 0:
		found = item
		break
else:  # no break
	items.append(divisor)
	found = divisor

print("{items} contains {found} which is a multiple of {divisor}".format(**locals()))



"""Alternative to for else approch

def ensure_has_divisible(items, divisor):
	for item in items:
		if item % divisor == 0:
			return item
	items.append(divisor)
	return divisor

items = [2, 25, 9]
divisor = 12

dividend =ensure_has_divisible(items, divisor)

print("{items} contains {dividend} which is a multiple of {divisor}".format(**locals()))"""