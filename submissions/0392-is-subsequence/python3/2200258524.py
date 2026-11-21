class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if s == "":
            return True
        sptr = 0
        for i in range(len(t)):
            if t[i] == s[sptr]:
                sptr += 1
            if sptr == len(s):
                return True
        return False