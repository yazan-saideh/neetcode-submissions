class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        visit = set()
        island = 0
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        if not grid:
            return 0
        def bfs(r , c):
            queue = deque()
            queue.append((r,c))
            while queue:
                r,c = queue.popleft()
                for dr,dc in directions:
                    nr,nc = r+dr, c+dc
                    if (nr in range(rows) and nc in range(cols) and 
                    (nr,nc) not in visit and grid[nr][nc] == "1"):
                        queue.append((nr,nc))
                        visit.add((nr,nc))
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r,c) not in visit:
                    bfs(r,c)
                    island += 1
        return island
        
