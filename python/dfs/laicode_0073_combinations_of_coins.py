"""
author: Zhengjian Kang
date: 10/11/2020

https://app.laicode.io/app/problem/73

73. Combinations Of Coins

Given a number of different denominations of coins (e.g., 1 cent, 5 cents,
10 cents, 25 cents), get all the possible ways to pay a target number of cents.

Arguments

coins - an array of positive integers representing the different denominations
of coins, there are no duplicate numbers and the numbers are sorted by
descending order, eg. {25, 10, 5, 2, 1}
target - a non-negative integer representing the target number of cents, eg. 99

Assumptions
coins is not null and is not empty, all the numbers in coins are positive
target >= 0
You have infinite number of coins for each of the denominations, you can pick
any number of the coins.

Return
a list of ways of combinations of coins to sum up to be target.
each way of combinations is represented by list of integer, the number at each
index means the number of coins used for the denomination at corresponding index.

Examples
coins = {2, 1}, target = 4, the return should be
[
  [0, 4],   (4 cents can be conducted by 0 * 2 cents + 4 * 1 cents)
  [1, 2],   (4 cents can be conducted by 1 * 2 cents + 2 * 1 cents)
  [2, 0]    (4 cents can be conducted by 2 * 2 cents + 0 * 1 cents)
]
"""


class Solution(object):
    def combinations(self, target, coins):
        """
        input: int target, int[] coins
        return: int[][]
        """
        res = []
        self.dfs(target, coins, 0, [], res)
        return res

    def dfs(self, target, coins, start, oneres, res):
        if start == len(coins) - 1:
            if target % coins[start] == 0:
                oneres.append(target // coins[start])
                res.append(list(oneres))
                oneres.pop()
            return

        num = 0
        while num * coins[start] <= target:
            oneres.append(num)
            self.dfs(target - num * coins[start],
                     coins, start + 1, oneres, res)
            oneres.pop()
            num += 1
