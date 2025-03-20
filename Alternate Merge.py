class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        merged = []
        i, j = 0, 0
        n, m = len(word1), len(word2)
        while i < n or j < m:
            if i < n:
                merged.append(word1[i])
                i += 1
            if j < m:
                merged.append(word2[j])
                j += 1
        
       
        return ''.join(merged)

word1 = input("Enter the first string (word1): ").strip()
word2 = input("Enter the second string (word2): ").strip()

# Create an instance of the Solution class
solution = Solution()

# Call the mergeAlternately method with user input
result = solution.mergeAlternately(word1, word2)

# Output the result
print("Merged string:", result)
