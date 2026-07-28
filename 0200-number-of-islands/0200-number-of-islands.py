class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        numIslands = 0
        visit = set()

        ROWS, COLS = len(grid), len(grid[0])

        def bfs(r,c):
            q = collections.deque()
            visit.add((r,c))
            q.append((r,c))

            directions = [[1,0], [-1,0], [0,1], [0,-1]]
            while q:
                new_r, new_c = q.popleft()
                for dr, dc in directions:
                    r, c = dr + new_r, dc + new_c
                    if (r >= 0 and r < ROWS and c >=0 and c < COLS and grid[r][c] == '1' and (r,c) not in visit):
                        visit.add((r,c))
                        q.append((r,c))
                
        for r in range(ROWS):
            for c in range(COLS):
                if (grid[r][c] == '1' and (r,c) not in visit):
                    bfs(r,c)
                    numIslands += 1
        
        return numIslands
                

        