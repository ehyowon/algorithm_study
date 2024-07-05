num = int(input())
cnt = 0
area = [[0 for j in range(100)] for i in range(100)]

for _ in range(num):
	x, y = map(int, input().split())
	for i in range(10):
		for j in range(10):
			area[x+i][y+j] = 1

for i in range(100):
	for j in range(100):
		if area[i][j] == 1:
			cnt += 1

print(cnt)
