class Solution:
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    def closedIsland(self, grid: List[List[int]]) -> int:
        self.ans = 0
        
        visited = set()
        for i in range(1, len(grid) - 1):
            for j in range(1, len(grid[i]) - 1):
                current = grid[i][j]
                if (i, j) in visited:
                    continue
                if current == 1:
                    continue
                # visited.add((i, j))
                ret = self.search(i, j, grid, visited)
                if ret:
                    self.ans += 1
        
        return self.ans

    def search(self, x, y, grid, visited):
        if (x, y) in visited:
            return True
        
        if x == 0 or x == len(grid) - 1 or y == 0 or y == len(grid[x]) - 1:
            return False
        
        visited.add((x, y))
        ret = []
        for i in range(4):
            nx = x + self.dx[i]
            ny = y + self.dy[i]
            if nx < 0 or nx >= len(grid) or ny < 0 or ny >= len(grid[x]):
                continue
            if grid[nx][ny] == 1:
                continue
            ret.append(self.search(nx, ny, grid, visited))
        for r in ret:
            if (r == False):
                return False
        return True
        