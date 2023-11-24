"""
author: Zhengjian Kang
date: 06/28/2021

残酷群每日一题: 06/27/2021

https://leetcode.com/problems/prime-palindrome/

866. Prime Palindrome

note: Palindrome deal with half of string

Find the smallest prime palindrome greater than or equal to n.
Recall that a number is prime if it's only divisors are 1 and itself, and it is greater than 1. 
For example, 2,3,5,7,11 and 13 are primes.
Recall that a number is a palindrome if it reads the same from left to right as it does from right to left. 
For example, 12321 is a palindrome.

Example 1:
Input: n = 6
Output: 7

Example 2:
Input: n = 8
Output: 11

Example 3:
Input: n = 13
Output: 101
 
Note:
1 <= n <= 10^8
The answer is guaranteed to exist and be less than 2 * 10^8.
"""


class Solution:
    def primePalindrome(self, n: int) -> int:
        def is_prime(k):
            if k == 1: return False
            if k % 2 == 0: return k == 2
            for i in range(3, int(math.sqrt(k))+1):
                if k % i == 0:
                    return False
            return True    
        
        if n > 7 and n <= 11: return 11
        M = str(n)
        l = len(M) // 2
        
        lower = pow(10, l)
        # XYZZYX is not prime
        for i in range(lower, 20000+1):
            s = str(i) + str(i)[:-1][::-1]
            k = int(s)
            if k >= n and is_prime(k):
                return k
        return -1
