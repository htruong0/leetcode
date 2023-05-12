romanToIntDict = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000
}

class Solution:
    def romanToIntReplace(self, s: str) -> int:
        ret = 0
        s = s.replace("IV", "IIII")
        s = s.replace("IX", "VIIII")
        s = s.replace("XL", "XXXX")
        s = s.replace("XC", "LXXXX")
        s = s.replace("CD", "CCCC")
        s = s.replace("CM", "DCCCC")
        for x in s:
            ret += romanToIntDict[x]
        return ret

    def romanToIntSignMap(self, s: str) -> int:
        parsed = [romanToIntDict[x] for x in list(s)]
        comp = 0
        ret = 0
        for x in parsed[::-1]:
            if x >= comp:
                ret += x
            else:
                ret -= x
            comp = x
        return ret
    

if __name__ == "__main__":
    s = "MCMXCIV"
    sol = Solution()
    a = sol.romanToIntReplace(s)
    b = sol.romanToIntSignMap(s)
    assert a == b
    print(a)