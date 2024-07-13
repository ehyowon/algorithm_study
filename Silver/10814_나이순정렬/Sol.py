N = int(input())
user = []
for _ in range(N):
  # 리스트 안에 리스트가 있는 꼴 : [[나이,이름],[나이,이름],[나이,이름]]
	age, name = input().split()
	user.append([int(age),name])

for i in sorted(user, key=lambda x : x[0]):
	print(i[0], i[1])
