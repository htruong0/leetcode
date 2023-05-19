class Solution:
    def threeSumSets(self, nums: list[int]) -> list[list[int]]:
        result = set()
        nums = sorted(nums)
        seen = {}

        for c in nums:
            for a, v in seen.items():
                # assume potential solution
                b = -a-c
                # if b isn't in seen then can't use it
                if b not in seen:
                    continue
                # skip duplicate combination
                if b == a and v == 1:
                    continue
                # keep combination orders consistent
                if b < a:
                    a, b = b, a
                result.add((a, b, c))
            # add elements to seen from outer loop
            # elements in seen become 'a' in the inner loop
            if c not in seen:
                seen[c] = 1
            else:
                seen[c] += 1
        return result


    def threeSumPointers(self, nums: list[int]) -> list[list[int]]:
        # need to sort nums for this method to work
        nums = sorted(nums)
        result = []
        n = len(nums)
        for i in range(n-2):
            # skip duplicate combinations
            if i > 0 and nums[i] == nums[i-1]:
                continue
                
            # left can't be i so choose +1
            # don't need to check smaller elements
            # as they aren't big enough to sum to 0
            # right is last element
            left = i+1
            right = n-1
            
            # if left ==  right then invalid combination
            while left < right:
                current = nums[i] + nums[left] + nums[right]
                if current < 0:
                    left += 1
                elif current > 0:
                    right -= 1
                else:
                    result.append([nums[i], nums[left], nums[right]])
                    # skip duplicates on left side
                    while left < right and nums[left] == nums[left+1]:
                        left += 1
                    # skip duplicates on right side
                    while left < right and nums[right] == nums[right-1]:
                        right -= 1
                    left += 1
                    right -= 1

        return result
    
if __name__ == "__main__":
    nums = [-1,0,1,2,-1,-4]
    sol = Solution()
    a = sol.threeSumPointers(nums)
    b = sol.threeSumSets(nums)
    print(a, b)
