class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        ROWS, COLUMNS = len(grid), len(grid[0])
        fresh = 0
        q = collections.deque()
        minutes = 0


        for r in range(ROWS):
            for c in range(COLUMNS):
                if grid[r][c] == 1:
                    fresh += 1
                elif grid[r][c] == 2:
                    q.append([r,c])
                
        directions = [[1,0], [-1, 0], [0,1], [0,-1]]

        while (q and fresh > 0):
            
            for i in range(len(q)):
                new_row, new_col = q.popleft()
                for dr, dc in directions:
                    r, c = new_row + dr, new_col + dc
                    if (r < 0 or r >= ROWS or c < 0 or c >= COLUMNS or grid[r][c] != 1 ):
                        continue
                    else:
                        grid[r][c] = 2
                        q.append([r,c])
                        fresh -= 1
            minutes += 1
        
        return minutes if fresh == 0 else -1
                    
        


        