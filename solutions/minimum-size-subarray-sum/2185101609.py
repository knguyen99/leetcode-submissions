import bisect
class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        prefix = [0]
        ret = math.inf
        for num in nums:
            curr = prefix[-1] + num
            idx = bisect.bisect(prefix, curr - target)
            if idx > 0:
                ret = min(ret, len(prefix) - idx + 1)
            prefix.append(curr)
        return ret if ret != math.inf else 0
