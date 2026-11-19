class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        val = 0
        for num in nums:
            val ^= num
        return val