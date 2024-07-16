import sys

input = sys.stdin.readline

def dfs(dep, i):
	if dep == 6: 
		print(*ret)
		return
	
	for i in range(i, k):
		if dep + k - i < 6: # 정답 배열에 넣으려는 인덱스를 더했을 경우 남은 요소들을 다 채워도 최종 길이를 만족하지 못한다면
			return 해당 재귀문 종료
		ret.append(s[i]) # 최종 길이를 만족할 수 있을 경우만 append
		dfs(dep + 1, i + 1) # 재귀
		ret.pop() # 다음 요소 탐색을 위해 pop

while True:
	g = list(map(int, input().split()))
	k = g[0]
	s = g[1:]
	if k == 0:
		break
	ret = []
	dfs(0, 0)
	print()

# https://velog.io/@highcho/Algorithm-baekjoon-6603
