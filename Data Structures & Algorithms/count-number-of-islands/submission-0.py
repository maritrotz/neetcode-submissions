class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def bfs(r,c):
            q = deque()
            visited.add((r,c))
            q.append((r,c))

            while q:
                r,c = q.pop()
                directions = [[1,0],[-1,0],[0,1],[0,-1]]
                for dr,dc in directions:
                    if (dr+r) in range(rows) and (dc+c) in range(cols) and ((dr+r),(dc+c)) not in visited and grid[dr+r][dc+c] == '1':
                        q.append((dr+r,dc+c))
                        visited.add((dr+r,dc+c))
        if not grid:
            return 0

        visited = set()
        islands = 0
        rows,cols = len(grid),len(grid[0])

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1'and (r,c) not in visited:
                    bfs(r,c)
                    islands+=1
        return islands
