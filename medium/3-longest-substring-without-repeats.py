class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i = 0
        longest = 0
        chars = {}
        # double sliding window
        for j, c in enumerate(s):
            # if there's a repeat update position of repeats in hashmap
            if c in chars:
                # move start of window to after the previous
                # instance of repeated character
                i = max(chars[c] + 1, i)
            # longest is size of window
            longest = max(longest, j - i + 1)
            chars[c] = j
        return longest
    

if __name__ == "__main__":
    s = "pwwkew"
    sol = Solution()
    a = sol.lengthOfLongestSubstring(s)
    print(a)
