class Solution:
    def firstBadVersion(self, n: int) -> int:
        i = self.binarySearch(n)
        return i

    def binarySearch(self, n: int) -> int:
        start = 0
        end = n

        while start <= end:
            mid = (start + end) // 2
            if self.isBadVersion(mid):
                if self.isFirstBad(mid):
                    return mid
                end = mid - 1
            elif not self.isBadVersion(mid):
                start = mid + 1
        
        return None

    def isFirstBad(self, index: int) -> bool:
        if not self.isBadVersion(index-1) and self.isBadVersion(index):
            return True
        else:
            return False
        
    def isBadVersion(self, n: int) -> bool:
        return True if n == bad_version else False
    

if __name__ == "__main__":
    n = 5
    bad_version = 4
    sol = Solution()
    a = sol.firstBadVersion(n)
    assert a == bad_version
    print(a)
