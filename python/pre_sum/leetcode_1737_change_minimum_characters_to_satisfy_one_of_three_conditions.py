
"""
author: Zhengjian Kang
date: 03/24/2021

残酷群每日一题: 01/25/2021

https://leetcode.com/problems/change-minimum-characters-to-satisfy-one-of-three-conditions/

1737. Change Minimum Characters to Satisfy One of Three Conditions

note: pre-sum + greedy

You are given two strings a and b that consist of lowercase letters.
In one operation, you can change any character in a or b to any lowercase
letter.

Your goal is to satisfy one of the following three conditions:

Every letter in a is strictly less than every letter in b in the alphabet.
Every letter in b is strictly less than every letter in a in the alphabet.
Both a and b consist of only one distinct letter.
Return the minimum number of operations needed to achieve your goal.

Example 1:
Input: a = "aba", b = "caa"
Output: 2
Explanation: Consider the best way to make each condition true:
1) Change b to "ccc" in 2 operations, then every letter in a is less than
every letter in b.
2) Change a to "bbb" and b to "aaa" in 3 operations, then every letter in b
is less than every letter in a.
3) Change a to "aaa" and b to "aaa" in 2 operations, then a and b consist of
one distinct letter.
The best way was done in 2 operations (either condition 1 or condition 3).

Example 2:
Input: a = "dabadd", b = "cda"
Output: 3
Explanation: The best way is to make condition 1 true by changing b to "eee".

Constraints:
1 <= a.length, b.length <= 10^5
a and b consist only of lowercase letters.

"""


class Solution:
    def minCharacters(self, a: str, b: str) -> int:
        # prefix accumulated sum count for letters
        a_count = [0] * 26
        b_count = [0] * 26
        for i in a:
            a_count[ord(i)-ord('a')] += 1
        for i in b:
            b_count[ord(i)-ord('a')] += 1
        for i in range(1, 26):
            a_count[i] += a_count[i-1]
        for i in range(1, 26):
            b_count[i] += b_count[i-1]

        res = float('inf')
        for i in range(26):
            if i > 0:
                res = min(res, b_count[i-1] + len(a) - a_count[i-1])
                res = min(res, a_count[i-1] + len(b) - b_count[i-1])
            pre_a = 0 if i == 0 else a_count[i-1]
            pre_b = 0 if i == 0 else b_count[i-1]
            res = min(res, len(a) - a_count[i] +
                      pre_a + len(b) - b_count[i] + pre_b)
        return res
