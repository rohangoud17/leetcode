class Solution(object):
    def floodFill(self, image, sr, sc, color):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type color: int
        :rtype: List[List[int]]
        """

        ROWS, COLS = len(image), len(image[0])
        q = collections.deque()
        og_color = image[sr][sc]
        image[sr][sc] = color
        r,c = sr,sc
        
        visit = set()

        visit.add((r, c))

        q.append((sr,sc))

        directions = [[1,0], [-1,0], [0,1], [0,-1]]
        while q:
            new_r, new_c = q.popleft()
            for dr,dc in directions:
                r, c = new_r + dr, new_c + dc
                if ( r >= 0 and r < ROWS and c >= 0 and c < COLS and image[r][c] == og_color and (r,c) not in visit):
                    image[r][c] = color
                    q.append((r,c))
                    visit.add((r,c))
        
        return image


        

        

            



        
                
        