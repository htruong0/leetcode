class Solution:
    def isPalindrome(self, x):
        if x < 0:
            return False
        
        reverse = 0
        temp = x
        while temp:
            temp, n = divmod(temp, 10)
            reverse = reverse*10 + n
        return reverse == x

    def isPalindromeString(self, x):
        x = list(str(x))
        if x == x[::-1]:
            return True
        else:
            return False
        
if __name__ == "__main__":
    x = 121
    sol = Solution()
    a = sol.isPalindrome(x)
    print(a)
