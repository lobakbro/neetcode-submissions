class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        row, col = len(grid), len(grid[0])
        islands = 0
        def bfs(r,c):
            q = deque([(r,c)])
            grid[r][c] = '0'
            while q:
                curr_r, curr_c = q.popleft()
                # top bot l r
                for dr, dc in [(-1, 0), (1,0),(0,-1), (0,1)]:
                    nr, nc = curr_r +dr, curr_c + dc
                    if 0<=nr <row and 0 <= nc < col and grid[nr][nc]=='1':
                        grid[nr][nc] = '0'
                        q.append((nr,nc))
        for r in range(row):
            for c in range(col):
                if grid[r][c] == '1':
                    islands +=1
                    bfs(r,c)
        return islands
