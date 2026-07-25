class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        if not grid:
            return 0

        islands = 0
        visit = set()
        rows, columns = len(grid), len(grid[0])

        def dfs(r,c):
            q = collections.deque()
            visit.add((r,c))
            q.append((r,c))

            while(q):
                new_row, new_col = q.pop()
                directions = [[1,0], [-1,0], [0,1], [0,-1]]

                for dr, dc in directions:
                    r, c = new_row + dr, new_col + dc
                    if (r in range(rows) and c in range(columns) and grid[r][c] == '1' and (r,c) not in visit):
                        visit.add((r,c))
                        q.append((r,c))


        for r in range(rows):
            for c in range(columns):
                if (grid[r][c] == '1' and (r,c) not in visit):
                    dfs(r,c)
                    islands += 1
        return islands
        