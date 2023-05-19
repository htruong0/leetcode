class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        n = len(nums)
        result = [1]*n

        # product of all numbers before nums[i]
        prefix = 1
        for i in range(n):
            result[i] = prefix
            prefix *= nums[i]

        # product of all numbers after nums[i]
        postfix = 1
        for i in range(n-1, -1, -1):
            result[i] *= postfix
            postfix *= nums[i]

        return result
    
if __name__ == "__main__":
    nums = [1,2,3,4]
    sol = Solution()
    a = sol.productExceptSelf(nums)
    print(a)
