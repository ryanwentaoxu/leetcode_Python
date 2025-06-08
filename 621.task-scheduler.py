import heapq
import functools

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = [0 for i in range(26)]
        for task in tasks:
            freq[ord(task) - ord('A')] +=1
        pq = []
        for f in freq:
            if (f != 0):
                heapq.heappush(pq, -f)

        ans = 0
        while pq:
            count = 0
            counter = n + 1
            remain = []
            while pq and count < counter:
                count += 1
                tmp = heapq.heappop(pq)
                if (tmp < -1):
                    remain.append(tmp + 1)
            
            for r in remain:
                heapq.heappush(pq, r)
            if pq:
                ans += n + 1
            else:
                ans += count
        return ans