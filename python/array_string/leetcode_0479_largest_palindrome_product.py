"""
author: Zhengjian Kang
date: 06/26/2021

残酷群每日一题: 06/26/2021

https://leetcode.com/problems/largest-palindrome-product/

479. Largest Palindrome Product

note: Brute force

Given an integer n, return the largest palindromic integer that can be represented 
as the product of two n-digits integers. Since the answer can be very large, return it modulo 1337.

Example 1:
Input: n = 2
Output: 987
Explanation: 99 x 91 = 9009, 9009 % 1337 = 987

Example 2:
Input: n = 1
Output: 9
 
Constraints:
1 <= n <= 8
"""

class Solution:
    def largestPalindrome(self, n: int) -> int:
        # enumerate all palindrom possibilities
        if n == 1: return 9
        lower = pow(10, n-1)
        upper = pow(10, n)-1
        for i in range(upper, lower-1, -1):
            palindrome = int(str(i) + str(i)[::-1])
            j = upper
            digit = math.sqrt(palindrome)
            while j >= digit:
                if palindrome % j == 0 and palindrome // j >= lower:
                    return palindrome % 1337
                j -= 1
        return -1
