"""
author: Zhengjian Kang
date: 11/22/2020

https://leetcode.com/problems/numbers-at-most-n-given-digit-set/

902. Numbers At Most N Given Digit Set

Given an array of digits, you can write numbers using each digits[i] as many
times as we want.  For example, if digits = ['1','3','5'], we may write numbers
such as '13', '551', and '1351315'.

Return the number of positive integers that can be generated that are less than
or equal to a given integer n.

Example 1:
Input: digits = ["1","3","5","7"], n = 100
Output: 20
Explanation:
The 20 numbers that can be written are:
1, 3, 5, 7, 11, 13, 15, 17, 31, 33, 35, 37, 51, 53, 55, 57, 71, 73, 75, 77.

Example 2:
Input: digits = ["1","4","9"], n = 1000000000
Output: 29523
Explanation:
We can write 3 one digit numbers, 9 two digit numbers, 27 three digit numbers,
81 four digit numbers, 243 five digit numbers, 729 six digit numbers,
2187 seven digit numbers, 6561 eight digit numbers, and 19683 nine digit
numbers.
In total, this is 29523 integers that can be written using the digits array.

Example 3:
Input: digits = ["7"], n = 8
Output: 1

Constraints:

1 <= digits.length <= 9
digits[i].length == 1
digits[i] is a digit from '1' to '9'.
All the values in digits are unique.
1 <= n <= 109
"""


# https://www.youtube.com/watch?v=swcKO4qagsA
# can use dfs
class Solution:
    def atMostNGivenDigitSet(self, digits: List[str], n: int) -> int:
        n_place = len(str(n))
        len_of_digits = len(digits)
        self.count = 0
        # number of digits less than n with one few place
        for i in range(1, n_place):
            self.count += len_of_digits**i
        str_n = str(n)
        self.dfs(digits, str_n, 0)
        return self.count

    def dfs(self, digits, str_n, pos):
        if pos == len(str_n):
            self.count += 1
            return
        len_of_digits = len(digits)
        for d in digits:
            if d < str_n[pos]:
                self.count += len_of_digits**(len(str_n)-pos-1)
            elif d == str_n[pos]:
                self.dfs(digits, str_n, pos+1)
