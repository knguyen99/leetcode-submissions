class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        
        def search(l_side):
            l = 0
            r = len(nums) - 1
            ans = -1
            while l <= r:
                mid = (l + r) // 2

                if nums[mid] > target:
                    r = mid -1
                elif nums[mid] < target:
                    l = mid + 1
                else:
                    ans = mid
                    if l_side:
                        r = mid - 1
                    else:
                        l = mid + 1
            return ans
                        
        return [search(True), search(False)]