class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        counts = {}
        mostCommon = 0
        for right, c in enumerate(s):
            if c in counts:
                counts[c] += 1
            else:
                counts[c] = 1

            mostCommon = max(mostCommon, counts[c])
            valid = (right+1-left) - mostCommon <= k
            if not valid:
                counts[s[left]] -= 1
                left += 1
        return len(s) - left
    

if __name__ == "__main__":
    s = "AABABBA"
    k = 1
    sol = Solution()
    a = sol.characterReplacement(s, k)
    print(a)
