# -*- coding: utf-8 -*-
"""
Created on Mon Nov 19 16:42:16 2018

@author: Michael
"""

"""
This is my attempt to produce a series of functions for computations related
to prime numbers. The following functions will be created:
    
    "isprime(n)" : Returns True or False based on whether "n" is prime
    or not.
    
    "ithprime(n)" : Returns the n-th prime number.
    
    "listprimes(n)" : Lists the first n primes.
    
    "primefactor(n)" : Decomposes n into prime factors.
    
"""

import math

def isprime(n):
    # Returns True if "n" is prime, otherwise returns False
    if n == 1:
        return False
    if n % 2 == 0:
        if n == 2:
            return True
        else:
            return False
    divisor = 3
    ceiling = math.ceil(math.sqrt(n))
    while divisor <= ceiling:
        if n % divisor == 0:
            return False
        else:    
            divisor = nextprime(divisor)
    return True

def ithprime(n):
    # Returns the n-th Prime
    if n == 1:
        return 2
    k = 1
    currentPrime = 2
    while k < n:
        currentPrime += 1
        if isprime(currentPrime):
            k += 1
    return currentPrime

def nextprime(n):
    # Returns the next prime after n
    temp = int(n + 1)
    while isprimesimple(temp) == False:
        temp += 1
    return temp

def primefactor(n):
    # Decomposes n into prime factors
    assert (n > 1), "The value of n must be greater than 1!"
    remainder = n
    factors = []
    divisor = 2
    while remainder != 1:
        if remainder % divisor == 0:
            factors.append(divisor)
            remainder /= divisor
        else:
            divisor = nextprime(divisor)
    return factors

def listprimes(n):
    # Lists the first n primes
    if  n == 0:
        return []
    primes = [2]
    for k in range(n-1):
        newPrime = nextprime(primes[-1])
        primes.append(newPrime)
    return primes

def isprimesimple(n):
    # Returns True if "n" is prime, otherwise returns False
    if n == 1:
        return False
    if n % 2 == 0:
        if n == 2:
            return True
        else:
            return False
    divisor = 3
    ceiling = math.ceil(math.sqrt(n))
    while divisor <= ceiling:
        if n % divisor == 0:
            return False
        else:    
            divisor += 2
    return True

def prevPrimesLoad():
    prevprimes = open("primes.txt","r")
    primeslist = []
    while True:
        tempnum = prevprimes.readline()
        if tempnum == "":
            break
        primeslist.append(int(tempnum))
    prevprimes.close()
    return primeslist
    
def prevPrimesAppend(prime):
    prevprimes = open("primes.txt", "a")
    newPrimeLine = str(prime) + "\n"
    prevprimes.write(newPrimeLine)
    prevprimes.close()