"""
author: Zhengjian Kang
date: 10/28/2020

https://leetcode.com/problems/split-array-into-fibonacci-sequence/

842. Split Array into Fibonacci Sequence

Given a string S of digits, such as S = "123456579", we can split it into a
Fibonacci-like sequence [123, 456, 579].

Formally, a Fibonacci-like sequence is a list F of non-negative integers
such that:

0 <= F[i] <= 2^31 - 1, (that is, each integer fits a 32-bit signed integer
type);
F.length >= 3;
and F[i] + F[i+1] = F[i+2] for all 0 <= i < F.length - 2.
Also, note that when splitting the string into pieces, each piece must not
have extra leading zeroes, except if the piece is the number 0 itself.

Return any Fibonacci-like sequence split from S, or return [] if it cannot
be done.

Example 1:
Input: "123456579"
Output: [123,456,579]

Example 2:
Input: "11235813"
Output: [1,1,2,3,5,8,13]

Example 3:
Input: "112358130"
Output: []
Explanation: The task is impossible.

Example 4:
Input: "0123"
Output: []
Explanation: Leading zeroes are not allowed, so "01", "2", "3" is not valid.

Example 5:
Input: "1101111"
Output: [110, 1, 111]
Explanation: The output [11, 0, 11, 11] would also be accepted.

Note:
1 <= S.length <= 200
S contains only digits.
"""


class Solution:
    def splitIntoFibonacci(self, S: str) -> List[int]:
        if not S:
            return []
        # the number range should be less than 10 digits
        # try to get the first 2 numbers, once first two are fixed, all others
        # are fixed
        max_len = 10
        for i in range(min(max_len, len(S))):
            n1 = S[:i+1]
            if len(n1) > 1 and n1[0] == '0':
                break
            for j in range(i+1, min(i+1+max_len, len(S))):
                n2 = S[i+1: j+1]
                if len(n2) > 1 and n2[0] == '0':
                    break
                res = self.get_fib(n1, n2, S, j+1)
                if res:
                    return res
        return []

    def get_fib(self, n1, n2, S, pos):
        if pos == len(S):
            return []
        res = [int(n1), int(n2)]
        while pos < len(S):
            next_num = int(n1) + int(n2)
            next_len = len(str(next_num))
            if next_num > 2**31 - 1:
                return []
            if pos + next_len > len(S):
                return []
            if int(S[pos: pos+next_len]) != next_num:
                return []
            res.append(next_num)
            n1, n2 = n2, next_num
            pos += next_len
        return res
