class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        start, end = 0,0
        
        def expand(i,j):
            nonlocal start, end
            while i >= 0 and j < len(s) and s[i] == s[j]:
                if end - start < j - i:
                    start, end = i, j
                i -= 1
                j += 1
            
        
        for i in range(len(s)):
            expand(i,i)
            if i != 0:
                expand(i-1, i)
        return s[start:end + 1]