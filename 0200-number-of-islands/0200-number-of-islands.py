class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid:
            return 0
        
        islands = 0
        rows, col = len(grid), len(grid[0])
        visit = set()

        def bfs(r,c):
            q = collections.deque()
            visit.add((r,c))
            q.append((r,c))

            while(q):
                row, colu = q.popleft()
                directions = [[1,0],[-1,0], [0,1], [0,-1]]

                for dr, dc in directions:
                    r , c = row + dr, colu + dc
                    if (r in range(rows) and c in range(col)and grid[r][c] == '1' and (r,c) not in visit):
                        q.append((r,c))
                        visit.add((r,c))


        for r in range(rows):
            for c in range(col):
                if grid[r][c] == '1' and (r,c) not in visit:
                    bfs(r,c)
                    islands += 1

        # print(visit)
                    

                
        
        return islands 

        