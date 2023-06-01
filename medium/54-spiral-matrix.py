class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        left, right = 0, len(matrix[0])
        top, bottom = 0, len(matrix)
        path = []
        size = right*bottom

        while left < right and top < bottom:
            # moving left
            for i in range(left, right):
                path.append(matrix[top][i])
            top += 1

            # moving down
            for i in range(top, bottom):
                path.append(matrix[i][right-1])
            right -= 1

            # check for single rows or single columns
            if len(path) == size:
                break

            # moving left
            for i in range(right-1, left-1, -1):
                path.append(matrix[bottom-1][i])
            left += 1

            # moving up
            for i in range(bottom-2, top-1, -1):
                path.append(matrix[i][left-1])
            bottom -= 1
        return path
    

if __name__ == "__main__":
    matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
    sol = Solution()
    a = sol.spiralOrder(matrix)
    print(a)
