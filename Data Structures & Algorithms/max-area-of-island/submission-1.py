class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows,cols = len(grid), len(grid[0])
        visit = set()
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        res = 0
        if not grid:
            return 0
        def bfs(r,c):
            queue = deque()
            queue.append((r,c))
            visit.add((r,c))
            area = 1
            while queue:
                row, col = queue.popleft()
                for rd, cd in directions:
                    nr, nc = row + rd, col + cd
                    if (nr in range(rows) and nc in range(cols)
                        and (nr,nc) not in visit and grid[nr][nc] == 1):
                        queue.append((nr,nc))
                        visit.add((nr,nc))
                        area += 1
            return area
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r,c) not in visit:
                    res = max(res,bfs(r,c))
        return res
                    