# 시간초과
N = int(input())
X = list(map(int, input().split()))
Y = set(X)
Z = [0 for _ in range(N)]
a = []

k = 0
for i in range(N):
	m = min(X)
	if k > 0 and m == a[-1]:
		k -= 1
	a.append(m)
	b = X.index(a[i])
	X[b] = float("inf")
	Z[b] = k
	k += 1

print(*Z)
