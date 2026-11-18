from collections import deque
class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: list[str]) -> int:
        
        seen = set()
        search = deque([(startGene,0)])


        while search:
            curr, muts = search.popleft()
            if curr == endGene:
                return muts
            for letter in "ACGT":
                for i in range(len(curr)):
                    next_str = curr[:i] + letter + curr[i+1:]
                    if next_str not in seen and next_str in bank:
                        search.append((next_str, muts + 1))
                        seen.add(next_str)
        return -1 
        

        