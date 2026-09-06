class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def bfs(r,c):
            q = deque()
            q.append((r,c))
            visited.add((r,c))

            while q:
                r,c = q.popleft()
                directions = [[1,0],[-1,0],[0,1],[0,-1]]
                for dr,dc in directions:
                    if (dr + r) in range(rows) and (dc + c) in range(cols) and grid[dr + r][dc + c] == '1' and ((dr + r,dc + c)) not in visited:
                        q.append((dr + r,dc + c))
                        visited.add((dr + r,dc + c))




        if not grid:
            return 0
    
        
        rows,cols = len(grid),len(grid[0])
        visited = set()
        numIslands = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1' and (r,c) not in visited:
                    bfs(r,c)
                    numIslands += 1
        return numIslands