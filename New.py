def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True  # This should be outside the loop

def closest_primes(left, right):
    primes = [num for num in range(left, right + 1) if is_prime(num)]
    
    if len(primes) < 2:
        return [-1, -1]  # No pair found
    
    min_diff = float('inf')
    result = [-1, -1]
    
    for i in range(len(primes) - 1):
        if primes[i + 1] - primes[i] < min_diff:
            min_diff = primes[i + 1] - primes[i]
            result = [primes[i], primes[i + 1]]
    
    return result

# Taking user input
left = int(input("Enter the left boundary: "))
right = int(input("Enter the right boundary: "))
print("Closest prime numbers:", closest_primes(left, right))
