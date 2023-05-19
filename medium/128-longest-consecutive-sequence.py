class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        seen = set(nums)

        longest = 0
        for num in nums:
            # start of a sequence has no number -1 of it
            if num - 1 not in seen:
                currentNum = num
                current = 1

                # construct sequence from num set
                while currentNum + 1 in seen:
                    currentNum += 1
                    current += 1

                longest = max(current, longest)
        return longest


if __name__ == "__main__":
    nums = [0,-1]
    sol = Solution()
    a = sol.longestConsecutive(nums)
    print(a)
