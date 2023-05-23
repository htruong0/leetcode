class Solution:
    def getsum(self, a: int, b: int) -> int:
        mask = 0xffff
        if b == 0:
            return a
        elif b & mask == 0:
            return a & mask
        else:
            return self.getsum(a^b, (a&b) << 1)
        

if __name__ == "__main__":
    a = -2
    b = 2
    sol = Solution()
    s = sol.getsum(a, b)
    print(f"{a}+{b}={s}")
