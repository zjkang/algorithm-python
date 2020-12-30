"""
author: Zhengjian Kang
date: 10/07/2020

https://app.laicode.io/app/problem/663

663. Coin Change II

You are given coins of different denominations and a total amount of money amount. Write a function to the number of different combinations that can sum up to that amount.

Example 1:
coins = [1,2] , amount = 5
return 3

Explanation: 

5 = 1 + 1 + 1 + 1 + 1 = 1 + 1 + 1 + 2 = 1 + 2 + 2

Note:
You may assume that you have an infinite number of each kind of coin.
"""


class Solution(object):
    def coinChange(self, amount, coins):
        """
        input: int amount, int[] coins
        return: int
        """
        dp = [0 for i in range(amount + 1)]
        dp[0] = 1
        for i in coins:
            for j in range(i, amount + 1):
                dp[j] = dp[j] + dp[j - i]
        return dp[amount]
