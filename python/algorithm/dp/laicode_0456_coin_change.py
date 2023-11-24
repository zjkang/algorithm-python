"""
author: Zhengjian Kang
date: 10/07/2020

https://app.laicode.io/app/problem/456

456. Coin Change

You are given coins of different denominations and a total amount of money
amount. Write a function to compute the fewest number of coins that you need
to make up that amount. If that amount of money cannot be made up by any
combination of the coins, return -1.

Example 1:
coins = [1, 2, 5], amount = 11
return 3 (11 = 5 + 5 + 1)

Example 2:
coins = [2], amount = 3
return -1.

Note:
You may assume that you have an infinite number of each kind of coin.
"""


class Solution(object):
    def coinChange(self, coins, amount):
        """
        input: int[] coins, int amount
        return: int
        """
        # minimum of coin change using amount i
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0
        for i in range(1, amount+1):
            for c in coins:
                if i - c >= 0:
                    dp[i] = min(dp[i-c] + 1, dp[i])
        return dp[-1] if dp[-1] != amount + 1 else -1
