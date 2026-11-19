class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2
        one_count = 1
        two_count = 2
        for i in range(3, n):
            curr = one_count + two_count
            one_count = two_count
            two_count = curr
        return one_count + two_count