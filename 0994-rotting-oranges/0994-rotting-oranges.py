class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        ROWS, COLS = len(grid), len(grid[0])
        visit = set()
        q = collections.deque()

        fresh = 0
        minutes = 0

        for r in range(ROWS):
            for c in range(COLS):
                if (grid[r][c] == 1):
                    fresh+= 1
                elif (grid[r][c] == 2):
                    q.append([r,c])
                
        
        directions = [[1,0],[-1,0],[0,1],[0,-1]]
        while (q and fresh >= 1):
            for i in range(len(q)):
                new_r, new_c = q.popleft()
                for dr, dc in directions:
                    r, c = new_r + dr, new_c + dc
                    if (r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0]) or grid[r][c] != 1 or (r,c) in visit):
                        continue
                    grid[r][c] = 2
                    visit.add((r,c))
                    q.append([r,c])
                    fresh -= 1
            minutes += 1
        
        print(fresh)
        
        return minutes if fresh == 0 else -1


    




        