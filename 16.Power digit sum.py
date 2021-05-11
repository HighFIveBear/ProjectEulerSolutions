s = 0
n = 2 ** 1000
while n >= 1:
	s += n%10
	n = n // 10
print(s)