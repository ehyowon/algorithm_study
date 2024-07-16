def Lotto(res, arr, idx, cnt):
	if cnt == 6:
		print(*res)
		return
	for i in range(idx, len(arr)):
		res[cnt] = arr[i]
		Lotto(res, arr, i + 1, cnt + 1)

while True:
	arr = list(map(int, input().split()))
	k = arr[0]
	arr.pop(0)
	if k == 0:
		break
	res = [0 for _ in range(6)]
	Lotto(res, arr, 0, 0)
	print()
