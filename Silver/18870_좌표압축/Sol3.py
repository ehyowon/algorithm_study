n = int(input())
X = list(map(int, input().split()))

Y = list(sorted(set(X)))
Z = dict()

for i in range(len(Y)):
    Z[Y[i]]=i

for i in X:
    print(Z[i], end=' ')
