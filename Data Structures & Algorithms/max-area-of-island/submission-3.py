class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def dfs(r,c):
            if r < 0 or c < 0 or r == rows or c == cols or (r,c) in visited or grid[r][c] == 0:
                return 0
            
            visited.add((r,c))
            return (1 + dfs(r + 1,c) + dfs(r - 1,c) + dfs(r,c + 1) + dfs(r,c - 1))

        visited = set()
        rows = len(grid)
        cols = len(grid[0])
        area = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r,c) not in visited:
                    area = max(area,dfs(r,c))
        return area

        