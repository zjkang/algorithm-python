"""
author: Zhengjian Kang
date: 01/03/2021

https://leetcode.com/problems/beautiful-arrangement/

note: 01/03/2021 daily problem

Suppose you have n integers labeled 1 through n. A permutation of those n
integers perm (1-indexed) is considered a beautiful arrangement if for every
i (1 <= i <= n), either of the following is true:

perm[i] is divisible by i.
i is divisible by perm[i].
Given an integer n, return the number of the beautiful arrangements that you
can construct.

Example 1:
Input: n = 2
Output: 2
Explanation:
The first beautiful arrangement is [1,2]:
    - perm[1] = 1 is divisible by i = 1
    - perm[2] = 2 is divisible by i = 2
The second beautiful arrangement is [2,1]:
    - perm[1] = 2 is divisible by i = 1
    - i = 2 is divisible by perm[2] = 1

Example 2:
Input: n = 1
Output: 1

Constraints:
1 <= n <= 15
"""


class Solution:
    def countArrangement(self, n: int) -> int:
        one_arr = [i for i in range(1, n+1)]
        self.res = 0
        self.dfs(one_arr, 0)
        return self.res

    def dfs(self, one_arr, index):
        if index == len(one_arr):
            self.res += 1
            return
        for i in range(index, len(one_arr)):
            if (one_arr[i] % (index+1) == 0) or ((index+1) % one_arr[i] == 0):
                one_arr[i], one_arr[index] = one_arr[index], one_arr[i]
                self.dfs(one_arr, index+1)
                one_arr[index], one_arr[i] = one_arr[i], one_arr[index]
