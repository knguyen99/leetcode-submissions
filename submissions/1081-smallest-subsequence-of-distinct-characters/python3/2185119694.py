class Solution:
    def smallestSubsequence(self, s: str) -> str:
        seen = set()
        d = {}
        for i in range(len(s)):
            d[s[i]] = i
        ret = []
        for i in range(len(s)):
            if s[i] not in seen:
                while ret and s[i] < ret[-1] and i < d[ret[-1]]:
                    seen.remove(ret.pop())
                seen.add(s[i])
                ret.append(s[i])
        return "".join(ret)