def dfs(k):
	visited[k] = 1
	cnt = 1
	for node in graph[k]:
		if visited[node] == 0:
			cnt += dfs(node)
	return cnt

computer = int(input())
connect = int(input())
graph = [[] for _ in range(computer+1)]
visited = [0 for _ in range(computer+1)]
for _ in range(connect):
	a, b = map(int,input().split())
	graph[a] += [b]
	graph[b] += [a]

print(dfs(1)-1)
