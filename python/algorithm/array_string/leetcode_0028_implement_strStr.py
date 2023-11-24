
"""
author: Zhengjian Kang
date: 02/26/2021

残酷群每日一题: 02/03/2021

https://leetcode.com/problems/implement-strstr/

28. Implement strStr()

note: kmp的自相关和互相关

Implement strStr().

Return the index of the first occurrence of needle in haystack, or -1 if
needle is not part of haystack.

Clarification:
What should we return when needle is an empty string? This is a great question
to ask during an interview.

For the purpose of this problem, we will return 0 when needle is an empty
string. This is consistent to C's strstr() and Java's indexOf().

Example 1:
Input: haystack = "hello", needle = "ll"
Output: 2

Example 2:
Input: haystack = "aaaaa", needle = "bba"
Output: -1

Example 3:
Input: haystack = "", needle = ""
Output: 0

Constraints:
0 <= haystack.length, needle.length <= 5 * 10^4
haystack and needle consist of only lower-case English characters.
"""


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n, m = len(haystack), len(needle)
        if m == 0:
            return 0
        if n == 0:
            return -1

        suffix = self.preprocess(needle)
        dp = [0] * n
        dp[0] = needle[0] == haystack[0]
        if m == 1 and dp[0] == 1:
            return 0

        for i in range(1, n):
            j = dp[i-1]
            while j > 0 and needle[j] != haystack[i]:
                j = suffix[j-1]
            dp[i] = j + (needle[j] == haystack[i])
            if dp[i] == len(needle):
                return i - len(needle) + 1
        return -1

    def preprocess(self, s):
        n = len(s)
        dp = [0] * n
        for i in range(1, n):
            j = dp[i-1]
            while j >= 1 and s[i] != s[j]:
                j = dp[j-1]
            dp[i] = j + (s[i] == s[j])
        return dp
