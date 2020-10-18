"""
author: Wei Li
date: 10/17/2020

https://leetcode.com/problems/find-right-interval/

436. Find Right Interval

You are given an array of intervals, where intervals[i] = [starti, endi] and each starti is unique.

The right interval for an interval i is an interval j such that startj >= endi and startj is minimized.

Return an array of right interval indices for each interval i. If no right interval exists for interval i, then put -1 at index i.

Example 1:
Input: intervals = [[1,2]]
Output: [-1]
Explanation: There is only one interval in the collection, so it outputs -1.

Example 2:
Input: intervals = [[3,4],[2,3],[1,2]]
Output: [-1,0,1]
Explanation: There is no right interval for [3,4].
The right interval for [2,3] is [3,4] since start0 = 3 is the smallest start that is >= end1 = 3.
The right interval for [1,2] is [2,3] since start1 = 2 is the smallest start that is >= end2 = 2.

Example 3:
Input: intervals = [[1,4],[2,3],[3,4]]
Output: [-1,2,-1]
Explanation: There is no right interval for [1,4] and [3,4].
The right interval for [2,3] is [3,4] since start2 = 3 is the smallest start that is >= end1 = 3.
 
Constraints:

1 <= intervals.length <= 2 * 104
intervals[i].length == 2
-106 <= starti <= endi <= 106
The start point of each interval is unique.
"""
# heap + sort
import heapq
class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        heap, result = [], [-1] * len(intervals)
               
        for i, interval in sorted(enumerate(intervals), key = lambda x: x[1]):
            while heap and heap[0][0] <= interval[0]:
                _, idx = heapq.heappop(heap)
                result[idx] = i
            
            heapq.heappush(heap, (interval[1], i))
        
        return result
        

# Binary Search
import bisect
class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        starts = sorted((interval[0], i) for i, interval in enumerate(intervals)) + [(float('inf'), -1)]
        result = []
        for interval in intervals:
            idx = bisect.bisect_left(starts, (interval[1],))
            result.append(starts[idx][1])
        return result        