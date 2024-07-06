# 이것도 인터넷에서 다른 사람들이 짠 코드 보고 찾은건데 이 문제는 DP를 이용해서 풀 수도 있다고 함!

n = int(input())

dp = [-1] * (n+8)

dp[2]=1
dp[4]=2
dp[5]=1
dp[6]=3
dp[7]=2
dp[8]=4

for i in range(9, n+1):
    dp[i] = min(dp[i-2], dp[i-5])+1

print(dp[n])
