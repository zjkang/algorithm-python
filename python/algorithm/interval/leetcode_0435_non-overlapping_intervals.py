
"""
author: Zhengjian Kang
date: 02/13/2021

残酷群每日一题: 01/01/2021

https://leetcode.com/problems/non-overlapping-intervals/

435. Non-overlapping Intervals

note: 这道题是按照ending排序，因为是max non-overlapping

Given a collection of intervals, find the minimum number of intervals you need
to remove to make the rest of the intervals non-overlapping.

Example 1:
Input: [[1,2],[2,3],[3,4],[1,3]]
Output: 1
Explanation: [1,3] can be removed and the rest of intervals are
non-overlapping.

Example 2:
Input: [[1,2],[1,2],[1,2]]
Output: 2
Explanation: You need to remove two [1,2] to make the rest of intervals
non-overlapping.

Example 3:
Input: [[1,2],[2,3]]
Output: 0
Explanation: You don't need to remove any of the intervals since they're
already non-overlapping.

Note:
You may assume the interval's end point is always bigger than its start point.
Intervals like [1,2] and [2,3] have borders "touching" but they don't
overlap each other.
"""


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        intervals.sort(key=lambda x: x[1])  # sort by end
        end = intervals[0][1]
        i = 1
        count = 0
        while i < len(intervals):
            if intervals[i][0] < end:
                count += 1
            else:
                end = intervals[i][1]
            i += 1
        return count
