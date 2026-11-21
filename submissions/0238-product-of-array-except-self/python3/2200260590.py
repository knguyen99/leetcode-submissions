class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        
        ret = []
        l = 1
        for i in nums:
            ret.append(l)
            l *= i
        
        r = 1
        for i in reversed(range(len(nums))):
            ret[i] *= r
            r *= nums[i]
        return ret