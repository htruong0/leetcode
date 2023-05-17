class Solution:
    def insert(self, intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
        if not intervals:
            return [newInterval]
        
        index = self.binarySearch(intervals, newInterval)
        intervals.insert(index, newInterval)
        return self.mergeIntervals(intervals, index)
    
    def mergeIntervals(self, intervals: list[list[int]], index: int) -> list[list[int]]:
        left = index
        right = index
        leftVal = intervals[index][0]
        rightVal = intervals[index][1]
        
        while right < len(intervals)-1 and intervals[right+1][0] <= rightVal:
            right += 1
            
        while left > 0 and intervals[left-1][1] >= leftVal:
            left -= 1
            
        leftVal = min(leftVal, intervals[left][0], intervals[right][0])
        rightVal = max(rightVal, intervals[right][1], intervals[left][1])
        
        return intervals[:left] + [[leftVal, rightVal]] + intervals[right+1:]
        
    def binarySearch(self, intervals: list[list[int]], newInterval: list[int]) -> int:
        start = 0
        end = len(intervals)-1
        
        target = newInterval[0]
        
        while start <= end:
            mid = (start + end) // 2
            if target <= intervals[mid][0]:
                end = mid - 1
            elif target > intervals[mid][0]:
                start = mid + 1
                
        # should insert newInterval after the first interval you can insert it to preserve order
        if target > intervals[mid][0]:
            return mid + 1
        else:
            return mid
        

if __name__ == "__main__":
    intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]]
    newInterval = [4,8]
    sol = Solution()
    a = sol.insert(intervals, newInterval)
    print(a)
