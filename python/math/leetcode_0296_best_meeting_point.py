"""
author: Zhengjian Kang
date: 10/18/2021

残酷群每日一题: 10/17/2021

https://leetcode.com/problems/best-meeting-point/

296. Best Meeting Point

note: medium of array to minimize sum of |x_0-x| + |x_1-x| + ....

Given an m x n binary grid grid where each 1 marks the home of one friend, return the minimal total travel distance.
The total travel distance is the sum of the distances between the houses of the friends and the meeting point.
The distance is calculated using Manhattan Distance, where distance(p1, p2) = |p2.x - p1.x| + |p2.y - p1.y|.

Example 1:
Input: grid = [[1,0,0,0,1],[0,0,0,0,0],[0,0,1,0,0]]
Output: 6
Explanation: Given three friends living at (0,0), (0,4), and (2,2).
The point (0,2) is an ideal meeting point, as the total travel distance of 2 + 2 + 2 = 6 is minimal.
So return 6.

Example 2:
Input: grid = [[1,1]]
Output: 1
 

Constraints:
m == grid.length
n == grid[i].length
1 <= m, n <= 200
grid[i][j] is either 0 or 1.
There will be at least two friends in the grid.
"""

class Solution:
    def minTotalDistance(self, grid: List[List[int]]) -> int:
    # calculate total distance of abs(x_1-med) + abs(x_2-med) + ... + abs(x_n-med) 
        m, n = len(grid), len(grid[0])
        rows, cols = [], []
        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    rows.append(i)
                    cols.append(j)
        
        rows.sort()
        cols.sort()
        m_x = rows[len(rows)//2]
        m_y = cols[len(cols)//2]
        
        res = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    res += abs(i-m_x) + abs(j-m_y)
        return res
