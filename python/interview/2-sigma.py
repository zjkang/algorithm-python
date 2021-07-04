# 1. the number of connected component between 2 grids
# from collections import deque

# def bfs(grid, x, y, visited):
#     visited[x][y] = True
#     queue = deque([(x,y)])
#     dx = [0,-1,0,1]
#     dy = [-1,0,1,0]
#     M, N = len(grid), len(grid[0])
#     flag = 0
#     while queue:
#         x, y = queue.popleft()
#         if grid[x][y] == 2:
#             flag = 1
#         for i in range(4):
#             cx = x + dx[i]
#             cy = y + dy[i]
#             if 0<= cx < M and 0<= cy < N and not visited[cx][cy] and grid[cx][cy] in [1,2]:
#                 queue.append((cx,cy))
#                 visited[cx][cy] = True
#     return flag == 1
                
# def count_connected_comp(grid1, grid2):
#     M, N = len(grid1), len(grid1[0])
#     diff_grid = [[0] * N for _ in range(M)]
#     for i in range(M):
#         for j in range(N):
#             if grid1[i][j] == grid2[i][j]:
#                 diff_grid[i][j] = grid1[i][j]
#             else:
#                 diff_grid[i][j] = 2

#     visited = [[False] * N for _ in range(M)]
#     res = 0
#     for i in range(M):
#         for j in range(N):
#             if diff_grid[i][j] in [1,2] and  not visited[i][j]:
#                 if not bfs(diff_grid, i, j, visited): # return true if find 2 in the connected component
#                     res += 1
#     return res
                    
# # test cases   
# a = [[1,0,0],[0,0,0],[0,1,1]]
# b = [[1,0,0],[0,0,0],[0,1,1]]
# print(count_connected_comp(a, b))

# a = [[1,0,0],[0,0,0],[0,1,1]]
# b = [[1,0,0],[0,0,0],[1,1,1]]
# print(count_connected_comp(a, b))

# 2. build dependency schedule


# 3 order execution buy/sell



# class OrderType:
#     BUY = 0
#     SELL = 1
    

    
# print(OrderType.BUY)
