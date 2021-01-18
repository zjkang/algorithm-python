
"""
author: Zhengjian Kang
date: 01/17/2021

You are given an integer array jobs, where jobs[i] is the amount of time it
takes to complete the ith job.
There are k workers that you can assign jobs to. Each job should be assigned
to exactly one worker. The working time of a worker is the sum of the time it
takes to complete all jobs assigned to them. Your goal is to devise an optimal
assignment such that the maximum working time of any worker is minimized.

Return the minimum possible maximum working time of any assignment.

Example 1:
Input: jobs = [3,2,3], k = 3
Output: 3
Explanation: By assigning each person one job, the maximum time is 3.

Example 2:
Input: jobs = [1,2,4,7,8], k = 2
Output: 11
Explanation: Assign the jobs the following way:
Worker 1: 1, 2, 8 (working time = 1 + 2 + 8 = 11)
Worker 2: 4, 7 (working time = 4 + 7 = 11)
The maximum working time is 11.

Constraints:
1 <= k <= jobs.length <= 12
1 <= jobs[i] <= 107
"""


class Solution:
    def minimumTimeRequired(self, jobs: List[int], k: int) -> int:
        jobs.sort(reverse=True)
        min_val, total_val = max(jobs), sum(jobs)
        start = min_val
        end = total_val
        while start < end:
            mid = (start + end) // 2
            if self.check(jobs, mid, k):
                end = mid
            else:
                start = mid + 1
        return start

    def check(self, jobs, mid, k):
        assign = [0] * k
        return self.dfs(jobs, mid, 0, assign)

    def dfs(self, jobs, bound, index, assign):
        if index == len(jobs):
            return True
        for i in range(len(assign)):
            if assign[i] + jobs[index] <= bound:
                assign[i] += jobs[index]
                if self.dfs(jobs, bound, index+1, assign):
                    return True
                assign[i] -= jobs[index]
                if assign[i] == 0:
                    break
        return False
