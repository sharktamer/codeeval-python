#!/usr/bin/env python


def isPrime(n):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

for i in range(1000)[::-1]:
    if isPrime(i):
        if str(i) == str(i)[::-1]:
            print i
            break
