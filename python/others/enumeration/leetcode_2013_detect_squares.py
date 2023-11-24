"""
author: Zhengjian Kang
date: 09/28/2021

残酷群每日一题: 09/27/2021

https://leetcode.com/problems/detect-squares/

2013. Detect Squares

note: brute force对于每一个点作为query point的对角线的点进行枚举，然后判断是否可以形成正方形。
进一步优化，考虑x坐标在一个区间，这样对于x坐标进行枚举。

You are given a stream of points on the X-Y plane. Design an algorithm that:

Adds new points from the stream into a data structure. Duplicate points are allowed and should be treated as different points.
Given a query point, counts the number of ways to choose three points from the data structure such that the three points
and the query point form an axis-aligned square with positive area.
An axis-aligned square is a square whose edges are all the same length and are either parallel or perpendicular to the x-axis and y-axis.

Implement the DetectSquares class:

DetectSquares() Initializes the object with an empty data structure.
void add(int[] point) Adds a new point point = [x, y] to the data structure.
int count(int[] point) Counts the number of ways to form axis-aligned squares with point point = [x, y] as described above.
 

Example 1:
Input
["DetectSquares", "add", "add", "add", "count", "count", "add", "count"]
[[], [[3, 10]], [[11, 2]], [[3, 2]], [[11, 10]], [[14, 8]], [[11, 2]], [[11, 10]]]
Output
[null, null, null, null, 1, 0, null, 2]

Explanation
DetectSquares detectSquares = new DetectSquares();
detectSquares.add([3, 10]);
detectSquares.add([11, 2]);
detectSquares.add([3, 2]);
detectSquares.count([11, 10]); // return 1. You can choose:
                               //   - The first, second, and third points
detectSquares.count([14, 8]);  // return 0. The query point cannot form a square with any points in the data structure.
detectSquares.add([11, 2]);    // Adding duplicate points is allowed.
detectSquares.count([11, 10]); // return 2. You can choose:
                               //   - The first, second, and third points
                               //   - The first, third, and fourth points
 

Constraints:
point.length == 2
0 <= x, y <= 1000
At most 3000 calls in total will be made to add and count.
"""

class DetectSquares:
    
    def __init__(self):
        self.counts = defaultdict(lambda: defaultdict(int))
        

    def add(self, point: List[int]) -> None:
        x, y = point
        self.counts[x][y] += 1
        

    def count(self, point: List[int]) -> int:
        x, y = point
        ret = 0
        x_points = list(self.counts.keys())
        for i in x_points:
            if i == x:
                continue
            dist = abs(x - i)
            
            j = y - dist
            if j >= 0 and j <= 1000:
                ret += self.counts[i][y]*self.counts[i][j]*self.counts[x][j]
            
            j = y + dist
            if j >= 0 and j <= 1000:
                ret += self.counts[i][y]*self.counts[i][j]*self.counts[x][j]
        
        return ret
        


# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)
