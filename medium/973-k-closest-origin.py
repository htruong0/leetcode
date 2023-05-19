class Solution:
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        # can just keep distance squared to save a sqrt
        points = sorted(points, key=lambda x: x[0]**2 + x[1]**2)
        return points[:k]
    

if __name__ == "__main__":
    points = [[3,3],[5,-1],[-2,4]]
    k = 2
    sol = Solution()
    a = sol.kClosest(points, k)
    print(a)
