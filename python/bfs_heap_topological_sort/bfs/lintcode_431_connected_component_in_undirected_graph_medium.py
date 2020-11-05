"""
author: Wei Li
date: 10/20/2020

https://www.lintcode.com/problem/connected-component-in-undirected-graph/

431. Connected Component in Undirected Graph

Find connected component in undirected graph.

Each node in the graph contains a label and a list of its neighbors.

(A connected component of an undirected graph is a subgraph in which any two
vertices are connected to each other by paths, and which is connected to no
additional vertices in the supergraph.)

You need return a list of label set.

样例
Example 1:
Input: {1,2,4#2,1,4#3,5#4,1,2#5,3}
Output: [[1,2,4],[3,5]]
Explanation:
  1------2  3
   \     |  |
    \    |  |
     \   |  |
      \  |  |
        4   5

Example 2:
Input: {1,2#2,1}
Output: [[1,2]]
Explanation:
1--2

说明
Learn more about representation of graphs

注意事项
Nodes in a connected component should sort by label in ascending order.
Different connected components can be in any order.
"""
"""
Definition for a undirected graph node
class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []
"""


class Solution:
    """
    @param {UndirectedGraphNode[]} nodes a array of undirected graph node
    @return {int[][]} a connected set of a undirected graph
    """

    def connectedSet(self, nodes):
        visited = set()
        ans = []

        for node in nodes:
            if node not in visited:
                ans.append(sorted(self.bfs(visited, node)))

        return ans

    def bfs(self, visited, node):
        labels = []
        labels.append(node.label)
        visited.add(node)
        import collections
        queue = collections.deque([node])

        while queue:
            curr = queue.popleft()
            for neighbor in curr.neighbors:
                if neighbor not in visited:
                    labels.append(neighbor.label)
                    visited.add(neighbor)
                    queue.append(neighbor)

        return labels
