import math
def primeNumbers(maxint):
    '''
    This function generates all prime numbers less than or equal to the supplied value 
    '''
    primes = []
    for num in range(2, maxint + 1):
        isPrime = True
        for div in range(2, int(math.sqrt(num)) + 1):
            if (num % div == 0):
        	isPrime = False
	if isPrime:
	    primes.append(num)
    return primes
