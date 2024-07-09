T = int(input())
airplane = [0 for _ in range(T)]

for i in range(T):
	N, M = map(int, input().split())
	for j in range(M):
		a, b = map(int, input().split())
	airplane[i] = N - 1

print(*airplane, sep='\n')
