
"""
author: Zhengjian Kang
date: 03/08/2021

残酷群每日一题: 03/08/2021

https://leetcode.com/problems/number-of-good-ways-to-split-a-string/

1525. Number of Good Ways to Split a String

You are given a string s, a split is called good if you can split s into 2
non-empty strings p and q where its concatenation is equal to s and the number
of distinct letters in p and q are the same.

Return the number of good splits you can make in s.

Example 1:
Input: s = "aacaba"
Output: 2
Explanation: There are 5 ways to split "aacaba" and 2 of them are good.
("a", "acaba") Left string and right string contains 1 and 3 different letters
respectively.
("aa", "caba") Left string and right string contains 1 and 3 different letters
respectively.
("aac", "aba") Left string and right string contains 2 and 2 different letters
respectively (good split).
("aaca", "ba") Left string and right string contains 2 and 2 different letters
respectively (good split).
("aacab", "a") Left string and right string contains 3 and 1 different letters
respectively.

Example 2:
Input: s = "abcd"
Output: 1
Explanation: Split the string as follows ("ab", "cd").

Example 3:
Input: s = "aaaaa"
Output: 4
Explanation: All possible splits are good.

Example 4:
Input: s = "acbadbaada"
Output: 2

Constraints:
s contains only lowercase English letters.
1 <= s.length <= 10^5
"""


class Solution:
    def numSplits(self, s: str) -> int:
        n = len(s)
        left = [0] * n
        right = [0] * n

        letters = set()
        for i in range(n):
            letters.add(s[i])
            left[i] = len(letters)

        letters = set()
        for i in range(n-1, -1, -1):
            letters.add(s[i])
            right[i] = len(letters)

        ret = 0
        for i in range(n-1):
            if left[i] == right[i+1]:
                ret += 1
        return ret
