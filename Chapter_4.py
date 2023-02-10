#Write a program to count the number of primes less than some number. 
#Make a log plot of the number of primes less than ten, one hundred, a thousand, ten thousand, a hundred thousand and a million. 
#Predict the number of primes less than 10 million

'''
def is_prime(number):
    if number <= 1:
        return False
    if number == 2:
        return True
    if number % 2 == 0:
        return False
    limit = floor(sqrt(number)) + 1
    for i in range(3, limit, 2):
        if number % i == 0:
            return False
    return True
'''

import math
import pandas as pd
import matplotlib.pyplot as plt

given_numbers = []
num_of_primes = []

def count_primes(number):
    count = 0
        
    for num in range(number):
        if num <= 1:
            continue
        for integer in range(2, num):
            if (num % integer) == 0:
                break
        else:
            count += 1
    
    return count

def add_to_lists():
    num = int(input("Enter a number: "))
    given_numbers.append(num)
    
    num_of_primes.append(count_primes(num))
    
    

if __name__ == '__main__':


    


    while len(given_numbers) < 5:
        add_to_lists()

    print(given_numbers)
    print(num_of_primes)
    
    
