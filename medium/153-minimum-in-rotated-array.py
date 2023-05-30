class Solution:
    def findMin(self, nums: list[int]) -> int:
        # nums has two subarrays:
        # upper half array will be on the left
        # lower half array will be on the right
        # we binary search until we get into the lower half array
        start = 0
        end = len(nums) - 1
        res = nums[0]

        while start <= end:
            # in the lower half array
            if nums[start] < nums[end]:
                res = min(res, nums[start])
                break
            mid = (start + end) // 2
            res = min(res, nums[mid])
            if nums[mid] >= nums[start]:
                start = mid + 1
            else:
                end = mid - 1
        return res
    

if __name__ == "__main__":
    nums = [4,5,6,7,0,1,2]
    sol = Solution()
    a = sol.findMin(nums)
    print(a)