
"""
author: Zhengjian Kang
date: 02/28/2021

残酷群每日一题: 02/04/2021

https://leetcode.com/problems/shortest-palindrome/

214. Shortest Palindrome

note: kmp的变形题目

Given a string s, you can convert it to a palindrome by adding
characters in front of it. Find and return the shortest palindrome
you can find by performing this transformation.

Example 1:
Input: s = "aacecaaa"
Output: "aaacecaaa"

Example 2:
Input: s = "abcd"
Output: "dcbabcd"

Constraints:
0 <= s.length <= 5 * 10^4
s consists of lowercase English letters only.
"""


class Solution:
    def shortestPalindrome(self, s: str) -> str:
        if s == "":
            return ""
        n = len(s)
        pattern = s
        target = s[::-1]

        suffix = self.preprocess(pattern)
        dp = [0] * n
        dp[0] = pattern[0] == target[0]
        if n == 1 and dp[0] == 1:
            return s

        for i in range(1, n):
            j = dp[i-1]
            while j > 0 and pattern[j] != target[i]:
                j = suffix[j-1]
            dp[i] = j + (pattern[j] == target[i])

        return s[dp[n-1]:][::-1] + s

    def preprocess(self, s):
        n = len(s)
        dp = [0] * n
        for i in range(1, n):
            j = dp[i-1]
            while j >= 1 and s[i] != s[j]:
                j = dp[j-1]
            dp[i] = j + (s[i] == s[j])
        return dp
