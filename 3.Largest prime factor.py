n = 28
prime_factors = []
i = 2
while i <= n:
    if n % i == 0:
        n = n / i
        prime_factors.append(i)
    else:
        i += 1
print(prime_factors)