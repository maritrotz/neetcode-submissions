class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def dfs(r,c):
            if r < 0 or c < 0 or r == Rows or c == Cols or grid[r][c] == 0 or (r,c) in visited:
                return 0
            visited.add((r,c))
            return (1 + dfs(r + 1,c) + dfs(r - 1,c) + dfs(r,c + 1) + dfs(r,c - 1))

        Rows,Cols = len(grid),len(grid[0])
        visited = set()
        maxIslands = 0

        for r in range(Rows):
            for c in range(Cols):
                maxIslands = max(maxIslands,dfs(r,c))
        return maxIslands
        