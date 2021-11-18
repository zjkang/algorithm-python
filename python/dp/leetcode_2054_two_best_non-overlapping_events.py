"""
author: Zhengjian Kang
date: 11/17/2021

残酷群每日一题: 11/16/2021

https://leetcode.com/problems/two-best-non-overlapping-events/

2054. Two Best Non-Overlapping Events

note: sort by end times + dp, the simplifed version of problem 1235

You are given a 0-indexed 2D integer array of events where events[i] = [startTimei, endTimei, valuei].
The ith event starts at startTimei and ends at endTimei, and if you attend this event, you will receive a value of valuei.
You can choose at most two non-overlapping events to attend such that the sum of their values is maximized.

Return this maximum sum.

Note that the start time and end time is inclusive: that is, you cannot attend two events where one of them starts and
the other ends at the same time. More specifically, if you attend an event with end time t, the next event must start at or after t + 1.

Example 1:
Input: events = [[1,3,2],[4,5,2],[2,4,3]]
Output: 4
Explanation: Choose the green events, 0 and 1 for a sum of 2 + 2 = 4.

Example 2:
Example 1 Diagram
Input: events = [[1,3,2],[4,5,2],[1,5,5]]
Output: 5
Explanation: Choose event 2 for a sum of 5.

Example 3:
Input: events = [[1,5,3],[1,5,1],[6,6,5]]
Output: 8
Explanation: Choose events 0 and 2 for a sum of 3 + 5 = 8.
 

Constraints:
2 <= events.length <= 10^5
events[i].length == 3
1 <= startTimei <= endTimei <= 10^9
1 <= valuei <= 10^6
"""


class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        events.sort(key=lambda x: x[1])
        n = len(events)
        
        dp = [0] * n # dp[i]: the max event value for the first i-th events
        mx = 0
        for i in range(n):
            mx = max(mx, events[i][2])
            dp[i] = mx
        
        maxTimes = [] # end time for events
        res = 0 
        for i in range(n):
            s = events[i][0]-1
            e = events[i][1]
            v = events[i][2]
            res = max(res, v)
            idx = bisect.bisect_right(maxTimes, s)
            if idx != 0:
                res = max(res, v + dp[idx-1])
            maxTimes.append(e)
            
        return res
        
