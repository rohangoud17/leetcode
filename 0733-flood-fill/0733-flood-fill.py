class Solution(object):
    def floodFill(self, image, sr, sc, color):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type color: int
        :rtype: List[List[int]]
        """
        

        ROWS, COLUMNS = len(image), len(image[0])
        visit = set()

        q = collections.deque()
        og_color = image[sr][sc]
        r, c = sr, sc
        q.append((r, c))
        visit.add((r,c))
        image[sr][sc] = color

        directions = [[1,0], [-1,0], [0,1], [0,-1]]

        while q:
            new_row, new_col = q.popleft()
            for dr, dc in directions:
                r, c = new_row + dr, new_col + dc
                if (r < ROWS and r >= 0 and c >= 0 and c < COLUMNS and image[r][c] == og_color and (r,c) not in visit):
                    image[r][c] = color
                    q.append((r,c))
                    visit.add((r,c))
        
        return image


            



        
                
        