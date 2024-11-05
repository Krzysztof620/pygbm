import math
import random

# 1.1 - Taylor expansion of sin(0.1) to order 5 (first 6 terms)

# Using Taylor expansion for sin(x):
# sin(x) ≈ x - x^3/3! + x^5/5! - x^7/7! + x^9/9! - ...
# Here, we compute up to x^5/5! (5th order)

x = 0.1
sin_approx = x - (x**3) / math.factorial(3) + (x**5) / math.factorial(5)

# 1.2 - Print result as descriptive string
sin_approx_str = f"Taylor expansion of sin(0.1) to order 5 gives approximately {sin_approx:.5f}"
print(sin_approx_str)

# 1.3 - Function to return a list of prime numbers less than a given integer N
def primes_less_than(N):
    # Initialize an empty list to store prime numbers
    primes = []
    
    # Iterate over each number from 2 up to (but not including) N
    for num in range(2, N):
        # Assume the current number is prime until proven otherwise
        is_prime = True
        
        # Check if num has any divisors other than 1 and itself
        # Only test divisors up to the square root of num (for optimization)
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:  # If num is divisible by i, it's not prime
                is_prime = False
                break  # No need to check further; num is not prime
        
        # If num has no divisors other than 1 and itself, it is prime
        if is_prime:
            primes.append(num)  # Add the prime number to the list
    
    return primes  # Return the list of prime numbers found

# Test for primes less than N = 20
N = 20
primes_list = primes_less_than(N)
print(f"Primes less than {N}: {primes_list}")

# 1.4 - Function to return the first N terms of the Recaman's sequence
def recaman_sequence(N):
    # If N is less than or equal to 0, return an empty list (no terms to generate)
    if N <= 0:
        return []

    # Initialize the sequence with the starting element 0
    recaman = [0]
    # Set to keep track of the terms that have been added to the sequence
    seen = {0}

    # Generate terms for the sequence from 1 up to N-1
    for n in range(1, N):
        # Calculate the next term by subtracting n from the previous term
        next_term = recaman[n-1] - n

        # If the next term is positive and has not been seen before, add it to the sequence
        if next_term > 0 and next_term not in seen:
            recaman.append(next_term)
        else:
            # Otherwise, calculate the next term by adding n to the previous term
            next_term = recaman[n-1] + n
            recaman.append(next_term)

        # Mark this term as seen by adding it to the set
        seen.add(recaman[-1])

    # Return the full sequence up to N terms
    return recaman

# Test for Recaman's sequence with N = 20
recaman_list = recaman_sequence(N)
print(f"First {N} terms of Recaman's sequence: {recaman_list}")

# 1.5 - List of numbers that appear in both lists when they are N items long
common_elements = list(set(primes_list) & set(recaman_list))
print(f"Common elements in the first {N} primes and Recaman's sequence: {common_elements}")

# 1.6 - List of all pairs of factors (as tuples) of 362880 using list comprehension
number_to_factor = 362880
factors_pairs = [(i, number_to_factor) for i in range(1, int(number_to_factor**0.5) + 1) if number_to_factor % i == 0]
print(f"Factor pairs of {number_to_factor}: {factors_pairs}")

# 1.7 - Generator function for a random walk with displacement of 10 steps
def random_walk_displacement_10():
    displacement = 0  # Initialize displacement to 0
    
    # Continue the walk until the absolute value of displacement reaches 10
    while abs(displacement) < 10:
        # Randomly choose the direction of the step: -1 (backward) or 1 (forward)
        step = random.choice([-1, 1])
        
        # Update the displacement by adding the chosen step
        displacement += step
        
        # Yield the current displacement value to the caller
        yield displacement  # This allows the function to be paused and resumed

# Test the random walk generator
print("Random walk displacements until 10 steps:")
print(list(random_walk_displacement_10()))