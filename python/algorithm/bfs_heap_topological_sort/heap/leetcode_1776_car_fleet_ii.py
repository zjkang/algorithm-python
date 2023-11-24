
"""
author: Zhengjian Kang
date: 03/04/2021

残酷群每日一题: 03/03/2021

https://leetcode.com/problems/car-fleet-ii/

1776. Car Fleet II

note: 这道题用heap更新位置信息

There are n cars traveling at different speeds in the same direction along a
one-lane road. You are given an array cars of length n, where cars[i] =
[positioni, speedi] represents:

positioni is the distance between the ith car and the beginning of the road
in meters. It is guaranteed that positioni < positioni+1.
speedi is the initial speed of the ith car in meters per second.
For simplicity, cars can be considered as points moving along the number line.
Two cars collide when they occupy the same position. Once a car collides with
another car, they unite and form a single car fleet. The cars in the formed
fleet will have the same position and the same speed, which is the initial
speed of the slowest car in the fleet.

Return an array answer, where answer[i] is the time, in seconds, at which the
ith car collides with the next car, or -1 if the car does not collide with
the next car. Answers within 10-5 of the actual answers are accepted.


Example 1:
Input: cars = [[1,2],[2,1],[4,3],[7,2]]
Output: [1.00000,-1.00000,3.00000,-1.00000]
Explanation: After exactly one second, the first car will collide with the
second car, and form a car fleet with speed 1 m/s. After exactly 3 seconds,
the third car will collide with the fourth car, and form a car fleet with
speed 2 m/s.

Example 2:
Input: cars = [[3,4],[5,4],[6,3],[9,1]]
Output: [2.00000,1.00000,1.50000,-1.00000]

Constraints:
1 <= cars.length <= 10^5
1 <= positioni, speedi <= 10^6
positioni < positioni+1
"""


class Solution:
    def getCollisionTimes(self, cars: List[List[int]]) -> List[float]:
        # build heap (time_collision, car index, previous car index
        m = len(cars)
        heap = []
        prev = [-1] * m
        for i in range(m):
            if i == 0:
                continue
            position_diff = cars[i][0] - cars[i - 1][0]
            speed_diff = cars[i - 1][1] - cars[i][1]
            prev[i] = i - 1
            if speed_diff > 0:
                heap.append((position_diff / speed_diff, i, i - 1))
        heapq.heapify(heap)

        # merge cars by time order
        result = [-1] * m
        while heap:
            time, i, j = heapq.heappop(heap)
            if result[j] != -1:
                continue
            result[j] = time

            prev[i] = prev[j]
            position_diff = cars[i][0] - cars[prev[i]][0]
            speed_diff = cars[prev[i]][1] - cars[i][1]
            if speed_diff > 0 and prev[i] != -1:
                heapq.heappush(heap, (position_diff / speed_diff, i, prev[i]))
        return result
