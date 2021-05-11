n = 1
m = 2
check = True
while check:
	for n in range(1, m + 1):
		a = m**2 - n**2
		b = 2*m*n
		c = m**2 + n**2
		if a + b + c == 1000 and a**2 + b**2 == c**2:
			print(a * b * c)
			check = False
			print (f'a = {a}, b = {b}, c = {c}')
			break
		
	m += 1

 