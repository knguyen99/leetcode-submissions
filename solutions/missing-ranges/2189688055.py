class Solution:
    def findMissingRanges(self, nums: list[int], lower: int, upper: int) -> list[list[int]]:
        if len(nums) == 0:
            return [[lower, upper]]
        
        ret = []
        prev_num = lower

        if lower < nums[0]:
            ret.append([lower, nums[0] - 1])
            prev_num = nums[0]

        for num in nums:
            if num - prev_num > 1:
                ret.append([prev_num + 1, num - 1])
            prev_num = num
        
        if prev_num < upper:
            ret.append([prev_num + 1, upper])
        
        return ret