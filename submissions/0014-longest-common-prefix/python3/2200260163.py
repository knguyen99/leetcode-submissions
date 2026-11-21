class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        prefix = ""

        min_word = min(strs, key=lambda x: len(x))

        for i in range(len(min_word)):
            char = min_word[i]
            for j in range(len(strs)):
                if strs[j][i] != char:
                    return prefix
            prefix += char
        return prefix