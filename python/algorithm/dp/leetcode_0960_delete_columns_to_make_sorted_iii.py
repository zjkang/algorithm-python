"""
author: Zhengjian Kang
date: 03/25/2021

残酷群每日一题: 01/06/2021

https://leetcode.com/problems/delete-columns-to-make-sorted-iii/

960. Delete Columns to Make Sorted III

note: DP LIS

You are given an array of n strings strs, all of the same length.

We may choose any deletion indices, and we delete all the characters in those
indices for each string.

For example, if we have strs = ["abcdef","uvwxyz"] and deletion indices
{0, 2, 3}, then the final array after deletions is ["bef", "vyz"].

Suppose we chose a set of deletion indices answer such that after deletions,
the final array has every string (row) in lexicographic order. (i.e.,
(strs[0][0] <= strs[0][1] <= ... <= strs[0][strs[0].length - 1]),
and (strs[1][0] <= strs[1][1] <= ... <= strs[1][strs[1].length - 1]),
and so on). Return the minimum possible value of answer.length.

Example 1:
Input: strs = ["babca","bbazb"]
Output: 3
Explanation: After deleting columns 0, 1, and 4, the final array is
strs = ["bc", "az"].
Both these rows are individually in lexicographic order (ie.
strs[0][0] <= strs[0][1] and strs[1][0] <= strs[1][1]).
Note that strs[0] > strs[1] - the array strs is not necessarily
in lexicographic order.

Example 2:
Input: strs = ["edcba"]
Output: 4
Explanation: If we delete less than 4 columns, the only row will not be
lexicographically sorted.

Example 3:
Input: strs = ["ghi","def","abc"]
Output: 0
Explanation: All rows are already lexicographically sorted.

Constraints:
n == strs.length
1 <= n <= 100
1 <= strs[i].length <= 100
strs[i] consists of lowercase English letters.
"""


class Solution:
    def minDeletionSize(self, A: List[str]) -> int:
        def larger_than(a, b):
            if a == b:
                return 1
            for i in range(len(a)):
                if a[i] < b[i]:
                    return -1
            return 1
        m, n = len(A), len(A[0])
        B = [''.join([A[i][j] for i in range(m)]) for j in range(n)]
        dp = [1] * n
        lis = 0
        for i in range(1, n):
            for j in range(i):
                if larger_than(B[i], B[j]) >= 0:
                    dp[i] = max(dp[i], dp[j] + 1)
            lis = max(lis, dp[i])
        return n - lis
