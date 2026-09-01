class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        def bfs(r,c):
            q = deque()
            q.append((r,c))
            visited.add((r,c))

            while q:
                r,c = q.popleft()
                directions = [[0,1],[0,-1],[1,0],[-1,0]]
                for dr,dc in directions:
                    if (dr+r) in range(Rows) and (dc+c) in range(Cols) and grid[dr+r][dc+c] == '1' and ((dr+r,dc+c)) not in visited:
                        q.append((dr+r,dc+c))
                        visited.add((dr+r,dc+c))

        if not grid:
            return 0

        Rows, Cols = len(grid),len(grid[0])
        numIslands = 0
        visited = set()

        for r in range(Rows):
            for c in range(Cols):
                if grid[r][c] == '1' and (r,c) not in visited:
                    bfs(r,c)
                    numIslands +=1
        return numIslands




        