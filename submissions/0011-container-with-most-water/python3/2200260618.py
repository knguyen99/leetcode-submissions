class Solution:
    def maxArea(self, height: list[int]) -> int:
        ret = 0
        l = 0
        r = len(height) - 1
        
        while l < r:
            ret = max(ret, min(height[l], height[r]) * (r - l))
            if height[l] > height[r]:
                r -= 1
            else:
                l += 1
        return ret