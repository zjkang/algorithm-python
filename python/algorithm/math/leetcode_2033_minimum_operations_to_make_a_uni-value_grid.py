"""
author: Zhengjian Kang
date: 10/18/2021

残酷群每日一题: 10/18/2021

https://leetcode.com/problems/minimum-operations-to-make-a-uni-value-grid/

2033. Minimum Operations to Make a Uni-Value Grid

note: medium of array to minimize sum of |x_0-x| + |x_1-x| + ....

You are given a 2D integer grid of size m x n and an integer x. In one operation, you can add x to or subtract x from any element in the grid.
A uni-value grid is a grid where all the elements of it are equal.

Return the minimum number of operations to make the grid uni-value. If it is not possible, return -1.

Example 1:
Input: grid = [[2,4],[6,8]], x = 2
Output: 4
Explanation: We can make every element equal to 4 by doing the following: 
- Add x to 2 once.
- Subtract x from 6 once.
- Subtract x from 8 twice.
A total of 4 operations were used.

Example 2:
Input: grid = [[1,5],[2,3]], x = 1
Output: 5
Explanation: We can make every element equal to 3.

Example 3:
Input: grid = [[1,2],[3,4]], x = 2
Output: -1
Explanation: It is impossible to make every element equal.

Constraints:
m == grid.length
n == grid[i].length
1 <= m, n <= 10^5
1 <= m * n <= 10^5
1 <= x, grid[i][j] <= 10^4
"""

class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        m, n = len(grid), len(grid[0])
        vals = []
        for i in range(m):
            for j in range(n):
                vals.append(grid[i][j])

        vals.sort()
        total = m*n
        m_val = vals[total//2]
        
        res = 0
        for i in range(total):
            if (vals[i] - vals[0]) % x != 0:
                return -1
            res += abs(vals[i]-m_val) // x
        return res
