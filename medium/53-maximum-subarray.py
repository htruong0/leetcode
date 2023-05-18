class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        currentSum = nums[0]
        maxSum = nums[0]
        
        for i in range(1, len(nums)):
            currentSum += nums[i]
            if currentSum < nums[i]:
                currentSum = nums[i]
            if currentSum > maxSum:
                maxSum = currentSum
        return maxSum
    

if __name__ == "__main__":
    nums = nums = [-2,1,-3,4,-1,2,1,-5,4]
    sol = Solution()
    a = sol.maxSubArray(nums)
    print(a)
