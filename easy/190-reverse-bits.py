class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        for i in range(32):
            bit = n & 1
            reverse_bit = bit << (31 - i)
            n >>= 1
            res = res | reverse_bit
        return res
    
    def reverseBitsLazy(self, n: int) -> int:
        n = format(n, "032b")
        return int(n[::-1], 2)
    

if __name__ == "__main__":
    n = 0b00000010100101000001111010011100
    sol = Solution()
    a = sol.reverseBits(n)
    b = sol.reverseBitsLazy(n)
    assert a == b
    print(a)
