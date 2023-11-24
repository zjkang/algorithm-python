"""
author: Zhengjian Kang
date: 07/20/2021

残酷群每日一题: 07/19/2021

https://leetcode.com/problems/sum-of-special-evenly-spaced-elements-in-array/

1714. Sum Of Special Evenly-Spaced Elements In Array
note: 根据d的大小拆分成2部分.d>sqrt使用brute force，另外使用dp

You are given a 0-indexed integer array nums consisting of n non-negative integers.

You are also given an array queries, where queries[i] = [xi, yi]. The answer to the ith
query is the sum of all nums[j] where xi <= j < n and (j - xi) is divisible by yi.

Return an array answer where answer.length == queries.length and answer[i]
is the answer to the ith query modulo 109 + 7.

Example 1:
Input: nums = [0,1,2,3,4,5,6,7], queries = [[0,3],[5,1],[4,2]]
Output: [9,18,10]
Explanation: The answers of the queries are as follows:
1) The j indices that satisfy this query are 0, 3, and 6. nums[0] + nums[3] + nums[6] = 9
2) The j indices that satisfy this query are 5, 6, and 7. nums[5] + nums[6] + nums[7] = 18
3) The j indices that satisfy this query are 4 and 6. nums[4] + nums[6] = 10

Example 2:
Input: nums = [100,200,101,201,102,202,103,203], queries = [[0,7]]
Output: [303]
 

Constraints:

n == nums.length
1 <= n <= 5 * 10^4
0 <= nums[i] <= 10^9
1 <= queries.length <= 1.5 * 10^5
0 <= xi < n
1 <= yi <= 5 * 10^4
"""

class Solution:
    def solve(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        dp = [[-1] * 50001 for _ in range(256)]
        MOD = 10**9 + 7
        
        rets = [0] * len(queries)
        n = len(nums)
        bound = math.sqrt(n)
        
        for k in range(len(queries)):
            s, d = queries[k][0], queries[k][1]
            if d >= bound: # brute force
                i = s
                total = 0
                while i < n:
                    total += nums[i]
                    i += d
                rets[k] = total % MOD
            else: # dp
                if dp[d][s] == -1:
                    for i in range(n-1, -1, -1):
                        dp[d][i] = ((dp[d][i+d] if i+d < n else 0) + nums[i]) % MOD
                
                rets[k] = dp[d][s]
                
        return rets
 
