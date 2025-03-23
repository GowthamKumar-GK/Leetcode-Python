"""n=int(input())
f=0
if n<0:
    n=abs(n)
    f=1
s=0
while n!=0:
    ld=n%10
    n=n//10
    s=s*10+ld
    n=n//10
if f==1:
    print(-(s))
else:
    print(s)"""

class Solution:
    def reverse(self, n: int) -> int:
        f = 0
        if n < 0:
            n = abs(n)#absolute positive to negative
            f = 1
        s = 0
        while n != 0:
            ld = n % 10  # Extract the last digit
            s = s * 10 + ld  # Append the last digit to the reversed number
            n = n // 10  # Remove the last digit from the original number
        if f == 1:
            s = -s  # Restore the negative sign if the input was negative
        
        # Handle 32-bit integer overflow
        if s < -2**31 or s > 2**31 - 1:
            return 0
        return s

# Create an instance of the Solution class
solution = Solution()

# Test cases
print(solution.reverse(901000))  # Output: 109
print(solution.reverse(123))     # Output: 321
print(solution.reverse(-123))    # Output: -321
print(solution.reverse(120))     # Output: 21
print(solution.reverse(1534236469))  # Output: 0 (overflow)

