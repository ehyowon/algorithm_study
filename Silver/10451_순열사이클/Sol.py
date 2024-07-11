T = int(input())
result = []
for _ in range(T):
	N = int(input())
	nums = list(map(int, input().split()))
	dict = {}
	for i in range(N):
		dict[i+1] = nums[i]
	cnt = 0
	#print(dict)
	
	a = 1
	k = 1
	while len(dict) != 0:
		#print(a, k, cnt)
		if a in dict:
			if dict[a] == a:
				del dict[a]
			elif dict[a] in dict.keys():
				b = dict[a]
				del dict[a]
				cnt += 1
				a = b
			elif dict[a] not in dict.keys():
				del dict[a]
		else:
			k += 1
			a = k
		#print(dict)
	
	result.append(N - cnt)

print(*result, sep = '\n')
