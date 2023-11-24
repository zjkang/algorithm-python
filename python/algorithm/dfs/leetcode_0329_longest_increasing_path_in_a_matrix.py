
"""
author: Zhengjian Kang
date: 04/11/2021

残酷群每日一题: 04/11/2021

https://leetcode.com/problems/longest-increasing-path-in-a-matrix/

329. Longest Increasing Path in a Matrix

note: dfs + memo

Given an m x n integers matrix, return the length of the longest increasing
path in matrix.

From each cell, you can either move in four directions: left, right, up,
or down. You may not move diagonally or move outside the boundary
(i.e., wrap-around is not allowed).

Example 1:
Input: matrix = [[9,9,4],[6,6,8],[2,1,1]]
Output: 4
Explanation: The longest increasing path is [1, 2, 6, 9].

Example 2:
Input: matrix = [[3,4,5],[3,2,6],[2,2,1]]
Output: 4
Explanation: The longest increasing path is [3, 4, 5, 6]. Moving diagonally is not allowed.

Example 3:
Input: matrix = [[1]]
Output: 1

Constraints:
m == matrix.length
n == matrix[i].length
1 <= m, n <= 200
0 <= matrix[i][j] <= 2^31 - 1
"""


class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        self.res = 1
        self.memo = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if self.memo[i][j] > 0:
                    continue
                self.dfs(matrix, i, j)

        return self.res

    def dfs(self, matrix, x, y):
        if self.memo[x][y] > 0:
            return
        m, n = len(matrix), len(matrix[0])
        self.memo[x][y] = 1
        dx = [0, -1, 0, 1]
        dy = [-1, 0, 1, 0]
        for i in range(4):
            cx = x + dx[i]
            cy = y + dy[i]
            if 0 <= cx < m and 0 <= cy < n and matrix[cx][cy] > matrix[x][y]:
                self.dfs(matrix, cx, cy)
                self.memo[x][y] = max(self.memo[x][y], 1 + self.memo[cx][cy])
                self.res = max(self.res, self.memo[x][y])
