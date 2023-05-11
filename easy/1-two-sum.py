class Solution:
    def twoSumSquare(self, nums, target):
        for i in range(len(nums)-1, 0, -1):
            for j in range(i):
                if nums[i] + nums[j] == target:
                    return [i, j]

    def twoSumLinear(self, nums, target):
        seen = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in seen:
                return [seen[diff], i]
            else:
                seen[nums[i]] = i

if __name__ == "__main__":
    nums = [3,2,4]
    target = 6
    sol = Solution()
    a = sol.twoSum(nums, target)
    print(sorted(a))
