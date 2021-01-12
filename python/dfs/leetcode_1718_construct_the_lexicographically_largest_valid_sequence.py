"""
author: Zhengjian Kang
date: 01/11/2021

https://leetcode.com/problems/construct-the-lexicographically-largest-valid-sequence/


Given an integer n, find a sequence that satisfies all of the following:

The integer 1 occurs once in the sequence.
Each integer between 2 and n occurs twice in the sequence.
For every integer i between 2 and n, the distance between the two
occurrences of i is exactly i.
The distance between two numbers on the sequence, a[i] and a[j], is the
absolute difference of their indices, |j - i|.

Return the lexicographically largest sequence. It is guaranteed that under the
given constraints, there is always a solution.

A sequence a is lexicographically larger than a sequence b (of the same length)
if in the first position where a and b differ, sequence a has a number greater
than the corresponding number in b. For example, [0,1,9,0] is lexicographically
larger than [0,1,5,6] because the first position they differ is at the third
number, and 9 is greater than 5.

Example 1:
Input: n = 3
Output: [3,1,2,3,2]
Explanation: [2,3,2,1,3] is also a valid sequence, but [3,1,2,3,2] is the
lexicographically largest valid sequence.

Example 2:
Input: n = 5
Output: [5,3,1,4,3,5,2,4,2]

Constraints:
1 <= n <= 20
"""


class Solution:
    def constructDistancedSequence(self, n: int) -> List[int]:
        res = []
        self.dfs(n, 0, [-1] * (2*n-1), set(), res)
        return res

    def dfs(self, n, index, cur, used, res):
        if index == len(cur):
            res.extend(cur[:])
            return True

        if cur[index] != -1:
            if self.dfs(n, index+1, cur, used, res):
                return True
            return False

        for i in range(n, 0, -1):
            if i in used:
                continue
            can_set = (cur[index] == -1) and (i == 1 or index +
                                              i < len(cur) and cur[index+i] == -1)
            if can_set:
                used.add(i)
                cur[index] = i
                if i != 1:
                    cur[index+i] = i
                if self.dfs(n, index+1, cur, used, res):
                    return True
                cur[index] = -1
                if i != 1:
                    cur[index+i] = -1
                used.remove(i)
        return False
