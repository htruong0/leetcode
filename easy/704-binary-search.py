class Solution:
    def search(self, nums: list[int], target: int) -> int:
        '''
        This binary search is O(log n) since you half the search area each time.
        You will need at worst log_2(n) comparisons to find your target.
        '''
        start = 0
        end = len(nums) - 1

        # if start > end then target won't be found
        while start <= end:
            # continually bisect search area
            mid = (start + end) // 2
            # found target
            if target == nums[mid]:
                return mid
            # if target in lower half, limit search to lower half
            elif target < nums[mid]:
                end = mid - 1
            # if target in upper half, limit search to upper half
            elif target > nums[mid]:
                start = mid + 1
        
        return -1
    

if __name__ == "__main__":
    nums = [-1,0,3,5,9,12]
    target = 9
    sol = Solution()
    a = sol.search(nums, target)
    print(a)
