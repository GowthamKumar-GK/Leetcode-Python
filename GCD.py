class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        # Step 1: Check concatenation property
        if str1 + str2 != str2 + str1:#ABCABC+ABC"=ABCABC+ABC"
            return "no gcd"

        # Step 2: Find GCD of lengths using Euclidean algorithm
        def find_gcd(a, b):#6,3
            while b:#3
                a, b = b, a % b #  6,3=3,0 Keep reducing until remainder is 0
            return a#1
        
        gcd_length = find_gcd(len(str1), len(str2))
        
        # Step 3: Return the substring from str1
        return str1[:gcd_length]

sol = Solution()
print(sol.gcdOfStrings("ABCABC", "ABC"))  
print(sol.gcdOfStrings("ABABAB", "ABAB"))  
print(sol.gcdOfStrings("LEET", "CODE"))   
