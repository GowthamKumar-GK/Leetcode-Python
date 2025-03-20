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
