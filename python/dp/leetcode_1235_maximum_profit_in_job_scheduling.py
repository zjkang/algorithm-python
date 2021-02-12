
"""
author: Zhengjian Kang
date: 01/18/2021

残酷群每日一题: 01/09/2021

https://leetcode.com/problems/maximum-profit-in-job-scheduling/

1235. Maximum Profit in Job Scheduling

We have n jobs, where every job is scheduled to be done from startTime[i] to
endTime[i], obtaining a profit of profit[i].
You're given the startTime , endTime and profit arrays, you need to output the
maximum profit you can take such that there are no 2 jobs in the subset with
overlapping time range.
If you choose a job that ends at time X you will be able to start another job
that starts at time X.

Example 1:
Input: startTime = [1,2,3,3], endTime = [3,4,5,6], profit = [50,10,40,70]
Output: 120
Explanation: The subset chosen is the first and fourth job.
Time range [1-3]+[3-6] , we get profit of 120 = 50 + 70.

Example 2:
Input: startTime = [1,2,3,4,6], endTime = [3,5,10,6,9], profit = [20,20,100,70,60]
Output: 150
Explanation: The subset chosen is the first, fourth and fifth job.
Profit obtained 150 = 20 + 70 + 60.

Example 3:
Input: startTime = [1,1,1], endTime = [2,3,4], profit = [5,6,4]
Output: 6

Constraints:
1 <= startTime.length == endTime.length == profit.length <= 5 * 10^4
1 <= startTime[i] < endTime[i] <= 10^9
1 <= profit[i] <= 10^4
"""


class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        n = len(startTime)
        jobs = []
        for i in range(n):
            jobs.append((startTime[i], endTime[i], profit[i]))
        jobs.sort(key=lambda x: x[1])
        # dp[i]: the most profit for first i jobs
        # dp[i] = max(dp[i-1], profit[i] + dp[j] max j <= start[i])
        dp = [0] * n
        dp[0] = jobs[0][2]
        for i in range(1, n):
            cur = self.binary_search(jobs, jobs[i][0])
            dp[i] = max(dp[i-1], jobs[i][2] + (0 if cur == -1 else dp[cur]))
        return dp[-1]

    def binary_search(self, jobs, cur):
        start, end = 0, len(jobs)-1
        while start + 1 < end:
            mid = (start + end) // 2
            if jobs[mid][1] <= cur:
                start = mid
            else:
                end = mid
        if jobs[end][1] <= cur:
            return end
        if jobs[start][1] <= cur:
            return start
        return -1
