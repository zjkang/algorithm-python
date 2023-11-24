"""
author: Zhengjian Kang
date: 08/18/2021
残酷群每日一题: 08/18/2021

https://leetcode.com/problems/filling-bookcase-shelves/
1105. Filling Bookcase Shelves

note: 考虑最后一层可以用几本书

You are given an array books where books[i] = [thickness_i, height_i]
indicates the thickness and height of the ith book. You are also given an integer shelfWidth.

We want to place these books in order onto bookcase shelves that have a total width shelfWidth.

We choose some of the books to place on this shelf such that the sum of their thickness
is less than or equal to shelfWidth, then build another level of the shelf of the bookcase
so that the total height of the bookcase has increased by the maximum height of the books we just put down.
We repeat this process until there are no more books to place.

Note that at each step of the above process, the order of the books we place is the same order as the given sequence of books.

For example, if we have an ordered list of 5 books, we might place the first and second book onto the first shelf,
the third book on the second shelf, and the fourth and fifth book on the last shelf.
Return the minimum possible height that the total bookshelf can be after placing shelves in this manner.
 

Example 1:
Input: books = [[1,1],[2,3],[2,3],[1,1],[1,1],[1,1],[1,2]], shelf_width = 4
Output: 6
Explanation:
The sum of the heights of the 3 shelves is 1 + 3 + 2 = 6.
Notice that book number 2 does not have to be on the first shelf.

Example 2:
Input: books = [[1,3],[2,4],[3,2]], shelfWidth = 6
Output: 4
 

Constraints:
1 <= books.length <= 1000
1 <= thicknessi <= shelfWidth <= 1000
1 <= heighti <= 1000
"""

class Solution:
    def minHeightShelves(self, books: List[List[int]], shelf_width: int) -> int:
        #dp[i]: the min height of first ith books
        n = len(books)
        dp = [float('inf')] * n
        for i in range(n):
            width = 0
            max_height = 0
            for j in range(i, -1, -1):
                width += books[j][0]
                max_height = max(max_height, books[j][1])
                if width > shelf_width:
                    break
                # when the width sum <= shelf_width
                dp[i] = min(dp[i], (dp[j-1] if j >= 1 else 0) + max_height)
        return dp[-1] 
        
