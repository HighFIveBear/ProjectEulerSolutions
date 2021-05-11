cur = 1
prev = 0
prom = cur
n = 1

while (cur/10**999) < 1:
	prom = cur
	cur += prev
	prev = prom
	n += 1
print(n)
