class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        non_obstacles = 0
        start_row, start_col = 0, 0
        for row in range(0, rows):
            for col in range(0, cols):
                if grid[row][col] >= 0:
                    non_obstacles += 1
                if grid[row][col] == 1:
                    start_row, start_col = row, col
        ans = 0
        
        def back_track(row, col, remain):
            nonlocal ans
            if grid[row][col] == 2 and remain == 1:
                ans += 1
                return
            
            tmp = grid[row][col]
            grid[row][col] = -4
            remain -= 1

            for r, c in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nr, nc = row + r, col + c
                if nr < 0 or nr >= rows or nc < 0 or nc >= cols:
                    continue
                
                if grid[nr][nc] < 0:
                    continue
                
                back_track(nr, nc, remain)
            grid[row][col] = tmp
        
        back_track(start_row, start_col, non_obstacles)

        return ans