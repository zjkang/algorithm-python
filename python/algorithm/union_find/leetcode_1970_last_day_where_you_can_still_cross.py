"""
author: Zhengjian Kang
date: 08/26/2021
残酷群每日一题: 08/25/2021

https://leetcode.com/problems/last-day-where-you-can-still-cross/
1970. Last Day Where You Can Still Cross

note: Union Find + 时光倒流从后往前推

There is a 1-based binary matrix where 0 represents land and 1 represents water.
You are given integers row and col representing the number of rows and columns in the matrix, respectively.

Initially on day 0, the entire matrix is land. However, each day a new cell becomes flooded with water.
You are given a 1-based 2D array cells, where cells[i] = [ri, ci] represents that on the ith day,
the cell on the rith row and cith column (1-based coordinates) will be covered with water (i.e., changed to 1).

You want to find the last day that it is possible to walk from the top to the bottom by only walking on land cells.
You can start from any cell in the top row and end at any cell in the bottom row.
You can only travel in the four cardinal directions (left, right, up, and down).

Return the last day where it is possible to walk from the top to the bottom by only walking on land cells.

Example 1:
Input: row = 2, col = 2, cells = [[1,1],[2,1],[1,2],[2,2]]
Output: 2
Explanation: The above image depicts how the matrix changes each day starting from day 0.
The last day where it is possible to cross from top to bottom is on day 2.

Example 2:
Input: row = 2, col = 2, cells = [[1,1],[1,2],[2,1],[2,2]]
Output: 1
Explanation: The above image depicts how the matrix changes each day starting from day 0.
The last day where it is possible to cross from top to bottom is on day 1.

Example 3:
Input: row = 3, col = 3, cells = [[1,2],[2,1],[3,3],[2,2],[1,1],[1,3],[2,3],[3,2],[3,1]]
Output: 3
Explanation: The above image depicts how the matrix changes each day starting from day 0.
The last day where it is possible to cross from top to bottom is on day 3.
 

Constraints:
2 <= row, col <= 2 * 10^4
4 <= row * col <= 2 * 10^4
cells.length == row * col
1 <= ri <= row
1 <= ci <= col
All the values of cells are unique.
"""


class Solution:
    def latestDayToCross(self, row: int, col: int, cells: List[List[int]]) -> int:
        m, n = row, col
        self.father = [i for i in range(n*m+2)]
        
        mat = [[0] * n for _ in range(m)]
        # initialize to final state
        for x, y in cells:
            mat[x-1][y-1] = 1
            
        dx = [0, -1, 0, 1]
        dy = [-1, 0, 1, 0]
        
        # initialize final connected componenet
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 1:
                    continue
                for k in range(4):
                    x = i + dx[k]
                    y = j + dy[k]
                    if x < 0 or x >= m or y < 0 or y >= n:
                        continue
                    if mat[x][y] == 1:
                        continue
                    self.union(x*n+y, i*n+j)

        # connect first row to virtual node 1
        for j in range(n):
            self.union(0*n+j, m*n)
        # connect last row to virtual node 2
        for j in range(n):
            self.union((m-1)*n+j, m*n+1)
            
        for t in range(len(cells)-1, -1, -1):
            if self.find_father(m*n) == self.find_father(m*n+1):
                return t+1

            i, j = cells[t][0]-1, cells[t][1]-1
            mat[i][j] = 0
 
            for k in range(4):
                x = i + dx[k]
                y = j + dy[k]
                if x < 0 or x >= m or y < 0 or y >= n:
                    continue
                if mat[x][y] == 1:
                    continue
                self.union(x*n+y, i*n+j) 
                
        return 0
            
    def find_father(self, x):
        if self.father[x] != x:
            self.father[x] = self.find_father(self.father[x])
        return self.father[x]

    def union(self, x, y):
        x = self.find_father(x)
        y = self.find_father(y)
        if x < y:
            self.father[y] = x
        else:
            self.father[x] = y
 
