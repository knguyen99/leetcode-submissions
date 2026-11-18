class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        available_rooms = list(range(n))
        heapify(available_rooms)
        in_use = []
        freq = [0] * n
        meetings.sort(key = lambda x: x[0])

        for start, end in meetings:
            while in_use and in_use[0][0] <= start:
                heappush(available_rooms, heappop(in_use)[1])

            if available_rooms:
                room_id = heappop(available_rooms)
                heappush(in_use, (end, room_id))
            else:
                free_at, room_id = heappop(in_use)
                heappush(in_use, (free_at + (end - start), room_id))
            freq[room_id] += 1
        
        return freq.index(max(freq))