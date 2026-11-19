from collections import defaultdict
class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        
        in_count = defaultdict(int)
        out_class = defaultdict(list)
        seen = [False] * numCourses
        search = []

        for post, pre in prerequisites:
            in_count[post] += 1
            out_class[pre].append(post)
        
        for i in range(numCourses):
            if in_count[i] == 0:
                search.append(i)
        
        while search:
            curr = search.pop()
            seen[curr] = True

            for next_class in out_class[curr]:
                in_count[next_class] -= 1
                if in_count[next_class] == 0 and not seen[next_class]:
                    search.append(next_class)
        return all(seen)