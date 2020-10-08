"""
author: Wei Li
date: 10/08/2020

https://www.lintcode.com/problem/first-unique-number-in-data-stream-ii/description

685. First Unique Number in Data Stream.

Given a continuous stream of data, write a function that returns the first unique number (including the last number) when the terminating number arrives. If the unique number is not found, return -1.

Example1

Input: 
[1, 2, 2, 1, 3, 4, 4, 5, 6]
5
Output: 3
Example2

Input: 
[1, 2, 2, 1, 3, 4, 4, 5, 6]
7
Output: -1
Example3

Input: 
[1, 2, 2, 1, 3, 4]
3
Output: 3
"""

class Solution:
    """
    @param nums: a continuous stream of numbers
    @param number: a number
    @return: returns the first unique number
    """
    def firstUniqueNumber(self, nums, number):
        # Write your code here
        counter = {}
        
        for num in nums:
            counter[num] = counter.get(num, 0) + 1
            
            if num == number:
                break
        else:
            return -1
        
        
        for num in nums:
            if counter[num] == 1:
                return num
        
        return -1        
                
