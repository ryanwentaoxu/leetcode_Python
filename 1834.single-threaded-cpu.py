import functools
import heapq

class State:
    def __init__(self, index, enqTime, processTime):
        self.index = index
        self.enqTime = enqTime
        self.processTime = processTime
    
    def __lt__(self, other):
        if self.processTime == other.processTime:
            return self.index < other.index
        return self.processTime < other.processTime

def c(a, b):
    if a.enqTime < b.enqTime:
        return -1
    elif a.enqTime == b.enqTime:
        return 0
    return 1

class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        s = []
        for i in range(len(tasks)):
            s.append(State(i, tasks[i][0], tasks[i][1]))
        states = sorted(s, key = functools.cmp_to_key(c))
        time = 0
        pq = []
        i = 0
        ans = []
        while i < len(states):
            if time < states[i].enqTime and not pq:
                time = states[i].enqTime
            
            while i < len(states) and time >= states[i].enqTime:
                heapq.heappush(pq, states[i])
                i += 1

            if pq:
                current = heapq.heappop(pq)
                ans.append(current.index)
                time = time + current.processTime
        while pq:
            current = heapq.heappop(pq)
            ans.append(current.index)
        return ans
            