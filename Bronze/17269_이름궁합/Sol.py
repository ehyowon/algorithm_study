def Num(alp):
	num = 0
	if alp == 'E':
		num = 4
	elif alp == 'A' or alp == 'F' or alp == 'H' or alp == 'K' or alp == 'M':
		num = 3
	elif alp == 'B' or alp == 'D' or alp == 'N' or alp == 'P' or alp == 'Q' or alp == 'R' or alp == 'T' or alp == 'X' or alp == 'Y':
		num = 2
	else:
		num = 1
	return num

def Sum(arr):
	if len(arr) <= 2:
		return arr[0] * 10 + arr[1]
	else:
		arr1 = [0 for _ in range(len(arr)-1)]
		for i in range(len(arr)-1):
			arr1[i] = (arr[i] + arr[i+1]) % 10
		return Sum(arr1)

n1, n2 = map(int, input().split())
name1, name2 = map(str, input().split())
n = max(n1, n2)

name = []
for i in range(n):
	if i < n1:
		num = Num(name1[i])
		name.append(num)
	if i < n2:
		num = Num(name2[i])
		name.append(num)

print(Sum(name), '%', sep='')
