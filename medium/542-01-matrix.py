class Solution:
    def updateMatrix(self, mat: list[list[int]]) -> list[list[int]]:
        rows = len(mat)
        cols = len(mat[0])
        result = [[float("inf") for _ in range(cols)] for _ in range(rows)]
        # do a BFS
        queue = []

        # set zeros to 0, keep others as inf
        for i in range(rows):
            for j in range(cols):
                if mat[i][j] == 0:
                    queue.append([i, j])
                    result[i][j] = 0

        # no diagonals
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        while queue:
            y, x = queue.pop(0)
            # look in every direction
            for (dy, dx) in directions:
                new_y = y + dy
                new_x = x + dx
                # boundary conditions
                if 0 <= new_y < rows and 0 <= new_x < cols:
                    # if the adjacent cells are bigger than the current cell
                    # then we set the new cell to the old cell + 1
                    # since we're searching from zeros, this adds 1 each
                    # step away from a zero.
                    # all subsequent search cells will keep adding 1
                    if result[new_y][new_x] > result[y][x] + 1:
                        result[new_y][new_x] = result[y][x] + 1
                        queue.append([new_y, new_x])
        return result
    
if __name__ == "__main__":
    mat = [[0,0,0],[0,1,0],[1,1,1]]
    sol = Solution()
    a = sol.updateMatrix(mat)
    print(a)
