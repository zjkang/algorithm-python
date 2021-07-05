# max independent vertex

# input undirect edge: 0 -> 1, 1 -> 2
# return 1, 3 as there is no direct edge between 1,3, 1,3 do not know each other directlly

from collections import defaultdict
def find_set(n, edges):
    # node [0,n-1]
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
    # print(graph)
    
    def dfs(node, graph, cur, res):
        # print(cur)
        if node == n:
            if len(cur) > len(res[0]):
                res[0] = list(cur)
            return
        # select node & make indenpendent set
        flag = 0
        for nei in graph[node]:
            if nei in cur:
                flag = 1
                break
        if flag == 0:
            cur.add(node)
            dfs(node+1, graph, cur, res)
            cur.remove(node)
        # not select node   
        dfs(node+1, graph, cur, res)
        
    cur = set()
    res = [[]]
    dfs(0, graph, cur, res)
    return res
    
# n = 3
# edges = [[0,1], [1,2]]
# print(find_set(n, edges))

n = 6
edges = [[0,1], [0,2], [1,4], [1,3], [2,3], [2,5], [3,5], [4,5]]
print(find_set(n, edges))
    

    
