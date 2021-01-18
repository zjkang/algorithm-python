"""
author: Zhengjian Kang
date: 01/17/2021

https://leetcode.com/problems/checking-existence-of-edge-length-limited-paths-ii/

1724. Checking Existence of Edge Length Limited Paths II

An undirected graph of n nodes is defined by edgeList, where edgeList[i] =
[ui, vi, disi] denotes an edge between nodes ui and vi with distance disi.
Note that there may be multiple edges between two nodes, and the graph may
not be connected.

Implement the DistanceLimitedPathsExist class:

DistanceLimitedPathsExist(int n, int[][] edgeList) Initializes the class with
an undirected graph.
boolean query(int p, int q, int limit) Returns true if there exists a path
from p to q such that each edge on the path has a distance strictly less than
limit, and otherwise false.

Input
["DistanceLimitedPathsExist", "query", "query", "query", "query"]
[[6, [[0, 2, 4], [0, 3, 2], [1, 2, 3], [2, 3, 1], [4, 5, 5]]], [2, 3, 2],
[1, 3, 3], [2, 0, 3], [0, 5, 6]]
Output
[null, true, false, true, false]

Explanation
DistanceLimitedPathsExist distanceLimitedPathsExist =
new DistanceLimitedPathsExist(6, [[0, 2, 4], [0, 3, 2], [1, 2, 3],
[2, 3, 1], [4, 5, 5]]);
distanceLimitedPathsExist.query(2, 3, 2); // return true.
There is an edge from 2 to 3 of distance 1, which is less than 2.
distanceLimitedPathsExist.query(1, 3, 3); // return false.
There is no way to go from 1 to 3 with distances strictly less than 3.
distanceLimitedPathsExist.query(2, 0, 3); // return true. There is a way to go
from 2 to 0 with distance < 3: travel from 2 to 3 to 0.
distanceLimitedPathsExist.query(0, 5, 6); // return false. There are
no paths from 0 to 5.

Constraints:
2 <= n <= 104
0 <= edgeList.length <= 104
edgeList[i].length == 3
0 <= ui, vi, p, q <= n-1
ui != vi
p != q
1 <= disi, limit <= 109
At most 104 calls will be made to query.
"""


class DistanceLimitedPathsExist:

    def __init__(self, n: int, edgeList: List[List[int]]):
        def find_father(x):
            if father[x] != x:
                father[x] = find_father(father[x])
            return father[x]

        def union(x, y):
            x = find_father(x)
            y = find_father(y)
            if x < y:
                father[y] = x
            else:
                father[x] = y

        father = [i for i in range(n)]
        edgeList.sort(key=lambda x: x[2])
        self.weights = []
        self.connections = []
        for index, (u, v, dist) in enumerate(edgeList):
            union(u, v)
            if index != len(edgeList)-1 and dist == edgeList[index+1][2]:
                continue
            self.weights.append(dist)
            self.connections.append([find_father(x)
                                     for i, x in enumerate(father)])

    def query(self, p: int, q: int, limit: int) -> bool:
        import bisect
        index = bisect.bisect_left(self.weights, limit)
        if index == 0:
            return False
        return self.connections[index-1][p] == self.connections[index-1][q]


# Your DistanceLimitedPathsExist object will be instantiated and called as such:
# obj = DistanceLimitedPathsExist(n, edgeList)
# param_1 = obj.query(p,q,limit)
