def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        # Initialize variables to store the first two numbers in the sequence
        a, b = 0, 1
        # Loop through the sequence up to n, updating a and b at each step
        for index in range(2, n+1):
            c = a + b
            a = b
            b = c
        return b


print(fibonacci(10))