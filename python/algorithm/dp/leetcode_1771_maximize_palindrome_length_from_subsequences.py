
"""
author: Zhengjian Kang
date: 02/26/2021

残酷群每日一题: 02/26/2021

https://leetcode.com/problems/maximize-palindrome-length-from-subsequences/

1771. Maximize Palindrome Length From Subsequences

note: 区间dp，这道题利用panlindrome的性质。然后保证i,j一个在word1一个在word2

You are given two strings, word1 and word2. You want to construct a string
in the following manner:

Choose some non-empty subsequence subsequence1 from word1.
Choose some non-empty subsequence subsequence2 from word2.
Concatenate the subsequences: subsequence1 + subsequence2, to make the string.
Return the length of the longest palindrome that can be constructed in the
described manner. If no palindromes can be constructed, return 0.

A subsequence of a string s is a string that can be made by deleting some
(possibly none) characters from s without changing the order of the remaining
characters.

A palindrome is a string that reads the same forward as well as backward.

Example 1:
Input: word1 = "cacb", word2 = "cbba"
Output: 5
Explanation: Choose "ab" from word1 and "cba" from word2 to make "abcba",
which is a palindrome.

Example 2:
Input: word1 = "ab", word2 = "ab"
Output: 3
Explanation: Choose "ab" from word1 and "a" from word2 to make "aba", which is
a palindrome.

Example 3:
Input: word1 = "aa", word2 = "bb"
Output: 0
Explanation: You cannot construct a palindrome from the described method,
so return 0.

Constraints:

1 <= word1.length, word2.length <= 1000
word1 and word2 consist of lowercase English letters.
"""


class Solution:
    def longestPalindrome(self, word1: str, word2: str) -> int:
        m = len(word1)
        word = word1 + word2
        n = len(word)
        dp = [[0] * n for i in range(n)]
        res = 0
        # dp[i][j]: longest subsequence between [i,j]
        for i in range(n-1, -1, -1):
            for j in range(i, n):
                if i == j:
                    dp[i][j] = 1
                elif i+1 == j:
                    dp[i][j] = 2 if word[i] == word[j] else 1
                else:
                    if word[i] == word[j]:
                        dp[i][j] = 2 + dp[i+1][j-1]
                    else:
                        dp[i][j] = max(dp[i+1][j], dp[i][j-1])
                if i < m and j >= m and word[i] == word[j]:
                    res = max(res, dp[i][j])
        return res
