"""
author: Zhengjian Kang
date: 04/17/2021

残酷群每日一题: 04/17/2021

https://leetcode.com/problems/sudoku-solver/

37. Sudoku Solver

note: dfs + bit操作

Write a program to solve a Sudoku puzzle by filling the empty cells.

A sudoku solution must satisfy all of the following rules:

Each of the digits 1-9 must occur exactly once in each row.
Each of the digits 1-9 must occur exactly once in each column.
Each of the digits 1-9 must occur exactly once in each of the 9 3x3
sub-boxes of the grid.
The '.' character indicates empty cells.

Example 1:
Input: board = [["5","3",".",".","7",".",".",".","."],
["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],
["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],
["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],
[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
Output: [["5","3","4","6","7","8","9","1","2"],
["6","7","2","1","9","5","3","4","8"],["1","9","8","3","4","2","5","6","7"],
["8","5","9","7","6","1","4","2","3"],["4","2","6","8","5","3","7","9","1"],
["7","1","3","9","2","4","8","5","6"],["9","6","1","5","3","7","2","8","4"],
["2","8","7","4","1","9","6","3","5"],["3","4","5","2","8","6","1","7","9"]]
Explanation: The input board is shown above and the only valid solution is
shown below:

Constraints:
board.length == 9
board[i].length == 9
board[i][j] is a digit or '.'.
It is guaranteed that the input board has only one solution.
"""


class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        self.rows = [0]*9
        self.cols = [0]*9
        self.cells = [0]*9
        self.process(board)
        self.dfs(board, 0)

    def process(self, board):
        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    d = 1 << (int(board[i][j]))
                    self.rows[i] |= d
                    self.cols[j] |= d
                    self.cells[i//3*3 + j//3] |= d

    def get_valid(self, board, r, c):
        res = []
        num = self.rows[r] | self.cols[c] | self.cells[r//3*3 + c//3]
        for i in range(1, 10):
            if num & (1 << i) == 0:
                res.append(i)
        return res

    def dfs(self, board, index):
        if index == 81:
            return True
        r = index // 9
        c = index % 9
        if board[r][c] == '.':
            for d in self.get_valid(board, r, c):
                # print(r,c,d)
                ds = 1 << d
                self.rows[r] += ds
                self.cols[c] += ds
                self.cells[r//3*3 + c//3] += ds
                board[r][c] = str(d)
                if self.dfs(board, index+1):
                    return True
                self.rows[r] -= ds
                self.cols[c] -= ds
                self.cells[r//3*3 + c//3] -= ds
                board[r][c] = '.'
        else:
            return self.dfs(board, index+1)
        return False
