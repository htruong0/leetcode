class Solution:
    def rotateLayers(self, matrix: list[list[int]]) -> None:
        """Rotate array in-place."""
        left = 0
        right = len(matrix)-1

        # rotate outermost edge, then move in
        while left < right:
            # i keeps track of offset in row/column
            for i in range(right-left):
                # square matrix -> top = left, bottom = right
                top = left
                bottom = right

                # keep track of initial value to move later
                # rotate ccw so only need one tmp variable
                tmpVal = matrix[top][left+i]

                matrix[top][left+i] = matrix[bottom-i][left]
                matrix[bottom-i][left] = matrix[bottom][right-i]
                matrix[bottom][right-i] = matrix[top+i][right]
                matrix[top+i][right] = tmpVal

            # move to inwards layer
            left += 1
            right -= 1


    def rotateTransposeReflect(self, matrix: list[list[int]]) -> None:
        """Rotation = transpose + reflect on middle vertical axis."""
        rows = len(matrix)
        cols = len(matrix)
        # ceil division
        axis = -(rows // -2)

        # transpose
        for i in range(rows):
            for j in range(i):
                matrix[j][i], matrix[i][j] = matrix[i][j], matrix[j][i]

        # reflect
        for i in range(axis):
            for j in range(rows):
                matrix[j][i], matrix[j][cols-1-i] = matrix[j][cols-1-i], matrix[j][i]



if __name__ == "__main__":
    from copy import deepcopy
    matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
    m = deepcopy(matrix)
    sol = Solution()
    a = sol.rotateLayers(matrix)
    b = sol.rotateLayers(m)
    assert a == b
    print(matrix)
