"""
author: Zhengjian Kang
date: 03/25/2021

残酷群每日一题: 02/20/2021

https://leetcode.com/problems/cat-and-mouse-ii/

1728. Cat and Mouse II

note: dfs + memo + 博弈dfs

A game is played by a cat and a mouse named Cat and Mouse.

The environment is represented by a grid of size rows x cols, where each
element is a wall, floor, player (Cat, Mouse), or food.

Players are represented by the characters 'C'(Cat),'M'(Mouse).
Floors are represented by the character '.' and can be walked on.
Walls are represented by the character '#' and cannot be walked on.
Food is represented by the character 'F' and can be walked on.
There is only one of each character 'C', 'M', and 'F' in grid.
Mouse and Cat play according to the following rules:

Mouse moves first, then they take turns to move.
During each turn, Cat and Mouse can jump in one of the four directions
(left, right, up, down). They cannot jump over the wall nor outside of
the grid.
catJump, mouseJump are the maximum lengths Cat and Mouse can jump at a time,
respectively. Cat and Mouse can jump less than the maximum length.
Staying in the same position is allowed.
Mouse can jump over Cat.
The game can end in 4 ways:

If Cat occupies the same position as Mouse, Cat wins.
If Cat reaches the food first, Cat wins.
If Mouse reaches the food first, Mouse wins.
If Mouse cannot get to the food within 1000 turns, Cat wins.
Given a rows x cols matrix grid and two integers catJump and mouseJump,
return true if Mouse can win the game if both Cat and Mouse play optimally,
otherwise return false.

Example 1:
Input: grid = ["####F","#C...","M...."], catJump = 1, mouseJump = 2
Output: true
Explanation: Cat cannot catch Mouse on its turn nor can it get the food
before Mouse.

Example 2:
Input: grid = ["M.C...F"], catJump = 1, mouseJump = 4
Output: true

Example 3:
Input: grid = ["M.C...F"], catJump = 1, mouseJump = 3
Output: false

Example 4:
Input: grid = ["C...#","...#F","....#","M...."], catJump = 2, mouseJump = 5
Output: false

Example 5:
Input: grid = [".M...","..#..","#..#.","C#.#.","...#F"], catJump = 3,
mouseJump = 1
Output: true

Constraints:
rows == grid.length
cols = grid[i].length
1 <= rows, cols <= 8
grid[i][j] consist only of characters 'C', 'M', 'F', '.', and '#'.
There is only one of each character 'C', 'M', and 'F' in grid.
1 <= catJump, mouseJump <= 8
"""


class Solution:
    def canMouseWin(self, grid: List[str], catJump: int, mouseJump: int) -> bool:
        rows, cols = len(grid), len(grid[0])
        c_p, m_p, f_p, avail = None, None, None, 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] != '#':
                    avail += 1
                if grid[i][j] == 'C':
                    c_p = (i, j)
                elif grid[i][j] == 'M':
                    m_p = (i, j)
                elif grid[i][j] == 'F':
                    f_p = (i, j)
        dp = {}
        dr = [0, -1, 0, 1]
        dc = [-1, 0, 1, 0]

        def helper(grid, t, m, c, food):
            if t == avail * 2:
                return False
            if m == c:
                return False
            if m == food:
                return True
            if c == food:
                return False

            if dp.get((t, m, c), -1) != -1:
                return dp[(t, m, c)]
            m_turn = (t % 2 == 0)
            if m_turn:  # mouse turn
                for i in range(4):
                    for j in range(mouseJump+1):
                        nr = m[0] + dr[i] * j
                        nc = m[1] + dc[i] * j
                        if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] != '#':
                            if helper(grid, t+1, (nr, nc), c, food):
                                dp[(t, m, c)] = True
                                return True
                        else:
                            break
                dp[(t, m, c)] = False
                return False
            else:  # cat turn
                for i in range(4):
                    for j in range(catJump+1):
                        nr = c[0] + dr[i] * j
                        nc = c[1] + dc[i] * j
                        if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] != '#':
                            if not helper(grid, t+1, m, (nr, nc), food):
                                dp[(t, m, c)] = False
                                return False
                        else:
                            break
                dp[(t, m, c)] = True
                return True

        return helper(grid, 0, m_p, c_p, f_p)
