class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        visited = set()
        rows,cols = len(grid),len(grid[0])
        numIslands = 0
        def dfs(r,c):
            q = deque()
            q.append((r,c))
            visited.add((r,c))

            while q:
                r,c = q.pop()
                directions = [[0,1],[0,-1],[1,0],[-1,0]]
                for dr,dc in directions:
                    if (dr+r) in range(rows) and (dc+c) in range(cols) and grid[dr+r][dc+c] == '1' and (dr+r,dc+c) not in visited:
                        q.append((dr+r,dc+c))
                        visited.add((dr+r,dc+c))

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1' and (r,c) not in visited:
                    dfs(r,c)
                    numIslands+=1
        return numIslands




        