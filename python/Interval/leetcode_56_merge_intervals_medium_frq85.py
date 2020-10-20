"""
author: Wei Li
date: 10/17/2020

https://leetcode.com/problems/merge-intervals/

56. Merge Intervals

Given a collection of intervals, merge all overlapping intervals.

Example 1:
Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].

Example 2:
Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.
NOTE: input types have been changed on April 15, 2019. Please reset to default code definition to get new method signature.

Constraints:

intervals[i][0] <= intervals[i][1]
"""


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []

        # first sort
        intervals.sort(key=lambda x: x[0])
        if len(intervals) == 1:
            return intervals

        result = [intervals[0]]

        curr = 1
        while curr < len(intervals):
            if result[-1][1] < intervals[curr][0]:
                result.append(intervals[curr])
            else:
                result[-1][1] = max(result[-1][1], intervals[curr][1])

            curr += 1

        return result
