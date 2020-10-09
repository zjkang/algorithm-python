"""
aurthor: Zhengjian Kang
date: 10/08/2020

https://app.laicode.io/app/problem/233

233. N Queens

Get all valid ways of putting N Queens on an N * N chessboard so that no two Queens threaten each other.

Assumptions

N > 0
Return

A list of ways of putting the N Queens
Each way is represented by a list of the Queen's y index for x indices of 0 to (N - 1)
Example

N = 4, there are two ways of putting 4 queens:

[1, 3, 0, 2] --> the Queen on the first row is at y index 1, the Queen on the second row is at y index 3, the Queen on the third row is at y index 0 and the Queen on the fourth row is at y index 2.
[2, 0, 3, 1] --> the Queen on the first row is at y index 2, the Queen on the second row is at y index 0, the Queen on the third row is at y index 3 and the Queen on the fourth row is at y index 1.
"""


class Solution(object):
    def nqueens(self, n):
        """
        input: int n
        return: int[][]
        """
        self.result = []
        self.dfs(n, 0, [])
        return self.result

    def dfs(self, n, row, one_res):
        if n == row:
            self.result.append(one_res[:])
            return
        for i in range(n):
            if not self.has_conflict(row, i, one_res):
                one_res.append(i)
                self.dfs(n, row + 1, one_res)
                one_res.pop()

    def has_conflict(self, cur_r, cur_c, one_res):
        for r, c in enumerate(one_res):
            if c == cur_c or (abs(cur_r - r) == abs(cur_c - c)):
                return True
        return False
