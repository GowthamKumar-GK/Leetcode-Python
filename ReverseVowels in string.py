class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = set("aeiouAEIOU")
        s = list(s)  # Convert string to list for easy swapping
        left, right = 0, len(s) - 1
        
        while left < right:
            while left < right and s[left] not in vowels:
                left += 1
            while left < right and s[right] not in vowels:
                right -= 1
            
            s[left], s[right] = s[right], s[left]  # Swap vowels
            left += 1
            right -= 1
        
        return "".join(s)  # Convert list back to string

# Testing the function
if __name__ == "__main__":
    sol = Solution()
    test_str = "IceCreAm"
    print(sol.reverseVowels(test_str))  # Output: "AceCreIm"
