class DSU:
    def __init__(self):
        self.parent = {}
        self.size = {}
    
    def put(self, node):
        if (self.parent.get(node, -1) == -1):
            self.parent[node] = node
            self.size[node] = 1
            return node
    
    def find(self, node):
        if (self.parent.get(node, -1) == -1):
            self.parent[node] = node
            self.size[node] = 1
            return node
        p = self.parent[node]
        if (p != node):
            self.parent[node] = self.find(p)
        return self.parent[node]
    
    def union(self, x, y):
        px = self.find(x)
        py = self.find(y)
        if (px == py):
            return py
        if (self.size[px] > self.size[py]):
            tmp = py
            py = px
            px = tmp
        self.parent[px] = py
        self.size[py] += self.size[px]
        return self.find(y)

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        dsu = DSU()
        for num in nums:
            dsu.put(num)
        
        for num in nums:
            if (dsu.parent.get(num - 1, -1) != -1):
                dsu.union(num, num - 1)
            if (dsu.parent.get(num + 1, -1) != -1):
                dsu.union(num, num + 1)
        
        ans = 0
        for num in nums:
            ans = max(ans, dsu.size[num])
        return ans
            