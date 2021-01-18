
"""
author: Zhengjian Kang
date: 01/18/2021

https://leetcode.com/problems/maximum-score-from-removing-substrings/

1717. Maximum Score From Removing Substrings

You are given a string s and two integers x and y. You can perform two types
of operations any number of times.

Remove substring "ab" and gain x points.
For example, when removing "ab" from "cabxbae" it becomes "cxbae".
Remove substring "ba" and gain y points.
For example, when removing "ba" from "cabxbae" it becomes "cabxe".
Return the maximum points you can gain after applying the above
operations on s.

Example 1:
Input: s = "cdbcbbaaabab", x = 4, y = 5
Output: 19
Explanation:
- Remove the "ba" underlined in "cdbcbbaaabab". Now, s = "cdbcbbaaab" and 5
points are added to the score.
- Remove the "ab" underlined in "cdbcbbaaab". Now, s = "cdbcbbaa" and 4
points are added to the score.
- Remove the "ba" underlined in "cdbcbbaa". Now, s = "cdbcba" and 5
points are added to the score.
- Remove the "ba" underlined in "cdbcba". Now, s = "cdbc" and 5
points are added to the score.
Total score = 5 + 4 + 5 + 5 = 19.
Example 2:

Input: s = "aabbaaxybbaabb", x = 5, y = 4
Output: 20

Constraints:
1 <= s.length <= 105
1 <= x, y <= 104
s consists of lowercase English letters.
"""


class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        first, second = ['a', 'b'], ['b', 'a']
        if y > x:
            first, second = second, first
            x, y = y, x
        res = 0
        cur1 = []
        for c in s:
            cur1.append(c)
            if len(cur1) >= 2 and cur1[-2:] == first:
                cur1.pop()
                cur1.pop()
                res += x
        cur2 = []
        for c in cur1:
            cur2.append(c)
            if len(cur2) >= 2 and cur2[-2:] == second:
                cur2.pop()
                cur2.pop()
                res += y
        return res
