class Solution:
    def isAnagramSet(self, s: str, t: str) -> bool:
        combined_set = set(s + t)
        for x in combined_set:
            if s.count(x) != t.count(x):
                return False
        return True

    def isAnagramSort(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)
    
if __name__ == "__main__":
    s = "anagram"
    t = "nagaram"
    sol = Solution()
    a = sol.isAnagramSort(s, t)
    b = sol.isAnagramSet(s, t)
    assert a == b
    print(a)
