class Solution:
    def hammingWeight(self, n: int) -> int:
        counter = 0
        while n:
            if n & 1:
                counter += 1
            n >>= 1
        return counter
    

if __name__ == "__main__":
    n = 0b00000000000000000000000000001011
    sol = Solution()
    a = sol.hammingWeight(n)
    print(a)
