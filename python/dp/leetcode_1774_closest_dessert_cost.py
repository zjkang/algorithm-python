
"""
author: Zhengjian Kang
date: 03/04/2021

残酷群每日一题: 03/01/2021

https://leetcode.com/problems/closest-dessert-cost/

1774. Closest Dessert Cost

note: 这道题可以用dp和dfs都可以求解。比赛的时候想到了dp，但还是有些麻烦了。

You would like to make dessert and are preparing to buy the ingredients.
You have n ice cream base flavors and m types of toppings to choose from.
You must follow these rules when making your dessert:

There must be exactly one ice cream base.
You can add one or more types of topping or have no toppings at all.
There are at most two of each type of topping.
You are given three inputs:

baseCosts, an integer array of length n, where each baseCosts[i] represents
the price of the ith ice cream base flavor.
toppingCosts, an integer array of length m, where each toppingCosts[i] is
the price of one of the ith topping.
target, an integer representing your target price for dessert.
You want to make a dessert with a total cost as close to target as possible.

Return the closest possible cost of the dessert to target. If there are
multiple, return the lower one.

Example 1:
Input: baseCosts = [1,7], toppingCosts = [3,4], target = 10
Output: 10
Explanation: Consider the following combination (all 0-indexed):
- Choose base 1: cost 7
- Take 1 of topping 0: cost 1 x 3 = 3
- Take 0 of topping 1: cost 0 x 4 = 0
Total: 7 + 3 + 0 = 10.

Example 2:
Input: baseCosts = [2,3], toppingCosts = [4,5,100], target = 18
Output: 17
Explanation: Consider the following combination (all 0-indexed):
- Choose base 1: cost 3
- Take 1 of topping 0: cost 1 x 4 = 4
- Take 2 of topping 1: cost 2 x 5 = 10
- Take 0 of topping 2: cost 0 x 100 = 0
Total: 3 + 4 + 10 + 0 = 17. You cannot make a dessert with a total cost of 18.

Example 3:
Input: baseCosts = [3,10], toppingCosts = [2,5], target = 9
Output: 8
Explanation: It is possible to make desserts with cost 8 and 10. Return 8 as
it is the lower cost.

Example 4:
Input: baseCosts = [10], toppingCosts = [1], target = 1
Output: 10
Explanation: Notice that you don't have to have any toppings, but you must
have exactly one base.

Constraints:
n == baseCosts.length
m == toppingCosts.length
1 <= n, m <= 10
1 <= baseCosts[i], toppingCosts[i] <= 10^4
1 <= target <= 10^4
"""


class Solution:
    # dfs
    def closestCost(self, baseCosts: List[int], toppingCosts: List[int], target: int) -> int:
        self.min_diff = float('inf')
        self.res = 0
        self.dfs(0, 0, baseCosts, toppingCosts, target)
        return self.res

    def dfs(self, index, cur, baseCosts, toppingCosts, target):
        if index == len(toppingCosts):
            for b in baseCosts:
                total = b + cur
                if (abs(total-target) < self.min_diff or
                        (abs(total-target) == self.min_diff and total < self.res)):
                    self.res = total
                    self.min_diff = abs(total-target)
            return
        for i in range(3):
            self.dfs(index+1, cur + i *
                     toppingCosts[index], baseCosts, toppingCosts, target)


class Solution2:
    def closestCost(self, baseCosts: List[int], toppingCosts: List[int], target: int) -> int:
        res = 0
        res_diff = float('inf')

        UPPER_BOUND = 10**4
        m = len(toppingCosts)
        # backpack dp[i][j]: select first ith toppings can be equal to target j
        dp = [[False] * (UPPER_BOUND+1) for _ in range(m)]
        for i in range(m):
            dp[i][0] = True
        for i in range(m):
            for j in range(1, UPPER_BOUND+1):
                dp[i][j] = dp[i-1][j]
                if j - toppingCosts[i] >= 0:
                    dp[i][j] = dp[i][j] or dp[i-1][j-toppingCosts[i]]
                if j - 2*toppingCosts[i] >= 0:
                    dp[i][j] = dp[i][j] or dp[i-1][j-2*toppingCosts[i]]

        for j in range(UPPER_BOUND+1):
            if dp[m-1][j]:
                for b in baseCosts:
                    diff = abs(b + j - target)
                    if diff < res_diff or (diff == res_diff and b+j < res):
                        res = b+j
                        res_diff = diff
        return res
