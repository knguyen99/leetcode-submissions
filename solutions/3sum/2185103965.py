class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        idx_map = {}

        for i in range(len(nums)):
            idx_map[nums[i]] = i
        
        i = 0
        while i < len(nums):
            j = i + 1
            while i < j < len(nums):
                curr = nums[i] + nums[j]
                if curr > 0:
                    break
                if -curr in idx_map and idx_map[-curr] > j:
                    res.append([nums[i], nums[j], nums[idx_map[-curr]]])
                    i = idx_map[nums[i]]
                    j = idx_map[nums[j]]
                j += 1
            i += 1
        return res