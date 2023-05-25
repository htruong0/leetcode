class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join(filter(str.isalnum, s)).lower()
        return s == s[::-1]
    

if __name__ == "__main__":
    s = "A man, a plan, a canal: Panama"
    sol = Solution()
    a = sol.isPalindrome(s)
    print(a)
