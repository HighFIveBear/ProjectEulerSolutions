import time
c0 = time.time()
comp = 0
for n in range(2, 1000000):
	i = 0
	prom = n
	while n != 1:
		if n % 2 == 0:
			n = n / 2
		else: 
			n = 3*n + 1 
		i += 1
	if i > comp:
		comp = i
		larg = prom
print(larg)

c1 = time.time()

print(c1-c0)
