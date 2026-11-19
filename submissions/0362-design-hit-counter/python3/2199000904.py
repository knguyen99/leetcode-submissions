import bisect
class HitCounter:

    def __init__(self):
        self.arr = []

    def hit(self, timestamp: int) -> None:
        self.arr.append(timestamp)

    def getHits(self, timestamp: int) -> int:
        target = timestamp - 300
        idx = bisect.bisect_right(self.arr, target)
        if idx == len(self.arr):
            self.arr = []
            return 0
        else:
            return len(self.arr) - idx


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)