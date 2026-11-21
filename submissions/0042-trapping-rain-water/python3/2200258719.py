class Solution:
    def trap(self, height: list[int]) -> int:
        lptr = 0
        rptr = len(height) - 1
        lheight = 0
        rheight = 0
        total = 0
        while lptr < rptr:
            if height[lptr] < height[rptr]:
                total += max(0, lheight - height[lptr])
                lheight = max(lheight, height[lptr])
                lptr += 1
            else:
                total += max(0, rheight - height[rptr])
                rheight = max(rheight, height[rptr])
                rptr -= 1
        return total