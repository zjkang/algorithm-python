
"""
author: Zhengjian Kang
date: 04/09/2021

残酷群每日一题: 04/09/2021

https://leetcode.com/problems/can-i-win/

464. Can I Win

note: 博弈dfs，考虑先手必赢或者必输的情况 + state compression

In the "100 game" two players take turns adding, to a running total,
any integer from 1 to 10. The player who first causes the running total
to reach or exceed 100 wins.

What if we change the game so that players cannot re-use integers?

For example, two players might take turns drawing from a common pool of
numbers from 1 to 15 without replacement until they reach a total >= 100.

Given two integers maxChoosableInteger and desiredTotal, return true if the
first player to move can force a win, otherwise return false. Assume both
players play optimally.

Example 1:
Input: maxChoosableInteger = 10, desiredTotal = 11
Output: false
Explanation:
No matter which integer the first player choose, the first player will lose.
The first player can choose an integer from 1 up to 10.
If the first player choose 1, the second player can only choose integers from 2 up to 10.
The second player will win by choosing 10 and get a total = 11, which is >= desiredTotal.
Same with other integers chosen by the first player, the second player will always win.

Example 2:
Input: maxChoosableInteger = 10, desiredTotal = 0
Output: true

Example 3:
Input: maxChoosableInteger = 10, desiredTotal = 1
Output: true

Constraints:
1 <= maxChoosableInteger <= 20
0 <= desiredTotal <= 300
"""


class Solution:
    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
        # need to must-lose case when total sum is less than desiredTotal
        total = (1+maxChoosableInteger)*maxChoosableInteger//2
        if total < desiredTotal:
            return False
        self.memo = {}
        return self.dfs(0, 0, maxChoosableInteger, desiredTotal)

    def dfs(self, state, cur, maxChoosableInteger, desiredTotal):
        if state in self.memo:
            return self.memo[state]
        for i in range(1, maxChoosableInteger+1):
            if (state >> i) & 1:
                continue
            if cur + i >= desiredTotal:
                self.memo[state] = True
                return True
            if not self.dfs(state + (1 << i), cur+i, maxChoosableInteger, desiredTotal):
                self.memo[state] = True
                return True
        self.memo[state] = False
        return False
