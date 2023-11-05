from utils.get_input import get_input
from math import gcd
from itertools import product

input = int(get_input(2015, 20))

def primes_lte(n:int) -> list[int]:
    out = list([2])
    sieve = [True] * (n+1)
    for p in range(3, n+1, 2):
        if sieve[p]:
            out.append(p)
            for i in range(p*p, n+1, p):
                sieve[i] = False
    return out

def prime_factorization(n:int, primes:list[int]) -> dict[int:int]:
    factors = {}
    for prime in primes:
        while n % prime == 0:
            factors[prime] = factors.get(prime, 0) + 1
            n //= prime
        if n == 1:
            break
    if n != 1:
        factors[n] = 1
    return factors

def lowest_house(bound:int, primes:set[int]) -> int:
    def sum_factors(prime_factors):
        total = 1
        for prime, exponent in prime_factors.items():
            total *= (prime**(exponent + 1) - 1) // (prime - 1)
        return total
    
    i = 1
    while True:
        prime_factors = prime_factorization(i, primes)
        total = sum_factors(prime_factors) * 10
        if total >= bound:
            return i
        i += 1

primes = primes_lte(int(input ** 0.5))
print(lowest_house(input, primes))

# add a new bound which checks if factor * 50 is less than the current number