class Solution:
    def maxArea(self, height: list[int]) -> int:
        left = 0
        right = len(height)-1
        maxA = 0

        while left < right:
            lh = height[left]
            rh = height[right]
            maxA = max(maxA, (right-left)*min(lh, rh))
            if lh < rh:
                left += 1
            else:
                right -= 1

        return maxA
    

if __name__ == "__main__":
    height = [1,8,6,2,5,4,8,3,7]
    sol = Solution()
    a = sol.maxArea(height)
    print(a)
