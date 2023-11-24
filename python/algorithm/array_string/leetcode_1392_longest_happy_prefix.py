
"""
author: Zhengjian Kang
date: 02/26/2021

https://leetcode.com/problems/longest-happy-prefix/

1392. Longest Happy Prefix

残酷群每日一题: 02/02/2021

note: 打卡kmp的题目。这道题是自相关的match问题

A string is called a happy prefix if is a non-empty prefix which is also a
suffix (excluding itself).

Given a string s. Return the longest happy prefix of s .

Return an empty string if no such prefix exists.

Example 1:
Input: s = "level"
Output: "l"
Explanation: s contains 4 prefix excluding itself ("l", "le", "lev", "leve"),
and suffix ("l", "el", "vel", "evel"). The largest prefix which is also
suffix is given by "l".

Example 2:
Input: s = "ababab"
Output: "abab"
Explanation: "abab" is the largest prefix which is also suffix. They can
overlap in the original string.

Example 3:
Input: s = "leetcodeleet"
Output: "leet"

Example 4:
Input: s = "a"
Output: ""

Constraints:
1 <= s.length <= 10^5
s contains only lowercase English letters.
"""


class Solution:
    def longestPrefix(self, s: str) -> str:
        # refer huifeng suffix array
        # https://github.com/wisdompeak/LeetCode/blob/master/String/1392.Longest-Happy-Prefix/1392.Longest-Happy-Prefix.cpp
        n = len(s)
        dp = [0] * n
        for i in range(1, n):
            j = dp[i-1]
            while j >= 1 and s[i] != s[j]:
                j = dp[j-1]
            dp[i] = j + (s[j] == s[i])
        return s[:dp[-1]]
