class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        
        q = collections.deque()
        rows, cols = len(grid), len(grid[0])
        fresh = 0
        minutes = 0

        for r in range(rows):
            for c in range(cols):
                if(grid[r][c] == 1):
                    fresh += 1
                elif (grid[r][c] == 2):
                    q.append([r,c])
        print(fresh)
        directions = [[1,0], [-1,0], [0,1], [0,-1]]
        while q and fresh > 0:
            for i in range(len(q)):
                new_row, new_col = q.popleft()
                for dr, dc in directions:
                    r, c = new_row + dr, new_col + dc
                    if ((r < 0 or r >= len(grid)) or (c < 0 or c >= len(grid[0])) or
                        grid[r][c] != 1  ):
                        continue
                    grid[r][c] = 2
                    q.append([r,c])
                    fresh -= 1
                    
            minutes += 1
        
        print(fresh)
        return minutes if fresh == 0 else -1
    


        

        
        