
"""
author: Zhengjian Kang
date: 03/08/2021

残酷群每日一题: 02/05/2021

https://leetcode.com/problems/repeated-substring-pattern/

459. Repeated Substring Pattern

note: KMP方法

Given a string s, check if it can be constructed by taking a substring of it
and appending multiple copies of the substring together.

Example 1:
Input: s = "abab"
Output: true
Explanation: It is the substring "ab" twice.

Example 2:
Input: s = "aba"
Output: false

Example 3:
Input: s = "abcabcabcabc"
Output: true
Explanation: It is the substring "abc" four times or the substring
"abcabc" twice.

Constraints:
1 <= s.length <= 10^4
s consists of lowercase English letters.
"""


class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        if not s:
            return False
        n = len(s)
        dp = [0] * n
        for i in range(1, n):
            j = dp[i-1]
            while j >= 1 and s[i] != s[j]:
                j = dp[j-1]
            dp[i] = j + (s[i] == s[j])
        return dp[n-1] != 0 and (dp[n-1] % (n - dp[n-1])) == 0
