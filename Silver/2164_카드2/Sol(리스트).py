# 시간초과 : list에서 pop(0)은 O(n), queue에서 pop(0)은 O(1) 
N = int(input())
arr = [i for i in range(1, N+1)]

while len(arr) > 1:
	arr.pop(0)
	a = arr.pop(0)
	arr.append(a)

print(*arr)
