def prime_counter(targ):
    primes = [2]
    x = 3
    
    while x > 0:
        for y in primes:
            if x % y == 0:
                x += 2
                break
        else:
            primes.append(x)
            x += 2
        if len(primes) == targ:
            break
    print(primes, x)
    return len(primes)

a = prime_counter(10001)
print(a)