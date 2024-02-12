n = int(input())
primes = set(range(2, n+1))

for i in range(2, n+1):
    if i in primes:
        point = i
        multiplier = i
        while multiplier <= n:
            multiplier = point + multiplier
            primes.discard(multiplier)

print(primes)
