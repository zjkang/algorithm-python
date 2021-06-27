"""
author: Zhengjian Kang
date: 06/27/2021

残酷群每日一题: 06/25/2021

https://leetcode.com/problems/super-ugly-number/

313. Super Ugly Number

note: 有点像dp的priority queue dp[i] = min(dp[k0]*nums[0], ...., dp[kn]*nums[t])

A super ugly number is a positive integer whose prime factors are in the array primes.
Given an integer n and an array of integers primes, return the nth super ugly number.
The nth super ugly number is guaranteed to fit in a 32-bit signed integer.

Example 1:
Input: n = 12, primes = [2,7,13,19]
Output: 32
Explanation: [1,2,4,7,8,13,14,16,19,26,28,32] is the sequence of the first 12 super ugly numbers given primes = [2,7,13,19].

Example 2:
Input: n = 1, primes = [2,3,5]
Output: 1
Explanation: 1 has no prime factors, therefore all of its prime factors are in the array primes = [2,3,5].

Constraints:
1 <= n <= 10^6
1 <= primes.length <= 100
2 <= primes[i] <= 1000
primes[i] is guaranteed to be a prime number.
All the values of primes are unique and sorted in ascending order.
"""

class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        N = len(primes)
        rets = [1]
        pq = []
        pointers = [0] * N # processed index in rets
        for i in range(N):
            heapq.heappush(pq, (rets[pointers[i]]*primes[i], i))

        for _ in range(n-1):
            cur, idx = pq[0]
            rets.append(cur)
            while pq and pq[0][0] == cur:
                _, i = pq[0]
                heapq.heappop(pq)
                pointers[i] += 1
                heapq.heappush(pq, (rets[pointers[i]]*primes[i], i))
                  
        return rets[-1]
