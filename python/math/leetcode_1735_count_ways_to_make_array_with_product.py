
"""
author: Zhengjian Kang
date: 03/24/2021

残酷群每日一题: 01/24/2021

https://leetcode.com/problems/count-ways-to-make-array-with-product/

1735. Count Ways to Make Array With Product

note: math + 排列组合数, 完全不会做的一道题

You are given a 2D integer array, queries. For each queries[i],
where queries[i] = [ni, ki], find the number of different ways you can
place positive integers into an array of size ni such that the product of
the integers is ki. As the number of ways may be too large, the answer to
the ith query is the number of ways modulo 109 + 7.

Return an integer array answer where answer.length == queries.length, and 
answer[i] is the answer to the ith query.

Example 1:
Input: queries = [[2,6],[5,1],[73,660]]
Output: [4,1,50734910]
Explanation: Each query is independent.
[2,6]: There are 4 ways to fill an array of size 2 that multiply to 6:
[1,6], [2,3], [3,2], [6,1].
[5,1]: There is 1 way to fill an array of size 5 that multiply to 1:
[1,1,1,1,1].
[73,660]: There are 1050734917 ways to fill an array of size 73 that
multiply to 660. 1050734917 modulo 109 + 7 = 50734910.

Example 2:
Input: queries = [[1,1],[2,2],[3,3],[4,4],[5,5]]
Output: [1,2,3,10,5]

Constraints:
1 <= queries.length <= 10^4
1 <= ni, ki <= 10^4
"""

from functools import lru_cache


class Solution:

    MOD = 1000000007

    @staticmethod
    @lru_cache(10000)
    def factorize(k):
        primes = []
        i = 2
        while i * i <= k:
            cnt = 0
            while k % i == 0:
                cnt += 1
                k //= i
            if cnt > 0:
                primes.append((i, cnt))
            i += 1
        if k != 1:
            primes.append((k, 1))
        return primes

    @staticmethod
    @lru_cache(100000)
    def C(n, m):  # calculate C(n, m), choose m in n
        if m > n:
            return 0
        tmp = 1
        for i in range(m):
            tmp *= n - i
        for i in range(m):
            tmp //= i + 1
        return tmp % Solution.MOD

    @staticmethod
    @lru_cache(1000)
    def getF(n, m):  # dp f(n, m) = f(n - 1, m - j) for j in 1,2,....
        if n == 0:
            if m == 0:
                return 1
            else:
                return 0
        if m < n:
            return 0
        tmp = 0
        for j in range(1, m + 1):
            tmp += Solution.getF(n - 1, m - j)
            tmp %= Solution.MOD
        return tmp

    @staticmethod
    @lru_cache(100000)
    def calc(n, m):  # add up all possibilities
        ans = 0
        for i in range(m):
            i += 1
            ans += Solution.C(n, i) * Solution.getF(i, m) % Solution.MOD
            ans %= Solution.MOD
        return ans

    def waysToFillArray(self, queries: List[List[int]]) -> List[int]:
        aq = []
        for sz, k in queries:
            ans = 1
            for p, cnt in self.factorize(k):
                # print(p, cnt)
                ans *= self.calc(sz, cnt)
                ans %= self.MOD
            aq.append(ans)
        return aq
