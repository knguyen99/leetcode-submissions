class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        
        for i in range(len(nums)):
            complement = target - nums[i]
            l, r = i + 1, len(nums) - 1
            while l <= r:
                mid = (l + r ) // 2
                if nums[mid] == complement:
                    return [i+1, mid + 1]
                elif nums[mid] > complement:
                    r = mid - 1
                else:
                    l = mid + 1
                

        return [-1, -1]