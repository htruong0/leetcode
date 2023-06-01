class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        rows = len(matrix)
        cols = len(matrix[0])
        row_vector = []
        col_vector = []

        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 0:
                    row_vector.append(i)
                    col_vector.append(j)

        for row in row_vector:
            for j in range(cols):
                matrix[row][j] = 0
                
        for col in col_vector:
            for i in range(rows):
                matrix[i][col] = 0
        

if __name__ == "__main__":
    matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
    sol = Solution()
    sol.setZeroes(matrix)
    print(matrix)
