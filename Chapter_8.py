from math import sqrt
'''
use fibonacci to make a list of fibonacci numbers (for loop would be nice)
use sieve to check which of those numbers is prime
'''

def fibonacci(num):
    sequence = [0, 1]
    if num <= 0:
        return [0]   
    else:
        # Initialize variables to store the first two numbers in the sequence
        a, b = 0, 1
        # Loop through the sequence up to num, updating a and b at each step
        for index in range(2, num+1):
            c = a + b
            sequence.append(c)
            a = b
            b = c
        #return b
        return sequence
    


def prime_checker(checklist, primelist):
    for num in checklist:
        if num == 1:
            pass
        elif num > 1:
            # check for factors
            for i in range(2, round(sqrt(num))):
               if (num % i) == 0:
                   break
            else:
                primelist.append(num)
       
        # if input number is less than
        # or equal to 1, it is not prime
        else:
            pass
    
    return primelist


if __name__ == "__main__":

    prime_fibonaccis = []

    fib_nums = int(input("How many fibonacci numbers do you want to generate?\n:"))
    fibonacci_sequence = fibonacci(fib_nums)
    #print(fibonacci_sequence)

    prime_checker(fibonacci_sequence, prime_fibonaccis)

    print(f"Out of {fib_nums} fibonacci numbers, {len(prime_fibonaccis)} were prime.")
    print("The prime fibonacci numbers were:")
    for number in prime_fibonaccis:
        print(number)
