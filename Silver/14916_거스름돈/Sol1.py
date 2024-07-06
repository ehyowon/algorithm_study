def Coin(n):
	x = -1
	for i in range(50000): # n의 최댓값이 100000이라서 2원짜리로 구성한게 최대 가짓수라고 생각해서 50000개까지 돌면 된다고 생각
		for j in range(50000):
			num = 2 * i + 5 * j
			if num == n:
				x = i + j
				return x
	return x

n = int(input())
print(Coin(n))
