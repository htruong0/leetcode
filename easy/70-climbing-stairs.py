cache = {}

class Solution:
    def climbStairs(self, n: int) -> int:
        # the number of ways you can climb the next set of stairs
        # is always +1 on each way you can climb the previous set
        # therefore fibonacci
        return self.fibonacci(n+1)
    
    def fibonacci(self, n: int) -> int:
        if n in cache:
            return cache[n]
        if n <= 1:
            return n
        else:
            cache[n] = self.fibonacci(n-1) + self.fibonacci(n-2)
            return cache[n]
        

if __name__ == "__main__":
    n = 45
    sol = Solution()
    a = sol.climbStairs(n)
    print(a)
