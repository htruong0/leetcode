class Solution:
    def countBitsTwo(self, n: int) -> list[int]:
        ans = [0]
        offset = 1
        for i in range(1, n+1):
            if i == 2*offset:
                offset *= 2
            ans.append(1 + ans[i - offset])
        return ans

    def countBitsOne(self, n: int) -> list[int]:
        ans = [0]*(n+1)
        for i in range(1, n+1):
            ans[i] = ans[i >> 1] + i % 2
        return ans
    

if __name__ == "__main__":
    n = 5
    sol = Solution()
    a = sol.countBitsOne(n)
    b = sol.countBitsTwo(n)
    assert a == b
    print(a)
