"""
author: Zhengjian Kang
date: 01/07/2021

残酷群每日一题: 01/07/2021

https://leetcode.com/problems/maximum-length-of-pair-chain/

646. Maximum Length of Pair Chain

note: Greedy + Interval or DP LIS

You are given n pairs of numbers. In every pair, the first number is always
smaller than the second number.

Now, we define a pair (c, d) can follow another pair (a, b) if and only
if b < c. Chain of pairs can be formed in this fashion.

Given a set of pairs, find the length longest chain which can be formed.
You needn't use up all the given pairs. You can select pairs in any order.

Example 1:
Input: [[1,2], [2,3], [3,4]]
Output: 2
Explanation: The longest chain is [1,2] -> [3,4]
Note:
The number of given pairs will be in the range [1, 1000].
"""


class Solution:
    # greedy method
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort(key=lambda x: x[1])
        res = 1
        end = pairs[0][1]
        for i in range(1, len(pairs)):
            if pairs[i][0] > end:
                res += 1
                end = pairs[i][1]
        return res


class Solution2:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort(key=lambda x: x[1])
        res = 0
        dp = [1] * len(pairs)
        # LIS
        for i in range(len(pairs)):
            for j in range(i):
                if pairs[j][1] < pairs[i][0]:
                    dp[i] = max(dp[i], dp[j]+1)
            res = max(res, dp[i])
        return res
