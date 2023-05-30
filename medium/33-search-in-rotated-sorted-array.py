class Solution:
    def search(self, nums: list[int], target: int) -> int:
        start = 0
        end = len(nums) - 1
        
        while start <= end:
            mid = (start + end) // 2
            
            if target == nums[mid]:
                return mid
            # upper half array
            elif nums[mid] >= nums[start]:
                if nums[start] <= target <= nums[mid]:
                    end = mid - 1
                # pivot to lower half array
                else:
                    start = mid + 1
            # lower half array
            else:
                if nums[mid] <= target <= nums[end]:
                    start = mid + 1
                # pivot to upper half array
                else:
                    end = mid - 1
        return
    

if __name__ == "__main__":
    nums = [4,5,6,7,0,1,2]
    target = 0
    sol = Solution()
    a = sol.search(nums, target)
    print(a)