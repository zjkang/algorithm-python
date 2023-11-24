'''
author: Zhengjian Kang
date: 05/01/2021

残酷群每日一题: 05/01/2021

https://leetcode.com/problems/candy/

135. Candy

note: two pass + greedy
#我们令f[0]=1，然后从左往右扫一遍，保证f[i]与f[i-1]比较时符合要求
#即f[i]=max(1, f[i-1]+1 if rating[i]>rating[i-1]). 这个操作更新了f[i]的下限，是f[i]合法的一个必要条件。
#言下之意就是说，f[i]不保证是一个合法的分配，但f[i]不能更小了。
# 然后从右往左扫一遍，保证f[i]与f[i+1]比较时符合要求，
# 即f[i]=max(f[i], f[i+1]+1 if rating[i]>rating[i+1]).
# 这个操作同样进一步更新了f[i]的下限，即f[i]不能更小了。
# 以上两步操作都是必要条件，找到了f[i]的一个下限。但是这个下限本身是否就是符合要求的方案呢？事实上就是如此。上面两轮two pass保证了每个小朋友与相邻两个人做比较时都是公平的。
# 换句话说，任意两个相邻小朋友之间的比较和分配都是公平的。所以此时f[i]的分布同时也是一个充分解。
# 贴着下限的充分解，就是题目要求的最优解（最少分发总数)

There are n children standing in a line. Each child is assigned a rating value given in the integer array ratings.

You are giving candies to these children subjected to the following requirements:

Each child must have at least one candy.
Children with a higher rating get more candies than their neighbors.
Return the minimum number of candies you need to have to distribute the candies to the children.

Example 1:
Input: ratings = [1,0,2]
Output: 5
Explanation: You can allocate to the first, second and third child with 2, 1, 2 candies respectively.

Example 2:
Input: ratings = [1,2,2]
Output: 4
Explanation: You can allocate to the first, second and third child with 1, 2, 1 candies respectively.
The third child gets 1 candy because it satisfies the above two conditions.

Constraints:
n == ratings.length
1 <= n <= 2 * 10^4
0 <= ratings[i] <= 2 * 10^4
'''

class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        candies = [1] * n
        for i in range(1, n):
            if ratings[i] > ratings[i-1]:
                candies[i] = max(candies[i], candies[i-1]+1)
        for i in range(n-2, -1, -1):
            if ratings[i] > ratings[i+1]:
                candies[i] = max(candies[i], candies[i+1]+1)
        
        return sum(candies)
        
