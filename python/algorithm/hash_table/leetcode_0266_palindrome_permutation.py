"""
author: Zhengjian Kang
date: 01/07/2021

https://leetcode.com/problems/palindrome-permutation/

266. Palindrome Permutation

Given a string, determine if a permutation of the string could form
a palindrome.

Example 1:
Input: "code"
Output: false

Example 2:
Input: "aab"
Output: true

Example 3:
Input: "carerac"
Output: true
"""


class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        from collections import Counter
        counter = Counter(s)
        # print(counter)
        res = 0
        for k, v in counter.items():
            if v % 2 == 1:
                res += 1
            if res > 1:
                return False
        return True
