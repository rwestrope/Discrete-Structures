'''
use fibonacci to make a list of fibonacci numbers (for loop would be nice)
use sieve to check which of those numbers is prime
'''


def fibonacci_iterative(num):
    if num == 0:
        return 0
    elif num == 1:
        return 1
    else:
        # Initialize variables to store the first two numbers in the sequence
        a, b = 0, 1
        # Loop through the sequence up to num, updating a and b at each step
        for index in range(2, num+1):
            #operation_counter.function_call_count += 1
            c = a + b
            a = b
            b = c
        return b
    

def sieve_of_eratosthenes(n):
    # Create a boolean array "prime[0..n]" and
    # initialize all entries it as true.
    prime = [True for i in range(n+1)]
    p = 2
    while(p * p <= n):
         
        # If prime[p] is not changed, then it is a prime
        if (prime[p] == True):
             
            # Update all multiples of p
            for i in range(p * p, n+1, p):
                prime[i] = False
        p += 1
    
    # Count the number of prime numbers
    count = 0
    for p in range(2, n):
        if prime[p]:
            count += 1
    return count
