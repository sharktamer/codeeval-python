#!/bin/env python


def isPrime(n):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


# def primeGenerator():
#     num = 1
#     while True:
#         if isPrime(num):
#             yield num
#         num += 1

# prime_list = []
# for p in primeGenerator():
#     if len(prime_list) < 1001:
#         prime_list.append(p)
#     else:
#         print sum(prime_list) - 1
#         break

first1000Primes = list()
i = 1
while len(first1000Primes) < 1001:
    if isPrime(i):
        first1000Primes.append(i)
    i += 1

print sum(first1000Primes) - 1
