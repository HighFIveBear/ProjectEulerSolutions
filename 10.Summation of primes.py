def prime_counter(targ):
    import math
    primes = [2]
    x = 3
    while x < targ:
        max_div = math.floor(math.sqrt(x))
        for y in range(3,max_div+1,2):
            if x % y == 0:
                x += 2
                break
        else:
            primes.append(x)
            x += 2
    print(primes)
    return sum(primes)

a = prime_counter(2000000)

print(a)