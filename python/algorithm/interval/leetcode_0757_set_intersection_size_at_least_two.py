"""
author: Zhengjian Kang
date: 01/08/2021

残酷群每日一题: 01/08/2021

https://leetcode.com/problems/set-intersection-size-at-least-two/

757. Set Intersection Size At Least Two

note: Greedy + Intervals

An integer interval [a, b] (for integers a < b) is a set of all consecutive
integers from a to b, including a and b.

Find the minimum size of a set S such that for every integer interval A in
intervals, the intersection of S with A has a size of at least two.

Example 1:
Input: intervals = [[1,3],[1,4],[2,5],[3,5]]
Output: 3
Explanation: Consider the set S = {2, 3, 4}.  For each interval,
there are at least 2 elements from S in the interval.
Also, there isn't a smaller size set that fulfills the above condition.
Thus, we output the size of this set, which is 3.

Example 2:
Input: intervals = [[1,2],[2,3],[2,4],[4,5]]
Output: 5
Explanation: An example of a minimum sized set is {1, 2, 3, 4, 5}.

Constraints:
1 <= intervals.length <= 3000
intervals[i].length == 2
0 <= ai < bi <= 10^8
"""


class Solution:
    # similar to 452 shoot balloons
    # sort by end if searching for max # of non-overlapping intervals
    # best two number at interval[1], interval[1]-1,on the rightmost of interval
    def intersectionSizeTwo(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: (x[1]))
        left = intervals[0][1]-1
        right = intervals[0][1]
        res = 2
        for i in range(1, len(intervals)):
            cur = intervals[i]
            if cur[0] <= left:
                continue
            elif cur[0] > right:
                left = cur[1]-1
                right = cur[1]
                res += 2
            elif right == cur[1]:
                left = cur[1]-1
                res += 1
            else:
                left, right = right, cur[1]
                res += 1
        return res
