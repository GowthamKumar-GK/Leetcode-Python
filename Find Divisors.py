def finddivisors(n):
    divisors = []
    for i in range(2, int(n ** 0.5) + 1):  # Start from 2, ignore 1 and n itself
        if n % i == 0:
            divisors.append(i)
            if i != n // i:  # Avoid adding the square root twice
                divisors.append(n // i)
    return sorted(divisors)

# Read input
t = int(input())#3
for i in range(t):
    num = int(input())#468
    
    result = finddivisors(num)#function call
    print(" ".join(map(str, result)) if result else "")#list output to sapce separate num
