class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        def bfs(r,c):
            q = deque()
            q.append((r,c))
            visited.add((r,c))
            areaVal = 1

            while q:
                r,c = q.popleft()
                directions = [[0,1],[0,-1],[1,0],[-1,0]]
                for dr,dc in directions:
                    if (dr + r) in range(rows) and (dc + c) in range(cols) and ((dr + r,dc + c)) not in visited and grid[dr + r][dc + c] == 1:
                        q.append((dr + r,dc + c))
                        visited.add((dr + r,dc + c))
                        areaVal += 1
            
            return areaVal

        
        if not grid:
            return 0

        visited = set()
        rows,cols = len(grid),len(grid[0])
        maxArea = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r,c) not in visited:
                    maxArea = max(maxArea,bfs(r,c))
        
        return maxArea
