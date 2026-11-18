class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        intervals.sort(key=lambda x: x[1])
        count = 0
        k = -math.inf
        for start, end in intervals:
            if start >= k:
                k = end
            else:
                count += 1
        return count 