def dfs(x,y):
  #주어진 범위를 벗어나는 경우 즉시 종료
  if x <= -1 or x >= n or y <= -1 or y >= m:
    return False
  #현재 노드를 아직 방문하지 않았다면  
  if graph[x][y] == 0:
    #해당 노드를 방문처리
    graph[x][y] = 1
    dfs(x-1,y)
    dfs(x+1,y)
    dfs(x,y-1)
    dfs(x,y+1)
    return True
  return False
  
n, m = map(int, input().split())
graph = []
for i in range(n):
  graph.append(list(map(int, input())))

result = 0
for i in range(n):
  for j in range(m):
    if dfs(i,j) == True:
      result += 1

print(result)