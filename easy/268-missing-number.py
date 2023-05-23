class Solution:
    def missingNumberSets(self, nums: list[int]) -> int:
        missing = set(range(len(nums)+1)) - set(nums)
        return next(iter(missing))
    
    def missingNumber(self, nums: list[int]) -> int:
        S = sum(nums)
        # sum of natural numbers
        Sn = len(nums)*(len(nums)+1)/2
        return int(Sn-S)
    

if __name__ == "__main__":
    nums = [3,0,1]
    sol = Solution()
    a = sol.missingNumber(nums)
    b = sol.missingNumberSets(nums)
    assert a == b
    print(a)
