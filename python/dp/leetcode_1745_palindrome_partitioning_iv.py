
"""
author: Zhengjian Kang
date: 02/12/2021

残酷群每日一题: 02/01/2021

https://leetcode.com/problems/palindrome-partitioning-iv/

1745. Palindrome Partitioning IV

note: 区间型dp，只要确定转移方程和初始条件就好

Given a string s, return true if it is possible to split the string s into
three non-empty palindromic substrings. Otherwise, return false.​​​​​

A string is said to be palindrome if it the same string when reversed.

Example 1:
Input: s = "abcbdd"
Output: true
Explanation: "abcbdd" = "a" + "bcb" + "dd", and all three substrings are
palindromes.

Example 2:
Input: s = "bcbddxy"
Output: false
Explanation: s cannot be split into 3 palindromes.

Constraints:
3 <= s.length <= 2000
s​​​​​​ consists only of lowercase English letters.
"""


class Solution:
    def checkPartitioning(self, s: str) -> bool:
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        self.get_partition(s, dp)
        for i in range(n):
            for j in range(i+2, n):  # 寻找断点
                if dp[0][i] and dp[i+1][j-1] and dp[j][n-1]:
                    return True
        return False

    def get_partition(self, s, dp):
        n = len(s)
        for i in range(n-1, -1, -1):
            for j in range(i, n):
                if i == j:
                    dp[i][j] = True
                elif i+1 == j:
                    dp[i][j] = s[i] == s[j]
                else:
                    dp[i][j] = s[i] == s[j] and dp[i+1][j-1]
