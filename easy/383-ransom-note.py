class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        checks = []
        for c in ransomNote:
            if c in magazine:
                magazine = magazine.replace(c, "", 1)
                checks.append(True)
            else:
                checks.append(False)
        return all(checks)
    
if __name__ == "__main__":
    ransomNote = "aa"
    magazine = "aab"
    sol = Solution()
    a = sol.canConstruct(ransomNote, magazine)
    print(a)
