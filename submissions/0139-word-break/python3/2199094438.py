class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        dp = [False] * (len(s))
        for i in range(len(s)):
            for word in wordDict:
                if i - len(word)  + 1 < 0:
                    continue
                if i == len(word) - 1 or dp[i - len(word)]:
                    if s[i - len(word) + 1: i + 1] == word:
                        dp[i] = True
                        break
        print(dp)
        return dp[-1]
