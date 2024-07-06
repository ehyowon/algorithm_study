def move(a, b):
	if a == 1:
		if b % 2 == 0:
			a += 1
			b -= 1
		elif b % 2 == 1:
			b += 1
		return a, b
	if b == 1:
		if a % 2 == 0:
			a += 1
		elif a % 2 == 1:
			a -= 1
			b += 1
		return a, b
	if (a + b) % 2 == 0:
		a -= 1
		b += 1
		return a, b
	if (a + b) % 2 == 1:
		a += 1
		b -= 1
		return a, b

x = int(input())
i, j = 1, 1

for _ in range(x-1):
	i, j = move(i, j)

print('{}/{}'.format(i, j))
