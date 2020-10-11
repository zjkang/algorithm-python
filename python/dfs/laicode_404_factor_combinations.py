"""
author: Zhengjian Kang
date: 10/11/2020

https://app.laicode.io/app/problem/404

404. Factor Combinations

Given an integer number, return all possible combinations of the factors that can multiply to the target number.

Example
Give A = 24
since 24 = 2 x 2 x 2 x 3
              = 2 x 2 x 6
              = 2 x 3 x 4
              = 2 x 12
              = 3 x 8
              = 4 x 6
your solution should return
{ { 2, 2, 2, 3 }, { 2, 2, 6 }, { 2, 3, 4 }, { 2, 12 }, { 3, 8 }, { 4, 6 } }
note: duplicate combination is not allowed.
"""


class Solution(object):
    def combinations(self, target):
        """
        input: int target
        return: int[][]
        """
        self.result = []
        factors = self.get_factors(target)
        self.dfs(target, factors, 0, [])
        return self.result

    def dfs(self, target, factors, index, one_res):
        if index == len(factors):
            if target == 1 and len(one_res) > 1:
                self.result.append(list(one_res))
            return

        self.dfs(target, factors, index + 1, one_res)
        num = factors[index]
        while target % num == 0:
            one_res.append(factors[index])
            self.dfs(target // num, factors, index + 1, one_res)
            num *= factors[index]
        while one_res and one_res[-1] == factors[index]:
            one_res.pop()

    def get_factors(self, target):
        factors = []
        for num in range(target // 2, 1, -1):
            if target % num == 0:
                factors.append(num)
        return factors


a = Solution()
print(a.combinations(24))
