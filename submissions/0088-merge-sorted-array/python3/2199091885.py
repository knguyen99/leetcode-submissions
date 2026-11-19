class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        l,r = m - 1, n -1
        for i in reversed(range(m+n)):
            if r < 0:
                break
            if l >= 0 and nums1[l] > nums2[r]:
                nums1[i] = nums1[l]
                l -= 1
            else:
                nums1[i] = nums2[r]
                r -= 1
                    