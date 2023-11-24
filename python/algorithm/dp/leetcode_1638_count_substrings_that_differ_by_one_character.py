
"""
author: Zhengjian Kang
date: 03/06/2021

残酷群每日一题: 03/05/2021

https://leetcode.com/problems/count-substrings-that-differ-by-one-character/

1638. Count Substrings That Differ by One Character

note: 找到s[i]!=t[j]的分割点，然后向左向右扩展,longest the same subtring, two pass

Given two strings s and t, find the number of ways you can choose a non-empty
substring of s and replace a single character by a different character such
that the resulting substring is a substring of t. In other words, find the
number of substrings in s that differ from some substring in t by exactly
one character.
For example, the underlined substrings in "computer" and "computation" only
differ by the 'e'/'a', so this is a valid way.
Return the number of substrings that satisfy the condition above.
A substring is a contiguous sequence of characters within a string.

Example 1:
Input: s = "aba", t = "baba"
Output: 6
Explanation: The following are the pairs of substrings from s and t that
differ by exactly 1 character:
("aba", "baba")
("aba", "baba")
("aba", "baba")
("aba", "baba")
("aba", "baba")
("aba", "baba")
The underlined portions are the substrings that are chosen from s and t.

​​Example 2:
Input: s = "ab", t = "bb"
Output: 3
Explanation: The following are the pairs of substrings from s and t that
differ by 1 character:
("ab", "bb")
("ab", "bb")
("ab", "bb")
​​​​The underlined portions are the substrings that are chosen from s and t.

Example 3:
Input: s = "a", t = "a"
Output: 0

Example 4:
Input: s = "abe", t = "bbc"
Output: 10

Constraints:
1 <= s.length, t.length <= 100
s and t consist of lowercase English letters only.
"""


class Solution:
    def countSubstrings(self, s: str, t: str) -> int:
        UPPER = 105
        dp1 = [[0] * UPPER for _ in range(UPPER)]
        dp2 = [[0] * UPPER for _ in range(UPPER)]

        m = len(s)
        n = len(t)
        s = '#' + s + '#'
        t = '#' + t + '#'

        for i in range(1, m+1):
            for j in range(1, n+1):
                if s[i] == t[j]:
                    dp1[i][j] = dp1[i-1][j-1] + 1
        for i in range(m, 0, -1):
            for j in range(n, 0, -1):
                if s[i] == t[j]:
                    dp2[i][j] = dp2[i+1][j+1] + 1

        res = 0
        for i in range(1, m+1):
            for j in range(1, n+1):
                if s[i] != t[j]:
                    res += (dp1[i-1][j-1]+1) * (dp2[i+1][j+1]+1)
        return res
