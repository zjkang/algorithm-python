
"""
author: Zhengjian Kang
date: 02/12/2021

残酷群每日一题: 02/09/2021

https://leetcode.com/problems/maximum-number-of-events-that-can-be-attended-ii/

1751. Maximum Number of Events That Can Be Attended II

note: 这道题和1235题目很类似，都是interval类的区间dp题目，唯一的区别在于在于额外的一维限制
出席event的数量.

interval的题目一般需要排序:
1.按照起始点排序，求mininum covering overlap intervals
2.按照终止点排序，求maximum number of non-overlap intervals

interval的题目有两类做法:
1.greedy的方法
2.interval dp

You are given an array of events where events[i] = [startDayi, endDayi, valuei]
. The ith event starts at startDayi and ends at endDayi, and if you attend this
event, you will receive a value of valuei. You are also given an integer k
which represents the maximum number of events you can attend.
You can only attend one event at a time. If you choose to attend an event,
you must attend the entire event. Note that the end day is inclusive: that is,
you cannot attend two events where one of them starts and the other ends on
the same day.

Return the maximum sum of values that you can receive by attending events.

Example 1:
Input: events = [[1,2,4],[3,4,3],[2,3,1]], k = 2
Output: 7
Explanation: Choose the green events, 0 and 1 (0-indexed) for a total value of
4 + 3 = 7.

Example 2:
Input: events = [[1,2,4],[3,4,3],[2,3,10]], k = 2
Output: 10
Explanation: Choose event 2 for a total value of 10.
Notice that you cannot attend any other event as they overlap, and that you do
not have to attend k events.

Example 3:
Input: events = [[1,1,1],[2,2,2],[3,3,3],[4,4,4]], k = 3
Output: 9
Explanation: Although the events do not overlap, you can only attend 3 events.
Pick the highest valued three.

Constraints:

1 <= k <= events.length
1 <= k * events.length <= 10^6
1 <= startDayi <= endDayi <= 10^9
1 <= valuei <= 10^6
"""


class Solution:
    def maxValue(self, events: List[List[int]], k: int) -> int:
        events.sort(key=lambda x: x[1])
        endings = [e[1] for e in events]
        # interval dp
        # dp[i][j]: first i meetings, attend at most j, the max value
        # dp[i][j]: dp[i-1][j], dp[k][j-1] + val[i], val[k][1] < val[i][0]
        n = len(events)
        dp = [[0] * (k+1) for _ in range(n+1)]
        for i in range(1, n+1):
            for j in range(1, k+1):
                dp[i][j] = dp[i-1][j]
                p = bisect.bisect_left(endings, events[i-1][0])
                dp[i][j] = max(dp[i][j], dp[p][j-1] + events[i-1][2])

        return dp[-1][-1]
