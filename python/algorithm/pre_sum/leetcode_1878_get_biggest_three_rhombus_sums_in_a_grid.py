'''
author: Zhengjian Kang
date: 06/03/2021

残酷群每日一题: 06/02/2021

https://leetcode.com/problems/get-biggest-three-rhombus-sums-in-a-grid/

1878. Get Biggest Three Rhombus Sums in a Grid

note: 暴力确定菱形的中心点,然后确定边的范围，可以优化到pre-sum O(MN*M)

You are given an m x n integer matrix grid​​​.

A rhombus sum is the sum of the elements that form the border of a regular rhombus shape in grid​​​.
The rhombus must have the shape of a square rotated 45 degrees with each of the corners centered in a grid cell.
Below is an image of four valid rhombus shapes with the corresponding colored cells that should be included in each rhombus sum:

Note that the rhombus can have an area of 0, which is depicted by the purple rhombus in the bottom right corner.

Return the biggest three distinct rhombus sums in the grid in descending order. If there are less than three distinct values, return all of them.

Example 1:
Input: grid = [[3,4,5,1,3],[3,3,4,2,3],[20,30,200,40,10],[1,5,5,4,1],[4,3,2,2,5]]
Output: [228,216,211]
Explanation: The rhombus shapes for the three biggest distinct rhombus sums are depicted above.
- Blue: 20 + 3 + 200 + 5 = 228
- Red: 200 + 2 + 10 + 4 = 216
- Green: 5 + 200 + 4 + 2 = 211

Example 2:
Input: grid = [[1,2,3],[4,5,6],[7,8,9]]
Output: [20,9,8]
Explanation: The rhombus shapes for the three biggest distinct rhombus sums are depicted above.
- Blue: 4 + 2 + 6 + 8 = 20
- Red: 9 (area 0 rhombus in the bottom right corner)
- Green: 8 (area 0 rhombus in the bottom middle)

Example 3:
Input: grid = [[7,7,7]]
Output: [7]
Explanation: All three possible rhombus sums are the same, so return [7].
 

Constraints:
m == grid.length
n == grid[i].length
1 <= m, n <= 50
1 <= grid[i][j] <= 10^5
'''

class Solution:
    def getBiggestThree(self, grid: List[List[int]]) -> List[int]:
        M, N = len(grid), len(grid[0])
        presum1 = [[0] * N for _ in range(M)] # '/'
        presum2 = [[0] * N for _ in range(M)] # '\'
        for i in range(M):
            for j in range(N):
                presum1[i][j] = (presum1[i-1][j+1] if i-1 >= 0 and j+1 < N else 0) + grid[i][j]

        for i in range(M):
            for j in range(N):
                presum2[i][j] = (presum2[i-1][j-1] if i-1 >= 0 and j-1 >= 0 else 0) + grid[i][j]
        
        res = set()
        for i in range(M):
            for j in range(N):
                R = min(i,j,M-1-i,N-1-j)
                res.add(grid[i][j]) # case1: radius = 0
                # from center to iterate with radius
                for r in range(1, R+1):
                    total = 0
                    
                    x1, y1 = i-r, j
                    x2, y2 = i, j-r
                    total += presum1[x2][y2] - (presum1[x1-1][y1+1] if x1-1>=0 and y1+1<N else 0)

                    x1, y1 = i, j+r
                    x2, y2 = i+r, j
                    total += presum1[x2][y2] - (presum1[x1-1][y1+1] if x1-1>=0 and y1+1<N else 0)
                    
                    x1, y1 = i, j-r
                    x2, y2 = i+r, j
                    total += presum2[x2-1][y2-1] - presum2[x1][y1]
                    
                    x1, y1 = i-r, j
                    x2, y2 = i, j+r
                    total += presum2[x2-1][y2-1] - presum2[x1][y1] 
                    
                    res.add(total)
                    
        res = sorted(list(res), reverse=True)
        if len(res) <= 3: return res
        return res[:3]
 
