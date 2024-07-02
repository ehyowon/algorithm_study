# 시간초과
N = int(input())
X = list(map(int, input().split()))
idx = sorted(X)

for i in range(N):
	k = 0
	for j in range(N) : 
		if j >=1 and idx[j] == idx[j-1] : 
			k -= 1
		if X[i] == idx[j] : 
			print(k, end=" ")
			break
		k += 1
