#numNodes: int
#visited[numNodes]: List[Boolean]
#next: List[List[int]] 

def main():
  # prepare next; // next[i][j]: there is a directional path i->j
  
  # dfs 判断有环
  for i in range(numNodes):
    if not dfs(i):
      return False
    return True
  
  # top bfs 判断有环
  return bfs()


def dfs(cur):
  #1: visited, 2: visiting
  if (visited[cur]==1):
    return True

    visited[cur] = 2
    for (next: next[cur]):
        if (visited[next]==1): continue
        if (visited[next]==2): return False
        if (dfs(next)==False):  return False
    
    visited[cur] = 1
    return True


def bfs():
  q = deque([])
  count = 0
  
  InDegree = [0] * numNodes
  for i in range(numNodes):
    for j in next[i]:
      InDegree[j] += 1
  
  for i in range(numNodes):
    if InDegree[i] == 0:
      q.append(i)
      count += 1
      
  while q:
    curCourse = q.popleft()
    for child in next[curCourse]:
      InDegree[child] -= 1
      if InDegree[child] == 0:
        q.append(child)
        count += 1
  
  return count == numNodes
