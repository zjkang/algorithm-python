"""
author: Wei Li
date: 10/17/2020

https://leetcode.com/problems/meeting-rooms-ii/

352. Data Stream as Disjoint Intervals

Given a data stream input of non-negative integers a1, a2, ..., an, ..., summarize the numbers seen so far as a list of disjoint intervals.

For example, suppose the integers from the data stream are 1, 3, 7, 2, 6, ..., then the summary will be:

[1, 1]
[1, 1], [3, 3]
[1, 1], [3, 3], [7, 7]
[1, 3], [7, 7]
[1, 3], [6, 7]
 

Follow up:

What if there are lots of merges and the number of disjoint intervals are small compared to the data stream's size?
"""
# Binary Search
class SummaryRanges:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.intervals = []

    def addNum(self, val: int) -> None:
        n = len(self.intervals)
        
        start, end = 0, n - 1
        while start + 1 < end:
            mid = (start + end) // 2
            
            if self.intervals[mid][0] <= val <= self.intervals[mid][1]:
                return None
            elif val < self.intervals[mid][0]:
                end = mid - 1
            else:
                start = mid + 1
                
      
        if self.intervals and self.intervals[start][0] <= val <= self.intervals[start][1]:
            return None
        
        if self.intervals and self.intervals[end][0] <= val <= self.intervals[end][1]:
            return None
        
        
        index = start
        if self.intervals and self.intervals[end] and self.intervals[end][0] < val:
            index = end + 1
        elif self.intervals and self.intervals[start] and self.intervals[start][0] < val:
            index = start + 1
        
       
        self.intervals.insert(index, [val, val])
        
        if index < n and self.intervals[index + 1][0] == val + 1:
            self.intervals[index][1] = self.intervals[index + 1][1]
            del self.intervals[index + 1]
        
        if index and self.intervals[index - 1][1] == val - 1:
            self.intervals[index][0] = self.intervals[index - 1][0]
            del self.intervals[index - 1]
            

    def getIntervals(self) -> List[List[int]]:
        return self.intervals
        


# Your SummaryRanges object will be instantiated and called as such:
# obj = SummaryRanges()
# obj.addNum(val)
# param_2 = obj.getIntervals()