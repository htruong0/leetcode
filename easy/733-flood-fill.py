class Solution:
    def floodFillWhile(
            self,
            image: list[list[int]],
            sr: int,
            sc: int,
            colour: int
        ) -> list[list[int]]:
        max_y = len(image)-1
        max_x = len(image[0])-1
        pv0 = image[sr][sc]
        toFill = [i for i in self.adjacentIndex(sr, sc, max_y, max_x) if image[i[0]][i[1]] == pv0]
        toFill.append([sr, sc])

        searching = True
        while searching:
            if not toFill:
                searching = False
            for p in toFill:
                y, x = p[0], p[1]
                ret = self.adjacentIndex(y, x, max_y, max_x)
                new = [i for i in ret if i not in toFill and image[i[0]][i[1]] == pv0]
                if any(new):
                    toFill.extend(new)
                else:
                    searching = False
        for (y, x) in toFill:
            image[y][x] = colour
        return image
    
    def adjacentIndex(self, sr: int, sc: int, max_y: int, max_x: int) -> list[list[int]]:
        up = [max(0, sr-1), sc]
        right = [sr, min(sc+1, max_x)]
        down = [min(sr+1, max_y), sc]
        left = [sr, max(0, sc-1)]
        dirs = [x for x in [up, right, down, left] if x != [sr, sc]]
        return dirs
    
    def floodFillRecursive(
            self,
            image: list[list[int]],
            sr: int,
            sc: int,
            colour: int
        ) -> list[list[int]]:
        pv0 = image[sr][sc]
        max_y = len(image)
        max_x = len(image[0])

        def fillOne(image: list[list[int]], sr: int, sc: int):
            if sr < 0 or sr >= max_y or sc < 0 or sc >= max_x or image[sr][sc] != pv0 or image[sr][sc] == colour:
                return
            
            if image[sr][sc] == pv0:
                image[sr][sc] = colour
            fillOne(image, sr+1, sc)
            fillOne(image, sr-1, sc)
            fillOne(image, sr, sc+1)
            fillOne(image, sr, sc-1)
            return
        
        fillOne(image, sr, sc)
        return image
            
        
if __name__ == "__main__":
    image = [[1,1,1],[1,1,0],[1,0,1]]
    sr = 1
    sc = 1
    colour = 2
    sol = Solution()
    a = sol.floodFillRecursive(image, sr, sc, colour)
    b = sol.floodFillWhile(image, sr, sc, colour)
    assert a == b
    print(a)
