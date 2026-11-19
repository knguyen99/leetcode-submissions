class Solution:
    def rob(self, nums: list[int]) -> int:
        rob = 0
        norob = 0
        for num in nums:
            temp = max(rob, norob + num)
            norob = rob
            rob = temp
        return rob
