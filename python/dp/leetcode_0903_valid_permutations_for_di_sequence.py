'''
author: Zhengjian Kang
date: 05/23/2021

残酷群每日一题: 05/20/2021

https://leetcode.com/problems/valid-permutations-for-di-sequence/

903. Valid Permutations for DI Sequence

note: https://github.com/wisdompeak/LeetCode/tree/master/Dynamic_Programming/903.Valid-Permutations-for-DI-Sequence
排列组合类问题的dp问题: 重点在于dp[i]的定义

We are given s, a length n string of characters from the set {'D', 'I'}.
(These letters stand for "decreasing" and "increasing".)

A valid permutation is a permutation p[0], p[1], ..., p[n] of integers {0, 1, ..., n}, such that for all i:
If s[i] == 'D', then p[i] > p[i+1], and;
If s[i] == 'I', then p[i] < p[i+1].
How many valid permutations are there?  Since the answer may be large, return your answer modulo 109 + 7.

Example 1:
Input: s = "DID"
Output: 5
Explanation: 
The 5 valid permutations of (0, 1, 2, 3) are:
(1, 0, 3, 2)
(2, 0, 3, 1)
(2, 1, 3, 0)
(3, 0, 2, 1)
(3, 1, 2, 0)
 

Note:
1 <= s.length <= 200
s consists only of characters from the set {'D', 'I'}.
'''

class Solution:
    def numPermsDISequence(self, S: str) -> int:
        #dp[i][j]: the number of valid permutations for [0,i] s.t i-th element is j
        n = len(S)
        S = '#' + S
        MOD = 10**9+7
        dp = [[0]*(n+1) for _ in range(n+1)]
        dp[0][0] = 1
        for i in range(1, n+1):
            for j in range(i+1):
                if S[i] == 'I':
                    for k in range(j):
                        dp[i][j] += dp[i-1][k]
                else:
                    for k in range(i-1, j-1, -1):
                        dp[i][j] += dp[i-1][k]
        ret = 0
        for j in range(n+1):
            ret += dp[n][j]
        return ret % MOD
