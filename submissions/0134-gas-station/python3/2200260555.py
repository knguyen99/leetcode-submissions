class Solution:
    def canCompleteCircuit(self, gas: list[int], cost: list[int]) -> int:
        total = 0
        curr = 0
        start = 0

        for i in range(len(gas)):
            curr += gas[i] - cost[i]
            total += gas[i] - cost[i]
            if curr < 0:
                curr = 0
                start = i + 1
        return start if total >= 0 else -1
