class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
            
        q = deque()
        visited = set()
        rows,cols = len(grid), len(grid[0])
        minutes = 0
        self.fresh = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    q.append((r,c))
                    visited.add((r,c))
                elif grid[r][c] == 1:
                    self.fresh += 1
    
        def bfs(r,c):
            directions = [[0,1], [0,-1], [1,0], [-1,0]]
            for dr, dc in directions:
                nr, nc = dr + r, dc + c
                if nr in range(rows) and nc in range(cols) and (nr,nc) not in visited and grid[nr][nc] == 1:
                    grid[nr][nc] = 2
                    q.append((nr,nc))
                    visited.add((nr,nc))
                    self.fresh -= 1

        while q and self.fresh > 0:
            for i in range(len(q)):
                r,c = q.popleft()
                bfs(r,c)
            minutes += 1
        return minutes if self.fresh == 0 else -1