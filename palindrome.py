class Solution:
    def isPalindrome(self, s):
        
        result = ""
        for char in s:
            if ('A' <= char <= 'Z') or ('a' <= char <= 'z') or ('0' <= char <= '9'):
                result += char.lower()
        
        # Check palindrome
        return result == result[::-1]

# Example usage
if __name__ == "__main__":
    s = "A man, a plan, a canal: Panama"
    solution = Solution()
    print(solution.isPalindrome(s))  # Output: True
