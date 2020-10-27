"""
author: Zhengjian Kang
date: 10/25/2020

https://leetcode.com/problems/the-skyline-problem/

218. The Skyline Problem

A city's skyline is the outer contour of the silhouette formed by all the
buildings in that city when viewed from a distance. Now suppose you are given
the locations and height of all the buildings as shown on a cityscape photo
(Figure A), write a program to output the skyline formed by these buildings
collectively (Figure B).

Buildings Skyline Contour
The geometric information of each building is represented by a triplet of
integers [Li, Ri, Hi], where Li and Ri are the x coordinates of the left and
right edge of the ith building, respectively, and Hi is its height. It is
guaranteed that 0 ≤ Li, Ri ≤ INT_MAX, 0 < Hi ≤ INT_MAX, and Ri - Li > 0. You
may assume all buildings are perfect rectangles grounded on an absolutely flat
surface at height 0.

For instance, the dimensions of all buildings in Figure A are recorded as:
[ [2 9 10], [3 7 15], [5 12 12], [15 20 10], [19 24 8] ] .

The output is a list of "key points" (red dots in Figure B) in the format of
[ [x1,y1], [x2, y2], [x3, y3], ... ] that uniquely defines a skyline. A key
point is the left endpoint of a horizontal line segment. Note that the last key
point, where the rightmost building ends, is merely used to mark the
termination of the skyline, and always has zero height. Also, the ground in
between any two adjacent buildings should be considered part of the skyline
contour.

For instance, the skyline in Figure B should be represented as:[ [2 10],
[3 15], [7 12], [12 0], [15 10], [20 8], [24, 0] ].

Notes:

The number of buildings in any input list is guaranteed to be in the range
[0, 10000].
The input list is already sorted in ascending order by the left x position Li.
The output list must be sorted by the x position.
There must be no consecutive horizontal lines of equal height in the output
skyline. For instance, [...[2 3], [4 5], [7 5], [11 5], [12 7]...] is not
acceptable; the three lines of height 5 should be merged into one in the final
output as such: [...[2 3], [4 5], [12 7], ...]
"""


class Solution:
    BEGIN = 0
    END = 1

    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        if not buildings or len(buildings) == 0:
            return []

        events = self.to_sorted_events(buildings)
        res = []

        from sortedcontainers import SortedDict
        heights = SortedDict()
        max_height = i = 0
        while i < len(events):
            time = events[i][0]
            nextI = i
            while nextI < len(events) and events[nextI][0] == time:
                self.process_event(heights, events[nextI])
                nextI += 1
            nextMax = 0 if len(heights) == 0 else heights.peekitem()[0]
            if nextMax != max_height:
                res.append([time, nextMax])
                max_height = nextMax
            i = nextI
        return res

    def process_event(self, heights, event):
        height = event[1]
        if event[2] == Solution.BEGIN:
            heights[height] = heights.get(height, 0) + 1
            return
        new_count = heights.get(height, 0) - 1
        if new_count > 0:
            heights[height] = new_count
        else:
            heights.pop(height)

    def to_sorted_events(self, buildings):
        events = []
        # event [time, height, begin/end]
        for b in buildings:
            events.append([b[0], b[2], Solution.BEGIN])
            events.append([b[1], b[2], Solution.END])
        events.sort()
        return events
