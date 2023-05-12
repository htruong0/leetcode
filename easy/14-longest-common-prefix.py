class Solution:
    def longestCommonPrefixMinMax(self, strs: list[str]) -> str:
        low = min(strs)
        high = max(strs)
        lcp = ""
        for i in range(len(low)):
            if low[i] == high[i]:
                lcp += low[i]
            else:
                break
        return lcp
    
    def longestCommonPrefixReverseSearch(self, strs: list[str]) -> str:
        lcp = strs[0]
        for word in strs:
            while not word.startswith(lcp):
                lcp = lcp[:-1]
        return lcp

    def longestCommonPrefixDumb(self, strs: list[str]) -> str:
        if len(strs) <= 1:
            return strs[0]
        if len(set(strs)) == 1:
            return strs[0]
        n = 1
        lcp = strs[0][:n]
        ret = ""
        while all([self.checkWord(word, lcp) for word in strs]):
            ret = lcp
            n += 1
            lcp = strs[0][:n]
            if lcp == strs[0]:
                break
        return ret
    
    def checkWord(self, word: str, lcp: str) -> bool:
        if len(lcp) == 0:
            return False
        elif lcp == word[:len(lcp)]:
            return True
        else:
            return False
        
if __name__ == "__main__":
    strs = ["a", "ac"]
    sol = Solution()
    a = sol.longestCommonPrefixDumb(strs)
    b = sol.longestCommonPrefixReverseSearch(strs)
    c = sol.longestCommonPrefixMinMax(strs)
    assert a == b
    assert a == c
    print(a)
