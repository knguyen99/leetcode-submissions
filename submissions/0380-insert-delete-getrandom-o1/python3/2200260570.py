class RandomizedSet:

    def __init__(self):
        self.idx = {}
        self.arr = []

    def insert(self, val: int) -> bool:
        if val in self.idx:
            return False
        self.idx[val] = len(self.arr)
        self.arr.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.idx:
            return False
        self.arr[self.idx[val]] = self.arr[-1]
        self.idx[self.arr[-1]] = self.idx[val]
        self.arr.pop()
        self.idx.pop(val)
        return True

    def getRandom(self) -> int:
        return self.arr[random.randint(0,len(self.arr) - 1)]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()