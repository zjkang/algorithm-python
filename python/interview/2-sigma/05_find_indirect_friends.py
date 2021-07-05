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
    
    
# ===================
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
    
    res = set() # as global var
        
    def dfs(node, graph, cur):
        # print(cur)
        nonlocal res
        if node == n:
            if len(cur) > len(res):
                res = list(cur)
            return
        # select node & make indenpendent set
        flag = 0
        for nei in graph[node]:
            if nei in cur:
                flag = 1
                break
        if flag == 0:
            cur.add(node)
            dfs(node+1, graph, cur)
            cur.remove(node)
        # not select node   
        dfs(node+1, graph, cur)
        
    cur = set()
    dfs(0, graph, cur)
    return res
    
# n = 3
# edges = [[0,1], [1,2]]
# print(find_set(n, edges))

n = 6
edges = [[0,1], [0,2], [1,4], [1,3], [2,3], [2,5], [3,5], [4,5]]
print(find_set(n, edges))
    
# =============================================================
# # 修改闭包变量实例
# def outer(a):       # outer是外部函数，a和b都是外部函数的临时变量
#     b = 10      # a和b都是闭包变量
#     c = [a]     # 这里对应修改闭包变量的方法2
    
#     def inner():    # inner是内部函数
#         # 内函数中想修改闭包变量
#         nonlocal b      # 方法1 nonlocal关键字声明
#         b += 1

#         c[0] += 1       # 方法2 把闭包变量修改成可变数据类型，比如：列表
#         print(c[0], b)
        
#     return inner    # 外部函数返回内部函数的引用


# demo = outer(5)
# demo()      # 6 11

    
