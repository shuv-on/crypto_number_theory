"""Reusable number-theory routines for the assignment."""
from math import isqrt

def gcd(a, b):
    a, b = abs(a), abs(b)
    while b:
        a, b = b, a % b
    return a

def extended_gcd(a, b):
    if b == 0:
        return abs(a), (1 if a >= 0 else -1), 0
    g, x1, y1 = extended_gcd(b, a % b)
    return g, y1, x1 - (a // b) * y1

def lcm(a, b):
    return 0 if a == 0 or b == 0 else abs(a // gcd(a, b) * b)

def mod_inverse(a, n):
    g, x, _ = extended_gcd(a, n)
    return x % n if g == 1 else None

def mod_pow(base, exponent, modulus):
    if modulus <= 0 or exponent < 0:
        raise ValueError("modulus must be positive and exponent non-negative")
    result, base = 1, base % modulus
    while exponent:
        if exponent & 1:
            result = result * base % modulus
        base = base * base % modulus
        exponent >>= 1
    return result

def is_prime(n):
    if n < 2: return False
    if n % 2 == 0: return n == 2
    d = 3
    while d*d <= n:
        if n % d == 0: return False
        d += 2
    return True

def sieve(n):
    if n < 2: return []
    flags = [True] * (n+1)
    flags[0] = flags[1] = False
    for p in range(2, isqrt(n)+1):
        if flags[p]:
            for k in range(p*p, n+1, p):
                flags[k] = False
    return [i for i, ok in enumerate(flags) if ok]
